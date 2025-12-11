# Data Engineer Assessment Practical (DEAP)
This repository contains a complete Anti-Microbial Resistance (AMR) Data Pipeline designed to showcase a simple but functional data flow between a pharmacy (public or private) and a public health institute’s AMR system. The project is packaged as a lightweight, single-file solution and is fully runnable using Docker Compose.
# Overview
The pipeline simulates an end-to-end AMR data workflow — from ingestion at the pharmacy level to transformation, loading, and modeling at the public health institute. It is intended as a demonstration of core data engineering concepts within an AMR surveillance context.
# Features
- Automated ingestion of AMR-related data from a simulated pharmacy source
- Transformation and cleaning of raw clinical and pharmaceutical data
- Loading of processed data into a structured storage layer
- Fully containerized setup using Docker Compose
- Local execution with minimal dependencies
# Tech Stack (Prerequisities)
- Django Framework
- Python
- Docker & Docker Compose
- PostgreSQL13+ (Install pgAdmin or DBeaver for database management on local computer)
- Airflow (for orchestrating tasks)
- Git/VSCODE (Important for cloning repository)
-----------------------------------------------------------
# Structure:
- deap/            -> Django Framework based project
- pipeline/        -> Django app with pipeline services
- data/            -> raw and processed data used by pipeline
- orchestration/airflow/ -> Airflow docker-compose and dags
  
# Quickstart Overview (clone repository local deployment)
    1. Ensure that Python 3.10+, Django, Docker & Docker Compose are installed.
    2. Create a virtualenv and install Django for running Django locally:
    python -m venv venv
    source venv/bin/activate (Linux) and or
    Run this command:
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    then 
    .\venv\Scripts\activate (windows command / power shell)
    
    confirm whether the venv exists:
     run command:
     Get-ChildItem .\venv\
     Ensure to install Requirement run commands
     
     pip install psycopg2-binary
     pip install -r requirements.txt
     
3. Start Airflow with docker:
    cd orchestration/airflow
    docker-compose up -d
    docker compose down
    docker compose run airflow-webserver airflow db init
    Note: If docker is not installed run docker install command
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
Login: airflow / airflow
    
    Ensure to add a admin user in order to login>
    docker exec -it airflow-airflow-webserver-1 airflow users create `
    --username airflow `
    --password airflow `
    --firstname Admin `
    --lastname User `
    --role Admin `
    --email chisangagm@yahoo.com

Visit Airflow UI: http://localhost:8080 (login airflow/airflow)

4. Run Django Framework with these command:
      python manage.py migrate
      python manage.py createsuperuser
      - username: admin
      - passowrd:airflow
      - email:chisangagm@yahoo.com
    This creates all necessary database tables for the Django application the proceed and run the command:
       python manage.py runserver
    
    5. Trigger via Django endpoint:
    http://localhost:8000/pipeline/run/
    
Developer Notes:
- The Airflow DAG expects the deap project folder to exist under the Airflow dags directory.
- For this ZIP, the folder `orchestration/airflow/dags/deap` contains a copy of the Django app so Airflow can import it.

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
    python manage.py createsuperuser
    username: admin
    passowrd:airflow
    email:chisangagm@yahoo.com
 This creates all necessary database tables for the Django application.
# STEP 6: START DJANGO DEVELOPMENT SERVER
    python manage.py runserver
    Django server runs at: http://localhost:8000
Available endpoints:
• POST http://localhost:8000/pipeline/run/ - Trigger pipeline via HTTP

# STEP 7: RUN THE DATA PIPELINE
OPTION A: Via Airflow UI (Recommended)
1. Go to http://localhost:8080
2. Login with airflow / airflow
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
# Attribution
Note: AI tools, including ChatGPT and Grok, were used in this project to help adapt and align my previously used project templates to the requirements of this assignment.
# Licence
