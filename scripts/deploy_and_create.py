from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    OPENSEA_URL,
    get_contract,
)
from brownie import Adavanced_collectible, config, network




def create_and_dep():
    account = get_account()
    advanced_collectible = Adavanced_collectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creatiing_tx = advanced_collectible.create_coll({"from": account})
    creatiing_tx.wait(1)
    print("token ban gaya kake")


def main():
    create_and_dep()
