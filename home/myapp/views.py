from django.shortcuts import render , HttpResponse
from web3 import Web3

import json
import requests


# Create your views here.
def index(request):
    return render(
         request,
         "index.html",
         {
             "title": "Eth-Check App",
         },
        
    )

def services(request):
        return HttpResponse("services")


# def transaction(request):
#     if request.method == 'POST':
#         address = request.POST['address']
#         address = Web3.to_checksum_address(address) # convert to checksum format
#         w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d928ea8bb2e84b5c821bf72fe222b96d'))
#         balance = w3.eth.get_balance(address)
#         transaction_count = w3.eth.get_transaction_count(address)
#         block_number = w3.eth.block_number
#         transactions = []
#         while len(transactions) < 5 and block_number > 0:
#             block = w3.eth.get_block(block_number, True)
#             for transaction in block.transactions:
#                 if transaction['from'] == address or transaction['to'] == address:
#                     transactions.append(transaction)
#                     if len(transactions) == 5:
#                         break
#             block_number -= 1
#         context = {'balance': balance, 'transactions': transactions , 'transaction_count':transaction_count}
#         return render(request, 'web3.html', context)
#     else:
#         return render(request, 'web3.html')

# def transaction(request):
#     if request.method == 'POST':
#         address = request.POST['address']
#         address = Web3.to_checksum_address(address) # convert to checksum format
#         w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d928ea8bb2e84b5c821bf72fe222b96d'))
#         balance = w3.eth.get_balance(address)
#         transaction_count = w3.eth.get_transaction_count(address)
#         print(transaction_count)
#         block_number = w3.eth.block_number
#         transactions = []
#         while len(transactions) < 5 and block_number > 0:
#             block = w3.eth.get_block(block_number, True)
#             for transaction in block.transactions:
#                 if transaction['from'] == address or transaction['to'] == address:
#                     transactions.append(transaction)
#                     if len(transactions) == 5:
#                         break
#             block_number -= 1
#         context = {'balance': balance, 'transactions': transactions , 'transaction_count':transaction_count}
#         return render(request, 'web3.html', context)
#     else:
#         return render(request, 'web3.html')


def transaction(request):
    if request.method == 'POST':
        address = request.POST['address']
        address = Web3.to_checksum_address(address) # convert to checksum format
        w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/{Infura-API-Key}'))

        balance = w3.eth.get_balance(address)
        transaction_count = w3.eth.get_transaction_count(address)
        url = f'http://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey=Your-etherscan-api'
        response = requests.get(url)
        data = json.loads(response.text)
        transactions = data['result'][:5]
        context = {'balance': balance, 'transactions': transactions , 'transaction_count':transaction_count}
        return render(request, 'web3.html', context)
    else:
        return render(request, 'web3.html')
