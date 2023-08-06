# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Common utils for connectors
"""
from datetime import datetime
import io
import csv

def serialize_csv(fieldnames, jsons):
    """
    Convert json of contents into string
    """
    csv_output = io.StringIO()
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()
    for json_obj in jsons:
        writer.writerow(json_obj)
    csv_str = csv_output.getvalue()
    csv_output.close()
    return csv_str

def save_csv(name, text, encoding='utf8'):
    """
    Write text to file
    """
    with open(name, "a", encoding=encoding) as csv_file:
        csv_file.write(text)


def get_name(prefix):
    """
    Construct name with current timestamp
    """
    time_stamp = datetime.utcnow().strftime("%H-%M-%S")
    return f"{prefix}-{time_stamp}"

def get_or_raise_error(config, param_name):
    """
    Function used for several connectors for validating if
    `config` dict contains a `param_name` key defined
    :param config:
    :param param_name:
    :return:
    """
    if param_name not in config:
        raise ValueError(
            f"Connector needs the `{param_name}` param to be defined. " +
            "Please use Unify Connector Portal.",
            )
    return config[param_name]
