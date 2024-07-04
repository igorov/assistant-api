# Imagen base
FROM python:3.10-slim-bullseye

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Compilar e instalar SQLite3 desde la fuente
RUN wget https://www.sqlite.org/2023/sqlite-autoconf-3420000.tar.gz \
    && tar xvfz sqlite-autoconf-3420000.tar.gz \
    && cd sqlite-autoconf-3420000 \
    && ./configure \
    && make \
    && make install \
    && cd .. \
    && rm -rf sqlite-autoconf-3420000 sqlite-autoconf-3420000.tar.gz

# Actualizar las librerías dinámicas
RUN ldconfig

# Establecer la variable de entorno para usar el nuevo SQLite
ENV LD_LIBRARY_PATH=/usr/local/lib

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8080

# Comando para iniciar la aplicación
CMD ["python", "src/app.py"]