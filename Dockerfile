# Wykorzystujemy obraz oficjalny Python 3.8 z repozytorium Docker Hub
FROM python:3.8-slim-buster

# Aktualizujemy system i instalujemy wymagane pakiety
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libjpeg-dev libpng-dev && \
    rm -rf /var/lib/apt/lists/*

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki aplikacji do kontenera
COPY . .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Ustawiamy zmienną środowiskową dla portu
ENV PORT=80

# Nasłuchujemy na porcie zdefiniowanym przez zmienną środowiskową
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]