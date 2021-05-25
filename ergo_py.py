import requests
import json

class ErgoAPI:
    def __init__(self):
        """ Initialize API """
        self.main_url = 'https://api.ergoplatform.com'
        self.address_url = '/api/v0/addresses/'
        self.block_url = '/api/v0/blocks/'
        self.info_url = '/api/v0/info'
        self.status_url = '/api/v0/stats'

    def get_complete_address(self, address:str) -> str:
        """ Get complete info about a address
        :param str address: Address """
        try:
            url = self.main_url + self.address_url
            response = requests.get(url + address)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_address_balance(self, address:str) -> str:
        """ Get address confirmed balance
        :param str address: Address """
        try:
            url = self.main_url + self.address_url
            response = requests.get(url + address)
            return json.loads(response.content.decode())['transactions']['confirmedBalance']
        except Exception as error:
            print(error)

    def get_complete_block(self, block:str) -> str:
        """ Get block data
        :param str block: Block """
        try:
            url = self.main_url + self.block_url
            response = requests.get(url + block)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_block_ref(self, block:str) -> str:
        """ Get block references
        :param str block: Block """
        try:
            url = self.main_url + self.block_url
            response = requests.get(url + block)
            return json.loads(response.content.decode())['references']
        except Exception as error:
            print(error)

    def get_blockchain_info(self):
        """ Get blockchain info like hashrate, supply, etc"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)
    
    def get_hash_rate(self):
        """ Get actual hashrate"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())['hashRate']
        except Exception as error:
            print(error)

    def get_supply(self):
        """ Get actual supply"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())['supply']
        except Exception as error:
            print(error)
