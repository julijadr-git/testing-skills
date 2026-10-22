---
name: hockey-u11
description: Randa visas nuo šiandien suplanuotas „Sostinė Hockey U11“ ledo ritulio rungtynes oficialiame hockey.lt skyriuje „Tvarkaraščiai“. Naudok, kai prašoma „panaudok hockey-U11“, komandos būsimų rungtynių, datų, laikų, varžovų ar arenų tvarkaraščio.
---

# Hockey U11 – būsimos rungtynės

## Tikslas
Rasti **visas būsimas Sostinė Hockey U11 rungtynių datas, laikus ir arenas**. Varžovai ir namų / svečių statusas nereikalingi. Patvirtintos komandos nuorodos:
- Komandos puslapis: https://www.hockey.lt/index.php/komandos/sostine-hockey-u11/120641
- Visas jos tvarkaraštis: https://www.hockey.lt/index.php/tvarkarasciai/12?team_id=120641

Naudotojas šią tvarkaraščio nuorodą gavo paspaudęs „Visas tvarkaraštis“ oficialiame komandos puslapyje, todėl **filtruotame tvarkaraštyje esančių rungtynių nereikia iš naujo priskirti komandai pagal varžovų pavadinimus**. Tikrink, kad atidarytas būtent šis adresas ir kad filtras nėra prarastas per peradresavimą. Nuorodos `utm_source` parametras nėra būtinas.

## Vykdymas
1. Kiekvieną kartą nustatyk dabartinę datą ir laiką `Europe/Vilnius`.
2. Pirmiausia atverk `https://www.hockey.lt/index.php/tvarkarasciai/12?team_id=120641`; tai oficialus konkrečios komandos „Visas tvarkaraštis“ adresas. Jei nepasiekiamas, bandyk komandos profilį ir jo skiltį „Artimiausios rungtynės“.
3. Filtruoto tvarkaraščio **kiekvienoje rungtynių eilutėje** ištrauk datą, laiką ir areną. Varžovų vardų / logotipų nerenk ir nereikalauk jų nuskaityti. Jeigu naudojamas atsarginis bendras U11 diviziono tvarkaraštis be komandos filtro, jo rungtynių **nepriskirk** „Sostinė Hockey U11“ automatiškai.
4. Įtrauk tik rungtynes, kurių pradžios momentas yra ateityje Lietuvos laiku. Rūšiuok chronologiškai, pašalink tik tikrus to paties įrašo dublikatus. Skirtingos rungtynės tuo pačiu laiku gali būti atskiri įrašai.
5. Patikrink visas filtruoto tvarkaraščio paskelbtas datas ir puslapius; jei prieinama tik „Artimiausios rungtynės“, aiškiai pažymėk, kad sąrašas gali būti nepilnas.
6. Jei oficialus puslapis neatsidaro arba nepavyksta perskaityti įrašų, **nesakyk, kad rungtynių nėra**. Pateik aiškią prieigos klaidą, o ankstesnius naudotojo pateiktus duomenis žymėk kaip istorinę patikrą.

## Atsakymo formatas
**SOSTINĖ HOCKEY U11 – būsimos rungtynės**
Patikrinta: YYYY-MM-DD HH:mm (Lietuvos laiku).

| Data | Laikas | Arena |
|---|---|---|

Nurodyk rungtynių skaičių, oficialią filtro nuorodą ir ar patikrintos visos būsimos datos. Varžovų ir namų / svečių komandos stulpelių nedėk.

## Patvirtinta HTML struktūra (2026-10-22)

Komandos profilio „Artimiausios rungtynės“ blokas yra `div.teams_item_block`, jo antraštė `div.teams_block_header`, rungtynių lentelė `div.schedules table.wf`. Iš kiekvienos duomenų eilutės (`tr.tr_odd` / `tr.tr_even`) skaityk:
- `td.t_game_date`: datą `YYYY MM DD` ir laiką `strong` elemente;
- `td.t_tpage a`: areną (tekstas arba `title` atributas).
Komandų `td.t_team` laukų skaityti **nereikia**, jei duomenys gaunami iš patvirtinto komandos puslapio arba su `team_id=120641` filtru.

2026-10-22 naudotojo pateiktame HTML šioje skiltyje buvo trys būsimi 2026-10-31 įrašai: 13:35, 14:05 ir 14:35, visų arena – Klaipėdos Akropolis. Tai **ankstesnės patikros pavyzdys**, o ne dabartinio tvarkaraščio garantija.

## Diagnostika

- Jei svetainė atsako su prieigos klaida, negalima tvirtinti, kad tvarkaraštis patikrintas.
- Jei skiltis „Artimiausios rungtynės“ rodoma, bet „Visas tvarkaraštis“ nepasiekiamas, pateik matomas datas ir pažymėk, kad sąrašas nebūtinai pilnas.
- Nereikalauk varžovų identifikavimo, rungtynių protokolų ar `game_id`, nes naudotojo tikslas – **data, laikas ir vieta**, o komandos filtras jau identifikuotas.
- Išsaugok svetainės šaltinio nuorodą atsakyme ir nesukurk nežinomų datų.

