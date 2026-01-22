# Usa Python versione "slim" (leggera)
FROM python:3.9-slim

# Crea una cartella di lavoro nel container
WORKDIR /app

# Copia il file delle dipendenze e installale
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice
COPY . .

# Comando per avviare Flask
#CMD ["python", "app.py"]
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]