from django.http import JsonResponse
from .services.airflow_trigger import trigger_airflow_dag
from django.views.decorators.http import require_GET

@require_GET
def run_pipeline(request):
    result = trigger_airflow_dag()
    return JsonResponse({'trigger': result})
