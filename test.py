#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2025 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved
#
#
# File: /c/Users/Administrator/git/python-env3/test.py
# Author: Hai Liang Wang
# Date: 2025-05-31:13:17:53
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2025 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2025-05-31:13:17:53"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

# Get ENV
import env3
ENV = env3.load_env(os.path.join(curdir, ".env"))

print("FOO=%s" % ENV.get("FOO"))
print("FOO=%s" % os.environ.get("FOO"))
