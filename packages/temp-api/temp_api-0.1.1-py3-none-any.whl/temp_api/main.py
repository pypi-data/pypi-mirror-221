from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel


class Measurement(BaseModel):
    mac: str
    humidity: int
    temperature: int
    pressure: int
    acceleration: int
    battery: int
    measurement_sequence_number: int
    movement_counter: int
    tx_power: int
    acceleration_x: int
    acceleration_y: int
    acceleration_z: int


app = FastAPI()


MEASUREMENTS = {}


def store_measurement(measurement: Measurement):
    MEASUREMENTS[measurement.mac] = measurement


def fetch_measurement(mac: str) -> Union[Measurement, None]:
    return MEASUREMENTS.get(mac)


def fetch_all_measurements() -> List[Measurement]:
    return list(MEASUREMENTS.values())


@app.post("/measurements", status_code=201)
def add_measurement(measurement: Measurement):
    store_measurement(measurement)


@app.get("/measurements")
def get_all_measurements() -> List[Measurement]:
    return fetch_all_measurements()


@app.get("/measurements/{mac}")
def get_measurement_by_mac(mac: str) -> Union[Measurement, None]:
    return fetch_measurement(mac)
