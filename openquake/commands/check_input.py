# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2018-2020 GEM Foundation
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
import sys
import logging
from openquake.baselib import sap
from openquake.risklib.asset import Exposure
from openquake.commonlib import readinput, logs
from openquake.calculators import base
from openquake.hazardlib import nrml
from openquake.risklib import read_nrml  # this is necessary


@sap.script
def check_input(job_ini_or_zip_or_nrmls):
    for job_ini_or_zip_or_nrml in job_ini_or_zip_or_nrmls:
        if job_ini_or_zip_or_nrml.endswith('.xml'):
            try:
                node = nrml.to_python(job_ini_or_zip_or_nrml)
                if node.tag.endswith('exposureModel'):
                    err = Exposure.check(job_ini_or_zip_or_nrml)
                    if err:
                        logging.warning(err)
                else:
                    logging.info('Checked %s', job_ini_or_zip_or_nrml)
            except Exception as exc:
                sys.exit(exc)
        else:
            oq = readinput.get_oqparam(job_ini_or_zip_or_nrml)
            base.calculators(oq, logs.init()).read_inputs()


check_input.arg('job_ini_or_zip_or_nrmls', 'Check the input', nargs='+')
