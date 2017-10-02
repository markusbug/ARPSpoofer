from setuptools import setup, find_packages
import os
os.system("chmod+x ARPSpoofer.py")
ENTRY_POINTS = {"console_scripts": ["arpspoofer = arpspoofer:run"]}
setup(
    name="ARPSpoofer",
    version="0.1",
    packages=find_packages(),
    entry_points=ENTRY_POINTS,
)
