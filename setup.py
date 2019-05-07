# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-canihitit',
    version='0.0.4',
    author=u'Jon Combe',
    author_email='jon@naremit.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url='https://github.com/joncombe/django-canihitit',
    license='BSD licence, see LICENCE file',
    description='Tiny object hit counter for Django',
    long_description='Tiny object hit counter for Django',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
