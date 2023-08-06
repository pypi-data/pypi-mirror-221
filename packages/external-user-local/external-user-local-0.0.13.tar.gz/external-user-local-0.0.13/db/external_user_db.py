import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..', 'db'))
from config import db_connection
from dotenv import load_dotenv
from logger_local.LoggerLocal import logger_local
import mysql.connector



load_dotenv()
COMPONENT_ID = 115
object_init = {
    'component_id': COMPONENT_ID
}
logger_local.init(object=object_init)
CONN = db_connection()
CURSOR = CONN.cursor()


class ExternalUserDb:
    def __init__(self):
        pass

    @staticmethod
    def insert_or_update_external_user_access_token(user_name, profile_id, system_id, access_token):
        try:
            object_start = {
                'user_name': user_name,
                'profile_id': profile_id,
                'access_token': access_token
            }
            logger_local.start(object=object_start)
            cursor = CONN.cursor()
            query_insert_external = "INSERT INTO external_user.external_user_table (system_id,username,token) VALUES (%s,%s,%s)"
            values = (system_id, user_name, access_token)
            cursor.execute(query_insert_external, values)
            CONN.commit()
            cursor.close()
            cursor = CONN.cursor()
            query_id = "SELECT id FROM external_user.external_user_table WHERE token=%s"
            cursor.execute(query_id, (access_token,))
            res = cursor.fetchone()
            cursor.close()
            id_new = res[0]
            cursor = CONN.cursor()
            query_max_id = "SELECT MAX(id) FROM external_user_profile.external_user_profile_table"
            cursor.execute(query_max_id)
            res = cursor.fetchone()
            cursor.close()
            max_id = res[0] + 1
            cursor = CONN.cursor()
            values = (max_id, id_new, profile_id)
            query_insert_external_user_profile = "INSERT INTO external_user_profile.external_user_profile_table (id,external_user_id,profile_id) VALUES (%s,%s,%s)"
            cursor.execute(query_insert_external_user_profile, values)
            cursor.close()
            CONN.commit()
            logger_local.end(object={})
        except mysql.connector.Error as error:
            logger_local.exception(object=error)

    @staticmethod
    def get_by_user_name(user_name, system_id):
        try:
            object_start = {
                'user_name': user_name
            }
            logger_local.start(object=object_start)
            cursor = cursor = CONN.cursor()
            query_get_all = "SELECT token FROM external_user.external_user_table WHERE username=%s AND system_id=%s"
            cursor.execute(query_get_all, (user_name, system_id))
            res = cursor.fetchone()
            logger_local.end(object={'res': res})
            return res
        except mysql.connector.Error as error:
            logger_local.exception(object=error)

    @staticmethod
    def select_by_profile_id(profile_id):
        try:
            object_start = {
                'profile_id': profile_id
            }
            logger_local.start(object=object_start)
            cursor = CONN.cursor()

            # Execute the select query
            select_query = """
                SELECT * 
                FROM external_user.external_user_table AS eu 
                JOIN external_user_profile.external_user_profile_table AS eup ON eu.id = eup.external_user_id 
                WHERE eup.profile_id = %s
            """
            cursor.execute(select_query, (profile_id,))
            result = cursor.fetchone()
            cursor.close()
            logger_local.end(object={'access_token': result})
            return result
        except mysql.connector.Error as error:
            logger_local.exception(object=error)

    @staticmethod
    def update_by_user_name(user_name, access_token):
        try:
            object_start = {
                'user_name': user_name,
                'access_token': access_token
            }
            logger_local.start(object=object_start)
            cursor = CONN.cursor()
            update_query = "UPDATE external_user.external_user_table SET token = %s WHERE username = %s"
            values = (access_token, user_name)
            cursor.execute(update_query, values)
            CONN.commit()
            cursor.close()
            logger_local.end(object={})
        except mysql.connector.Error as error:
            logger_local.exception(object=error)

    @staticmethod
    def update_by_profile_id(profile_id, access_token):
        try:
            object_start = {
                'profile_id': profile_id,
                'access_token': access_token
            }
            logger_local.start(object=object_start)
            cursor = CONN.cursor()

            update_query = """
                UPDATE external_user.external_user_table 
                SET token = %s 
                WHERE id IN (
                    SELECT external_user_id
                    FROM external_user_profile.external_user_profile_table 
                    WHERE profile_id = %s
                )
            """
            values = (access_token, profile_id)
            cursor.execute(update_query, values)
            CONN.commit()
            cursor.close()
            logger_local.end(object={})
        except mysql.connector.Error as error:
            logger_local.exception(error)

    @staticmethod
    def delete_by_profile_id(profile_id):
        try:
            object_start = {
                'profile_id': profile_id
            }
            logger_local.start(object=object_start)
            # Create a cursor object to execute queries
            cursor = CONN.cursor()
            get_query = """Select external_user_id FROM external_user_profile.external_user_profile_table where profile_id=%s"""
            cursor.execute(get_query, (profile_id,))
            external_user_ids = cursor.fetchone()
            delete_query = """UPDATE external_user_profile.external_user_profile_table
SET external_user_id = NULL, profile_id = NULL WHERE profile_id=%s;"""
            cursor.execute(delete_query, (profile_id,))
            for id in external_user_ids:

                delete_query = """
                UPDATE external_user.external_user_table 
                SET token = NULL,system_id=NULL, username=NULL
                WHERE id = %s
            """
                cursor.execute(delete_query, (id,))

            CONN.commit()
            cursor.close()
            logger_local.end(object={})
        except mysql.connector.Error as error:
            logger_local.exception(object=error)
