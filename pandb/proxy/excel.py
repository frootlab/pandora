# -*- coding: utf-8 -*-
# Copyright (c) 2019 Patrick Michl
#
# This file is part of pandora, https://frootlab.github.io/pandora
#
#  pandora is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  pandora is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  pandora. If not, see <http://www.gnu.org/licenses/>.
#
"""Table Proxy for Microsoft Excel Office Open XML Files."""

__author__ = 'Patrick Michl'
__email__ = 'frootlab@gmail.com'
__license__ = 'GPLv3'
__docformat__ = 'google'

try:
    import openpyxl
except ImportError as err:
    raise ImportError(
        "requires package openpyxl: "
        "https://pypi.org/project/openpyxl") from err

from flab.base import attrib
from pandb.core import table

#
# Classes
#

class Table(table.Proxy):
    """Excel-Table Proxy."""

    _file: property = attrib.Temporary()
