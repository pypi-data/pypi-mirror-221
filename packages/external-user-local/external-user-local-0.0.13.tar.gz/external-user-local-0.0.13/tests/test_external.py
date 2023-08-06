import pytest
import dotenv
import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..'))
from src.external_user import ExternalUser

dotenv.load_dotenv()


@pytest.mark.test
def test_insert_get():
    ExternalUser.insert_or_update_external_user_access_token("test", 2, 1, "test1")
    token = ExternalUser.get_access_token_by_user_name("test", 1)
    assert token[0] == "test1"


@pytest.mark.test
def test_update_access_token():
    ExternalUser.update_user_external(2, "test2")
    token = ExternalUser.get_access_token_by_user_name("test", 1)
    assert token[0] == "test2"


@pytest.mark.test
def test_delete_access_token():
    ExternalUser.delete_access_token_by_profile_id(2)
    token = ExternalUser.get_access_token_by_profile_id(2)
    assert token is None
