import requests


url = "https://api.yoshlardaftari.uz/api/v2/check-application"


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,ru;q=0.9,uz;q=0.8",
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
    "Origin": "https://yoshlardaftari.uz",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"YaBrowser\";v=\"23\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
}

payload = {
        "passport": "AD0573350",
        "pin": "",
        "passport_type": 1,
        "birth_date": "17.04.2005",
        "type": "young"
    }

def getINFO(payload: dict) -> dict:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'status': 'error', 'message': f'Error {response.status_code}'}
