#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import ValuesView

from ..dto.field_dto import FieldDTO


class FieldsDAO:
    """! Fields DAO."""

    def __init__(self):
        self.__fields = {}

    def get_fields(self) -> ValuesView[FieldDTO]:
        """!
        Return fields.

        @return sequence of FieldDTO objects
        """

        return self.__fields.values()

    def add_field(self, field: FieldDTO):
        """!
        Add a field.

        @param field: FieldDTO object to add
        """

        self.__fields[field.get_name()] = field
