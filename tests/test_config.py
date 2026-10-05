import pytest
from pydantic import ValidationError

from enterprise_ai.config import APIConfig

def test_api_config_creation():
    config = APIConfig(
        base_url="https://api.example.com",
        timeout=30,
        api_key="my_api_key"
    )

    assert config.base_url == "https://api.example.com"
    assert config.timeout == 30
    assert config.api_key.get_secret_value() == "my_api_key"

def test_api_config_invalid_timeout():
    with pytest.raises(ValidationError):
        APIConfig(
            base_url="https://api.example.com",
            timeout=-10,
            api_key="my_api_key"
        )