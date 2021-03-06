# Copyright (c) 2015 Intel Research and Development Ireland Ltd.
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

import unittest
from experimental_framework.constants import conf_file_sections as cfs

__author__ = 'vmriccox'


class TestConfFileSection(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_sections_api_for_success(self):
        expected = ['PacketGen', 'General', 'InfluxDB', 'OpenStack']
        output = cfs.get_sections_api()
        self.assertEqual(expected, output)
