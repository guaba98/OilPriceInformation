import requests
import xmltodict

import LocationHandler

# 내 API = F240811248
MYAPI = "F240811248"


# 오피넷 유가정보 API
def domestic_average_price():
    """
    1. 전국 주유소 평균가격
    """

    url = f"http://www.opinet.co.kr/api/avgAllPrice.do?out=xml&code={MYAPI}"
    result = xmltodict.parse(requests.get(url).content)
    # (result)

    # 전국 휘발유 가격 평균가격 출력
    for i in result['RESULT']['OIL']:
        if i['PRODNM'] == '휘발유':
            print(i['PRICE'])

def radius_gas_station():
    """
    반경내 주유소: 특정 위치 내에 있는 주유소의 위치를 반환한다.
    """
    url = f"http://www.opinet.co.kr/api/aroundAll.do?code={MYAPI}&x=314681.8&y=544837&radius=5000&sort=1&prodcd=B027&out=xml"
    result = xmltodict.parse(requests.get(url).content)
    print(result)

radius_gas_station()