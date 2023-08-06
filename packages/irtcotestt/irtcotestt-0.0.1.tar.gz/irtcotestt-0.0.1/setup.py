from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'test'

# Setting up
setup(
    name="irtcotestt",
    version=VERSION,
    author="irtco",
    author_email="<mail@test.com>",
    description=DESCRIPTION,
    long_description_content_type="textmarkdown",
    packages=find_packages(),
    install_requires=[''],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
)