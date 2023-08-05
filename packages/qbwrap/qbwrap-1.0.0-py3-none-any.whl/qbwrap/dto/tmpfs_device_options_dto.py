#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Literal
from typing import Union


TmpfsSize = Union[str, Literal[False]]
TmpfsPerms = Union[str, Literal[False]]


class TmpfsDeviceOptionsDTO:
    """! Tmpfs Device options DTO."""

    def __init__(self, size: TmpfsSize = False, perms: TmpfsPerms = False):
        self.__size = size
        self.__perms = perms

    def get_size(self) -> TmpfsSize:
        """! Tmpfs Device size getter."""

        return self.__size

    def set_size(self, size: TmpfsSize):
        """! Tmpfs Device options DTO size setter."""

        self.__size = size

    def get_perms(self) -> TmpfsPerms:
        """! Tmpfs Device options DTO perms getter."""

        return self.__perms

    def set_perms(self, perms: TmpfsPerms):
        """! Tmpfs Device options DTO perms setter."""

        self.__perms = perms
