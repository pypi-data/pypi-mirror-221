import pytest
import unittest

from promptflow.connections import CustomConnection
from yao_test_package2.tools.yao_tool import yao_tool


@pytest.fixture
def my_custom_connection() -> CustomConnection:
    my_custom_connection = CustomConnection(
        {
            "api-key" : "my-api-key",
            "api-secret" : "my-api-secret",
            "api-url" : "my-api-url"
        }
    )
    return my_custom_connection


class TestMyTool1:
    def test_yao_tool(self, my_custom_connection):
        result = yao_tool(my_custom_connection, input_text="Microsoft")
        assert result == "Hello Microsoft"


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
