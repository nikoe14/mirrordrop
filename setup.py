#!/usr/bin/env python

from setuptools import setup
from os import path
from sys import version_info, prefix

tests_require = []
install_requires = [
    'flask==0.12.2',
]

if version_info < (3,):
    install_requires += ['six>=1.10.0', 'futures>=3.0.5', 'enum34>=1.1.5']

setup(name='mirrordrop',
    version=0.1,
    description='Traffic Drop App',
    author='Nicolas Espejo',
    author_email='nikoe14@gmail.com',
    license='Apache License 2.0',
    install_requires=install_requires,
    classifiers=[
      'Development Status :: 3 - Alpha',
    ],
    data_files=[(
      '{prefix}/mirrordrop_templates'.format(prefix=prefix), [
        'templates/form_delete_rule.html',
        'templates/form_error.html',
        'templates/form_show.html',
        'templates/form_submit.html',
        'templates/form_success.html',
      ]), (
      '{prefix}/mirrordrop_static'.format(prefix=prefix), [
        'static/style.css',
      ])
    ],
    packages=['mirrordrop'],
    entry_points= {  # Optional
      'console_scripts': [
        'mirrordrop=mirrordrop.app:main',
      ],
    },
  )
