from io import BytesIO
from PIL import Image
import base64
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader

load_dotenv()

API_KEY = os.getenv('ACCESS_TOKEN')

ACCOUNT_ID = os.getenv('ACCOUNT_ID')

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CLOUDINARY_CLOUD_NAME=os.getenv('CLOUD_NAME')
CLOUDINARY_API = os.getenv('API_KEY')
CLOUDINARY_SECRET = os.getenv('API_SECRET')


cloudinary.config( 
    cloud_name = CLOUDINARY_CLOUD_NAME, 
    api_key = CLOUDINARY_API, 
    api_secret = CLOUDINARY_SECRET, # Click 'View API Keys' above to copy your API secret
    secure=True
)


API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
headers = {"Authorization": f"Bearer {API_KEY}"}


genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')


meme_generation_prompt = """You are a meme creation expert who understands internet humor, cultural references, and trending meme formats.

Given a summary text, generate two outputs:

1. Meme Text:
- Create a concise, witty text that can be placed on a meme image
- Use humor, sarcasm, or irony relevant to the summary
- Aim for 3-4 words that capture the essence of the text
- Ensure the text is punchy and memorable
- Use internet slang or meme-style language if appropriate

2. Meme Description:
- Describe a potential meme image that would complement the meme text
- Suggest a specific meme format or template (e.g., "Distracted Boyfriend", "Surprised Pikachu")
- Describe the visual composition and characters/elements
- Explain how the image relates to the text and summary

Summary: "{summary}"

Output Format:
[Your witty meme text]|[Detailed meme image description]
"""


def run(model, prompt):
    input = {"prompt": prompt}
    response = requests.post(
        f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()



def gen_meme(summary: str):
    out = model.generate_content(
        meme_generation_prompt.format(summary=summary)).text


    text = out.split("|")[0]
    desc = out.split("|")[1]


    prompt = f"{desc}with a text box '{text}', do not put text anywhere else"

    output = run("@cf/black-forest-labs/flux-1-schnell", prompt=prompt)
    # print(output)

    base64_string = output['result']['image'].strip().replace("\n", "")

    imagedata = base64.b64decode(base64_string)

    image = Image.open(BytesIO(imagedata))
    image.save('test2.png')

    upload_result = cloudinary.uploader.upload('test2.png')
    image_url = upload_result.get("secure_url")

    return image_url


