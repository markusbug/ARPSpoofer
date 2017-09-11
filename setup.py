#!/usr/bin/env python
from distutils.core import setup
import os
os.system("chmod +x ARPSpoofer.py")
setup(name='ARPSpoofer',
      version='1.0',
      description='Setup to ARPSpoofer',
      license= 'GNU',
      author='Markus Haas',
      author_email='mhaas2@student.tgm.ac.at',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command', 'scapy', 'os', 'threading', 'sys', 'signal', 'pcapy'],
     )