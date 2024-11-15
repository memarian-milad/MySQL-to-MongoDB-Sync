<h1 align="left">MySQL to MongoDB Sync</h1>

📖 Overview
-----------

This Python project transfers data from a MySQL database to a MongoDB database using **OOP principles**. It allows the user to sync tables from MySQL as collections in MongoDB, providing options to delete existing MongoDB documents before insertion.

🛠 Features
-----------

*   **Automatic Table Detection**: Detects all tables in the MySQL database.
    
*   **Full Data Sync**: Transfers all rows of each table as documents in MongoDB.
    
*   **Clean MongoDB Collections**: Optionally deletes existing documents before inserting new ones.
    
*   **OOP Design**: Fully structured with classes and methods.
    

🚀 How to Use
-------------

### 1\. Prerequisites

*   Python 3.7+
    
*   MySQL Server
    
*   MongoDB Server
    
*   Python Packages:
    
    *   mysql-connector-python
        
    *   pymongo
        

Install the required packages:

```bash
  pip install mysql-connector-python pymongo
```
    
### 2\. Configuration

Update the MySQL and MongoDB configurations in the \_\_main\_\_ section of the script:

```bash
MYSQL_CONFIG = {
    "host": "localhost",
    "database": "sarveno",
    "user": "root",
    "password": ""
}

MONGO_CONFIG = {
    "uri": "mongodb://root:example@mongo:8082/",
    "database": "sarveno"
}
```
### 3\. Run the Script

Execute the script:

```bash
python sync.py
```

📌 Notes
--------

*   Ensure both MySQL and MongoDB services are running.
    
*   The script uses dictionary cursors for easier record handling.
    
*   Connection errors are automatically handled; ensure credentials are correct.
    

🤝 Contributing
---------------

Feel free to fork and modify the project. Contributions are welcome!

License
-------

This project is licensed under the MIT License.