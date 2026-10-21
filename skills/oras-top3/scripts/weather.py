#!/usr/bin/env python3
"""Meteo.lt: artimiausia Vilniaus, Ukmergės ir Klaipėdos prognozė. Tik standartinė Python biblioteka."""
import json
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from zoneinfo import ZoneInfo

BASE = "https://api.meteo.lt/v1"
CITIES = ("Vilnius", "Ukmergė", "Klaipėda")
CONDITIONS = {
    "clear": "Giedra", "partly-cloudy": "Mažai debesuota",
    "cloudy-with-sunny-intervals": "Debesuota su pragiedruliais",
    "cloudy": "Debesuota", "light-rain": "Nedidelis lietus",
    "rain": "Lietus", "heavy-rain": "Smarkus lietus",
    "thunder": "Perkūnija", "isolated-thunderstorms": "Trumpas lietus su perkūnija",
    "thunderstorms": "Lietus su perkūnija",
    "heavy-rain-with-thunderstorms": "Smarkus lietus su perkūnija",
    "light-sleet": "Nedidelė šlapdriba", "sleet": "Šlapdriba",
    "freezing-rain": "Lijundra", "hail": "Kruša",
    "light-snow": "Nedidelis sniegas", "snow": "Sniegas",
    "heavy-snow": "Smarkus sniegas", "fog": "Rūkas",
}

def fetch_json(url):
    req = Request(url, headers={"User-Agent": "oras-top3/1.0 (weather data)", "Accept": "application/json"})
    try:
        with urlopen(req, timeout=15) as response:
            return json.load(response)
    except (HTTPError, URLError, OSError, ValueError) as exc:
        raise RuntimeError(f"užklausa nepavyko: {exc}") from exc

def utc_date(value):
    if not isinstance(value, str):
        raise ValueError("trūksta laiko")
    return datetime.fromisoformat(value.replace(" ", "T").replace("Z", "+00:00")).replace(tzinfo=timezone.utc) if not ("+" in value or value.endswith("Z")) else datetime.fromisoformat(value.replace(" ", "T").replace("Z", "+00:00")).astimezone(timezone.utc)

def interpret(city, payload, now):
    place = payload.get("place") or {}
    if place.get("name", "").casefold() != city.casefold() or place.get("countryCode") != "LT":
        raise ValueError("prognozė priklauso kitai vietovei")
    future = []
    for entry in payload.get("forecastTimestamps", []):
        try:
            moment = utc_date(entry["forecastTimeUtc"])
            if moment >= now:
                future.append((moment, entry))
        except (KeyError, ValueError, TypeError):
            continue
    if not future:
        raise ValueError("nėra būsimos prognozės")
    moment, record = min(future, key=lambda e: e[0])
    temp = record.get("airTemperature")
    if not isinstance(temp, (int, float)) or isinstance(temp, bool):
        temp_text = "Duomenų nėra"
    else:
        temp_text = f"{temp:g} °C"
    code = record.get("conditionCode")
    condition = CONDITIONS.get(code, f"Nežinomas kodas: {code}" if code is not None else "Oro sąlygos nenustatytos")
    local = moment.astimezone(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M")
    return temp_text, condition, local

def run(fetch=fetch_json, now=None):
    now = now or datetime.now(timezone.utc)
    print("| Miestas | Oro temperatūra | Oro sąlygos | Prognozės laikas (Lietuvos) |")
    print("| --- | --- | --- | --- |")
    try:
        places = fetch(f"{BASE}/places")
        codes = {p["name"].casefold(): p["code"] for p in places if p.get("countryCode") == "LT" and "name" in p and "code" in p}
    except (RuntimeError, KeyError, TypeError, ValueError) as exc:
        codes = {}
        place_error = str(exc)
    else:
        place_error = None

    ok = 0
    for city in CITIES:
        code = codes.get(city.casefold())
        try:
            if code is None:
                raise ValueError("miesto nerasta vietovių sąraše" if not place_error else f"vietovių sąrašas nepasiekiamas: {place_error}")
            payload = fetch(f"{BASE}/places/{code}/forecasts/long-term")
            temp, condition, when = interpret(city, payload, now)
            ok += 1
            print(f"| {city} | {temp} | {condition} | {when} |")
        except (RuntimeError, ValueError, KeyError, TypeError) as exc:
            reason = str(exc).replace("|", "/").replace("\n", " ")
            print(f"| {city} | Duomenų nėra | {reason} | — |")
    print("\nŠaltinis: Lietuvos hidrometeorologijos tarnyba (meteo.lt), https://api.meteo.lt/")
    print("Duomenų tipas: orų prognozė (ne faktiniai matavimai).")
    return 0 if ok == len(CITIES) else 1

if __name__ == "__main__":
    sys.exit(run())
