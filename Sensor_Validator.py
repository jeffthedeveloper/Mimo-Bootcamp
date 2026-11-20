readings = [
    {"sensor": "greenhouse", "value": "23.5"},
    {"sensor": "freezer", "value": "not available"},
    {"value": "18.0"},
    {"sensor": "boiler", "value": "140"},
]


def parse_reading(reading):
    sensor = reading["sensor"]
    value = float(reading["value"])
    if value < -50 or value > 100:
        raise ValueError(f"{sensor} reported an unsupported value.")
    return (sensor, value)


valid_readings = []


for reading in readings:
    try:
        valid_readings.append(parse_reading(reading))
    except (KeyError, TypeError, ValueError) as error:
        print(f" Erro: {error}, por favor, verifique a integridade do dicionário")

if valid_readings:
    total = sum(value for _, value in valid_readings)
    media = total / len(valid_readings)
    print(f"{media:.1f}")
else:
    print("Nenhuma leitura válida detectada")
