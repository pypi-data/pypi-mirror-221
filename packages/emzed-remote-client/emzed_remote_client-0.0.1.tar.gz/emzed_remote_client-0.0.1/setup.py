from __future__ import print_function

import os
import sys

from setuptools import setup

VERSION = (0, 0, 1)  # no need to adapt version in other locations

AUTHOR = "Uwe Schmitt"
AUTHOR_EMAIL = "uwe.schmitt@id.ethz.ch"

DESCRIPTION = "client side of emzed remote execution"

LICENSE = "https://opensource.org/licenses/MIT"

LONG_DESCRIPTION = ""


if __name__ == "__main__":

    setup(
        version="%d.%d.%d" % VERSION,
        name="emzed_remote_client",
        py_modules=["emzed_remote_client"],
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        # the following makes a plugin available to pytest
        install_requires = ["numpy"],
        include_package_data=True,
    )
