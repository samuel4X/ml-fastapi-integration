# ml-fastapi-integration

1. Al descargar el repositorio se recomienda crear el entorno virtual ejecutando "uv venv", activarlo segun OS

2. Ejecutar docker build -t ml-fastapi .

3. Luego ejecutar docker run -p 8000:8000 ml-fastapi

4. Luego ingresar a la url http://localhost:8000/docs#/ o desde un cliente postman o thunderclient

5. Luego realizar la peticion modificando los valores
{
  "sepal_length": 0,
  "sepal_width": 0,
  "petal_length": 0,
  "petal_width": 0
}

6. Por ultimo revisar el resultado del modelo
