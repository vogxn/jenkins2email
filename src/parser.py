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

from tabulate import tabulate

class Parser(object):

    def __init__(self):
        self.summary = {}
        self.report = {}
        self.header = ["name", "pass", "fail", "skip"]
        self.number = 0 #build number

        self.table = [] #table holding overall summary
        self.fixed = [] #table holding fixed tests
        self.regressions = [] #table for regressions
        self.failures = [] #table for failures

    def format(self):
        """Format into table for plaintext output"""
        print "Test Run: #{}".format(self.number)
        print "--------"
        print "{}:{}".format("Total", self.summary['total'])
        print "{}:{}".format("Fail ", self.summary['fail'])
        print "{}:{}".format("Skip ", self.summary['skip'])
        print "--------\n"
        print tabulate(self.table, headers=self.header, tablefmt="plain")
        print "--------\n"

        print "\nRegressions"
        print "--------"
        print tabulate(self.regressions, headers=["name", "duration", "age"], tablefmt="plain")

        print "\nFailures"
        print "--------"
        print tabulate(self.failures, headers=["name", "duration", "age"], tablefmt="plain")

        print "\nFixed"
        print "--------"
        print tabulate(self.fixed, headers=["name", "duration", "age"], tablefmt="plain")

    def parse(self, report):
        """Parse report JSON from jenkins for tabulate processing"""
        self.report = report
        self.summary['total'] = self.report['totalCount']
        self.summary['fail'] = self.report['failCount']
        self.summary['skip'] = self.report['skipCount']

        suite_details = self.report['childReports']
        for suite in suite_details:
            self.number = suite['child']['number']
            #FIXME: This custom name building logic might not always work
            suite_name = suite['child']['url'].split("suite=")[-1].split(str(self.number))[0]
            suite_summary = {}
            suite_summary['pass'] = suite['result']['passCount']
            suite_summary['fail'] = suite['result']['failCount']
            suite_summary['skip'] = suite['result']['skipCount']
            self.table.append([suite_name, suite_summary['pass'], suite_summary['fail'], suite_summary['skip']])

            suites = suite['result']['suites']
            for suit in suites:
                for case in suit['cases']:
                    if case['status'] == "REGRESSION":
                        self.regressions.append(["{}.{}".format(case['className'], case['name']),
                                                 case['duration'],
                                                 case['age']
                        ])
                    elif case['status'] == "FAILED":
                        self.failures.append(["{}.{}".format(case['className'], case['name']),
                                                 case['duration'],
                                                 case['age']
                        ])
                    elif case['status'] == "FIXED":
                        self.fixed.append(["{}.{}".format(case['className'], case['name']),
                                                 case['duration'],
                                                 case['age']
                        ])

