alembic upgrade head
uvicorn api.main:app --host 0.0.0.0 --port $PORT