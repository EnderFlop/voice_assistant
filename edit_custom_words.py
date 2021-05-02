from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import json

IBM_API_KEY=os.environ.get("IBM_API_KEY")
IBM_URL=os.environ.get("IBM_URL")

authenticator = IAMAuthenticator(f'{IBM_API_KEY}')
watson = SpeechToTextV1(authenticator=authenticator)
watson.set_service_url(f'{IBM_URL}')

language_model = watson.create_language_model(
  name="voice_assistant", 
  base_model_name="en-US_BroadbandModel", 
  dialect="en-US", 
  description="voice_assistant custom phrases").get_result()
print(json.dumps(language_model, indent=2))

#Figure out why create_language_model doesnt work
#https://github.com/watson-developer-cloud/python-sdk/issues/639
#https://cloud.ibm.com/apidocs/speech-to-text?code=python#createlanguagemodel
#END GOAL - https://cloud.ibm.com/apidocs/speech-to-text?code=python#addwords