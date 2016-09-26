#!/usr/bin/env python3

import datetime
import subprocess
import sys
import os.path
import glob


SNAPCRAFT = 'snapcraft-stg'


def main():
    if '--loop' in sys.argv:
        looping = True
        sys.argv.remove('--loop')
    else:
        looping = False
    while True:
        if len(sys.argv) > 1:
            comment = sys.argv[1]
        else:
            comment = "No Comment"

        now = datetime.datetime.now()
        status = "Version released at %s with comment: %s" % (now, comment)
        here = os.path.dirname(__file__)
        target_file = os.path.join(here, 'thomir-says.py')

        # Clean the old data:
        subprocess.check_call([SNAPCRAFT, 'clean'])

        # Edit the script file:
        subprocess.check_call([
            'sed',
            '-i',
            's/^MESSAGE.*/MESSAGE = %r/' % (status),
            target_file])

        # do a new build:
        subprocess.check_call([SNAPCRAFT])

        # find the snap file:
        snaps = glob.glob(os.path.join(here, '*.snap'))

        assert len(snaps) == 1

        # release the snap:
        subprocess.check_call([SNAPCRAFT, 'push', snaps[0], '--release', 'stable'])
        if not looping:
            break

if __name__ == '__main__':
    main()
