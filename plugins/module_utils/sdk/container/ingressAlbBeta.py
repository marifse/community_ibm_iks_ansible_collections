# coding: utf-8

# Copyright 2022 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
import traceback

try:
    import requests
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True


class IngressALBBeta:
    """IngressAlbBeta class to support following functionalities.
    * update_alb
    * create_alb
    * disable_alb
    * enable_alb
    """

    # Class Variable
    DEFAULT_SERVICE_URL = "https://containers.cloud.ibm.com/global/"

    # The init method or constructor
    def __init__(self, cluster_id):

        # Instance Variable
        self.cluster_id = cluster_id

    # Method to fetch error code based on status code
    def get_status(self, status_code):
        if status_code == 200 or status_code == 204:
            status = "OK. Request successfully processed"
        elif status_code == 401:
            status = "Unauthorized. The IAM token is invalid or expired."
        elif status_code == 404:
            status = "Not found. The specified cluster could not be found."
        elif status_code == 500:
            status = "Internal Server Error. IBM Cloud Kubernetes Service is currently unavailable."
        else:
            status = "ERROR. status_code mismatch"
        return status

    # Method to update the ALB in the Cluster
    def updateAlb(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/alb/updateAlb"
        response = requests.post(
            IngressALBBeta.DEFAULT_SERVICE_URL + TARGET_URL,
            headers=headers,
            json=data["config"],
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False, response.json()
        elif response.status_code == 404:
            return True, False, response.json()
        elif response.status_code == 500:
            return True, False, response.json()
        else:
            return True, False, response.json()

    # Method to create the ALB in the Cluster
    def createAlb(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/alb/vpc/createAlb"
        response = requests.post(
            IngressALBBeta.DEFAULT_SERVICE_URL + TARGET_URL,
            headers=headers,
            json=data["config"],
        )

        if response.status_code == 200 or response.status_code == 201:
            return False, True, response.json()
        elif response.status_code == 401:
            return True, False, response.json()
        elif response.status_code == 404:
            return True, False, response.json()
        elif response.status_code == 500:
            return True, False, response.json()
        else:
            return True, False, response.json()

    # Method to disable the ALB in the Cluster
    def disableAlb(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/alb/vpc/disableAlb"
        response = requests.post(
            IngressALBBeta.DEFAULT_SERVICE_URL + TARGET_URL,
            headers=headers,
            json=data["config"],
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False, response.json()
        elif response.status_code == 404:
            return True, False, response.json()
        elif response.status_code == 500:
            return True, False, response.json()
        else:
            return True, False, response.json()

    # Method to enable the ALB in the Cluster
    def enableAlb(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/alb/vpc/enableAlb"
        response = requests.post(
            IngressALBBeta.DEFAULT_SERVICE_URL + TARGET_URL,
            headers=headers,
            json=data["config"],
        )

        if (
            response.status_code == 200
            or response.status_code == 204
            or response.status_code == 201
        ):
            return False, True
        elif response.status_code == 401:
            return True, False, response.json()
        elif response.status_code == 404:
            return True, False, response.json()
        elif response.status_code == 500:
            return True, False, response.json()
        else:
            return True, False, response.json()
