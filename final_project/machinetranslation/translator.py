""" Module to translate text from English to French and vice versa"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

# API Environment Variables
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
except ApiException as ex:
    print(f"Method failed with status code {str(ex.code)}: {ex.message}")

def english_to_french(text=None):
    """
    This function translates text from English to French
    """
    if not text:
        # If no text is provided, return None
        return None
    translation = language_translator.translate(
    text=text,
    model_id='en-fr').get_result()
    return translation["translations"][0]['translation']

def french_to_english(text=None):
    """
    This function translates text from French to English
    """
    if not text:
        # If no text is provided, return None
        return None
    translation = language_translator.translate(
    text=text,
    model_id='fr-en').get_result()
    return translation["translations"][0]['translation']
