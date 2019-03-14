# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab Developers
#
# This file is part of Pandora, https://github.com/frootlab/pandora
#
#  Pandora is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Pandora is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Pandora. If not, see <http://www.gnu.org/licenses/>.
#
"""Table Proxy for Microsoft Excel Office Open XML Files."""

__copyright__ = '2019 Frootlab Developers'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

try:
    import openpyxl
except ImportError as err:
    raise ImportError(
        "requires package openpyxl: "
        "https://pypi.org/project/openpyxl") from err

from flib.base import attrib
from pandb.core import table

#
# Classes
#

class Table(table.Proxy):
    """Excel-Table Proxy."""

    _file: property = attrib.Temporary()
