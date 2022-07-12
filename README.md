# Quick-sqlite
### Overview
A lightweight key-value database basic sqlite.
### Install
```
pip install quick-sqlite-database
```
### Example
```py
from quick_sqlite import Database

db = Database("example.db")

db.set("name", "Dada878")

db.get("name") #Dada878
```
### Documentation
```Database(path, tableName?)```\
connect to database

```db.set(key,value)```\
set value by string key

```db.get(key)```\
return value by string key

```db.append(key,more)```\
add more to key's value

```db.get_all()```\
return all key and value as array

```db.get_all_key()```\
return all key as array

```db.delete(key)```\
delete item by key

```db.exists(key)```\
check if key exists, return boolean