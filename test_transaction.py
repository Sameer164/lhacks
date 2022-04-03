from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/0980f5c175354d97817e44a7f964798f'))
private_key='a134bbc28bb05f9f23fa90e24f2bd576d1c75e0278bf0bd4db7704404f950b08'
acct=w3.eth.account.privateKeyToAccount(private_key)
from_address=acct.address
to_address= '0x6d9da1B7b90406772dad050f479771126fEF5FBf'
abi=[
	{
		"constant": False,
		"inputs": [
			{
				"name": "from",
				"type": "address"
			},
			{
				"name": "tokens",
				"type": "uint256"
			},
			{
				"name": "token",
				"type": "address"
			},
			{
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "receiveApproval",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

contract_address='0xd5174bF8b6DD70fF424281140b52C24D4D3BaC5D'
contract= w3.eth.contract(address=contract_address, abi=abi)
nonce= w3.eth.getTransactionCount(from_address)

token_txn = contract.functions.transfer(
     to_address,
     1,
 ).buildTransaction({
     'chainId': 3,
     'gas': 70000,
     'gasPrice': w3.toWei('1', 'gwei'),
     'nonce': nonce,
 })
signed_txn = w3.eth.account.signTransaction(token_txn, private_key=private_key)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)  


