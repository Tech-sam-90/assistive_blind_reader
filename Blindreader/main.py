from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import requests
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from array import array
import json
from PIL import Image
import sys
import time

credential = json.load(open('credential.json'))
subscription_key = credential['API_KEY']
endpoint = credential['ENDPOINT']

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

read_image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
loca_file = "./Capture.jpg"

start_time = time.time()

#read_response = computervision_client.read(read_image_url,  raw=True)
read_response = computervision_client.read_in_stream(open(loca_file, 'rb'), language='en', raw=True)
read_operation_location = read_response.headers["Operation-Location"]
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

end_time = time.time()

ocr_duration =  end_time - start_time
print(ocr_duration)
extracted_text = ""
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            extracted_text += line.text + " "

mp3_fp = BytesIO()
tts = gTTS(extracted_text, lang='en', tld='com.ng')
tts.write_to_fp(mp3_fp)

mp3_fp.seek(0)

audio = AudioSegment.from_file(mp3_fp, format='mp3')
play(audio)
