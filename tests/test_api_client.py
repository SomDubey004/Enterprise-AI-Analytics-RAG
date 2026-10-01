from enterprise_ai.ingestion.api_client import APIClient

def test_api_client_store_config():
    
    config = {
        "api_url": "https://api.example.com",
        "timeout": 30
    }

    client = APIClient(config)

    assert client.config == config