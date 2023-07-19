import sqlalchemy as sql

class Database:
    engine = None

    def __init__(self):
        cls = self.__class__
        cls.engine = sql.create_engine('sqlite://servers.db', echo=True)

        # SCHEMA


    @staticmethod
    def connect(callback):
        with Database.engine.connect() as connection:
            return callback(connection)

    @staticmethod
    @connect
    def init_servers(cls, con):
        con.execute(
            sql.text("""
            CREATE TABLE IF NOT EXISTS config (
            id INT PRIMARY KEY AUTOINCREMENT,
            guild_id INT UNIQUE NOT NULL,
            
            """)
        )


    @classmethod
    @connect
    def get_server(cls, con, guild_id):
        pass

