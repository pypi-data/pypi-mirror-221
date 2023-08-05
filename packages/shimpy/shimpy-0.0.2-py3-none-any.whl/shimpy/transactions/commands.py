import click
from iota_sdk import Wallet
from dotenv import load_dotenv
import os

load_dotenv()

@click.command()
@click.argument('alias')
@click.argument('address')
@click.argument('amount')
def send(alias, address, amount):
    """Send SMR to an address"""
    wallet = Wallet(os.environ['WALLET_DB_PATH'])

    account = wallet.get_account(alias)

    # Sync account with the node
    response = account.sync()

    if 'STRONGHOLD_PASSWORD' not in os.environ:
        raise Exception(".env STRONGHOLD_PASSWORD is undefined, see .env.example")

    wallet.set_stronghold_password(os.environ["STRONGHOLD_PASSWORD"])

    print("Sending", amount, "to", address)
    params = [{
        "address": address,
        "amount": amount,
    }]

    transaction = account.send_with_params(params, {"allowMicroAmount": True})
    print(f'Transaction sent: {transaction.transactionId}')

    block_id = account.retry_transaction_until_included(transaction.transactionId)

    print(
        f'Block sent: {os.environ["EXPLORER_URL"]}/block/{block_id}')
