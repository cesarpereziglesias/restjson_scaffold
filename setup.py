# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
]

setup(
    name='restjson_scaffold',
    version='0.1.0',
    author='Cesar Perez',
    author_email='cesarpereziglesias@gmail.com',
    url='https://github.com/ouvigna/restjson_scaffold',
    license='LICENSE.txt',
    description='Pyramid scaffold to create REST/JSON services',
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points="""\
        [pyramid.scaffold]
        restjson=restjson_scaffold.scaffolds:RestJsonTemplate
    """,
)
