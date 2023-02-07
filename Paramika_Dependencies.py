import os
try:
    import paramiko
    import sys
except ImportError:
    os.system('/usr/bin/python3.6 -m pip install --upgrade pip')
    os.system('/usr/bin/python3.6 -m pip install --upgrade setuptools')
    os.system('/usr/bin/python3.6 -m pip install paramiko')