# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Module tests."""

from __future__ import absolute_import, print_function

from werkzeug.test import EnvironBuilder


def wsgi_output(app):
    data = {}

    def start_response(status, headers):
        data['status'] = status
        data['headers'] = headers

    data['output'] = app(
        EnvironBuilder(path='/', method='GET').get_environ(),
        start_response
    )

    return data


def test_wsgi():
    """Test WSGI applications."""
    from invenio_app.wsgi import application
    res = wsgi_output(application)
    assert res['status'] == '404 NOT FOUND'

    from invenio_app.wsgi_ui import application
    res = wsgi_output(application)
    assert res['status'] == '404 NOT FOUND'

    from invenio_app.wsgi_rest import application
    res = wsgi_output(application)
    assert res['status'] == '404 NOT FOUND'
