import requests

class ApiClient:
    BASE_URL = 'http://127.0.0.1:8000'

    @staticmethod
    def fetch_items():
        try:
            response = requests.get(f'{ApiClient.BASE_URL}/items/')
            response.raise_for_status()  # Проверяет наличие ошибок HTTP
            return response.json()  # Возвращает JSON-ответ как Python-объект
        except requests.RequestException as e:
            print(f"Error fetching items: {e}")
            return None