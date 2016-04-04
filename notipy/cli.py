import os
from enum import Enum


class SupportedImplementation(Enum):
    sendNotify = 'sendNotify'
    osascript = 'osascript'


class Notipy:
    def __init__(self):
        self.implementation = self.__get_available_implementation()

    def send(self, message):
        self._send_message(message)

    def _send_message(self, message):
        if self.implementation == SupportedImplementation.osascript:
            os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, 'Notification'))
        elif self.implementation == SupportedImplementation.sendNotify:
            os.system('send-notify "{}"'.format(message))

    @staticmethod
    def _command_exists(command):
        return any(
            os.access(os.path.join(path, command), os.X_OK)
            for path in os.environ["PATH"].split(os.pathsep)
        )

    def __get_available_implementation(self):
        if self._command_exists('osascript'):
            return SupportedImplementation.osascript
        elif self._command_exists('send-notify'):
            return SupportedImplementation.sendNotify
        return None