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

from jenkinsapi import jenkins

class Connector(object):
    """Jenkins connection wrapper
    """

    def __init__(self, config):
        if not config:
            raise RuntimeError("No configuration file provided")

        jenkins_instance_url = config.get('defaults', 'url')
        jenkins_user = config.get('defaults','username')
        jenkins_passwd = config.get('defaults', 'password')

        self.config = config
        self.connection = jenkins.Jenkins(baseurl=jenkins_instance_url,
            username=jenkins_user, password=jenkins_passwd)

    def get_job(self):
        """get job
        """
        test_job = self.config.get('defaults', 'job')
        return self.connection.get_job(jobname=test_job)

    def get_raw_result(self):
        """return unformatted report as returned by the jenkins instance
        """
        if self.connection:
            last_good_build = self.get_job().get_last_good_build()

            if last_good_build and last_good_build.has_resultset():
                return last_good_build.get_resultset()._data
            else:
                return EnvironmentError("No tests have run")
        else:
            raise RuntimeError("Connection lost")

    def get_result(self):
        """ Returns the test result for the job as a dictionary
        """
        return self.get_raw_result()
