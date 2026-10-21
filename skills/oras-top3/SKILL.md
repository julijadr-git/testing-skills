---
name: oras-top3
description: Pateikia naujausią prieinamą Vilniaus, Ukmergės ir Klaipėdos oro temperatūros bei sąlygų suvestinę pagal oficialius meteo.lt duomenis. Naudok, kai vartotojas prašo „oras-top3“, šių trijų miestų orų, temperatūros arba greito orų palyginimo. Kiekvieną kartą patikrink duomenis, nespėliok.
---

# Oras TOP 3

## Tikslas
Pateik artimiausią ateities orų **prognozę** Vilniui, Ukmergei ir Klaipėdai: oro temperatūrą (°C) ir sąlygas. Prognozės nevadink tiesioginiais stebėjimais.

## Oficialus šaltinis
- Lietuvos hidrometeorologijos tarnybos dokumentacija: https://api.meteo.lt/
- Vietovių kodai: https://api.meteo.lt/v1/places
- Prognozės užklausa: `https://api.meteo.lt/v1/places/{place-code}/forecasts/long-term`

## Rekomenduojamas vykdymas

Jeigu agentas gali vykdyti Python programas ir turi interneto prieigą, paleisk iš šio įgūdžio katalogo:

```bash
python3 scripts/weather.py
```

Programa pati suranda tikruosius miestų kodus per `/places`, atlieka JSON užklausas, atrenka artimiausius būsimus prognozės įrašus ir išveda lentelę. Jai pakanka standartinės Python 3.9+ bibliotekos (laiko juostoms naudojamas `zoneinfo`). Jei programa rodo klaidą, **nepakeisk rezultato spėjimu**. Testams paleisk `python3 -m unittest discover -s evals -p 'test_*.py'` įgūdžio kataloge. Testai naudoja fiktyvius duomenis ir nereikalauja interneto.

Jei agentas negali vykdyti kodo, naudok toliau aprašytą tiesioginių užklausų būdą. Tiesiog naršyklėje atidarytas JSON puslapis gali neturėti matomo turinio – tokiu atveju nelaikyk jo tinkamai nuskaitytu rezultatu.

## Vykdymas
1. Kiekvieną kartą iš naujo patikrink meteo.lt duomenis. Jei turi interneto ar HTTP užklausų įrankį, naudok jį; jei ne, atvirai nurodyk, kad įgūdžio neįmanoma įvykdyti be duomenų prieigos.
2. Vietovių sąraše surask tikslius Lietuvos vietovių pavadinimus Vilnius, Ukmergė ir Klaipėda bei jų `code`. Jei vietovių sąrašas neprieinamas, gali bandyti kodus `vilnius`, `ukmerge`, `klaipeda`, bet prieš naudodamas rezultatą patikrink API atsakymo `place.name` ir `place.countryCode` (`LT`).
3. Atskirai užklausk kiekvieno miesto `forecasts/long-term`. Jei grąžinamas netinkamas HTTP statusas, blogas JSON arba klaidinga vietovė, pažymėk konkrečiam miestui trūkstamus duomenis.
4. Lauką `forecastTimeUtc` skaityk kaip **UTC** laiką, net jei pateikta eilutė yra `YYYY-MM-DD HH:MM:SS` be laiko juostos žymos. Iš `forecastTimestamps` pasirink laiko atžvilgiu artimiausią įrašą, kurio prognozės laikas nėra ankstesnis už dabartinį UTC laiką. Jeigu būsimo įrašo nėra, pranešk, kad aktualios prognozės nėra.
5. Iš to paties pasirinkto įrašo paimk `airTemperature` (tikroji prognozuojama oro temperatūra, ne `feelsLikeTemperature`) ir `conditionCode`. Trūkstamų reikšmių neatspėk.
6. Kodą išversk pagal oficialų reikšmių sąrašą:
   - `clear` – giedra; `partly-cloudy` – mažai debesuota; `cloudy-with-sunny-intervals` – debesuota su pragiedruliais; `cloudy` – debesuota;
   - `light-rain` – nedidelis lietus; `rain` – lietus; `heavy-rain` – smarkus lietus; `thunder` – perkūnija; `isolated-thunderstorms` – trumpas lietus su perkūnija; `thunderstorms` – lietus su perkūnija; `heavy-rain-with-thunderstorms` – smarkus lietus su perkūnija;
   - `light-sleet` – nedidelė šlapdriba; `sleet` – šlapdriba; `freezing-rain` – lijundra; `hail` – kruša; `light-snow` – nedidelis sniegas; `snow` – sniegas; `heavy-snow` – smarkus sniegas; `fog` – rūkas.
   - Jei `conditionCode` yra `null`, nurodyk „oro sąlygos nenustatytos“. Jei nepažįstamas, pateik nepaaiškintą kodą ir jo neinterpretuok savavališkai.
7. Prognozės laiką konvertuok į `Europe/Vilnius` laiko juostą, įskaitant vasaros / žiemos laiko kaitą.
8. Dalinio sutrikimo atveju išsaugok sėkmingai gautų miestų rezultatus; nepavykus visiems – aiškiai nurodyk, kad duomenų gauti nepavyko. Nekeisk šaltinio nepaaiškinęs ir nepateik senų skaičių kaip naujų.

## Atsakymo forma

| Miestas | Temperatūra | Oro sąlygos | Prognozės laikas (Lietuvos) |
| --- | --- | --- | --- |
| Vilnius | ... °C | ... | ... |
| Ukmergė | ... °C | ... | ... |
| Klaipėda | ... °C | ... | ... |

Po lentele įrašyk: **Šaltinis:** Lietuvos hidrometeorologijos tarnyba (meteo.lt), https://api.meteo.lt/. **Duomenų tipas:** orų prognozė.

## Galutinė patikra
- Ar visų trijų miestų pavadinimai ir tvarka teisingi?
- Ar kiekvieno miesto temperatūra ir sąlygos paimtos iš to paties prognozės laiko įrašo?
- Ar nevadini prognozės faktiniais stebėjimais?
- Ar prognozės laikas nurodytas Lietuvos laiku?
- Ar nėra sugalvotų temperatūrų ar sąlygų, kai API nepasiekiama?
