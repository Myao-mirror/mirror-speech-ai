#!/usr/bin/env python3

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import subprocess

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('shutdown')

    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said ', text, '"')
            if 'shutdown' in text:
                subprocess.call(["sudo", "shutdown", "-h", "now"])

if __name__ == '__main__':
    main()
