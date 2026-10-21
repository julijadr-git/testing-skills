---
name: oras-top3
description: Pateikia aktualią Vilniaus, Ukmergės ir Klaipėdos oro temperatūrą bei sąlygas. Naudok, kai prašoma „oras-top3“ arba šių trijų miestų orų palyginimo. Pirmiausia naudok prieinamą aktualių orų paslaugą ir tiksliai įvardyk faktiškai naudotą šaltinį; jei pirminis duomenų tiekėjas neatskleistas, taip ir parašyk. Jei aiškiai prašoma meteo.lt, naudok tik patvirtintus meteo.lt duomenis arba nurodyk, kad jų negavai.
---

# Oras TOP 3

## Tikslas
Kiekvieną kartą pateik Vilniaus, Ukmergės ir Klaipėdos **aktualią oro temperatūrą (°C) ir oro sąlygas**. Jei pateikiama prognozė, nurodyk prognozės laiką. Dabartines sąlygas ir prognozę aiškiai atskirk.

## Šaltinio pasirinkimas ir skaidrumas
1. Pagal nutylėjimą naudok agentui prieinamą **aktualių orų informacijos paslaugą** (pvz., integruotą „ChatGPT“ orų paslaugą), jei ją galima iškviesti. Kiekvieno užklausimo metu gauk naujus duomenis.
2. Jeigu integruota paslauga duoda rezultatus, šaltinį įvardyk tiksliai: **„ChatGPT integruota orų informacijos paslauga; pirminis meteorologinių duomenų tiekėjas neatskleistas“**, nebent konkreti užklausa aiškiai nurodo patikrinamą kitą tiekėją. **Neminek meteo.lt kaip šaltinio be įrodymų.**
3. Kai vartotojas aiškiai prašo duomenų **būtent iš meteo.lt**, naudok oficialią Lietuvos hidrometeorologijos tarnybos API: https://api.meteo.lt/ . Tam gali naudoti `scripts/weather.py` (instrukcijos žemiau). Jei nepavyksta, pranešk apie neprieinamumą; nekeisk šaltinio tyliai.
4. Jei abiem būdais gauti duomenų nepavyksta, aiškiai parašyk „Duomenų gauti nepavyko“. **Nespėliok temperatūros ir oro sąlygų.**
5. Jei vieno miesto duomenų trūksta, parodyk likusius miestus ir aiškiai pažymėk klaidą. Visus laikus pateik Lietuvos laiku (Europe/Vilnius), kiek leidžia šaltinis.

## Kaip naudoti integruotą orų paslaugą
- Atskirai užklausk Vilnių, Ukmergę ir Klaipėdą, Lietuva.
- Paimk **dabartinę** temperatūrą ir dabartines sąlygas; nepakeisk jų dienos didžiausia / mažiausia temperatūra ar kitos valandos prognoze.
- Jei šaltinis pateikia tik prognozę, pažymėk ją kaip prognozę ir nurodyk jos laiką.
- Patikrink, kad visi trys duomenų įrašai atitinka reikiamus miestus.

## Pasirinktinis oficialus meteo.lt kelias
Jeigu reikia konkrečiai meteo.lt šaltinio ir agentas turi Python 3.9+ bei tinklo prieigą, iš šio įgūdžio katalogo paleisk:

```bash
python3 scripts/weather.py
```

Ši programa skaito **meteo.lt orų prognozę**, o ne integruotos orų paslaugos dabartinių sąlygų duomenis. Ji naudoja https://api.meteo.lt/v1/places ir kiekvienos vietovės `/forecasts/long-term` duomenis. **Jos išvesties negalima vadinti tiesioginiais stebėjimais.** Jei programos nepavyksta paleisti arba ji grąžina klaidą, nurodyk tikrą rezultatą, ne tariamą meteo.lt prognozę.

Programos logikos testai (su fiktyviais duomenimis, be interneto):
```bash
python3 -m unittest discover -s evals -p 'test_*.py'
```

## Atsakymo forma

| Miestas | Oro temperatūra | Oro sąlygos |
| --- | --- | --- |
| Vilnius | ... °C | ... |
| Ukmergė | ... °C | ... |
| Klaipėda | ... °C | ... |

Po lentele pateik **duomenų laiką**, **duomenų tipą** (dabartinės sąlygos arba prognozė), **faktiškai naudotą šaltinį** ir, jei tiekėjas nenurodytas, informaciją apie **nežinomą pirminį tiekėją**. Jei šaltiniai tarp miestų skiriasi, tai nurodyk atskirai.

## Patikra
- Ar visi trys miestai pateikti taisyklinga tvarka?
- Ar nenaudojamos senos arba išgalvotos reikšmės?
- Ar aiškiai atskiriamos dabartinės sąlygos nuo prognozės?
- Ar meteo.lt įvardytas tik jei iš tikrųjų panaudotas?
- Ar pirminis tiekėjas nepriskirtas be patvirtinimo?
