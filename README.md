Data Engineer Assessment Practical (DEAP) # AMR Data Pipeline — repo Is single-file repository that demonstrates a small, basic data pipeline linking a Public/Private pharmacy and a public health institute Anti Microbial System. It setup is runnable locally with Docker Compose and performs ingestion → transformation → load → modeling steps.

DEAP Django + Airflow demo for CHAI Inteview Assesment Only
-----------------------------------------------------------
Structure:
- deap/            -> Django project
- pipeline/        -> Django app with pipeline services
- data/            -> raw and processed data used by pipeline
- orchestration/airflow/ -> Airflow docker-compose and dags

Quickstart (local development)
1. Ensure that Python 3.10+, Docker & Docker Compose are installed.
2. Create a virtualenv and install Django for running Django locally:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. Start Airflow:
    cd orchestration/airflow
    docker compose up -d
   Wait until http://localhost:8080 is available (default user/password airflow/airflow)
4. Run Django:
    python manage.py migrate
    python manage.py runserver
5. Trigger via Django endpoint:
    http://localhost:8000/pipeline/run/

Assesor Notes:
- The Airflow DAG expects the deap project folder to exist under the Airflow dags directory.
- For this ZIP, the folder `orchestration/airflow/dags/deap` contains a copy of the Django app so Airflow can import it.
