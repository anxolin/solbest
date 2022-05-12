import requests

# TODO:
# - allowance

def swap_1inch(sell_token, buy_token, sell_amount):
    payload = {
        'fromTokenAddress': sell_token,
        'toTokenAddress': buy_token,
        'amount': sell_amount,
        # settlement contract
        'fromAddress': '0x9008D19f58AAbD9eD0D60971565AA8510560ab41',
        'slippage': 50,
        'disableEstimate': True,
    }
    r = requests.get('https://api.1inch.io/v4.0/100/swap', params=payload)
    r.raise_for_status()
    r =  r.json()
    return {
      'buy_amount': r['toTokenAmount'],
      'tx_to': r['tx']['to'],
      'tx_calldata': r['tx']['data'],
    }

if __name__ == '__main__':
    a = swap_1inch(
        # wxdai
        '0xe91d153e0b41518a2ce8dd3d7944fa863463a97d',
        # usdc
        '0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83',
        # 1e18
        1000000000000000000
    )
    print(a)
