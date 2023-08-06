from setuptools import setup,find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Common functionality to share among different services in bidso'

setup(
    name = "common_bidso",
    version=VERSION,
    author="Bidso Dev",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['PyJWT==2.6.0','djangorestframework==3.14.0','Django==4.2']
)
