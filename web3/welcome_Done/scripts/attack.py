from brownie import *

def deploy_local():
    return Welcome.deploy({"from": accounts[0]})


def solved_locally():
    if Welcome[-1].balance() > 0:
        return True, "Solved!"
    else:
        return False, "Need more coins!"


def solved(welcome_address):
    if Welcome.at(welcome_address).balance() > 0:
        return "Solved!"
    else:
        return "Need more coins!"

def main(welcome_address=None):
    if welcome_address:
        # print("Yo")
        CONFIG = {
            "RPC": "https://ctf.nahamcon.com/challenge/39/4b1c3f26-f849-4ead-b563-6ddc5f5d477b",
            # "BLOCK_NUMBER": '',
            # 'FLAGS': '',
            "MNEMONIC": "test test test test test test test test test test test junk",
            # 'RUNNABLES': [],
            "ALLOWED_RPC_METHODS": [],
        }
        # welcome_address = "0x0cB8C2Fe5f94B3b9a569Df43a9155AC008c9884b"
        attacker = accounts.from_mnemonic(CONFIG["MNEMONIC"])
        tx = attacker.transfer(to=welcome_address, amount="0.01 ether")
        tx.wait(1)

        print(f"{solved(welcome_address)}")

    else:
        welcome = deploy_local()
        welcome_address = welcome.address
        # print(address)

        # send ether forcefully
        attacker = accounts[1]
        tx = attacker.transfer(to=welcome_address, amount="0.001 ether")
        tx.wait(1)

        print(f"Solved: {solved_locally()}")
