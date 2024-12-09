## Load dotenv
from dotenv import load_dotenv
import os

load_dotenv()
ACCOUNT_ID = os.getenv("ACCOUNT_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CLOUD_NAME = os.getenv("CLOUD_NAME")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

## Import librariesimport requests
import base64
import PIL
from io import BytesIO
import cloudinary
import cloudinary.uploader
import requests

from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages.ai import AIMessage
from typing import Literal
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

from IPython.display import Image, display

## config
# Cloudinary for image storage
cloudinary.config(
    cloud_name = CLOUD_NAME,
    api_key = API_KEY,
    api_secret = API_SECRET
)

# Gen image API fetching
API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Config gemini
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

## Init
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
SYSINT = (
    "system",
    "You are an image editor for a popular news magazine"
    "Your main purpose is to generating eye capturing images on the landing page of the news magazine."
    "You'll be provide with a prompt, and you're job is to transform the prompt into"
    "a detailed description of the image of the landing page that you're going to create."
    "Do not provide the description back to the user, just select the description you think is the best one."
    "Do not provide details on how the image will be placed or used, just the description is needed"
    "\n\n"
    "Do not transform the original prompt away from its original meaning. Do not go off-topic"
)

def gen_image(prompt: str) -> str:
    input = { "prompt": prompt }
    model = "@cf/black-forest-labs/flux-1-schnell"
    
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    output = response.json()

    base64_string = output['result']['image'].strip().replace("\n", "")
    imagedata = base64.b64decode(base64_string)
    image = PIL.Image.open(BytesIO(imagedata))

    res = "test.png"
    image.save(res)    

    return res


def generate_image(content: str) -> str:
    output = llm.invoke([SYSINT] + [content])
    print(output.content)

    return gen_image(output.content)


# example = "Australia increased welfare payments to combat rising living costs.  San Jose utilizes AI to improve government services.  Over-reliance on the finance industry for economic growth is cautioned against, while the UK considers government intervention for Thames Water.  Malawi's food relief program reached 4.5 million people.  Syrian rebels seized the capital, prompting Syrian refugees' return.  Canada's government faces criticism for its treatment of certain citizens, and Yorkshire's top-performing schools were identified based on new GCSE data."
# generate_image(example)

