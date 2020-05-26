from django.shortcuts import render
from django.http import HttpResponse
import os
from urllib.parse import quote
import hmac
import hashlib
import binascii
import requests


# Create your views here.
def index(request):
    print("Entered index")
    my_variable = os.environ.get('ENV_VARIABLE')
    string = "Welcome to Hamburger API Homepage. Here will be the documentation + "
    string_env = string + my_variable
    key = hashCalc('post', 'https://khipu.com/api/2.0/banks')
    print("KEY")
    print(key)
    return HttpResponse(string_env)

def banks(request):
    # url = 'https://khipu.com/api/2.0/banks'
    # auth_hash = hashCalc('GET', url)
    # headers_dic = {'Authorization': auth_hash}
    # print(headers_dic)
    # response_dic = requests.get(url, headers=headers_dic)
    # print(response_dic.request.headers)
    # print(response_dic.json())

    crear_un_pago()

    return HttpResponse("Estoy en vista de banks")

def test(request):

    auth_hash = hashCalc('GET', 'https://khipu.com/api/2.0/payments/yqbmf4mzgkwa')
    print("AUTH HASH")
    print(auth_hash)

    return HttpResponse("Estoy en vista de test para correr funcion test")


def retorna(request):
    #url = 'https://khipu.com/api/2.0/banks'
    #auth_hash = hashCalc('GET', url)
    #headers_dic = {'Authorization': auth_hash}
    #response_dic = requests.get(url, headers=headers_dic)
    #print(response_dic.request.headers)
    #print(response_dic.json())

    return HttpResponse("Espera a que se confirme tu pago")

#receiverId #Secret
def hashCalc(requestMethod, url, params=None):
    secret = os.environ.get('SECRET_KEY')
    requestMethod = quote(requestMethod, safe='')
    receiver_id = os.environ.get('RECEIVER_ID')
    to_sign = requestMethod.upper()
    to_sign += "&"
    to_sign +=  quote(url, safe='')
    if params:
        for i in sorted(params.keys()) : 
            print(i) 
            to_sign += '&' + quote(i, safe='') + '=' + quote(params[i], safe='')
    print("TO SIGN:")
    print(to_sign)
    #hmac.new(key, data, hashlib.sha256).hexdigest()
    key_bytes = bytes(secret , 'latin-1')
    data_bytes = bytes(to_sign, 'latin-1') # Assumes `data` is also a string.
    hash_key = hmac.new(key_bytes, data_bytes , hashlib.sha256).hexdigest()

    answer = receiver_id + ":" + hash_key
    print(answer)
    return answer


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

def crear_un_pago():
    print("Creando Pago")
    subject = "Pago de prueba, este es el subject"
    currency = "CLP"
    amount = "500"
    transaction_id = "F1"
    body = "Este cobro es de prueba, este es el body"
    url = 'https://khipu.com/api/2.0/payments'
    cuerpo = {
        'subject': subject,
        'currency': currency,
        'amount': amount,
        'transaction_id': transaction_id,
        'body': body,
        'notify_url': 'https://f5240269.ngrok.io/api/notify',
        'return_url': 'https://f5240269.ngrok.io/return',


    }

    auth_hash = hashCalc('post', url, params=cuerpo)
    header = {'Authorization':auth_hash}

    response = requests.post(url, data = cuerpo ,headers=header).json()

    print("Respuesta")
    print(response)




