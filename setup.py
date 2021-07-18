# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='iot_api',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'uvicorn==0.14.0',
            'click==8.0.1',
            'asgiref==3.4.1',
            'h11==0.12.0',
        'starlette==0.15.0',
            'anyio==3.2.1',
            'idna==3.2',
            'sniffio==1.2.0',
        'httpx==0.18.2',
            'httpcore==0.13.6',
            'rfc3986[idna2008]==1.5.0',
            'certifi',
        'aiosqlite==0.17.0',
    ])
