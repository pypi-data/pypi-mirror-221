# -------------------------------------------------------------------------------------------------------------------- #

# Copyright © 2021-2023 Peter Mathiasson
# SPDX-License-Identifier: ISC

# -------------------------------------------------------------------------------------------------------------------- #

import os
import sys

from . import cli, shexec
from .. import init_radstar, list_apps, panic

# -------------------------------------------------------------------------------------------------------------------- #

@cli.command()
def setup():
    ''' Configure radstar environment. '''

    # check that we're executing in a radstar environment
    for dir_name in ['/rs', '/rs/env', '/rs/project', '/node_modules']:
        if not os.path.isdir(dir_name):
            panic(f'invalid environment ({dir_name} missing)')

    # XXX: remove before v1.0.0
    cleanup()

    # remove existing /rs/radstar link
    if os.path.islink('/rs/radstar'):
        os.unlink('/rs/radstar')

    # create /rs/radstar link
    link_src = os.getcwd()
    if os.path.isdir(os.path.join(link_src, 'radstar')):
        link_src += '/radstar'
    os.symlink(link_src, '/rs/radstar')

    # setup apps
    shexec('rs setup-apps')

# -------------------------------------------------------------------------------------------------------------------- #

@cli.command(hidden=True)
def setup_apps():

    init_radstar(no_init=True)

    for app in list_apps():
        if (mod := app.import_module('setup')) is not None:
            mod.setup()

# -------------------------------------------------------------------------------------------------------------------- #

# XXX: remove before v1.0.0

def cleanup():

    for link_name in ['core', 'jetapp', 'rs', 'scripts', 'templates']:
        if os.path.islink((link_path := os.path.join('/rs/radstar', link_name))):
            os.unlink(link_path)

    if os.path.isdir('/rs/radstar') and not os.path.islink('/rs/radstar'):
        os.rmdir('/rs/radstar')

# -------------------------------------------------------------------------------------------------------------------- #
