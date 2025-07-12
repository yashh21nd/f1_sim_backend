import requests
def fetch_driver_laps(driver: str, year: int, circuit: str):
    # 🔧 MOCK response (until Ergast API is back online)
    return {
        "MRData": {
            "RaceTable": {
                "Races": [
                    {
                        "Laps": [
                            {"number": "1", "Timings": [{"driverId": driver, "time": "1:28.245"}]},
                            {"number": "2", "Timings": [{"driverId": driver, "time": "1:28.501"}]},
                            {"number": "3", "Timings": [{"driverId": driver, "time": "1:28.297"}]},
                            {"number": "4", "Timings": [{"driverId": driver, "time": "1:28.880"}]},
                            {"number": "5", "Timings": [{"driverId": driver, "time": "1:29.032"}]},
                            {"number": "6", "Timings": [{"driverId": driver, "time": "1:28.774"}]},
                            {"number": "7", "Timings": [{"driverId": driver, "time": "1:29.012"}]},
                            {"number": "8", "Timings": [{"driverId": driver, "time": "1:28.991"}]},
                            {"number": "9", "Timings": [{"driverId": driver, "time": "1:29.145"}]},
                            {"number": "10", "Timings": [{"driverId": driver, "time": "1:29.310"}]},
                        ]
                    }
                ]
            }
        }
    }
