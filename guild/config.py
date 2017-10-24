# Copyright 2017 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

_cwd = None
_guild_home = None

def set_cwd(cwd):
    globals()["_cwd"] = cwd

def set_guild_home(path):
    globals()["_guild_home"] = path

def cwd():
    if _cwd is None:
        raise SystemExit("cwd is not configured")
    return _cwd

def guild_home():
    if _guild_home is None:
        raise SystemExit("guild_home is not configured")
    return _guild_home
