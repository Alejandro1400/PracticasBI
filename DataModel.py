from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    year: float
    km_driven: float
    selling_price: float
    engine: float 
    max_power: float
    seats: float
    owner: float
    fuel: str
    seller_type: str
    transmission: str
    mileage: float

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["year","km_driven", "selling_price", "engine", "max_power", "seats", "owner", "fuel", "seller_type", "transmission", "mileage"]
