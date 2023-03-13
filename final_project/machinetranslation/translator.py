import json
import os
from ibm_watson import LanguageTranslatorV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
language_translator = LanguageTranslatorV3(
    version='2018-05-01'
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')


_englishtext = None
_frenchtext = None

def english_to_french(_englishtext):

    translation = language_translator.translate(
    text='Hello, How are you today?', model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return _frenchtext

def french_to_english(_frenchtext):
    translation = language_translator.translate(
    text='Bonjour, Comment allez-vous aujourd?', model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return _englishtext
