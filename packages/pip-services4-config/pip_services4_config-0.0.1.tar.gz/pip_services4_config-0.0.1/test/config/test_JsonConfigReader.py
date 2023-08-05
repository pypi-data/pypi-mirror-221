# -*- coding: utf-8 -*-
"""
    tests.config.test_JsonConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.config import ConfigParams

from pip_services4_config.config import JsonConfigReader


class TestJsonConfigReader:

    def test_read_config(self):
        parameters = ConfigParams.from_tuples(
            "param1", "Test Param 1",
            "param2", "Test Param 2"
        )
        config = JsonConfigReader.read_config(None, "./data/config.json", parameters)
        
        assert 9 == len(config)
        assert 123 == config.get_as_integer("field1.field11")
        assert "ABC" == config.get_as_string("field1.field12")
        assert 123 == config.get_as_integer("field2.0")
        assert "ABC" == config.get_as_string("field2.1")
        assert 543 == config.get_as_integer("field2.2.field21")
        assert "XYZ" == config.get_as_string("field2.2.field22")
        assert True == config.get_as_boolean("field3")
        assert "XYZ" == config.get_as_string("field2.2.field22")
        assert "Test Param 1" == config.get_as_string("field4")
        assert "Test Param 2" == config.get_as_string("field5")

