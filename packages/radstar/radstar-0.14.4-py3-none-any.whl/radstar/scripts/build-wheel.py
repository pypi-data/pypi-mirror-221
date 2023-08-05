#!/usr/bin/env python3

# -------------------------------------------------------------------------------------------------------------------- #

# Copyright © 2021-2023 Peter Mathiasson
# SPDX-License-Identifier: ISC

# -------------------------------------------------------------------------------------------------------------------- #

import base64
import hashlib
import os
import sys
import zipfile

# -------------------------------------------------------------------------------------------------------------------- #

INCLUDE_DIRS = [
    'core',
    'rs',
    'scripts',
    'templates',
]
WHEEL_FILE = 'dist/radstar-{version}-py3-none-any.whl'
DIST_INFO = 'radstar-{version}.dist-info'

# -------------------------------------------------------------------------------------------------------------------- #

def build_wheel(whl, version):

    # radstar package
    for x in INCLUDE_DIRS:
        add_dir(whl, x, prefix='radstar')

    dist_info = DIST_INFO.format(version=version)

    # files in dist-info dir
    for x in os.listdir('dist-info'):
        with open(os.path.join('dist-info', x)) as f:
            data = f.read().format(version=version)
        add_string(whl, f'{dist_info}/{x}', data)

    # license file
    add_file(whl, 'LICENSE', prefix=dist_info)

    # record file
    _records.append(f'{dist_info}/RECORD,,')
    add_string(whl, f'{dist_info}/RECORD', '\n'.join(_records) + '\n')

# -------------------------------------------------------------------------------------------------------------------- #

def add_dir(whl, directory, prefix=None):
    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        for x in files:
            if x.startswith('.') or os.path.islink(os.path.join(root, x)):
                continue
            add_file(whl, os.path.join(root, x), prefix=prefix)

# -------------------------------------------------------------------------------------------------------------------- #

def add_file(whl, filename, prefix=None):
    dst = f'{prefix}/{filename}' if prefix else filename
    record_file(dst, chksum_file(filename), os.stat(filename).st_size)
    whl.write(filename, dst)

# -------------------------------------------------------------------------------------------------------------------- #

def add_string(whl, filename, data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    record_file(filename, hashlib.sha256(data).digest(), len(data))
    whl.writestr(filename, data)

# -------------------------------------------------------------------------------------------------------------------- #

def record_file(filename, chksum, size):
    chksum = base64.urlsafe_b64encode(chksum).rstrip(b'=').decode('ascii')
    _records.append(f'{filename},sha256={chksum},{size}')

_records = []

# -------------------------------------------------------------------------------------------------------------------- #

def chksum_file(filename):
    chksum = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(16384)
            if not data:
                break
            chksum.update(data)
    return chksum.digest()

# -------------------------------------------------------------------------------------------------------------------- #

def main():

    # get version from command line
    if len(sys.argv) < 2:
        print('no version specified', file=sys.stderr)
        sys.exit(1)
    version = sys.argv[1]

    # chdir to radstar dir
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))

    # create dist dir if needed
    if not os.path.isdir('dist'):
        os.mkdir('dist')

    # build wheel
    with zipfile.ZipFile(WHEEL_FILE.format(version=version), 'w') as whl:
        build_wheel(whl, version)

# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------------- #
