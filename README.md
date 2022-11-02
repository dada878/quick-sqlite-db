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
Connect to database

```db.set(key,value)```\
Set value by key and retune the value

```db.get(key)```\
Return value by string key

```db.append(key,more)```\
Add more to key's value

```db.get_all()```\
Return all key and value as array

```db.get_all_key()```\
Return all key as array

```db.delete(key)```\
Delete item by key

```db.exists(key)```\
Check if key exists, return boolean

```db.change_name(name)```\
Change the table name

```db.remove(key,more)```\
Remove some value from the key and retune the value

```db.append(key,more)```\
Add some value from the key and retune the value