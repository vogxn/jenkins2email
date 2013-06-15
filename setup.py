# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from distribute_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError:
        raise RuntimeError("python setuptools is required")

VERSION = '0.1.0'

import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

setup(name="Jenkins2Email",
    version=VERSION,
    description="Jenkins2Email - Convert Jenkins Test Result to PlainText Email",
    author="Prasanna Santhanam",
    author_email="tsp@apache.org",
    long_description="Jenkins2Email - Convert Jenkins Test Result to PlainText Email",
    platforms=("Any",),
    packages=["src"],
    license="ASLv2",
    install_requires=[
        "jenkinsapi",
        "tabulate"
    ],
    zip_safe=True,
    entry_points="""
    [console_scripts]
    jenkins2email = src.main:main
    """
)