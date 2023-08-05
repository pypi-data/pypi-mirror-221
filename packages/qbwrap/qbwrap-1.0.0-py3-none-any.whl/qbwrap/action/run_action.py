#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from subprocess import run
from typing import List


class RunAction:
    """! Run action."""

    def __init__(
        self,
        command_arguments: List[str],
        become_root: bool,
        become_method: str,
        fake_execution: bool,
        quiet_execution: bool,
    ):
        self.__become_method = become_method
        self.__become_root = become_root
        self.__command_arguments = command_arguments
        self.__fake_execution = fake_execution
        self.__quiet_execution = quiet_execution

    def execute(self):
        """! Execute the Run action."""

        arguments = []

        if self.__become_root:
            if self.__become_method == "su":
                arguments.append("su")
                arguments.append("-c")
                arguments.append(
                    " ".join([f'"{s}"' for s in self.__command_arguments])
                )
            else:
                arguments.append(self.__become_method)
                arguments.extend(self.__command_arguments)
        else:
            arguments.extend(self.__command_arguments)

        # Show what will be executed.
        if not self.__quiet_execution:
            print(" * Executing: ", end="")

            for argument in arguments:
                print(argument, end=" ")

            print("")

        if not self.__fake_execution:
            run(arguments, check=True)
