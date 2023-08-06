# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xjet']

package_data = \
{'': ['*']}

install_requires = \
['ecdsa>=0.18.0', 'httpx>=0.23.1']

setup_kwargs = {
    'name': 'xjet',
    'version': '0.1.3',
    'description': 'Python SDK for t.me/xJetSwapBot',
    'long_description': '# Python SDK for xJet Connect API\n\n## Authors\n- [@xJetLabs](https://github.com/xJetLabs) (forked from)\n- [@nik-1x](https://www.github.com/nik-1x)\n \n## Installation\n```shell\npip install xjet\n```\nIf requires <b>nacl</b> package, install it <i>manually</i>:\n```shell\npip install pynacl\n```\n\n## Webhook analog\n```python\nwhile True:\n    res = httpx.get(\n        \'https://api.xjet.io/v1/account.events\',\n        params={\'timeout\': 10},\n        headers={\n            \'X-API-Key\': api_key,\n        },\n        timeout=11,\n    )\n    print(res.json)\n\n    time.sleep(3)\n```\n\n\n## Usage/Examples  \n[Live example](https://replit.com/@delpydoc/xJetAPI)\n\n### Initialization\n```python\nfrom xjet import JetAPI\n\n# api_key: str\n# private_key: str\napi = JetAPI(\n    api_key="API_KEY",\n    private_key="PRIVATE_KEY",\n    network=\'mainnet\'  # mainnet / testnet\n)\n```\n\n\n### Info\n```python\nawait xjet.currencies() # Shows all saved xJetSwap currencies\n```\n\n\n### Account\n```python\nawait api.me() # get API Application information.\n# {\'id\': <str>, \'name: <str>, \'service_wallet\': <str>}\n\nawait api.balance() # get balance\n# {\n#   \'balances\': [\n#       {\'currency\': <int>, \'amount\': <float>, \n#           \'values\': {\'byn\': 0.0, \'cny\': 0.0, \'eur\': 0.0, \'gbp\': 0.0, \'kzt\': 0.0, \'rub\': 0.0, \'uah\': 0.0, \'usd\': 0.0}}], \n#   \'timestamp\': <int>\n# }\n\nawait api.submit_deposit() # check for deposit\n# {\'success\': <bool>}\n\n# ton_address: str\n# currency: str\n# amount: float\nawait api.withdraw(ton_address, currency, amount) # check for deposit\n\n# limit: int\n# offset: int\nawait xjet.operations(limit, offset) # operations\n```\n\n### Cheque\n```python\n# currency: str\n# amount: float\n# expires: [int, None]\n# description: [str, None]\n# activates_count: [int, None]\n# groups_id: [int, None]\n# personal_id: [int, None]\n# password: [str, None]\n\nawait api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque\n# {\'cheque_id\': <str>, \'external_link\': \'https://t.me/xJetSwapBot?start=c_<cheque_id>\'}\n\nawait api.cheque_status(cheque_id) # get cheque status\n# {\n#   \'id\': <str>, \n#   \'issuer_id\': <str>, \n#   \'amount\': <float>, \n#   \'activates_count\': <int>, \n#   \'activates: <list[str]>, \n#   \'locked_value\': <float>, \n#   \'currency\': <Str>, \n#   \'expires\': <bool>, \n#   \'description\': <str>, \n#   \'status\': \'activated/canceled/expired/active\', \n#   \'password\': <str | None>, \n#   \'groups_id\': <list[str] | None>, \n#   \'personal_id\': <int | None>, \n#   \'is_for_premium\': <bool>\n# }\n\n\nawait api.cheque_list() # get cheques on account\n# list of cheque_status\n\nawait api.cheque_cancel(cheque_id) # delete cheque\n# returns cheque_status\n```\n\n\n### Invoice\n```python\n# currency: str\n# amount: float\n# description: [str, None]\n# max_payments: [int, None]\nawait api.invoice_create(currency, amount, description, max_payments) # create invoice\n# {\'invoice_id\': <str>, \'external_link\': \'https://t.me/xJetSwapBot?start=inv_<cheque_id>\'}\n\nawait api.invoice_status(invoice_status) # get invoice status\n# {\n#   \'id\': <str>, \n#   \'description\': <str>, \n#   \'currency\': <str>, \n#   \'amount\': <float>, \n#   \'max_amount\': None, \n#   \'min_amount\': None, \n#   \'payments\': [{\'telegram_id\': <int>, \'amount\': <float>, \'comment\': [str | None}, ... ], \n#   \'max_payments\': 1, \n#   \'after_pay\': [], \n#   \'created\': \'2023-04-20T22:55:24.313000\'\n# }\n\nawait api.invoice_list() # get invoices on account\n# list of invoice_status\n```\n\n```python\n# NFT methods\nawait api.nft_list()\nawait api.nft_transfer(nft_address, to_address)\n```\n\n## License\n[GNUv3](https://github.com/nik-1x/pyxJetAPI/blob/main/LICENSE)  \n',
    'author': 'delpydoc',
    'author_email': 'delpydoc@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xJetLabs/python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
