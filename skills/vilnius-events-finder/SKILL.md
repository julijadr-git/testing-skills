---
name: vilnius-events-finder
description: Randa Vilniaus kultūrinius renginius vartotojo nurodytai datai ar laikotarpiui ir grąžina patikrinamą struktūrizuotą sąrašą. Naudok, kai prašoma rasti Vilniaus renginius, koncertus, spektaklius, parodas, festivalius, edukacijas, kiną ar ekskursijas. Neatlik asmeninio atrinkimo ar dienos planavimo.
---

# Vilniaus kultūrinių renginių paieška

## Paskirtis ir ribos
Surink kuo daugiau atitinkamo laikotarpio kultūrinių renginių **Vilniaus mieste**. Tai pirmas trijų įgūdžių darbo eigos etapas. Neatrink pagal pomėgius ir nesudaryk maršrutų: tai kitų įgūdžių atsakomybė.

## Įvestis
- Reikalauk vienos datos arba datų intervalo (imtinai). Formatas: YYYY-MM-DD.
- Jei data nenurodyta, paprašyk jos. Jei intervalo pabaiga ankstesnė už pradžią, paprašyk pataisyti.
- Santykines datas perskaičiuok Vilniaus laiko juostoje Europe/Vilnius; rezultate parodyk konkrečias datas.

## Kategorijos
Visuomet tikrink visas septynias kategorijas:
1. Koncertai ir muzikiniai renginiai
2. Teatro spektakliai
3. Parodos ir muziejų renginiai
4. Festivaliai
5. Edukaciniai renginiai ir kūrybinės dirbtuvės
6. Kinas
7. Ekskursijos ir kultūriniai pasivaikščiojimai

## Privalomi atradimo šaltiniai
1. https://visitvilnius.lt/lt/renginiai – bendri Vilniaus kultūriniai renginiai
2. https://allevents.lt/ – įvairūs bilietiniai renginiai
3. https://www.bilietai.lt/ – koncertai, festivaliai, teatras ir kitos kategorijos
4. https://kakava.lt/ – koncertai ir kiti bilietiniai renginiai
5. https://vsteatras.lt/ – oficialus Vilniaus senojo teatro repertuaras

Nenaudok Kavakare.com. Kitų organizatorių tinklalapius leidžiama naudoti **tik jau atrastiems** renginiams patikrinti. Atskirai ieškok koncertų abiejuose Bilietai.lt ir Kakava.lt, nepriklausomai nuo rezultatų kituose portaluose. Atskirai tikrink Vilniaus senojo teatro repertuarą, net jei jo spektaklių jau rado agregatoriai. Kiekviename iš keturių bendrųjų šaltinių išbandyk visų septynių kategorijų paiešką pagal miestą ir datą; naudok svetainės filtrus arba tikslines site: paieškas. Jei šaltinis neprieinamas, žymėk „šaltinis nepatikrintas“, o ne „renginių nėra“.

## Paieškos užbaigimas
Tik atlikęs pradinius patikrinimus visuose 5 šaltiniuose, vykdyk papildomas tikslines paieškas kitais raktažodžiais. Baik po **3 iš eilės papildomų paieškų, nesuradusių nė vieno naujo unikalaus seanso**. Jei įrankių ar svetainių ribojimai neleidžia to įvykdyti, sąžiningai pažymėk, kurios dalys nepatikrintos. Neteik išsamumo garantijos.

## Tikrinimas ir dublikatai
- Atrink renginius, kurie atitinka miestą ir laikotarpį; nepateik kitų miestų ar dienų renginių kaip tinkamų.
- Duomenų patikimumo eilė: (1) oficialus organizatoriaus repertuaras / puslapis, (2) konkretaus seanso bilietų platintojo puslapis, (3) agregatoriaus įrašas. Pirmenybę teik naujausiai patikimai renginio informacijai. Jei išlieka prieštaravimas, jį nurodyk, o ne spėk.
- Atšauktą arba į kitą datą perkeltą renginį pašalink iš aktyvaus pasirinkto laikotarpio sąrašo; perkėlimą gali paminėti atskirai.
- Sujunk to paties renginio **to paties seanso** įrašus, išsaugodamas visas naudingas tikras nuorodas. Skirtingomis datomis ar skirtingu laiku vykstančius seansus laikyk atskirais.
- Jei trūksta reikšmingų duomenų arba jų patvirtinimo, naudok būseną „Informacija nepatvirtinta“. Nežinomiems laukams rašyk „Nenurodyta“. Neišgalvok kainų, adresų, laikų ar interneto nuorodų.

## Privaloma išvestis kiekvienam seansui
- `pavadinimas`
- `data` (YYYY-MM-DD arba „Nenurodyta“)
- `pradzios_laikas` (HH:MM arba „Nenurodyta“)
- `vieta`
- `adresas`
- `kaina` (valiuta, intervalas, „Nemokamas“ arba „Nenurodyta“)
- `aprasymas` (trumpas ir faktinis)
- `kategorija` (viena iš septynių)
- `saltiniai` (tikros patikrintos URL nuorodos; sąrašas)
- `patikra` („Patvirtinta“ arba „Informacija nepatvirtinta“)
- `pastabos` (prieštaravimai, trūkstami laukai ar kiti apribojimai)

Pateik struktūrizuotą sąrašą arba JSON (struktūrizuotus duomenis), tinkamą perduoti `vilnius-events-filter`. Rikiuok pagal datą ir pradžios laiką, nežinomus laikus dėk dienos pabaigoje. Antraštėje pateik datas, miestą, unikalių seansų skaičių, patikrintus ir nepatikrintus šaltinius, apribojimus. Jei rezultatų nerasta, sakyk „Paieškoje renginių nerasta“, ne „Renginių nėra“.

## Kokybės patikra prieš atsakymą
Patikrink, kad kiekvienas įrašas turi visus laukus ir bent vieną realią šaltinio nuorodą; penki šaltiniai buvo patikrinti arba pažymėti kaip neprieinami; visos septynios kategorijos buvo bandytos; koncertų ir Vilniaus senojo teatro paieškos atliktos atskirai; dublikatai sujungti; nepatvirtinti duomenys nežymimi „Patvirtinta“; užbaigimo taisyklė įvykdyta arba aiškiai nurodytas ribojimas.
