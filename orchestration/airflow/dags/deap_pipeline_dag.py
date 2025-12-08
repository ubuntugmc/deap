from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys, os

# Ensure Airflow can import the deap project placed inside dags/deap
dags_deap_path = os.path.join(os.path.dirname(__file__), 'deap')
if dags_deap_path not in sys.path:
    sys.path.insert(0, dags_deap_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deap.settings')
try:
    import django
    django.setup()
except Exception as e:
    print('Django setup warning:', e)

from pipeline.services.pipeline_runner import run_pipeline_logic

with DAG(
    dag_id='deap_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False,
    tags=['deap','amr']
) as dag:
    run_task = PythonOperator(
        task_id='run_pipeline_task',
        python_callable=run_pipeline_logic
    )
