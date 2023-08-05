#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dao.argument_parser_dao import ArgumentParserDAO
from ..dao.qbwrap_setup_dao import QBwrapSetupDAO

from .run_action import RunAction


class SetupAction:
    """! Setup action."""

    def __init__(
        self,
        argument_parser: ArgumentParserDAO,
        qbwrap_setup_dao: QBwrapSetupDAO,
    ):
        self.__qbwrap_setup_dao = qbwrap_setup_dao

        become_root = qbwrap_setup_dao.get_setup_stanza().get_privileged()
        become_method = argument_parser.get_become_root_method()
        fake_execution = argument_parser.get_fake()
        quiet_execution = argument_parser.get_quiet()

        self.__mkdir_run_action = RunAction(
            command_arguments=["mkdir", "-p", qbwrap_setup_dao.get_location()],
            become_root=become_root,
            become_method=become_method,
            fake_execution=fake_execution,
            quiet_execution=quiet_execution,
        )
        self.__url_download_run_action = RunAction(
            command_arguments=qbwrap_setup_dao.get_download_command(),
            become_root=become_root,
            become_method=become_method,
            fake_execution=fake_execution,
            quiet_execution=quiet_execution,
        )
        self.__archive_extraction_run_action = RunAction(
            command_arguments=qbwrap_setup_dao.get_extraction_command(),
            become_root=become_root,
            become_method=become_method,
            fake_execution=fake_execution,
            quiet_execution=quiet_execution,
        )

    def execute(self):
        """! Execute the Setup action."""

        self.__mkdir_run_action.execute()
        self.__url_download_run_action.execute()

        self.__qbwrap_setup_dao.verify_archive()

        self.__archive_extraction_run_action.execute()
