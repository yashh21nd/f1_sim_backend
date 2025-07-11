import requests

def fetch_driver_laps(driver: str, year: int, circuit: str):
    url = f"http://ergast.com/api/f1/{year}/circuits/{circuit}/laps.json?limit=1000"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch lap data"}
    
    return response.json()
