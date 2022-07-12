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

```set(key,value)```\
set value by string key

```get(key)```\
return value by string key

```append(key,more)```\
add more to key's value

```get_all()```\
return all key and value as array

```get_all_key()```\
return all key as array

```delete(key)```\
delete item by key

```exists(key)```\
check if key exists, return boolean