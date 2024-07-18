from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
ssl_ca = './ca.pem'

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": './ca.pem'
                       }})

# with engine.connect() as connection:
#     result = connection.execute(text("select * from jobs;"))
#     print(result.all())


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(result.keys(), row)))
        return jobs
