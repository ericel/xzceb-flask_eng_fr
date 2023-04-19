import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = "2018-05-01"

try:
    # Create an instance of the IBM Watson Language translator
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator
    )

    language_translator.set_service_url(URL)

    language_translator.set_disable_ssl_verification(True)
    
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def englishToFrench(englishText):
    """
    This function translates text from English to French
    """
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText = translation["translations"][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """
    This function translates text from French to English
    """
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText = translation["translations"][0]['translation']
    return englishText