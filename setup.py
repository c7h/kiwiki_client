from setuptools import find_packages, setup

REQUIRED = [
    'requests', 'python-dateutil'
]

setup(
    name='kiwiki_client',
    description='KIWI Lock Client Library',
    version='0.1',
    author='Christoph Gerneth',
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED
)
