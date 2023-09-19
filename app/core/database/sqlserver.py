from sqlalchemy import MetaData, Table, create_engine

from app.core.config import get_config


class SQLServer:
    def __init__(self) -> None:
        self._config = get_config()
        self._engine = None

    def get_engine(self):
        if self._engine is None:
            self._engine = create_engine(self._config.SQL_SERVER_DATABASE_URI)
        return self._engine

    def get_metadata(self):
        return MetaData()

    def get_table(self, table_name: str):
        metadata = self.get_metadata()
        self._engine = self.get_engine()
        return Table(table_name, metadata, autoload_with=self._engine)

    def get_table_columns(self, table_name: str):
        table = self.get_table(table_name)
        return table.columns.keys()

    def get_table_columns_type(self, table_name: str):
        table = self.get_table(table_name)
        return table.columns.type

    

