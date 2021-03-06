from setuptools import find_packages
from setuptools import setup

try:
    with open('.version') as f:
        VERSION = f.readline().strip()
except IOError:
    VERSION = 'unknown'

setup(
    name='ocflib',
    version=VERSION,
    author='Open Computing Facility',
    author_email='help@ocf.berkeley.edu',
    description='libraries for account and server management',
    url='https://www.ocf.berkeley.edu',
    packages=find_packages(),
    package_data={
        'ocflib.printing': ['ocfprinting.schema'],
    },
    install_requires=(
        'cached_property',
        'cracklib',
        'dnspython3',
        'ldap3',
        'paramiko',
        'pexpect',
        'pycrypto',
        'pymysql',
        'pysnmp',
        'pyyaml',
        'redis',
        'requests',
        'sqlalchemy',
    ),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
