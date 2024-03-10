import io
import requests
import avro.schema
import avro.io
from kafka import KafkaProducer
# def load_client(token):   
#     return token

# def lookup_ticker(ticker):
#     return ticker 

def ticker_validator(token,ticker):
    url = "https://real-time-finance-data.p.rapidapi.com/stock-time-series"

    querystring = {"symbol":"ticker","period":"1Y","language":"en"}

    headers = {
        "X-RapidAPI-Key": f"{token}",
        "X-RapidAPI-Host": "real-time-finance-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    #setting up a Kafka connection
def load_producer(kafka_server):
    return KafkaProducer(bootstrap_servers=kafka_server)

#parse Avro schema
def load_avro_schema(schema_path):
    return avro.schema.parse(open(schema_path).read())
    
#encode message into avro format
def avro_encode(data, schema):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()