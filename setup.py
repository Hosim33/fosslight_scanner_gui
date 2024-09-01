#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Copyright (c) 2021 LG Electronics Inc.

# SPDX-License-Identifier: Apache-2.0

from codecs import open

import os

import shutil

from setuptools import setup, find_packages



with open('README.md', 'r', 'utf-8') as f:

    readme = f.read()



with open('requirements.txt', 'r', 'utf-8') as f:

    install_requires = f.read().splitlines()



_PACKAEG_NAME = 'fosslight_Scanner_Gui'

_LICENSE_FILE = 'LICENSE'

_LICENSE_DIR = 'LICENSES'



if __name__ == "__main__":

    dest_path = os.path.join('src', _PACKAEG_NAME, _LICENSE_DIR)

    try:

        if not os.path.exists(dest_path):

            os.mkdir(dest_path)

        if os.path.isfile(_LICENSE_FILE):

            shutil.copy(_LICENSE_FILE, dest_path)

        if os.path.isdir(_LICENSE_DIR):

            license_f = [f_name for f_name in os.listdir(_LICENSE_DIR) if f_name.upper().startswith(_LICENSE_FILE)]

            for lic_f in license_f:

                shutil.copy(os.path.join(_LICENSE_DIR, lic_f), dest_path)

    except Exception as e:

        print(f'Warning: Fail to copy the license text: {e}')



    setup(

        name=_PACKAEG_NAME,

        version='1.0.0',

        package_dir={"": "src"},

        packages=find_packages(where='src'),

        description='FOSSLight Scanner Gui',

        long_description=readme,

        long_description_content_type='text/markdown',

        license='Apache-2.0',

        author='LG Electronics',

        url='https://github.com/fosslight/fosslight_scanner_gui',

        download_url='https://github.com/fosslight/fosslight_scanner_gui',

        classifiers=['License :: OSI Approved :: Apache Software License',

                     "Programming Language :: Python :: 3",

                     "Programming Language :: Python :: 3.6",

                     "Programming Language :: Python :: 3.7",

                     "Programming Language :: Python :: 3.8",

                     "Programming Language :: Python :: 3.9", ],

        install_requires=install_requires,

        extras_require={

            ':sys_platform == "win32"': [

                'python-magic-bin'

            ],

            ':"darwin" in sys_platform': [

                'python-magic'

            ],

            ':"linux" in sys_platform': [

                'python-magic'

            ],

        },

        package_data={_PACKAEG_NAME: [os.path.join(_LICENSE_DIR, '*')]},

        include_package_data=True,


    )

    shutil.rmtree(dest_path, ignore_errors=True)