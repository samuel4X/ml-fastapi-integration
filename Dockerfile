#Se utiliza una imagen base ligera de Python 3.12.
FROM python:3.12-slim

#Se copian los binarios de uv desde una imagen preconstruida para gestionar dependencias y entornos virtuales.
COPY --from=ghcr.io/astral-sh/uv:0.8.15  /uv /uvx /bin/

#Se copian todos los archivos del proyecto al directorio /app en el contenedor.
COPY . /app/

#Se establece el directorio de trabajo en /app.
WORKDIR /app

#Se instala las dependencias del proyecto utilizando uv con un entorno virtual en .venv.
RUN uv sync --frozen --no-cache

#Se expone el puerto 8000 para la aplicación FastAPI.
EXPOSE 8000

#Se define el comando para iniciar la aplicación utilizando uvicorn.
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]
