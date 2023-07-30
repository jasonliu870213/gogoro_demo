import pytest, requests, os
from dotenv.main import load_dotenv


@pytest.fixture()
def session():
    result = requests.Session()
    return result


if 'ENV_FILE' in os.environ:
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)

else:
    load_dotenv()
    print('jason')