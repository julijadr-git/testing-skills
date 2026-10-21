---
name: hockey-u11
description: Randa visas nuo šiandien suplanuotas „Sostinė Hockey U11“ ledo ritulio rungtynes oficialiame hockey.lt skyriuje „Tvarkaraščiai“. Naudok, kai prašoma „panaudok hockey-U11“, komandos būsimų rungtynių, datų, laikų, varžovų ar arenų tvarkaraščio.
---

# Hockey U11 – būsimos rungtynės

## Tikslas
Patikrink oficialų [Hockey Lietuva tvarkaraštį](https://www.hockey.lt/index.php/tvarkarasciai/12) ir pateik **visas svetainėje paskelbtas būsimas** būtent **Sostinė Hockey U11** komandos rungtynes, neapsiribodamas artimiausiomis dienomis ar pirmuoju puslapiu.

## Vykdymas
1. Kiekvieno paleidimo metu nustatyk dabartinę Lietuvos datą ir laiką laiko juostoje `Europe/Vilnius`. Nenaudok seno anksčiau gauto tvarkaraščio kaip dabartinio.
2. **Pirmasis ir pagrindinis šaltinis:** atverk oficialų komandos puslapį `https://www.hockey.lt/index.php/komandos/sostine-hockey-u11/120641`. Naudotojas patvirtino, kad jame matoma skiltis **„Artimiausios rungtynės“**. Perskaityk joje pateiktas rungtynes (data, laikas, abi komandos, arena, nuoroda, jei yra), tikrink, ar įrašai ateityje. Tada ieškok nuorodos **„Visas tvarkaraštis“** ir sek ją, kad rastum visas vėlesnes paskelbtas datas. Jei komandos puslapyje matomos tik kelios artimiausios rungtynės, nevadink jų pilnu sąrašu.
3. **Atsarginis kelias, kai komandos puslapis nepasiekiamas:** atverk `https://www.hockey.lt/index.php/tvarkarasciai/12` ir naudok naudotojo nurodytą komandos filtrą. **ID patikra:** jokio `team_id` nelaikyk patvirtintu vien todėl, kad užklausa pateikia U-11 įrašus. Reikalauk oficialaus komandos puslapio arba išsaugotos naršyklės filtro parinkties, kuri tiesiogiai sieja `Sostinė Hockey U11` su ID. Naudotojas pasirinkęs „Sostinė Hockey U11“ filtrą oficialioje svetainėje pateikė nuorodą su `team_id=120641` ir `div_id=47`. Naudok šį ID kaip naudotojo patvirtintą filtro pasirinkimą, tačiau tikrink, ar svetainės rezultatai atitinka tą komandą; senas `team_id=127728` netinkamas ir jo nenaudok.
4. Jei komandos filtras nepasiekiamas, nagrinėk visus tvarkaraščio puslapius ir ieškok komandos tarp **namų** arba **svečių** komandų; prireikus naudok oficialų „U-11“ diviziono filtrą. Vien diviziono pavadinimo `U-11` nepakanka rungtynėms priskirti komandai.
5. Pereik per **visą puslapiavimą** (pvz. `?page=2`, `?page=3` ir toliau) iki paskutinio pasiekiamo puslapio. Jei svetainė teikia datų filtrus, nustatyk pradžią nuo šiandien ir neribok pabaigos data, nebent svetainė to techniškai reikalauja. Jei filtrai riboja datas, tęsk per visą prieinamą intervalą. Jei matomas rezultatų skaičius, palygink jį su surinktomis eilutėmis.
6. Išsaugok tik tas rungtynes, kuriose aiškiai identifikuota tiksliai `Sostinė Hockey U11` (ne `Sostinė Hockey-2 U11`, ne `U10` ar `U12`). Išlaikyk skirtingas rungtynes net jei jos vyksta tą pačią dieną ar valandą.
7. Įtrauk tik rungtynes, kurių Lietuvos vietinis pradžios laikas yra **vėlesnis už patikros momentą**; praėjusių, prasidėjusių ar pasibaigusių rungtynių nerodyk. Jei nurodyta tik data, o ne laikas, tos dienos įrašą pažymėk kaip nepatvirtintą pagal laiką ir atskirai paaiškink.
8. Iš kiekvienos rungtynių eilutės surink datą, pradžios laiką, namų komandą, svečių komandą, areną ir tiesioginę rungtynių nuorodą, jeigu pateikta. Nežinomas reikšmes žymėk „nenurodyta“; nieko neatspėk.
9. Pašalink tik **tikrus pasikartojimus** pagal oficialų rungtynių ID arba tą patį datą, laiką, namų ir svečių komandų derinį bei areną. Surikiuok viską nuo artimiausių iki vėliausių.
10. Jei naršyklėje nesimato komandų pavadinimų (pvz., jie pateikti tik vaizduose), patikrink svetainės prieinamą HTML, komandų nuorodas, rungtynių detales arba naršyklės peržiūrą. **Nedaryk išvados apie komandą vien pagal laiką, areną ar U-11 divizioną.**
11. Jei negali perskaityti visų rezultatų, paaiškink apribojimą, nurodyk patikrintą diapazoną ir **neteik dalinio sąrašo kaip pilno**. Nenaudok paieškos sistemos fragmentų kaip vienintelio viso tvarkaraščio įrodymo.

## Diagnostika, jei komandų pavadinimai paslėpti

- Pirmiausia bandyk komandos profilį `https://www.hockey.lt/index.php/komandos/sostine-hockey-u11/120641`. Šio adreso turinio automatinis pasiekiamumas 2026-10-21 nebuvo patvirtintas; niekada netvirtink, kad nuskaitei rungtynes, jei puslapis neatsidaro. Jei prieinamas tik „Artimiausios rungtynės“, pažymėk, kad visos būsimos datos nepatikrintos.
- Jei komandos profilis neveikia, tikrink naudotojo tiesiogiai pateiktą oficialaus filtro adresą: `https://www.hockey.lt/index.php/tvarkarasciai/12?date_from=&date_till=&div_id=47&team_id=120641&div_tr=0&tr_id=0`. Palygink jį su U-11 divizionu `https://www.hockey.lt/index.php/tvarkarasciai/12?div_id=47`. Jei svetainė neatsako, nurodyk klaidą ir nekurk rungtynių.
- Jei naršymo priemonė grąžina tik tekstinį puslapį, ji gali praleisti paveikslėliuose ar nesusietuose HTML elementuose pateiktus komandų pavadinimus. Jei leidžiama, naudok interaktyvią naršyklę: rankiniu būdu pasirink `Sostinė Hockey U11` ir nukopijuok rezultato adresą.
- Jei interaktyvi naršyklė leidžia, atverk „Inspect“ → „Network“ („Tinklas“), pasirink komandą, pažiūrėk, kuri užklausa pasikeitė, ir palygink `team_id` su komandos pavadinimu filtro `select/option` HTML. Niekada nenaudok slapukų, prieigos žetonų ar privačios prisijungimo informacijos kaip tvarkaraščio šaltinio.
- Jei įrašai turi `game_id` nuorodas, patikrink kiekvieno įrašo oficialius rungtynių duomenis. Jei nuorodų nėra ir vienodo laiko U-11 rungtynių yra kelios, **nespėk varžovų**.
- Jei pirmos datos vienos, o U-11 diviziono puslapyje yra vėlesnių datų, nevadink filtruoto sąrašo užbaigtu, kol nenustatei, ar filtro rezultatai turi puslapiavimą / datos apribojimus. Bandymas atverti nepatvirtintą `page` parametrą nėra puslapiavimo patikra.

## Atsarginis metodas: rungtynių protokolai

1. Jei komandos filtras neveikia, atverk oficialų U-11 tvarkaraštį su `div_id=47` ir fiksuok visas būsimas eilutes jų **nesuplakdamas** pagal vienodą datą ir laiką.
2. Patikrink, ar kiekvienos eilutės HTML arba atveriamas elementas turi faktinį rungtynių `game_id` ir nuorodą į `/index.php/rungtyniu-statistika/73?game_id=...`. Nesugalvok ID ir nebandyk išvesti jo iš paeiliui einančių skaičių.
3. Jei rastas konkrečios eilutės `game_id`, atverk jos statistiką ir patikrink, ar **bent viena** komanda tiksliai yra `Sostinė Hockey U11`. Tik tada įtrauk tą eilutę į patvirtintų rungtynių sąrašą.
4. Protokolai su `game_id=10718` („Sostinė Hockey U11 – KSM STARTAS U11“) ir `game_id=10715` („Sostinė Hockey U11 – Elektrėnų SSC U11“) rodo, kad statistikos puslapis gali atskleisti pavadinimus, **bet neįrodo**, kad tai būsimos rungtynės ar kad jų ID susieti su dabartiniu tvarkaraščiu.
5. Jei per tekstinį naršymą tvarkaraščio nuorodos paslėptos, atlik interaktyvų atvėrimą tik turint naršyklės galimybę; kitu atveju nurodyk, kad protokolo ir datos sąsaja nepatvirtinta.
6. Paieškos sistemos rastą protokolą naudok tik kaip papildomą patikrinimą, o ne kaip visų būsimų rungtynių sąrašą.

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
