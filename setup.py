import os
import codecs
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-autocomplete',
    version='0.1',
    description="...",
    long_description = read('README.md'),
    author='Sjoerd Arendsen',
    author_email='s.arendsen@hub.nl',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
)
