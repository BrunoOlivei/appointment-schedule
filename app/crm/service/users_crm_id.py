from typing import Optional
from sqlalchemy import select, Table
from sqlalchemy.orm import Session

from app.core.database.sqlserver import SQLServer


class CRMUserId:
    def __init__(self, email: Optional[str] = None) -> None:
        self._email = email
        self._sqlserver = SQLServer()

    def get_user_id(self) -> Optional[str]:
        engine = self._sqlserver.get_engine()
        metadata = self._sqlserver.get_metadata()

        table = Table("USUARIO", metadata, autoload_with=engine)

        query = select(table).where(table.c.EMAIL == self._email)

        with Session(engine) as session:
            result = session.execute(query)
            row = result.fetchone()

            if row:
                return row[0]
            else:
                return None
