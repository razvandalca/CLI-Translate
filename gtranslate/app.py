import os
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class TranslateApp(App):

    def __init__(self):
        super(TranslateApp, self).__init__(
            description='Google Translate CLI',
            version=os.environ.get('CLI_APP_VERSION', default='0.0'),
            command_manager=CommandManager('gtranslate.cli'),
        )


def main(argv=sys.argv[1:]):
    translateApp = TranslateApp()
    return translateApp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
