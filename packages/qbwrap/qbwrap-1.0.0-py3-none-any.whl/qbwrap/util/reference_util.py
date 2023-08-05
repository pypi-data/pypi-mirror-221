#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


import re


__reference_regexp = re.compile(r"^\$\..+")


def is_reference_string(path_string: str) -> bool:
    """! Check if path is a reference."""

    return bool(__reference_regexp.match(path_string))


def reference_string_to_path(reference_string: str) -> str:
    """! Convert reference_string to a path list."""

    return reference_string[2:]
