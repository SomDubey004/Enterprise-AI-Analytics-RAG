from pydantic import BaseModel, Field, SecretStr

class APIConfig(BaseModel):

    base_url: str
    timeout: int = Field(gt= 0)
    api_key: SecretStr