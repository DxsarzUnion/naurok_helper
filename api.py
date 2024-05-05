from requests import request
from bs4 import BeautifulSoup

class Client:

	url = "https://naurok.com.ua"


	def get_session_info(self, sessionId: str) -> dict:
		result = request("GET", url=f"{self.url}/api2/test/sessions/{sessionId}")
		try:result.json()
		except: raise Exception(f"Decoding error: {result.text}")
		return result.json()


	def get_session_id(self, uuid: str) -> int:
		result = request("GET", f"{self.url}/test/testing/{uuid}").text
		soup = BeautifulSoup(result, 'html.parser')
		div_element = soup.find('div', attrs={'ng-app': 'testik'})
		if div_element:
			ng_init_attr = div_element.get('ng-init')
			init_values = ng_init_attr.split(',')
			target_value = init_values[1] if len(init_values) > 1 else None
			return int(target_value)
		else:
			return None