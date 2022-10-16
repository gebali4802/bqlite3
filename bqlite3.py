import sqlite3

class Bqlite3():
    def __init__(self):
        pass

    def insert(self, file: str, table: str, values: tuple):
        try:
            con = sqlite3.connect(file)
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO {table} VALUES {values}")
            con.commit()
            con.close()
        except:
            return False
        else:
            return True

    def update(self, file: str, table: str, values: dict, where: dict):
        try:
            con = sqlite3.connect(file)
            cursor = con.cursor()
            valuesKeyList = list(values.keys())
            valuesValueList = list(values.values())
            whereKeyList = list(where.keys())
            whereValueList = list(where.values())
            cursor.execute(f"UPDATE {table} SET {valuesKeyList[0]} = '{valuesValueList[0]}' WHERE {whereKeyList[0]} = '{whereValueList[0]}'")
            con.commit()
            con.close()
        except:
            return False
        else:
            return True

    def delete(self, file: str, table: str,  where: dict):
        try:
            con = sqlite3.connect(file)
            cursor = con.cursor()
            whereKeyList = list(where.keys())
            whereValueList = list(where.values())
            cursor.execute(f"DELETE FROM {table} WHERE {whereKeyList[0]} = '{whereValueList[0]}'")
            con.commit()
            con.close()
        except:
            return False
        else:
            return True

    def selectOne(self, file: str, table: str,  where: dict, method: str, field: str):
        try:
            con = sqlite3.connect(file)
            cursor = con.cursor()
            whereKeyList = list(where.keys())
            whereValueList = list(where.values())
            cursor.execute(f"SELECT {field} FROM {table} WHERE {whereKeyList[0]} = '{whereValueList[0]}'")
            if method == "fetchone":
                result = cursor.fetchone()
            elif method == "fetchall":
                result = cursor.fetchall()
            else:
                raise
            con.commit()
            con.close()
        except:
            return False
        else:
            return result

    def selectMany(self, file: str, table: str, method: str):
        try:
            con = sqlite3.connect(file)
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            if method == "fetchone":
                result = cursor.fetchone()
            elif method == "fetchall":
                result = cursor.fetchall()
            else:
                raise
            con.commit()
            con.close()
        except:
            return False
        else:
            return result