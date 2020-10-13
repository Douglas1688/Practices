from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import  IAMAuthenticator
mensaje = """
Osita bebé, Osita bebé bebé.
Osita bebé, e qué la osita e una bebé
"""
api = IAMAuthenticator("pkvNYLc_ww9nTHZSRq1nbAvEPHXpC5AJPsHWQzDl-taA")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/716a8c7f-1668-48bf-afe0-f904d8595e5c")

pronunciacion = text_2_speech.get_pronunciation(
    text='IEEE',
    voice='es-ES_EnriqueV3Voice',
    format='ibm'
).get_result()

voices = text_2_speech.list_voices().get_result()
with open("osi.mp3","wb") as audiofile:
    audiofile.write(
        text_2_speech.synthesize(mensaje,voice='es-ES_EnriqueV3Voice',accept="audio/mp3").get_result().content

    )