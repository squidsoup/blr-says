#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2016 Canonical Ltd.  This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

import re
import pkg_resources
from setuptools import find_packages, setup


VERSION = '0.1.1'


setup(
    name='blr-says',
    version=VERSION,
    scripts=['blr-says.py'],
)

