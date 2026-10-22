---
name: hockey-u11
description: Nuskaito Sostinė Hockey U11 komandos „Artimiausios rungtynės“ lentelę hockey.lt ir grąžina datą, laiką, svečių komandą bei areną. Naudok komandai „panaudok hockey-u11“. Tik paprašius tikrina visą sezono tvarkaraštį.
---

# Hockey U11 – artimiausios rungtynės

## Numatytasis vykdymas (greitas)
1. Naudodamas Work naršyklę atidaryk **tik** oficialų komandos puslapį: https://www.hockey.lt/index.php/komandos/sostine-hockey-u11/120641
2. Rask skiltį **„Artimiausios rungtynės“** ir nuskaityk **visas joje pateiktas eilutes**. Neatlik bendros paieškos, neatidarinėk kitų puslapių ar viso tvarkaraščio, jei ši skiltis perskaitoma.
3. Iš kiekvienos eilutės paimk: **datą, laiką, svečių komandą, areną**. Nekurk trūkstamų duomenų. Komandos puslapyje svečių komanda pateikta antrajame `td.t_team` elemente (nuorodos `title` arba paveikslėlio `alt` atributas); data / laikas – `td.t_game_date`, arena – `td.t_tpage a`.
4. Išlaikyk svetainėje rodomą eilučių tvarką. Pateik šaltinio nuorodą, patikros datą Lietuvos laiku ir eilučių skaičių. **Netvirtink, kad tai visos sezono rungtynės**: ši skiltis gali rodyti tik dalį tvarkaraščio.
5. Jei puslapis nepasiekiamas arba lentelės nepavyksta perskaityti, pateik konkrečią klaidą. Nenaudok ankstesnių pokalbių, ankstesnių patikrų ar šio failo pavyzdžių kaip naujų duomenų.

## Tik paprašius viso tvarkaraščio
Jei naudotojas aiškiai prašo **visų sezono / visų būsimų rungtynių**, atidaryk https://www.hockey.lt/index.php/tvarkarasciai/12?team_id=120641, patikrink, ar išliko `team_id=120641` filtras, prireikus peržiūrėk kitus puslapius ir atrink dar neprasidėjusias rungtynes pagal `Europe/Vilnius` laiką. Jei pilno tvarkaraščio perskaityti negalima, pažymėk apribojimą; nepriskirk bendro U11 diviziono rungtynių šiai komandai be patvirtinimo.

## Atsakymo formatas
**SOSTINĖ HOCKEY U11 – artimiausios rungtynės**

Patikrinta: YYYY-MM-DD HH:mm (Lietuvos laiku).

| Data | Laikas | Svečių komanda | Arena |
|---|---|---|---|

Iš viso: N rungtynių. Šaltinis: oficialus komandos puslapis.

Jei skiltyje nėra eilučių, aiškiai nurodyk, kad **šiuo metu lentelėje rungtynių nepateikta**, o ne kad visame sezone rungtynių nėra.
