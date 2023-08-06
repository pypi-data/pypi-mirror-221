#!/usr/bin/python

from .case import TestCase
from .running.config import Cdxg
from .running.loader_extend import SeldomTestLoader
from .running.runner import main, TestMainExtend
from .utils.send_extend import SMTP
from .webdriver_chaining import Steps

from .skip import *
from .driver import *
from .testdata.parameterization import *


__author__ = "mastersaa"

__version__ = "1.1"

__description__ = "WebUI/HTTP automation testing framework."
