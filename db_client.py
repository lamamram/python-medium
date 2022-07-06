# %%
import sqlite3 as lite
from exo_singleton_meta import SingleMeta

class SqliteDb(metaclass=SingleMeta):
    
    def __init__(self, path):
        self.__path = path

    def __enter__(self):
        self.__db = lite.connect(self.__path)
        # fetch de dict au lieu de tuple
        self.__db.row_factory = lite.Row
        return self
    

    def execute_script(self, path):
        """
        exécution de scripts sql
        """
        with open(path, "r", encoding="utf8") as f:
            script = f.read()
        cur = self.__db.cursor()
        try:
            cur.executescript(script) 
            return {"valid": True, "response": cur.rowcount}
        except lite.OperationalError as e:
            return {"valid": False, "response": e}


    def insert(self, table, fields, values):
            # requête préparée
            insert_query = f"insert into {table} ({','.join(fields)}) values ({','.join(['?'] * len(fields))})"
            print(insert_query)
            cur = self.__db.cursor()
            cur.executemany(insert_query, values)
            return f"{cur.rowcount} lines inserted."


    def execute(self, req, *, one=False):
        cur = self.__db.cursor()
        try:
            cur.execute(req)
            if one:
                return {"valid": True, "response": dict(cur.fetchone())} 
            return {"valid": True, "response": list(map(dict, cur.fetchall()))}
        except lite.OperationalError as e:
            return {"valid": False, "response": e}

    
    def close(self):
        self.__db.close()
    
    def __exit__(self, x_type, x_name, x_trace):
        self.close()


if __name__ == "__main__":
    with SqliteDb("users.db") as db:
        db.execute_script("users.sql")
        print(db.execute("SELECT COUNT(1) as nb FROM users"))


# %%
','.join(['?'] * 7)
# %%
