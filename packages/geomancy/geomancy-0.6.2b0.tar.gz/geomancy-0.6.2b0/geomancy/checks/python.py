"""
Checks for python environment and packages
"""
from .base import CheckBase, CheckResult


class CheckPythonPackage(CheckBase):
    """Check the availability of a python package"""
