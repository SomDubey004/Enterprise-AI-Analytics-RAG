from enterprise_ai.config import APIConfig

class APIClient:

    def __init__(self, config: APIConfig):
        self.config = config