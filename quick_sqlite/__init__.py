import json
import sqlite3

class Database():
    def __init__(self, path: str, db_name: str = "__default__", auto_init: any = False) -> None:
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

    def set(self, key, value):
        c = self.conn.cursor()
        c.execute(
            f'REPLACE INTO `{self.name}` VALUES ("{key}", \'{json.dumps(value)}\');')
        self.conn.commit()

    def get(self, key):
        c = self.conn.cursor()
        result = list(
            c.execute(f'SELECT `value` FROM `{self.name}` WHERE `key` == "{key}";'))

        if not result:
            if self.auto_init != False:
                self.set(key, self.auto_init)
            else: return self.auto_init
        else:
            try:
                return json.loads(result[0][0])
            except:
                return result[0][0]

    def get_all(self):
        c = self.conn.cursor()
        sql = list(c.execute(f'SELECT * FROM `{self.name}`;'))

        result = []

        for i in sql:
            result.append({"key": i[0], "value": i[1]})

        return result

    def get_all_key(self):
        c = self.conn.cursor()
        sql = list(c.execute(f'SELECT `key` FROM `{self.name}`;'))

        result = []

        for i in sql:
            result.append(i[0])

        return result

    def delete(self, key):
        c = self.conn.cursor()
        c.execute(f'DELETE FROM `{self.name}` WHERE `key` == "{key}";')
        self.conn.commit()

    def append(self, key, more):
        value = self.get(key)
        value += more
        self.set(key, value)

    def exists(self, key):
        if (self.get(key) == None): return False
        else: return True