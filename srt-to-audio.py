import os
import argparse

import pysrt
from gtts import gTTS
from pydub import AudioSegment


def main():
    ''' arguments
        $ python srt-to-audio.py -f test.srt -o test.mp3
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', help="input srt file")
    parser.add_argument('--output', '-o', help="output mp3 file")
    args = parser.parse_args()

    subs = pysrt.open(args.file)

    final = AudioSegment.empty()
    sounds = []
    sound_path = os.path.join(os.path.dirname(__file__), 'sounds')

    for sub in subs:
        ''' 1.mp3     | text |
            2.mp3     |---- silent ----| text |
            3.mp3     |--------------- silent ---------| text |

            test.mp3  | text |-silent--| text |-silent-| text |
        '''
        text = sub.text
        silent_t = sub.start.ordinal  # milliseconds

        mp3fn = os.path.join(sound_path, text + '.mp3')

        if text != '':  # text not empty
            print('%s [%s]' % (sub.start, text))
            if not os.path.exists(mp3fn):
                tts = gTTS(text, lang='zh-TW')
                tts.save(mp3fn)

            mp3 = AudioSegment.from_mp3(mp3fn)

            if silent_t > 0:
                silent = AudioSegment.silent(silent_t)
                sounds.append(silent + mp3)
            else:
                sounds.append(mp3)
    ''' final is the longest one / overlay all sounds
    '''
    final = sounds[-1]
    for a in sounds[:-1]:
        final = final.overlay(a)
    final.export(args.output, format='mp3')


if __name__ == "__main__":
    main()
