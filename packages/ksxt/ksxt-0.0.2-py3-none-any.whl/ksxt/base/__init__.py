
import abc


class APIBrokerImpl(abc.ABC):
    """
    TODO : 필요한 함수 정의 필요.
    """
    @abc.abstractmethod
    def create_order(self, acc_num: str, symbol: str, ticket_type: str, price: float, qty: float, otype: str):
        """
        주문 발행

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            symbol (str): 종목정보(종목코드)
            ticket_type (str): EntryLong, EntryShort, ExitLong, ExitShort, ... 
            price (float): 가격
            qty (float): 수량
            otype (str): 시장가, 지정가, ...
        """
        pass

    @abc.abstractmethod
    def cancel_order(self, acc_num: str, order_id: str, symbol: str, price: float=0., qty: float=0., *args):
        """
        미체결 주문 취소

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            order_id (str): 주문 정보(주문 id)
            symbol (str): 종목정보(종목코드)
            price (float, optional): 가격. Defaults to 0..
            qty (float, optional): 수량. Defaults to 0..
        """
        pass

    @abc.abstractmethod
    def modify_order(self, acc_num: str, order_id: str, price: float, qty: float, *args):
        """
        미체결 주문 정정

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            order_id (str): 주문 정보(주문 id)
            price (float): 가격
            qty (float): 수량
        """
        pass
        
    
    @abc.abstractmethod
    def fetch_open_order(self, acc_num: str, symbol: str=''):
        """
        미체결 주문 내역 조회

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            symbol (str, optional): 종목정보(종목코드). Defaults to ''.
        """
        pass

    @abc.abstractmethod
    def fetch_closed_order(self, acc_num:str, symbol: str=''):
        """
        체결 내역 조회

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            symbol (str, optional): 종목정보(종목코드). Defaults to ''.
        """
        pass

    def reserve_order(self, acc_num:str, symbol: str, price: float, qty: float, target_date: str):
        """
        예약 주문 발행

        Args:
            acc_num (str): 계좌정보(계좌번호, 지갑정보)
            symbol (str): 종목정보(종목코드)
            price (float): 가격
            qty (float): 수량
            target_date (str): 예약일자
        """
        pass


class APIPublicFeedImpl(abc.ABC):
    """
    OpenAPI의 Public 영역 함수들 선언.
    * auth 정보 불필요
    """
    @abc.abstractmethod
    def fetch_markets(self):
        """
        Market 정보 조회
        """
        pass

    @abc.abstractmethod
    def fetch_ticker(self, symbol: str):
        """
        시세 정보 조회
        """
        pass

    @abc.abstractmethod
    def fetch_historical_data(self, symbol: str, time_frame: str):
        """
        과거 봉 정보 조회
        """
        pass

    def resample(self, df, timeframe: str, offset):
        ohlcv = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }
        
        result = df.resample(timeframe.upper(), offset=offset).apply(ohlcv)
        return result


class APIPrivateFeedImpl(abc.ABC):
    """
    OpenAPI의 Private 영역 함수들 선언.
    * auth 정보 필요
    """
    @abc.abstractmethod
    def fetch_user_info(self):
        """
        회원 정보 조회
        """
        pass

    @abc.abstractmethod
    def fetch_balance(self, acc_num: str):
        """
        보유 자산 조회

        Args:
            acc_num (str): 계좌 번호
        """
        pass

    @abc.abstractmethod
    def fetch_cash(self, acc_num: str):
        """
        예수금 조회

        Args:
            acc_num (str): 계좌 번호
        """
        pass

    @abc.abstractmethod
    def fetch_screener(self, screen_id: str):
        """
        Screen

        Args:
            screen_id (str): Screener 조회 값 (조건식 조회 결과)
        """
        pass

    @abc.abstractmethod
    def fetch_deposit_history(self, acc_num: str):
        """
        입금 내역 조회

        Args:
            acc_num (str): 계좌 번호
        """
        pass

    @abc.abstractmethod
    def fetch_withdraw_history(self, acc_num: str):
        """
        출금 내역 조회

        Args:
            acc_num (str): 계좌 번호
        """
        pass
