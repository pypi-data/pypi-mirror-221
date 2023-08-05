import requests
import json
import hashlib

from cryptoService import cipher_hmac_payload

def send_data_with_hmac(env, endpoint, data, hmac_signature, validator):
    try:
        if not data or not hmac_signature or hmac_signature == '':
            raise ValueError(f"You have not provided Data or Hmac Signature:\nData: {data}\nhmacSignature: {hmac_signature}")

        payload_validation_result = validator(data)

        if payload_validation_result is not True:
            raise ValueError(payload_validation_result)

        hashed_payload = cipher_hmac_payload(json.dumps(data), hmac_signature)
        headers = {
            'Authorization': f'hmac {hashed_payload}',
            'Content-Type': 'application/json'
        }

        url = f'https://in.{env + "." if env != "prod" else "."}killbills.{"dev" if env != "prod" else "co"}/{endpoint}'
        response = requests.post(url, data=json.dumps(data), headers=headers)

        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

        return response.json()
    except (requests.exceptions.RequestException, ValueError) as error:
        return str(error)

# Exemple d'utilisation :
env = 'dev'
endpoint = 'example_endpoint'
data = {
    'key1': 'value1',
    'key2': 'value2'
}
hmac_signature = 'your_hmac_key'

def payload_validator(data):
    # Ajoutez ici votre logique de validation de la charge utile (payload)
    # Renvoie True si la validation réussit, sinon une chaîne de caractères décrivant l'erreur
    return True

result = send_data_with_hmac(env, endpoint, data, hmac_signature, payload_validator)
print(result)
