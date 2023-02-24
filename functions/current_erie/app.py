from base64 import b64decode
import http.client
import json
from os import environ as env
import boto3

api_key = boto3.client('kms').decrypt(CiphertextBlob=b64decode(env['api_key']))['Plaintext'].decode('utf-8')

def lambda_handler(event, context):
    connection = http.client.HTTPSConnection("api.weatherapi.com")
    connection.request("GET", "/v1/current.json?key=" + api_key + "&q=Erie")

    response = connection.getresponse()
    return {
        "statusCode": 200,
        "body": response.read().decode()
    }