import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = "2018-05-01"

# Create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator('{APIKEY}')
language_translator = LanguageTranslatorV3(
    version='{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url('{URL}')

language_translator.set_disable_ssl_verification(True)


def englishToFrench(englishText):
    #write the code here
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    return englishText