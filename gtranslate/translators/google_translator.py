from google.cloud import translate_v2 as translate

from gtranslate.translators.base_translator import Translator


class GoogleTranslator(Translator):

    def __init__(self):
        self.translate_client = translate.Client()

    def translate_text(self, text_to_translate, target_language):
        return self.translate_client.translate(text_to_translate, target_language=target_language)
