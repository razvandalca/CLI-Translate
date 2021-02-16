from abc import ABC


class Translator(ABC):

    def translate_text(self, text_to_translate, target_language):
        raise Exception("NotImplementedException")
