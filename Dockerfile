
FROM python:3.11-slim
WORKDIR /app
COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt \
    && find /usr/local/lib/python3.11/site-packages/ \
    \( -name "tests" -o -name "test" -o -name "doc" -o -name "docs" -o -name "__pycache__" \) \
    -type d -exec rm -rf {} + \
    && find /usr/local/lib/python3.11/site-packages/ -name "*.pyc" -exec rm -f {} + \
    && find /usr/local/lib/python3.11/site-packages/ -name "*.pyo" -exec rm -f {} +

COPY src/ ./src
COPY models/ ./models
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8080"]