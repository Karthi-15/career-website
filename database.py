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


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),
                              {"val": id})
    rows = result.all()
    if (len(rows) == 0):
        return None
    else:
        return dict(zip(result.keys(), rows[0]))


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            f"INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )

        conn.execute(
            query,
            {
                "job_id": job_id,
                "full_name": data["full_name"],
                "email": data["email"],
                "linkedin_url": data["linkedin_url"],
                "education": data["education"],
                "work_experience": data["work_experience"],
                "resume_url": data["resume_url"],
            },
        )
        conn.commit()
