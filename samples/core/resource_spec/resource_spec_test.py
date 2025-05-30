# Copyright 2021 The Kubeflow Authors
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

from kfp.samples.test.utils import run_pipeline_func
from kfp.samples.test.utils import TestCase
from resource_spec import my_pipeline


def EXPECTED_OOM(run_id, run, **kwargs):
    """confirms a sample test case is failing, because of OOM."""
    assert run.status == 'Failed'


run_pipeline_func([
    TestCase(pipeline_func=my_pipeline,),
    TestCase(
        pipeline_func=my_pipeline,
        arguments={'n': 21234567},
        verify_func=EXPECTED_OOM,
    ),
])
