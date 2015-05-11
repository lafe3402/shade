# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.V

"""
fakes
----------------------------------

Fakes used for testing
"""


class FakeFlavor(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FakeImage(object):
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status


class FakeProject(object):
    def __init__(self, id):
        self.id = id


class FakeServer(object):
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status


class FakeUser(object):
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name


class FakeVolume(object):
    def __init__(self, id, status, display_name):
        self.id = id
        self.status = status
        self.display_name = display_name