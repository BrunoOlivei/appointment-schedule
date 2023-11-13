# import uvicorn


# if __name__ == '__main__':
#     uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)


from app.core.database.postgres import PostgresSQL


db = PostgresSQL()

engine = db.get_engine()

metadata = db.get_metadata()

metadata.reflect(bind=engine)

print(metadata.tables.keys())
