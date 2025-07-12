from app.services.ergast import fetch_driver_laps
import random

def predict_lap_time(driver: str, year: int, circuit: str, compound: str):
    try:
        data = fetch_driver_laps(driver, year, circuit)

        races = data["MRData"]["RaceTable"].get("Races", [])
        if not races:
            raise ValueError("No races found for this circuit/year")

        laps = races[0].get("Laps", [])
        lap_times = []

        for lap in laps:
            for timing in lap.get("Timings", []):
                if timing.get("driverId", "").lower() == driver.lower():
                    time_str = timing["time"]  # mm:ss.sss
                    minutes, seconds = time_str.split(":")
                    total_seconds = int(minutes) * 60 + float(seconds)
                    lap_times.append(total_seconds)

        if not lap_times:
            raise ValueError("No valid lap times found for this driver")

        avg_lap_time = sum(lap_times) / len(lap_times)

    except Exception as e:
        print(f"[Lap Time Error] {e}")
        avg_lap_time = 90.0 + random.uniform(-1.0, 1.0)  # fallback default

    # Adjust for tyre compound
    tyre_modifier = {
        "soft": 0,
        "medium": 1.2,
        "hard": 2.0
    }

    lap_time = avg_lap_time + tyre_modifier.get(compound.lower(), 0)

    # Format to mm:ss.sss
    minutes = int(lap_time // 60)
    seconds = lap_time % 60
    formatted_time = f"{minutes}:{seconds:06.3f}"

    return {
        "driver": driver,
        "year": year,
        "circuit": circuit,
        "compound": compound,
        "predicted_lap_time_seconds": round(lap_time, 3),
        "predicted_lap_time_formatted": formatted_time
    }

def simulate_race_pace(driver: str, year: int, circuit: str, compound: str, laps: int):
    try:
        data = fetch_driver_laps(driver, year, circuit)

        races = data["MRData"]["RaceTable"].get("Races", [])
        if not races:
            raise ValueError("No races found")

        lap_data = races[0].get("Laps", [])
        lap_times = []

        for lap in lap_data:
            for timing in lap.get("Timings", []):
                if timing.get("driverId", "").lower() == driver.lower():
                    time_str = timing["time"]
                    minutes, seconds = time_str.split(":")
                    total_seconds = int(minutes) * 60 + float(seconds)
                    lap_times.append(total_seconds)

        if not lap_times:
            raise ValueError("No lap times found")

        avg_lap = sum(lap_times) / len(lap_times)

    except Exception as e:
        print(f"[Race Pace Error] {e}")
        avg_lap = 90.0 + random.uniform(-2.0, 2.0)

    # Tyre impact
    tyre_modifier = {
        "soft": 0,
        "medium": 1.2,
        "hard": 2.0
    }

    base_lap = avg_lap + tyre_modifier.get(compound.lower(), 0)

    simulated_laps = []
    for _ in range(laps):
        fluctuation = random.uniform(-0.5, 0.8)
        lap_time = base_lap + fluctuation
        minutes = int(lap_time // 60)
        seconds = lap_time % 60
        formatted = f"{minutes}:{seconds:06.3f}"
        simulated_laps.append(formatted)

    total_seconds = sum(
        [int(t.split(":")[0]) * 60 + float(t.split(":")[1]) for t in simulated_laps]
    )
    total_minutes = int(total_seconds // 60)
    remaining_seconds = total_seconds % 60
    total_time_formatted = f"{total_minutes}:{remaining_seconds:06.3f}"

    return {
        "driver": driver,
        "circuit": circuit,
        "laps": laps,
        "lap_times": simulated_laps,
        "total_race_time": total_time_formatted
    }

