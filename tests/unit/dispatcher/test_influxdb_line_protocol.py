# Unittest for yardstick.dispatcher.influxdb_line_protocol

# yardstick comment: this file is a modified copy of
# influxdb-python/influxdb/tests/test_line_protocol.py

import unittest
from third_party.influxdb.influxdb_line_protocol import make_lines


class TestLineProtocol(unittest.TestCase):

    def test_make_lines(self):
        data = {
            "tags": {
                "empty_tag": "",
                "none_tag": None,
                "integer_tag": 2,
                "string_tag": "hello"
            },
            "points": [
                {
                    "measurement": "test",
                    "fields": {
                        "string_val": "hello!",
                        "int_val": 1,
                        "float_val": 1.1,
                        "none_field": None,
                        "bool_val": True,
                    }
                }
            ]
        }

        self.assertEqual(
            make_lines(data),
            'test,integer_tag=2,string_tag=hello '
            'bool_val=True,float_val=1.1,int_val=1i,string_val="hello!"\n'
        )

    def test_string_val_newline(self):
        data = {
            "points": [
                {
                    "measurement": "m1",
                    "fields": {
                        "multi_line": "line1\nline1\nline3"
                    }
                }
            ]
        }

        self.assertEqual(
            make_lines(data),
            'm1 multi_line="line1\\nline1\\nline3"\n'
        )
