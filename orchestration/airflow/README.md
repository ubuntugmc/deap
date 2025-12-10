Airflow docker-compose for DEAP demo.

Start:
    cd orchestration/airflow
    docker-compose up -d

Visit Airflow UI: http://localhost:8080 (login airflow/airflow)

Note: Ensure that the airflow database is intialised by running the command : docker exec -it airflow-airflow-webserver-1 airflow db init

#The 'dags' folder contains a copy of the deap project (dags/deap).
