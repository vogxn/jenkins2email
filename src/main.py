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

from ConfigParser import SafeConfigParser
from argparse import ArgumentParser
from connector import Connector
from parser import Parser
from os import path

PROPERTIES_FILE='jmail.cfg'

def main():
    config = SafeConfigParser()
    config.read(PROPERTIES_FILE)
    ctor = Connector(config)
    report = ctor.get_result()

    prsr = Parser()
    prsr.parse(report)
    prsr.format()

if __name__ == '__main__':
    opts = ArgumentParser()
    opts.add_argument("-c","--config",dest="config",help="Path to configuration file")
    args = opts.parse_args()

    if args.config and path.exists(args.config):
        PROPERTIES_FILE = args.config
    else:
        raise RuntimeError("Need a configuration file")
    main()
