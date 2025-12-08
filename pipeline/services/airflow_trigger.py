import requests
AIRFLOW_URL = "http://localhost:8080/api/v1"
DAG_ID = "deap_pipeline"
USER = "airflow"
PASS = "airflow"

def trigger_airflow_dag():
    url = f"{AIRFLOW_URL}/dags/{DAG_ID}/dagRuns"
    resp = requests.post(url, auth=(USER, PASS), json={})
    try:
        return resp.json()
    except Exception:
        return {'status_code': resp.status_code, 'text': resp.text}
