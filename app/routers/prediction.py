#Se importa APIRouter y HTTPException de fastapi para crear rutas en la API y manejar excepciones HTTP.
from fastapi import APIRouter, HTTPException
#Se importan los esquemas de solicitud y respuesta para la predicción de iris.
from app.schemas.iris_schema import IrisPredictionRequest, IrisPredictionResponse
#Se importa la función de predicción del servicio de iris.
from app.services.iris_service import iris_predict

#definición del enrutador para las predicciones 
predict_router = APIRouter(prefix="", tags=["prediction"])

#Definición de la ruta POST /predict para realizar predicciones y se define la respuesta esperada segun el esquema IrisPredictionResponse.
@predict_router.post("/predict", response_model=IrisPredictionResponse)
#Definición de la función que maneja las solicitudes de predicción y define el schema de entrada de la solicitud.
def predict(data: IrisPredictionRequest):
    #Se define un bloque try-except para manejar posibles errores durante la predicción.
    try:
        #Se llama a la función de predicción con los datos proporcionados en la solicitud.
        species_name, confidence = iris_predict(data)
        #Se retorna la respuesta con el nombre de la especie y la confianza.
        return IrisPredictionResponse(
            species=species_name,
            confidence=confidence
            )
    #En caso de error, se lanza una excepción HTTP 500 con el detalle del error.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
