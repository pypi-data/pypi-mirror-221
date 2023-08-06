# -------------------------------------------------------------------------------------------------------------------- #

# Copyright © 2021-2023 Peter Mathiasson
# SPDX-License-Identifier: ISC

# -------------------------------------------------------------------------------------------------------------------- #

import os
import subprocess

from rs import shsplit

# -------------------------------------------------------------------------------------------------------------------- #

def setup():

    # create jetapp/node_modules link
    if not os.path.islink('core/webix/jetapp/node_modules'):
        os.symlink('/node_modules', 'core/webix/jetapp/node_modules')

    # install jetapp js dependencies
    subprocess.check_call(shsplit('yarn install'), cwd='core/webix/jetapp')

# -------------------------------------------------------------------------------------------------------------------- #
