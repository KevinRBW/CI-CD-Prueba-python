
FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "tu_aplicacion_principal.py"] # Reemplaza "tu_aplicacion_principal.py" con el script que inicia tu app.
