# app/observability/metrics.py

from prometheus_client import Counter, Histogram

# Métricas técnicas
http_requests_total = Counter(
    "http_requests_total",
    "Total de requisições HTTP",
    ["method", "endpoint", "status"]
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "Duração das requisições HTTP",
    ["endpoint"]
)

# Métricas de domínio
user_actions_total = Counter(
    "user_actions_total",
    "Total de ações de usuários",
    ["action", "source"]
)
