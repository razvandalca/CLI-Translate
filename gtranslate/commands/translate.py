import threading
from pathlib import Path
from cliff.command import Command
from gtranslate.translators.google_translator import GoogleTranslator


class Translate(Command):
    """A command to translate a text file to a specific language"""

    def __init__(self, app, app_args, cmd_name=None):
        super().__init__(app, app_args, cmd_name)
        self.supported_languages = ['en', 'it', 'de']

    def get_parser(self, prog_name):
        parser = super(Translate, self).get_parser(prog_name)
        parser.add_argument(
            '-f', '--file',
            type=str,
            default=None,
            help='path to input filename to be translated',
        )
        parser.add_argument(
            '-l', '--language',
            type=str,
            default='en',
            help='output language, can be one of "en", "it" or "de"',
        )

        parser.add_argument(
            '--fullOutput',
            type=bool,
            default=False,
            help='Show full data after translation'
        )

        return parser

    def take_action(self, parsed_args):
        if parsed_args.language.lower() not in self.supported_languages:
            return f"Language {parsed_args.language} not supported."
        if not parsed_args.file:
            return 'No file provided'
        if not Path(parsed_args.file).exists():
            return 'File does not exist'

        file = open(parsed_args.file, 'r')
        lines = file.readlines()
        for line in lines:
            # Using daemon thread so it exists if main thread is killed Example: user exiting cli interface
            threading.Thread(target=self.translate_line(line,
                                                        parsed_args.language,
                                                        parsed_args.fullOutput),
                             daemon=True)

    def translate_line(self, text_lin, lang, show_full_output):
        translation = GoogleTranslator().translate_text(text_lin.rstrip(), lang)
        if show_full_output:
            print(translation)
        else:
            print(translation['translatedText'])
