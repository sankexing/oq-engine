# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2014-2017 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import login, logout

from openquake.server import views as oqserver

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/engine/', permanent=True)),
    url(r'^engine_version$', oqserver.get_engine_version),
    url(r'^v1/calc/', include('openquake.server.v1.calc_urls')),
    url(r'^v1/valid/', oqserver.validate_nrml),
    url(r'^engine/?$', oqserver.web_engine, name="index"),
    url(r'^engine/(\d+)/outputs$',
        oqserver.web_engine_get_outputs, name="outputs"),
    url(r'^engine/license$', oqserver.license,
        name="license"),
]

if settings.LOCKDOWN:
    from django.contrib import admin

    admin.autodiscover()
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^accounts/login/$', login,
            {'template_name': 'account/login.html'}, name="login"),
        url(r'^accounts/logout/$', logout,
            {'template_name': 'account/logout.html'}, name="logout"),
        url(r'^accounts/ajax_login/$', oqserver.ajax_login),
        url(r'^accounts/ajax_logout/$', oqserver.ajax_logout),
    ]
