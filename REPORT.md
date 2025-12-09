# 1. Design and Architecture Choices
The application use a modular, containerized architecture using Django, Airflow, and PostgreSQL, each running as its own service in Docker Compose. PostgreSQL is selected as the main database for its reliability and ACID compliance. Airflow manages the end-to-end ETL and scheduling workflows via DAGs, while Django provides APIs, admin management, and data modeling. The separation of services ensures clear boundaries, maintainability, and future scalability of this application.

# 2. Optimization Strategies Applied

  Several optimizations are incorporated across the stack:
  Database: indexing, partitioning strategies, and connection pooling for faster queries and high-volume ingestion.
  Airflow: task parallelization, optimized retries, minimal XCom usage, and efficient scheduler configurations.
  Django: query optimization, use of select_related/prefetch_related, caching, and bulk inserts/updates.
  Containers: persistent volumes for durability, resource limits for stability, and lightweight base images for faster builds.

# 3. Scaling or Extending the Pipeline

  The system is built for horizontal and vertical scalability:
  Airflow can scale to Celery executors, Kubernetes, or managed cloud services like MWAA or GCP Composer.
  PostgreSQL can scale via replicas, partitioned large tables, and deployment on high-availability clusters.
  Django can scale using load balancers, distributed workers, caching layers, and API gateways.
  The architecture allows easy addition of new ETL pipelines, APIs, analytics layers, and CI/CD automation for continuous improvement.
