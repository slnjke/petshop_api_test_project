import os
from dotenv import load_dotenv
import pytest
import requests


HOST = "petstore.swagger.io/v2 " if os.environ["STAGE"] == "qa" else "petstore.swagger.io/v1"


@pytest.fixture(scope="session")
def init_environment():
    response = requests.post(
        url=f"{HOST}/user",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 200
