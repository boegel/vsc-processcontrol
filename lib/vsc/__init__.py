#!/usr/bin/env python
##
# Copyright 2011-2013 Ghent University
#
# This file is part of vsc-processcontrol,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/vsc-processcontrol
#
# vsc-processcontrol is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# vsc-processcontrol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with vsc-processcontrol. If not, see <http://www.gnu.org/licenses/>.
##
"""
@author: Jens Timmerman (Ghent University)

Initialize vsc package.
the vsc namespace is used in different folders allong the system
so explicitly declare this is also the vsc namespace
"""
from pkgutil import extend_path

# we're not the only ones in this namespace
__path__ = extend_path(__path__, __name__)  #@ReservedAssignment
