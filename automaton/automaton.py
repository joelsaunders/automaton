# -*- coding: utf-8 -*-
#
# Copyright 2015 Federico Ficarelli
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__all__ = (
    "Event",
    "Automaton",
)


class Event(object):
    def __init__(self, source_state, dest_state):
        self.source_state = source_state
        self.dest_state = dest_state

    def __repr__(self):
        return "<Event '{}' -> '{}'>".format(self.source_state, self.dest_state)


class AutomatonMeta(type):
    def __new__(mcls, class_name, class_bases, class_dict):
        cls = super().__new__(mcls, class_name, class_bases, class_dict)
        for attr in dir(cls):
            value = getattr(cls, attr)
            if isinstance(value, Event):
                # ...
                pass
        return cls


class Automaton(metaclass=AutomatonMeta):
    pass
