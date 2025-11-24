
class Connection:

    def __init__(self, sql_type, user, password, server, port = None, **args) -> None:
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.sql_type = sql_type
        self.args = args

    @property
    def engine(self):
        if self.sql_type == 'MSSQL':
            return f'mssql+pymssql://{self.user}:{self.password}@{self.server}/{self.args['db_name']}'
        if self.sql_type == 'PostgresSQL':
            return f'postgresql://{self.user}:{self.password}@{self.server}:{str(self.port)}/{self.args['db_name']}'
        else: print("Нет соединения")

    @property
    def async_engine(self):
        if self.sql_type == 'MSSQL':
            return f'mssql+aioodbc://{self.user}:{self.password}@{self.server}/{self.args['db_name']}'
        if self.sql_type == 'PostgresSQL':
            return f'postgresql+asyncpg://{self.user}:{self.password}@{self.server}:{str(self.port)}/{self.args['db_name']}'
        else: print("Нет соединения")
