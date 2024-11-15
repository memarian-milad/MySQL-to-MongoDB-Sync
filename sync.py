import mysql.connector
import pymongo


class DatabaseSync:
    """
    A class to handle data migration from MySQL to MongoDB.

    Attributes:
        mysql_config (dict): Configuration for MySQL connection.
        mongo_config (dict): Configuration for MongoDB connection.
        delete_existing_documents (bool): Whether to delete existing MongoDB documents before inserting new data.
    """

    def __init__(self, mysql_config, mongo_config, delete_existing_documents=True):
        """
        Initializes the DatabaseSync object with MySQL and MongoDB configurations.

        Args:
            mysql_config (dict): Configuration dictionary for MySQL.
            mongo_config (dict): Configuration dictionary for MongoDB.
            delete_existing_documents (bool): Flag to indicate if existing documents in MongoDB should be deleted.
        """
        self.mysql_config = mysql_config
        self.mongo_config = mongo_config
        self.delete_existing_documents = delete_existing_documents

    def connect_to_mysql(self):
        """
        Establishes a connection to the MySQL database.

        Returns:
            mysql.connector.connection_cext.CMySQLConnection: MySQL connection object.
        """
        return mysql.connector.connect(
            host=self.mysql_config["host"],
            database=self.mysql_config["database"],
            user=self.mysql_config["user"],
            password=self.mysql_config["password"]
        )

    def connect_to_mongodb(self):
        """
        Establishes a connection to the MongoDB database.

        Returns:
            pymongo.database.Database: MongoDB database object.
        """
        client = pymongo.MongoClient(self.mongo_config["uri"])
        return client[self.mongo_config["database"]]

    def sync_data(self):
        """
        Synchronizes data from MySQL to MongoDB.
        """
        # Connect to databases
        mysql_connection = self.connect_to_mysql()
        mongo_db = self.connect_to_mongodb()

        try:
            cursor = mysql_connection.cursor(dictionary=True)
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[f'Tables_in_{self.mysql_config["database"]}']
                cursor.execute(f"SELECT * FROM {table_name};")
                records = cursor.fetchall()

                if records:
                    collection = mongo_db[table_name]

                    if self.delete_existing_documents:
                        collection.delete_many({})  # Delete all documents in the collection

                    result = collection.insert_many(records)
                    print(f"{table_name}: {len(result.inserted_ids)} records inserted.")
        finally:
            mysql_connection.close()


if __name__ == "__main__":
    # MySQL Configuration
    MYSQL_CONFIG = {
        "host": "localhost",
        "database": "database-name",
        "user": "user-name",
        "password": "password"
    }

    # MongoDB Configuration
    MONGO_CONFIG = {
        "uri": "mongodb://root:example@mongo:8082/",
        "database": "database-name"
    }

    # Initialize the sync process
    sync_process = DatabaseSync(MYSQL_CONFIG, MONGO_CONFIG, delete_existing_documents=True)
    sync_process.sync_data()
