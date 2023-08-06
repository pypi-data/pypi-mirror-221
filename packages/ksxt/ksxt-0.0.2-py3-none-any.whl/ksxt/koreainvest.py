from base.exchange import RestExchange

import requests
import json
import pprint as pp


class KoreaInvest(RestExchange):
    def __init__(self, open_key: str, secret_key: str, is_dev: bool = False) -> None:
        super().__init__(
            id=__name__, 
            name='korea_investment', 
            zone='Asia/Seoul',
            is_dev=is_dev,
            open_key=open_key, 
            secret_key=secret_key
        )
        
        self.token = self._get_token()
    
    # region _____
    def __url__(self, path):
        return f'{self.URL_BASE}/{path}'

    def _get_token(self):
        path = "oauth2/tokenP"
        url = self.__url__(path=path)

        headers = {"content-type":"application/json"}
        body = {
            "grant_type":"client_credentials",
            "appkey":self.OPEN_KEY, 
            "appsecret":self.SECRET_KEY
        }
        
        res = requests.post(url, headers=headers, data=json.dumps(body))
        token = res.json()["access_token"]
        return token
    
    def _get_hash_key(self, datas):        
        path = "uapi/hashkey"
        url = self.__url__(path=path)

        headers = {
            'content-Type' : 'application/json',
            'appKey' : self.OPEN_KEY,
            'appSecret' : self.SECRET_KEY,
        }

        res = requests.post(url, headers=headers, data=json.dumps(datas))
        hkey = res.json()["HASH"]

        return hkey
    
    def _get_header(self, tr_id, request_type='get', datas=None):
        headers = {
            "content-type":"application/json", 
            "authorization": f"Bearer {self.token}",
            "appKey":self.OPEN_KEY,
            "appSecret":self.SECRET_KEY,
            "tr_id":tr_id
        }

        if request_type.upper() == 'post'.upper():
            if datas is None:
                assert Exception('post request need data.')
            
            headers['custtype'] = 'P'   # 개인 회원. 법인은 'B'
            headers['hashkey'] = self._get_hash_key(datas)

        return headers

    # endregion ____

    # region public feeder
    def fetch_markets(self):
        # TODO : API 지원하지 않음
        _config = self.tr_config['stock']['rest']
        return super().fetch_markets()
    
    def fetch_ticker(self, symbol: str):
        _config = self.tr_config['stock']['rest']['feeder']['fetch_ticker_price']
        path = _config['url'] #"uapi/domestic-stock/v1/quotations/inquire-price"
        url = self.__url__(path=path)
        tr_id = _config['tr'] #'FHKST01010100'
        headers = self._get_header(tr_id=tr_id)

        params = {
            "fid_cond_mrkt_div_code":"J",
            "fid_input_iscd": symbol
        }

        res = requests.get(url, headers=headers, params=params).json()
        
        return res
    
    def fetch_historical_data(self, symbol: str, time_frame: str):
        _config = self.tr_config['stock']['rest']['feeder']['fetch_ohlcv_stock_recent']
        path = _config['url'] #"uapi/domestic-stock/v1/quotations/inquire-daily-price"
        url = self.__url__(path=path)
        tr_id = _config['tr'] #'FHKST01010400'
        headers = self._get_header(tr_id=tr_id)

        params = {
            # find_cond_mrkt_div_code : J (주식, ETF, ETN)
            "fid_cond_mrkt_div_code":"J",
            "fid_input_iscd":symbol,
            "fid_org_adj_prc":"1",
            "fid_period_div_code":time_frame
        }

        res = requests.get(url, headers=headers, params=params).json()
        
        return res
    # endregion public feeder

    # region private feeder
    def fetch_user_info(self):
        # TODO : API 지원하지 않음
        return super().fetch_user_info()
    
    def fetch_balance(self, acc_num: str):
        _config = self.tr_config['stock']['rest']['feeder']['fetch_balance']
        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        headers = self._get_header(tr_id=tr_id)

        params = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "AFHR_FLPR_YN": 'N',
            "OFL_YN": 'N',
            "INQR_DVSN": '01',
            "UNPR_DVSN": '01',
            "FUND_STTL_ICLD_YN": "N",
            "FNCG_AMT_AUTO_RDPT_YN": 'N',
            "PRCS_DVSN": '01',
            "CTX_AREA_FK100": '',
            "CTX_AREA_NK100": ''
        }

        res = requests.post(url, headers=headers, params=params).json()
        return res
    
    def fetch_cash(self, acc_num: str):
        _config = self.tr_config['stock']['rest']['feeder']['fetch_cash']
        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        headers = self._get_header(tr_id=tr_id)

        params = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "PDNO": '',
            "ORD_UNPR": str(0),
            "ORD_DVSN": '00',
            "CMA_EVLU_AMT_ICLD_YN": 'N',
            "OVRS_ICLD_YN": "N"
        }

        res = requests.post(url, headers=headers, params=params).json()
        return res

    def fetch_screener(self, screen_id: str):
        # TODO : STEP3
        return super().fetch_screener(screen_id)
    
    def fetch_deposit_history(self, acc_num: str):
        # TODO : API 지원하지 않음
        return super().fetch_deposit_history(acc_num)
    
    def fetch_withdraw_history(self, acc_num: str):
        # TODO : API 지원하지 않음
        return super().fetch_withdraw_history(acc_num)
    # endregion private feeder

    # region broker
    def create_order(self, acc_num: str, symbol: str, ticket_type: str, price: float, qty: float, otype: str):
        if ticket_type == 'entry_long':
            _config = self.tr_config['stock']['rest']['broker']['send_order_entry']
        elif ticket_type == 'exit_long':
            _config = self.tr_config['stock']['rest']['broker']['send_order_exit']

        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        if otype.upper() == 'limit'.upper():
            order_dvsn = '00'
        elif otype.upper() == 'market'.upper():
            order_dvsn = '01'

        datas = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "PDNO": symbol,
            "ORD_DVSN": order_dvsn,
            "ORD_QTY": str(qty),    # string type 으로 설정
            "ORD_UNPR": str(price), # string type 으로 설정
        }

        headers = self._get_header(tr_id=tr_id, request_type='post', datas=datas)

        res = requests.post(url, headers=headers, data=json.dumps(datas)).json()
        return res
    
    def cancel_order(self, acc_num: str, order_id: str, symbol: str, price: float = 0, qty: float = 0, *args):
        _config = self.tr_config['stock']['rest']['broker']['send_modify_order']
        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        if 'KRX_FWDG_ORD_ORGNO' not in args:
            # TODO : ArgumentError or ParameterError 정의 필요.
            assert Exception('Parameter Error.')
            
        krx_order_id = args['KRX_FWDG_ORD_ORGNO']

        datas = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "KRX_FWDG_ORD_ORGNO": str(krx_order_id),
            "ORGN_ODNO":str(order_id),
            "RVSE_CNCL_DVSN_CD":"02",
            "ORD_DVSN":"00",
            "ORD_QTY":str(qty),
            "ORD_UNPR":str(price),
            "QTY_ALL_ORD_YN": "N",
        }

        # 수량 미입력시 전량 취소
        if qty == 0:
            datas['QTY_ALL_ORD_YN'] = 'Y'
        
        headers = self._get_header(tr_id=tr_id, request_type='post', datas=datas)

        res = requests.post(url, headers=headers, data=json.dumps(datas)).json()
        return res
    
    def modify_order(self, acc_num: str, order_id: str, price: float, qty: float, *args):
        _config = self.tr_config['stock']['rest']['broker']['send_modify_order']
        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        if 'KRX_FWDG_ORD_ORGNO' not in args:
            # TODO : ArgumentError or ParameterError 정의 필요.
            assert Exception('Parameter Error.')
            
        krx_order_id = args['KRX_FWDG_ORD_ORGNO']

        datas = {
            "CANO": acc_num,
            "ACNT_PRDT_CD": acc_num[-2:],
            "KRX_FWDG_ORD_ORGNO": str(krx_order_id),
            "ORGN_ODNO":str(order_id),
            "RVSE_CNCL_DVSN_CD":"01",
            "ORD_DVSN":"00",
            "ORD_QTY":str(qty),
            "ORD_UNPR":str(price),
            "QTY_ALL_ORD_YN": "Y",
        }

        # 수량 미입력시 전량 수정
        if qty == 0:
            datas['QTY_ALL_ORD_YN'] = 'Y'
        
        headers = self._get_header(tr_id=tr_id, request_type='post', datas=datas)

        res = requests.post(url, headers=headers, data=json.dumps(datas)).json()
        return res
    
    def fetch_open_order(self, acc_num: str, symbol: str = ''):
        return super().fetch_open_order(acc_num, symbol)
    
    def fetch_closed_order(self, acc_num: str, symbol: str = ''):
        return super().fetch_closed_order(acc_num, symbol)
    
    # endregion broker

    def is_holiday(self):
        _config = self.tr_config['stock']['rest']['feeder']['fetch_calendar_holiday']
        path = _config['url']
        url = self.__url__(path=path)
        tr_id = _config['tr']

        headers = self._get_header(tr_id=tr_id)

        params = {
            "BASS_DT": self.now.strftime('%Y%m%d'),
            "CTX_AREA_NK": '',
            "CTX_AREA_FK": ''
        }

        res = requests.post(url, headers=headers, params=params).json()
        return res