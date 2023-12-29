FROM ubuntu:latest
WORKDIR /app
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "src/main.py"]