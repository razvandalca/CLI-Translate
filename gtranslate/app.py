import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class TranslateApp(App):

    def __init__(self):
        super(TranslateApp, self).__init__(
            description='Google Translate CLI',
            version='0.1',
            command_manager=CommandManager('gtranslate.cli'),
            deferred_help=True,
            )


def main(argv=sys.argv[1:]):
    translateApp = TranslateApp()
    return translateApp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
