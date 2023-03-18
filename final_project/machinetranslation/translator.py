"""Translation from English to French & vice-versa with IBM Watson"""
import os, json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['API_KEY']
url = os.environ['URL']

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(text):
    """English to French translation function"""
    if text is None:
        return None
    translation_result = language_translator.translate(
        text=text,
        source='en',
        target='fr'
    ).get_result()
    translation = translation_result['translations'][0]['translation']
    return translation

def french_to_english(text):
    """French to English translation function"""
    if text is None:
        return None
    translation_result = language_translator.translate(
        text=text,
        source='fr',
        target='en'
    ).get_result()
    translation = translation_result['translations'][0]['translation']
    return translation
