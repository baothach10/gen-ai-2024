import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# API_KEY = "AIzaSyAJek4zKNvDHDDZZ37J6Cmk42yLT6Fed-c"
API_KEY = os.getenv('GOOGLE_API_KEY')
print(API_KEY)

class ImageGen:
    def __init__(self):
        # Configure the API key
        genai.configure(api_key=API_KEY)

        # Check available attributes for debugging (optional)
        print(dir(genai))

        # Initialize the model
        self.model = genai.ImageGenerationModel("imagen-3.0-generate-001")
        # self.model = genai.

    def generate_image(self, prompt):
        result = self.model.generate_images(
            prompt=prompt,
            number_of_images=1,
            safety_filter_level="block_only_high",
            person_generation="allow_adult",
            aspect_ratio="3:4",
            negative_prompt="Outside",
        )

        # Display the generated image
        for image in result.images:
            image._pil_image.show()

# Create an instance and generate an image
imageGen = ImageGen()
imageGen.generate_image("A beautiful sunset over the ocean")