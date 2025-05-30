#!/bin/bash -ex
# Copyright 2022 Kubeflow Pipelines contributors
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

source_root=$(pwd)

python3 -m pip install --upgrade pip
python3 -m pip install $(grep 'yapf==' sdk/python/requirements-dev.txt)
python3 -m pip install pre_commit_hooks
python3 -m pre_commit_hooks.string_fixer $(find sdk/python/kfp/**/*.py -type f)
yapf --recursive --diff "${source_root}/sdk/python/"
