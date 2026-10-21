---
name: hockey-u11
description: Randa visas nuo šiandien suplanuotas „Sostinė Hockey U11“ ledo ritulio rungtynes oficialiame hockey.lt skyriuje „Tvarkaraščiai“. Naudok, kai prašoma „panaudok hockey-U11“, komandos būsimų rungtynių, datų, laikų, varžovų ar arenų tvarkaraščio.
---

# Hockey U11 – būsimos rungtynės

## Tikslas
Patikrink oficialų [Hockey Lietuva tvarkaraštį](https://www.hockey.lt/index.php/tvarkarasciai/12) ir pateik **visas svetainėje paskelbtas būsimas** būtent **Sostinė Hockey U11** komandos rungtynes, neapsiribodamas artimiausiomis dienomis ar pirmuoju puslapiu.

## Vykdymas
1. Kiekvieno paleidimo metu nustatyk dabartinę Lietuvos datą ir laiką laiko juostoje `Europe/Vilnius`. Nenaudok seno anksčiau gauto tvarkaraščio kaip dabartinio.
2. Atverk `https://www.hockey.lt/index.php/tvarkarasciai/12` („Tvarkaraščiai“). Rask komandos filtrą ir pasirink **Sostinė Hockey U11**. Jei įmanoma, naudok svetainės sugeneruotą filtruotą nuorodą su patikrintu `team_id`, tačiau nekonstruok ar neatspėk komandos ID.
3. **ID patikra:** jokio `team_id` nelaikyk patvirtintu vien todėl, kad užklausa pateikia U-11 įrašus. Reikalauk oficialaus komandos puslapio arba išsaugotos naršyklės filtro parinkties, kuri tiesiogiai sieja `Sostinė Hockey U11` su ID. Naudotojas pasirinkęs „Sostinė Hockey U11“ filtrą oficialioje svetainėje pateikė nuorodą su `team_id=120641` ir `div_id=47`. Naudok šį ID kaip naudotojo patvirtintą filtro pasirinkimą, tačiau tikrink, ar svetainės rezultatai atitinka tą komandą; senas `team_id=127728` netinkamas ir jo nenaudok.
4. Jei komandos filtras nepasiekiamas, nagrinėk visus tvarkaraščio puslapius ir ieškok komandos tarp **namų** arba **svečių** komandų; prireikus naudok oficialų „U-11“ diviziono filtrą. Vien diviziono pavadinimo `U-11` nepakanka rungtynėms priskirti komandai.
5. Pereik per **visą puslapiavimą** (pvz. `?page=2`, `?page=3` ir toliau) iki paskutinio pasiekiamo puslapio. Jei svetainė teikia datų filtrus, nustatyk pradžią nuo šiandien ir neribok pabaigos data, nebent svetainė to techniškai reikalauja. Jei filtrai riboja datas, tęsk per visą prieinamą intervalą. Jei matomas rezultatų skaičius, palygink jį su surinktomis eilutėmis.
6. Išsaugok tik tas rungtynes, kuriose aiškiai identifikuota tiksliai `Sostinė Hockey U11` (ne `Sostinė Hockey-2 U11`, ne `U10` ar `U12`). Išlaikyk skirtingas rungtynes net jei jos vyksta tą pačią dieną ar valandą.
7. Įtrauk tik rungtynes, kurių Lietuvos vietinis pradžios laikas yra **vėlesnis už patikros momentą**; praėjusių, prasidėjusių ar pasibaigusių rungtynių nerodyk. Jei nurodyta tik data, o ne laikas, tos dienos įrašą pažymėk kaip nepatvirtintą pagal laiką ir atskirai paaiškink.
8. Iš kiekvienos rungtynių eilutės surink datą, pradžios laiką, namų komandą, svečių komandą, areną ir tiesioginę rungtynių nuorodą, jeigu pateikta. Nežinomas reikšmes žymėk „nenurodyta“; nieko neatspėk.
9. Pašalink tik **tikrus pasikartojimus** pagal oficialų rungtynių ID arba tą patį datą, laiką, namų ir svečių komandų derinį bei areną. Surikiuok viską nuo artimiausių iki vėliausių.
10. Jei naršyklėje nesimato komandų pavadinimų (pvz., jie pateikti tik vaizduose), patikrink svetainės prieinamą HTML, komandų nuorodas, rungtynių detales arba naršyklės peržiūrą. **Nedaryk išvados apie komandą vien pagal laiką, areną ar U-11 divizioną.**
11. Jei negali perskaityti visų rezultatų, paaiškink apribojimą, nurodyk patikrintą diapazoną ir **neteik dalinio sąrašo kaip pilno**. Nenaudok paieškos sistemos fragmentų kaip vienintelio viso tvarkaraščio įrodymo.

## Diagnostika, jei komandų pavadinimai paslėpti

- Tikrink naudotojo tiesiogiai pateiktą oficialaus filtro adresą: `https://www.hockey.lt/index.php/tvarkarasciai/12?date_from=&date_till=&div_id=47&team_id=120641&div_tr=0&tr_id=0`. Palygink jį su U-11 divizionu `https://www.hockey.lt/index.php/tvarkarasciai/12?div_id=47`. Jei svetainė neatsako, nurodyk klaidą ir nekurk rungtynių.
- Jei naršymo priemonė grąžina tik tekstinį puslapį, ji gali praleisti paveikslėliuose ar nesusietuose HTML elementuose pateiktus komandų pavadinimus. Jei leidžiama, naudok interaktyvią naršyklę: rankiniu būdu pasirink `Sostinė Hockey U11` ir nukopijuok rezultato adresą.
- Jei interaktyvi naršyklė leidžia, atverk „Inspect“ → „Network“ („Tinklas“), pasirink komandą, pažiūrėk, kuri užklausa pasikeitė, ir palygink `team_id` su komandos pavadinimu filtro `select/option` HTML. Niekada nenaudok slapukų, prieigos žetonų ar privačios prisijungimo informacijos kaip tvarkaraščio šaltinio.
- Jei įrašai turi `game_id` nuorodas, patikrink kiekvieno įrašo oficialius rungtynių duomenis. Jei nuorodų nėra ir vienodo laiko U-11 rungtynių yra kelios, **nespėk varžovų**.
- Jei pirmos datos vienos, o U-11 diviziono puslapyje yra vėlesnių datų, nevadink filtruoto sąrašo užbaigtu, kol nenustatei, ar filtro rezultatai turi puslapiavimą / datos apribojimus. Bandymas atverti nepatvirtintą `page` parametrą nėra puslapiavimo patikra.

## Atsakymo forma
Pateik lietuviškai:

**Sostinė Hockey U11 – būsimos rungtynės**
Patikrinta: `YYYY-MM-DD HH:mm` (Lietuvos laiku).

| Data | Laikas | Varžovas | Namų / svečių rungtynės | Arena |
|---|---|---|---|---|

Po lentele nurodyk:
- iš viso rastų rungtynių skaičių;
- **šaltinį** – veikiančią oficialią filtruoto tvarkaraščio nuorodą ir, jei yra, rungtynių nuorodas;
- ar patikrintos visos viešai skelbiamos būsimos datos ir visi puslapiai.

Jei patikrinus visą tvarkaraštį nėra rungtynių, aiškiai parašyk „Šiuo metu būsimų rungtynių nepaskelbta“. Jei tikrinimas nepavyko, parašyk „Nepavyko patvirtinti viso tvarkaraščio“, o ne „Rungtynių nėra“.

## Patikimumas
- Vienintelis pirminis oficialaus tvarkaraščio šaltinis: `hockey.lt`.
- Kiti šaltiniai gali padėti rasti tinkamą puslapį, tačiau tokią informaciją pažymėk ir nesuplak su oficialiai patikrintais įrašais.
- Kai komandos pavadinimas, rungtynių būsena ar data neaiški, neatvaizduok įrašo kaip patvirtinto.
- Kiekvieną kartą iš naujo tikrink datas: tvarkaraščiai gali keistis.
