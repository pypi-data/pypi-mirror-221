import tls_client
from typing import Optional

class StakeError(Exception):
    pass

class Stakeapi:
    
    def __init__(self, apikey: str) -> None:
        self.headers = {
            'authority': 'stake.com',
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8,ja-JP;q=0.7,zh-CN;q=0.6,zh;q=0.5,ru;q=0.4',
            'content-type': 'application/json',
            'origin': 'https://stake.com',
            'referer': 'https://stake.com/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-access-token': apikey,
        }
        self.session = tls_client.Session(client_identifier="chrome112", random_tls_extension_order=True,pseudo_header_order=[":method", ":authority", ":scheme", ":path"])
        self.apikey = apikey
    


    def get_balances(self):
        json_data = {
            'query': 'query UserBalances {\n  user {\n    id\n    balances {\n      available {\n        amount\n        currency\n        __typename\n      }\n      vault {\n        amount\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'UserBalances',
        }
        response = self.session.post("https://stake.com/_api/graphql", headers=self.headers, json=json_data)
        if "errors" in response.json():
            raise StakeError(response.json()["errors"][0]["message"])
        return response.json()

    def kyc_info(self):
        json_data = {
            'query': 'query UserKycInfo {\n  isDiscontinuedBlocked\n  user {\n    id\n    roles {\n      name\n      __typename\n    }\n    kycStatus\n    dob\n    createdAt\n    isKycBasicRequired\n    isKycExtendedRequired\n    isKycFullRequired\n    isKycUltimateRequired\n    hasEmailVerified\n    phoneNumber\n    hasPhoneNumberVerified\n    email\n    registeredWithVpn\n    isBanned\n    isSuspended\n    kycBasic {\n      ...UserKycBasic\n      __typename\n    }\n    kycExtended {\n      ...UserKycExtended\n      __typename\n    }\n    kycFull {\n      ...UserKycFull\n      __typename\n    }\n    kycUltimate {\n      ...UserKycUltimate\n      __typename\n    }\n    veriffStatus\n    jpyAlternateName: cashierAlternateName(currency: jpy) {\n      firstName\n      lastName\n      __typename\n    }\n    nationalId\n    outstandingWagerAmount {\n      currency\n      amount\n      progress\n      __typename\n    }\n    activeRollovers {\n      id\n      active\n      user {\n        id\n        __typename\n      }\n      amount\n      lossAmount\n      createdAt\n      note\n      currency\n      expectedAmount\n      expectedAmountMin\n      progress\n      activeBets {\n        id\n        iid\n        game {\n          id\n          slug\n          name\n          __typename\n        }\n        bet {\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserKycBasic on UserKycBasic {\n  active\n  address\n  birthday\n  city\n  country\n  createdAt\n  firstName\n  id\n  lastName\n  phoneNumber\n  rejectedReason\n  status\n  updatedAt\n  zipCode\n  occupation\n}\n\nfragment UserKycExtended on UserKycExtended {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycFull on UserKycFull {\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycUltimate on UserKycUltimate {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n',
            'operationName': 'UserKycInfo',
        }
        response = self.session.post("https://stake.com/_api/graphql", headers=self.headers, json=json_data)
        if "errors" in response.json():
            raise StakeError(response.json()["errors"][0]["message"])
        return response.json()

    def get_tiplimit(self, currency: str) -> dict:
        json_data = {
            'query': 'query TipLimit($currency: CurrencyEnum!) {\n  info {\n    currency(currency: $currency) {\n      tipMin {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'TipLimit',
            'variables': {
                'currency': currency,
            },
        }
        response = self.session.post("https://stake.com/_api/graphql", headers=self.headers, json=json_data)
        if "errors" in response.json():
            raise StakeError(response.json()["errors"][0]["message"])
        return response.json()

    def send_tip(self, user_id: str, amount: float, currency: str, is_public: bool = True, tfa_token: Optional[str] = None):
        json_data = {
            'query': 'mutation SendTip($userId: String!, $amount: Float!, $currency: CurrencyEnum!, $isPublic: Boolean, $chatId: String!, $tfaToken: String) {\n  sendTip(\n    userId: $userId\n    amount: $amount\n    currency: $currency\n    isPublic: $isPublic\n    chatId: $chatId\n    tfaToken: $tfaToken\n  ) {\n    id\n    amount\n    currency\n    user {\n      id\n      name\n      __typename\n    }\n    sendBy {\n      id\n      name\n      balances {\n        available {\n          amount\n          currency\n          __typename\n        }\n        vault {\n          amount\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'SendTip',
            'variables': {
                'userId': user_id,
                'amount': amount,
                'currency': currency,
                'isPublic': is_public,
                'chatId': 'c65b4f32-0001-4e1d-9cd6-e4b3538b43ae'
            }
        }
        if tfa_token:
            json_data['variables']['tfaToken'] = tfa_token
        response = self.session.post("https://stake.com/_api/graphql", headers=self.headers, json=json_data)
        if "errors" in response.json():
            raise StakeError(response.json()["errors"][0]["message"])
        return response.json()

    def get_address(self, currency: str):
        json_data = {
            "query":"query DepositAddress($chain: CryptoChainEnum, $currency: CryptoCurrencyEnum!, $type: WalletAddressType!, $infoCurrency: CurrencyEnum!) {\n  info {\n    currency(currency: $infoCurrency) {\n      requiredConfirmations\n      __typename\n    }\n    __typename\n  }\n  user {\n    id\n    depositAddress(chain: $chain, currency: $currency, type: $type) {\n      id\n      address\n      currency\n      __typename\n    }\n    __typename\n  }\n}\n",
            "operationName":"DepositAddress",
            "variables":{"currency":currency,"type":"default","infoCurrency":currency}
        }
        response = self.session.post("https://stake.com/_api/graphql", headers=self.headers, json=json_data)
        if "errors" in response.json():
            raise StakeError(response.json()["errors"][0]["message"])
        return response.json()
