from app.ml_model.model import predict_species

def iris_predict(data: dict):

    data_list = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]

    species_name, confidence = predict_species(data_list)
    return species_name, confidence
