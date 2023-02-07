import os

try:
    import jwt
except ImportError:
    os.system('/usr/bin/python3.6 -m pip install --upgrade pip')
    os.system('/usr/bin/python3.6 -m pip install --upgrade setuptools')
    os.system('/usr/bin/python3.6 -m pip install "PyJWT==1.7.1"')



