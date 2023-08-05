from circles_local_database_python.database import database
from dotenv import load_dotenv
from logger_local_python_package.LoggerLocal import logger_local
from functools import wraps
load_dotenv()

object_init = {
    'component_id': 114
}
logger_local.init(object=object_init)
USER_ID = 1


def log_function_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        object1 = {
            'args': str(args),
            'kawargs': str(kwargs),
        }
        logger_local.start(object=object1)
        result = func(*args, **kwargs)  # Execute the function
        object2 = {
            'result': result,
        }
        logger_local.end(object=object2)
        return result
    return wrapper


class Importer:
    def __init__(self, source):
        self.source_name = source

    @log_function_execution
    def insert_new_entity(self, entity_type_name):
        object1 = {
            'entity_type_name': entity_type_name
        }
        logger_local.start(object=object1)
        database_conn = database()
        db = database_conn.connect_to_database()
        cursor = db.cursor()

        cursor.execute("SELECT entity_type_id FROM entity_type.entity_type_ml_table WHERE entity_type_name = '{}'".format(
            entity_type_name))
        entity_type_id = cursor.fetchone()

        if not entity_type_id:
            query_entity = "INSERT INTO entity_type.entity_type_table(`created_user_id`,`updated_user_id`)" \
                " VALUES ({}, {})".format(USER_ID, USER_ID)
            cursor.execute(query_entity)
            db.commit()
            last_inserted_id = cursor.lastrowid
            query_entity_ml = "INSERT INTO entity_type.entity_type_ml_table(`entity_type_name`,`entity_type_id`,`lang_code`,`created_user_id`,`updated_user_id`)" \
                              " VALUES (%s, %s, %s, {}, {})".format(
                                  USER_ID, USER_ID)
            cursor.execute(query_entity_ml,
                           (entity_type_name, last_inserted_id, 'en'))
            logger_local.end(object={})
            db.commit()
        else:
            logger_local.end("Entity %s already exist." % entity_type_name)
        db.close()

    @log_function_execution
    def insert_new_source(self):
        logger_local.start(object={})
        database_conn = database()
        db = database_conn.connect_to_database()
        cursor = db.cursor()

        cursor.execute("SELECT source_id FROM source.source_ml_table WHERE source_name = '{}'".format(
            self.source_name))
        source_id = cursor.fetchone()

        if not source_id:
            query_importer_source = "INSERT INTO source.source_table(`created_user_id`,`updated_user_id`)" \
                " VALUES (1, 1)"
            cursor.execute(query_importer_source)
            db.commit()

            last_inserted_id = cursor.lastrowid
            query_importer_source_ml = "INSERT INTO source.source_ml_table(`source_name`,`source_id`,`created_user_id`,`updated_user_id`)" \
                " VALUES (%s, %s, 1, 1)"
            cursor.execute(query_importer_source_ml,
                           (self.source_name, last_inserted_id))
            db.commit()
            logger_local.end(object={"source name": self.source_name})
        else:
            logger_local.end(
                object={"message": "Source %s already exist." % self.source_name})
        db.close()

    @log_function_execution
    def insert_record_source(self, location_id, entity_type_name, entity_id, url):

        object1 = {
            'entity_type_name': entity_type_name,
            'entity_id': entity_id,
            'url': url,
            'location_id':location_id
        }
        logger_local.start(object=object1)
        database_conn = database()
        db = database_conn.connect_to_database()
        cursor = db.cursor()

        cursor.execute("SELECT source_id FROM source.source_ml_table WHERE source_name = '{}'".format(
            self.source_name))
        source_id = cursor.fetchone()

        cursor.execute(
            "SELECT country_id FROM location.location_table WHERE name = '{}'".format(location_id))
        country_id = cursor.fetchone()

        cursor.execute("SELECT entity_type_id FROM entity_type.entity_type_ml_table WHERE entity_type_name = '{}'".format(
            entity_type_name))
        entity_type_id = cursor.fetchone()

        query_importer = "INSERT INTO importer.importer_table(`source_id`,`country_id`,`entity_type_id`,`entity_id`,`url`,`created_user_id`,`updated_user_id`)" \
            " VALUES (%s, %s, %s, %s, %s, 1, 1)"

        cursor.execute(
            query_importer, (source_id[0], country_id[0], entity_type_id[0], entity_id, url))

        db.commit()
        db.close()
        logger_local.end(object={})


if __name__ == "__main__":
    pass
