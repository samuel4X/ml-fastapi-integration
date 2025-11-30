# ml-fastapi-integration

1. Al descargar el repositorio se recomienda crear el entorno virtual ejecutando "uv venv", activarlo segun OS
  1.1 ejecutar uv sync --frozen
  1.2 Seleccionar el interprete del entorno virtual

3. Ejecutar docker build -t ml-fastapi .

4. Luego ejecutar docker run -p 8000:8000 ml-fastapi

5. Luego ingresar a la url http://localhost:8000/docs#/ o desde un cliente postman o thunderclient

6. Luego realizar la peticion modificando los valores
{
  "sepal_length": 0,
  "sepal_width": 0,
  "petal_length": 0,
  "petal_width": 0
}

7. Por ultimo revisar el resultado del modelo
