#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


class QBwrapStanzaDelegateDAO:
    """! QBwrap stanza delegate DAO."""

    def __init__(self, config):
        self.__config = config

    def _get_stanza(self, stanza_class: type):
        stanza = stanza_class()

        stanza.load_dict_data(self.__config)

        return stanza
