Run below commands in terminal to execute the application :

Setup python environment: python -m venv venv

Activate virtual environment: .\venv\Scripts\activate

Install FastAPI framework with ASGI server: pip install fastapi[all] uvicorn

Install requests library: pip install requests

Run the fast server: uvicorn main:app --reload

Server will run at: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Consume API in python: python consume_api.py




