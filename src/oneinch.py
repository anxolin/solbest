# All data is strings. Functions may throw.

import requests
import asyncio

settlement_contract_address = '0x9008D19f58AAbD9eD0D60971565AA8510560ab41',

def swap(sell_token, buy_token, sell_amount):
    params = {
        'fromTokenAddress': sell_token,
        'toTokenAddress': buy_token,
        'amount': sell_amount,
        'fromAddress': settlement_contract_address,
        'slippage': 50,
        'disableEstimate': True,
    }
    r = requests.get('https://api.1inch.io/v4.0/100/swap', params=params)
    r.raise_for_status()
    r =  r.json()
    return {
      'buy_amount': r['toTokenAmount'],
      'tx_to': r['tx']['to'],
      'tx_calldata': r['tx']['data'],
    }

# allowance that settlement contract has given to 1inch
def allowance(token):
  params = {
    'tokenAddress': token,
    'walletAddress': settlement_contract_address,
  }
  r = requests.get('https://api.1inch.io/v4.0/100/approve/allowance', params=params)
  r.raise_for_status()
  r = r.json()
  return r['allowance']

# tx data for approving 1inch to use max allowance
def approve(token):
  params = {
    'tokenAddress': token,
    'amount': 2**256 - 1,
  }
  r = requests.get('https://api.1inch.io/v4.0/100/approve/transaction', params=params)
  r.raise_for_status()
  r =  r.json()
  return {
      'tx_to': r['to'],
      'tx_calldata': r['data'],
    }

if __name__ == '__main__':
  if False:
    a = swap(
        # wxdai
        '0xe91d153e0b41518a2ce8dd3d7944fa863463a97d',
        # usdc
        '0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83',
        # 1e18
        1000000000000000000
    )
    print(a)
  if False:
    a = allowance('0xe91d153e0b41518a2ce8dd3d7944fa863463a97d')
    print(a)
  if False:
    a = approve('0xe91d153e0b41518a2ce8dd3d7944fa863463a97d')
    print(a)
