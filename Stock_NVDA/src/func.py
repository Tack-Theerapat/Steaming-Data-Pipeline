import orjson as json
from kafka import KafkaProducer

def my_api_key():
    filename = "api_keys.txt"
    with open(filename, "r", encoding="utf-8") as f:
        key = f.readline()
        f.close()
    return key
