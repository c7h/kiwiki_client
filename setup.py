from setuptools import find_packages, setup

REQUIRED = [
    'requests', 'python-dateutil'
]

setup(
    name='kiwiki_client',
    description='KIWI Lock Client Library',
    version='0.1.2',
    author='Christoph Gerneth',
    author_email='christoph.gerneth@gmail.com',
    url='https://github.com/c7h/kiwiki_client',
    packages=find_packages(exclude=('tests',)),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    install_requires=REQUIRED
)
