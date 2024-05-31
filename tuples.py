def get_coordinate(record):
    coordinate = record
    return coordinate


def convert_coordinate(coordinate):
    y = (coordinate[0], coordinate[1])
    return y


def create_record(azara_record, rui_record):
    az_tesoro, az_coordenada = azara_record
    rui_ubicacion, rui_coordenada, rui_cuadrante = rui_record
    if az_coordenada[0] != rui_coordenada[0] or az_coordenada[1] != rui_coordenada[1]:
        return "not a match"
    return {(az_tesoro, az_coordenada, rui_coordenada, rui_cuadrante)}
