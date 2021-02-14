from cliff.command import Command
from cliff.lister import Lister


class Translate(Command):
    """A command to translate a text file to a specific language"""

    def get_parser(self, prog_name):
        parser = super(Translate, self).get_parser(prog_name)
        group = parser.add_mutually_exclusive_group()

        group.add_argument(
            '-f',
            help='path to input filename to be translated',
            action='store_true',
        )
        group.add_argument(
            '-l',
            help='output language, can be one of "en", "it" or "de"',
            action='store_true',
        )

        return parser

    def take_action(self, parsed_args):
        return "This will be translated text"
