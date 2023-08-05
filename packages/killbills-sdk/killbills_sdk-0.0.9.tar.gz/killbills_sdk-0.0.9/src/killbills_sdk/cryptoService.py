import hashlib

def cipher_hmac_payload(payload, hmac):
    hmac_bytes = bytes(hmac, 'utf-8')
    payload_bytes = bytes(payload, 'utf-8')
    hmac_sha256 = hashlib.sha256(hmac_bytes)
    hmac_sha256.update(payload_bytes)
    return hmac_sha256.hexdigest()