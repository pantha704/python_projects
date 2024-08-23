"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="AIzaSyCrf9sSuHNFv38pUffaqDbz286BptEyAQ0")

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
if not (img := Path("image0.png")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/png",
    "data": Path("image0.png").read_bytes()
  },
  {
    "mime_type": "image/png",
    "data": Path("image1.png").read_bytes()
  },
  {
    "mime_type": "image/png",
    "data": Path("image2.png").read_bytes()
  },
  {
    "mime_type": "image/png",
    "data": Path("image3.png").read_bytes()
  },
  {
    "mime_type": "image/png",
    "data": Path("image3.png").read_bytes()
  },
]

prompt_parts = [
  "make a flutter app named Cardiocare whose home screen will show check your heart ",
  image_parts[0],
  "like this with",
  image_parts[1],
  " this glowing logo and the button check your heart brings up the second screen where we provide the range of our heart rate from; Belove 60, 60-100 and Above 100 and after providing the value it travels to the third page showing the result, for example if the heart rate is low it displays a caption that their heart rate is low and also advices some safety precautions. also if the heart rate is low it turns the glow color of the heart to brownish ",
  image_parts[2],
  " like this and if its normal it turns green ",
  image_parts[3],
  " like this and if its high it turns into deep red  ",
  image_parts[4],
  " like this",
]

response = model.generate_content(prompt_parts)
# print(response.text)
with open(file='response.txt', mode='w') as file:
  file.write(response.text)