# Data Engineer Assessment Practical (DEAP) # The Anti-Microbial Resistance (AMR) Data Pipeline is a single-file repository that demonstrates a simple data flow linking a public or private pharmacy to a public health institute’s Anti-Microbial System.This environment runs locally through Docker Compose and executes the complete workflow: data ingestion, transformation, loading, and modeling steps.
DEAP Django + Airflow demo for CHAI Inteview Assesment Only.
-----------------------------------------------------------
Structure:
- deap/            -> Django Framework based project
- pipeline/        -> Django app with pipeline services
- data/            -> raw and processed data used by pipeline
- orchestration/airflow/ -> Airflow docker-compose and dags
# Quickstart Overview (local development)
    1. Ensure that Python 3.10+, Docker & Docker Compose are installed.
    2. Create a virtualenv and install Django for running Django locally:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    3. Start Airflow:
    cd orchestration/airflow
    docker compose up -d or docker-compose up -d
    Note: If docker is not installed run docker install command
    pip install docker
    Wait until http://localhost:8080 is available (default user/password airflow/airflow)
    4. Run Django:
    python manage.py migrate
    python manage.py runserver
    5. Trigger via Django endpoint:
    http://localhost:8000/pipeline/run/
Assesor Notes:
- The Airflow DAG expects the deap project folder to exist under the Airflow dags directory.
- For this ZIP, the folder `orchestration/airflow/dags/deap` contains a copy of the Django app so Airflow can import it.

# AMR DATA PIPELINE SETUP MANUAL
Complete Setup Guide for Windows + PowerShell

# PREREQUISITES
Ensure you have the following installed:
    Python 3.11+ → https://www.python.org/downloads/
    Docker Desktop → https://www.docker.com/products/docker-desktop/
    Git/VSCODE (Important for cloning repositories)
    PostgreSQL Client (optional: pgAdmin or DBeaver for database management)
# STEP 1: SET UP PYTHON VIRTUAL ENVIRONMENT
Navigate to your project directory:
    cd path to assessors project folder *(i.e something like C:\Users\Gregory Malunga\Documents\MEneg\CHAI\deap)*
Create virtual environment:
    python -m venv venv
Activate virtual environment:
    .\venv\Scripts\Activate.ps1
# TROUBLESHOOTING: If you get an execution policy error, run:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# STEP 2: INSTALL PYTHON DEPENDENCIES
Once your virtual environment is activated:
    pip install -r requirements.txt
    pip install psycopg2-binary
# STEP 3: START AIRFLOW WITH DOCKER
Navigate to Airflow directory:
    cd orchestration/airflow
Start all services:
    docker compose up -d
What this will do:
• Creates Airflow PostgreSQL database
• Initializes Airflow metadata
• Creates default admin user (admin / admin)
• Starts Airflow webserver and scheduler
Verify services are running:
    docker ps
Output:
    > 1. airflow-webserver
    > 2. airflow-scheduler
    > 3. airflow-init
    > 4. postgres
Access Airflow UI:
Open browser → http://localhost:8080
Login: admin / admin
# STEP 4: SET UP POSTGRESQL DATABASE
Open your PostgreSQL client (psql command, pgAdmin) and run:
    CREATE DATABASE amrdb;
    CREATE USER amruser WITH PASSWORD 'amr123';
    GRANT ALL PRIVILEGES ON DATABASE amrdb TO amruser;
    \c amrdb
    GRANT ALL ON SCHEMA public TO amruser;
# STEP 5: APPLY DJANGO MIGRATIONS
Important: navigate back to project root:
     cd path to the assesors project folder *(i.e something like C:\Users\Gregory Malunga\Documents\MEneg\CHAI\deap)*
# Run migrations:
    python manage.py migrate
 This creates all necessary database tables for the Django application.
# STEP 6: START DJANGO DEVELOPMENT SERVER
    python manage.py runserver
    Django server runs at: http://localhost:8000
Available endpoints:
• POST http://localhost:8000/pipeline/run/ - Trigger pipeline via HTTP

# STEP 7: RUN THE DATA PIPELINE
OPTION A: Via Airflow UI (Recommended)
1. Go to http://localhost:8080
2. Login with admin / admin
3. Find the DAG: deap_pipeline
4. Click the Trigger DAG button
OPTION B: Via Django Endpoint
    curl -X POST http://localhost:8000/pipeline/run/
Or use Postman to send POST request
# STEP 8: VERIFY PIPELINE EXECUTION
Check Airflow DAG Status:
• Go to Airflow UI → DAGs → deap_pipeline
• Monitor task execution in the Graph or Grid view

Check Database Tables:
Connect to PostgreSQL and run:

    SELECT * FROM staging_pharmacy_sales LIMIT 20;
    SELECT * FROM analytics_mart_antibiotic_usage LIMIT 20;
    SELECT COUNT(*) FROM staging_pharmacy_sales;
    SELECT COUNT(*) FROM analytics_mart_antibiotic_usage;

# Expected Results:
 1. Cleaned data in staging_pharmacy_sales
 2. Aggregated analytics in analytics_mart_antibiotic_usage
 3. Properly partitioned tables (if configured)
# COMMON TROUBLESHOOTING
Docker Issues:
    docker compose down
    docker compose up -d
    docker compose logs -f
Database Connection Issues:
• Verify PostgreSQL is running: docker ps
• Check connection settings in Django settings.py
• Ensure database user has proper permissions

Virtual Environment Not Activating:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\venv\Scripts\Activate.ps1

# Note: AI tools, including ChatGPT and Grok, were used in this project to help adapt and align my previously used project templates to the requirements of this assignment.
