from geopy.geocoders import Nominatim
import requests
import json


class LocationHandler:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="South Korea", timeout=None)

    def get_coordinates(self, address):
        """
        주어진 주소의 좌표를 반환합니다.

        Parameters:
        address (str): 좌표를 얻고자 하는 주소

        Returns:
        dict: 위도(latitude)와 경도(longitude)를 포함한 딕셔너리
        """
        try:
            geo = self.geolocator.geocode(address)
            if geo:
                crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
                return crd
            else:
                print("주소를 찾을 수 없습니다.")
                return None
        except Exception as e:
            print(f"좌표 변환 중 오류 발생: {e}")
            return None

    def get_current_location(self):
        """
        현재 위치의 좌표를 반환합니다.

        Returns:
        dict: 위도(latitude)와 경도(longitude)를 포함한 딕셔너리
        """
        try:
            here_req = requests.get("http://www.geoplugin.net/json.gp")
            if here_req.status_code != 200:
                print("현재좌표를 불러올 수 없음")
                return None
            else:
                location = json.loads(here_req.text)
                crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}
                return crd
        except Exception as e:
            print(f"현재 위치 좌표를 불러오는 중 오류 발생: {e}")
            return None


# 클래스 사용 예제
handler = LocationHandler()

# 현재 위치의 좌표 가져오기
current_crd = handler.get_current_location()
if current_crd:
    print(f"현재 위치 - 위도: {current_crd['lat']}, 경도: {current_crd['lng']}")

# 특정 주소의 좌표 가져오기
address_crd = handler.get_coordinates("대구 태전동")
if address_crd:
    print(f"주소 좌표 - 위도: {address_crd['lat']}, 경도: {address_crd['lng']}")
