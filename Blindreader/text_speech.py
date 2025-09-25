import os 
import io
import json
#from pydub import AudioSegment
#from pydub.playback import play
import azure.cognitiveservices.speech as speechsdk

# def play_audio_from_bytes(audio_data, format='wave'):
#     audio_data_io = io.BytesIO(audio_data)
#     audio_segment = AudioSegment.from_file(audio_data_io, format=format)
#     play(audio_segment)

credential = json.load(open('credential.json'))
subscription_key = credential['speech_api']
endpoint = credential['speech_endpoint']
region = credential['region']
speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

text = """Various libraries were used throughout the project to implement machine learning algorithms and the web server. The majority of the algorithms are Python libraries, which are widely used in machine learning. However, machine learning libraries are not the only ones that are used. For example, a library called Split-folders is used to divide the data into percentages. Python was used only for this project, and a Jupyter notebook was used to record the analysis. To carry out various studies, common Python libraries were employed.""".strip()
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")