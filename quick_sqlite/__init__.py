import json
import sqlite3
from typing import List
from xmlrpc.client import Boolean

class DatabaseItem():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class Database():
    """
    Quick-Sqlite-Database
    """
    def __init__(self, path: str, db_name: str = "__default__", auto_init: any = None) -> None:
        self.conn = sqlite3.connect(path)
        self.name = db_name
        self.auto_init = auto_init

        c = self.conn.cursor()
        check = c.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.name}';")

        if (not list(check)):
            c = self.conn.cursor()
            c.execute(
                f'CREATE TABLE `{self.name}` (`key` CHAR(255) NOT NULL PRIMARY KEY, `value` JSON);')
            self.conn.commit()

    def set(self, key, value) -> any:
        """
        Set value by key and retune the value
        """
        c = self.conn.cursor()
        c.execute(
            f'REPLACE INTO `{self.name}` VALUES ("{key}", \'{json.dumps(value)}\');')
        self.conn.commit()
        return value

    def get(self, key, no_init=False) -> any:
        """
        Get value by key
        """
        c = self.conn.cursor()
        result = list(c.execute(f'SELECT `value` FROM `{self.name}` WHERE `key` == "{key}";'))

        if result:
            try:
                return json.loads(result[0][0])
            except:
                return result[0][0]
        elif self.auto_init != None and not no_init: #有使用 auto init
            self.set(key, self.auto_init)
            return self.auto_init
        else:
            return None

    def get_all(self) -> List[DatabaseItem]:
        """
        Get all key and value as array
        """
        c = self.conn.cursor()
        sql = list(c.execute(f'SELECT * FROM `{self.name}`;'))

        result = []

        for i in sql:
            result.append(DatabaseItem(i[0], i[1]))

        return result

    def get_all_key(self) -> List[any]:
        """
        Get all key as array
        """
        c = self.conn.cursor()
        sql = list(c.execute(f'SELECT `key` FROM `{self.name}`;'))

        result = []

        for i in sql:
            result.append(i[0])

        return result

    def delete(self, key) -> None:
        """
        Delete item from database
        """
        c = self.conn.cursor()
        c.execute(f'DELETE FROM `{self.name}` WHERE `key` == "{key}";')
        self.conn.commit()

    def append(self, key, more) -> any:
        """
        Add some value from the key and retune the value
        """
        value = self.get(key)
        value += more
        self.set(key, value)
        return value

    def remove(self, key, more) -> any:
        """
        Remove some value from the key and retune the value
        """
        value = self.get(key)
        value -= more
        self.set(key, value)
        return value

    def exists(self, key) -> Boolean:
        """
        Check if key exists
        """
        return False if (self.get(key, no_init=True) == None) else True

    def rename(self, new_name) -> None:
        """
        Rename the table from database
        """
        c = self.conn.cursor()
        c.execute(f'ALTER TABLE `{self.name}` RENAME TO `{new_name}`;')
        self.conn.commit()

if __name__ == "__main__":
    db = Database("test.db", auto_init=0)
    a = db.get_all()
    print(db.set("bb", 1))