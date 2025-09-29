import json
import time
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Get the credentials from the JSON file
try:
    with open('./Blindreader/credential.json') as f:
        credential = json.load(f)
        api_key = credential["API_KEY"]
        endpoint = credential["ENDPOINT"]
except FileNotFoundError:
    print("Missing credential.json file")
    exit()
except KeyError as e:
    print(f"Missing key in credential.json: {e}")
    exit()

# Create client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

# Load image from local machine
with open("./OCR/capture 1.png", "rb") as f:
    image_data = f.read()
    print("Image loaded successfully")

# Call OCR
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.READ],
    language="en"
)

# Print extracted text
if result.read is not None:
    extracted_text = ""
    for block in result.read.blocks:
        for line in block.lines:
            extracted_text += line.text
            print(line.text)
else:
    print("No text detected")

#To read out the text gotten
