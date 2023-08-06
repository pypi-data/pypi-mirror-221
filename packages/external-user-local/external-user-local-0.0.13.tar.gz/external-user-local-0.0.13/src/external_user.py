import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))

from db.external_user_db import ExternalUserDb
from logger_local.LoggerLocal import logger_local
import dotenv

dotenv.load_dotenv()
EXTERNAL_USER_COMPONENT_ID = 115
object_init = {
    'component_id': EXTERNAL_USER_COMPONENT_ID,
    'component_name': 'external-user-local-python-package'
}
logger_local.init(object=object_init)


class ExternalUser:
    
    @staticmethod
    def insert_or_update_external_user_access_token(user_name, profile_id, system_id, access_token):
        object_start = {
            'user_name': user_name,
            'profile_id': profile_id,
            'system_id': system_id,
            'access_token': access_token
        }
        logger_local.start(object=object_start)
        ExternalUserDb.insert_or_update_external_user_access_token(
            user_name, profile_id, system_id, access_token)
        logger_local.end(object={})

    @staticmethod
    def update_user_external(profile_id, access_token):
        object_start = {
            'profile_id': profile_id,
            'access_token': access_token
        }
        logger_local.start(object=object_start)
        ExternalUserDb.update_by_profile_id(profile_id, access_token)
        logger_local.end(object={})

    @staticmethod
    def get_access_token_by_profile_id(profile_id):
        object_start = {
            'profile_id': profile_id
        }
        logger_local.start(object=object_start)
        res = ExternalUserDb.select_by_profile_id(profile_id)
        logger_local.end(object={'access_token': res})
        return res

    @staticmethod
    def get_access_token_by_user_name(user_name, system_id):
        object_start = {
            'user_name': user_name,
            'system_id': system_id
        }
        logger_local.start(object=object_start)
        res = ExternalUserDb.get_by_user_name(user_name, system_id)
        logger_local.end(object={'access_token': res})
        return res

    @staticmethod
    def delete_access_token_by_profile_id(profile_id):
        object_start = {
            'profile_id': profile_id
        }
        logger_local.start(object=object_start)
        ExternalUserDb.delete_by_profile_id(profile_id)
        logger_local.end(object={})

    @staticmethod
    def update_user_external_by_user_name(user_name, system_id, access_token):
        object_start = {
            'user_name': user_name,
            'system_id': system_id,
            'access_token': access_token
        }
        logger_local.start(object=object_start)
        ExternalUserDb.update_by_user_name(user_name, access_token)
        logger_local.end(object={})
