# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /conecta

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt /conecta/
COPY requirements-dev.txt /conecta/

# Instale dependências do sistema necessárias (ex: para compilar dependências Python)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libmagic1 \
    libgl1 \
    libglib2.0-0 \
    libcairo2-dev \
    libgdk-pixbuf-xlib-2.0-dev \
    libglib2.0-dev \
    gir1.2-glib-2.0 \
    libpango1.0-dev \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /conecta/requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copie o restante da aplicação para o contêiner
COPY . /conecta/

# Exponha a porta que será usada pela aplicação
EXPOSE 8000

# Comando padrão para iniciar o Gunicorn com a aplicação Django
CMD ["/env/bin/gunicorn", "--bind", ":8000", "--workers", "2", "--timeout", "300", "--max-requests", "1000", "--max-requests-jitter", "50", "--preload", "conecta.wsgi"]
