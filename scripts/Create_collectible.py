from brownie import Adavanced_collectible
from scripts.helpful_scripts import fund_with_link, get_account
from scripts.deploy_and_create import create_and_dep
from web3 import Web3


def create_collectible():
    account = get_account()
    deploy = create_and_dep()
    advanced_collectible = Adavanced_collectible[-1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    creation_transaction = advanced_collectible.create_coll({"from": account})
    creation_transaction.wait(1)
    print("Collectible created!")


def main():
    create_collectible()
