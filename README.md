# Pregled dinamike epidemije u posljednjih mjesec dana

## Objašnjenje načina mjerenja

U sljedećem tekstu nisu navedeni klasični podaci kakvi se viđaju svakog dana u vijestima te je zbog toga potrebno objasniti korištene metrike. S obzirom da se promatra dinamika epidemije, to znači da je bitna promjena brzine njezinog širenja. Ovakav način prikaza koristan je jer daje dublji uvid u epidemiju te se na temelju njega mogu uočiti trendovi i raditi prognoze.

Ugrubo, postoje tri opcije za brzinu širenja epidemije:

1. **Epidemija ubrzava** - broj novih (dnevnih) slučajeva raste u roku od tjedan dana (npr. 1000 novih slučajeva 1. studenog i 2000 novih slučajeva 8. studenog)
2. **Epidemija stagnira** - broj novih (dnevnih) slučajeva je ostao otprilike isti u roku od tjedan dana (npr. 1000 novih slučajeva 1. studenog i 1000 novih slučajeva 8. studenog)
3. **Epidemija usporava** - broj novih (dnevnih) slučajeva opada u roku od tjedan dana (npr. 1000 novih slučajeva 1. studenog i 500 novih slučajeva 8. studenog)

Ovakva kretanja najbolje je pratiti izračunom **postotne promjene broja (npr. zaraženih) za odabrani dan u odnosu na isti dan točno 7 dana ranije**. Primjer izračuna:

> (Broj novih zaraženih 8. studenog - Broj novih zaraženih 1. studenog) / (Broj novih zaraženih 1. studenog) × 100%

Za prvu opciju takav izračun će dati 100%, za drugu 0% te za treću opciju -50%. Da bi epidemija završila, potreban je duži period njezinog usporavanja, tj. pada broja zaraženih. To dovodi i do sve manjeg broja preminulih. Ukoliko epidemija ubrzava, broj zaraženih raste, a posljedično tome i broj preminulih (s vremenskim odmakom) te se epidemija pogoršava. Ako epidemija stagnira (aktualno stanje u Hrvatskoj), broj zaraženih je otprilike konstantan, a takav je i broj preminulih.

Zašto izračun na tjednoj razini? Zato što je to optimalna vremenska razlika da se uvide trendovi, ali i zato što se na isti dan otprilike jednako testira. Stoga ponedjeljak nije usporediv s petkom jer će uvijek imati manje brojeve zaraženih zbog manje odrađenih testova tijekom vikenda.

Podatke se može podijeliti u dvije grupe:

1. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv u oba smjera u budućnosti** - hospitalizirani, na respiratoru i aktivno oboljeli
2. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv samo prema gore u budućnosti** - broj zaraženih i broj preminulih

Stoga su za prvu grupu dovoljno dobri podaci o kumulativnom broju, dok su za drugu grupu korisniji podaci o promjeni broja, sve gledano kao **dan u odnosu na isti dan 7 dana ranije.**

## Promjena broja hospitaliziranih osoba

Vrlo važna metrika koja mnogo govori o brzini širenja epidemije, znatno točnije od broja novih slučajeva. Razlog tome je jednostavan - određeni udio zaraženih će svakako završiti u bolnici. Sadašnje stanje je posljedica zaraza od prije 7-10 dana, što je vrijeme potrebno da se dobiju prvi simptomi i nakon toga se razvije dovoljno ozbiljan oblik bolesti za odlazak u bolnicu.

### Graf

![image](/1911/1911_promjena_hospitaliziranih.png)

### Tablica protekla dva tjedna

Datum | Ukupno hospitalizirani | Novi hospitalizirani | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 1307 | 29 | 27%
7.studeni | 1330 | 23 | 27%
8.studeni | 1396 | 66 | 27%
9.studeni | 1451 | 55 | 29%
10.studeni | 1513 | 62 | 27%
11.studeni | 1545 | 32 | 27%
12.studeni | 1598 | 53 | 25%
13.studeni | 1620 | 22 | 24%
14.studeni | 1655 | 35 | 24%
15.studeni | 1710 | 55 | 22%
16.studeni | 1816 | 106 | 25%
17.studeni | 1827 | 11 | 21%
18.studeni | 1878 | 51 | 22%
19.studeni | 1944 | 66 | 22%

### Zaključak

Zaključak je da je broj hospitaliziranih `naglo rastao kroz cijeli listopad` da bi početkom studenog taj `rast postao sve manji uz tendenciju prema stagnaciji`. To znači da je epidemija `nakon značajnog ubrzavanja kroz listopad` dobila `tendenciju prema stagnaciji krajem tog mjeseca` ako se uzme u obzir da hospitalizacije kasne 7-10 dana za zarazama.

## Promjena broja osoba na respiratoru

Također vrlo važna metrika koja nam mnogo govori o brzini širenja epidemije, s razlikom što zaključci vrijede 7-14 dana unazad. To je tako jer je potrebno jedan do dva tjedna da pacijent nakon zaraze dobije prve simptome i zatim razvije tako ozbiljan oblik bolesti da završi na respiratoru.

### Graf

![image](/1911/1911_promjena_respirator.png)

### Tablica protekla dva tjedna

Datum | Ukupno na respiratoru | Novi na respiratoru | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 135 | 13 | 82%
7.studeni | 128 | -7 | 56%
8.studeni | 145 | 17 | 79%
9.studeni | 142 | -3 | 51%
10.studeni | 167 | 25 | 49%
11.studeni | 178 | 11 | 51%
12.studeni | 178 | 0 | 46%
13.studeni | 179 | 1 | 33%
14.studeni | 184 | 5 | 44%
15.studeni | 194 | 10 | 34%
16.studeni | 191 | -3 | 35%
17.studeni | 196 | 5 | 17%
18.studeni | 205 | 9 | 15%
19.studeni | 204 | -1 | 15%

### Zaključak

Zaključak je da je broj osoba na respiratoru u dva navrata `naglo rastao`, a zadnjih tjedan dana `rast ima tendenciju prema stagnaciji`. To također znači da je epidemija `krenula prema stagnaciji širenja krajem listopada`, ako se uzme u obzir da pacijenti završe na respiratoru tek 7-14 dana nakon zaraze. Takav zaključak se poklapa i sa zaključkom o hospitalizacijama.

## Promjena broja novih preminulih osoba

Važna metrika koja nam mnogo govori o razmjerima epidemije, također točnije od broja slučajeva. Naglasak je da je sadašnje stanje posljedica zaraza od prije otprilike tri tjedna - vrijeme potrebno da se razviju simptomi, osoba završi na intenzivnoj njezi i na kraju premine.

### Graf

![image](/1911/1911_promjena_preminulih.png)

### Tablica protekla dva tjedna

Datum | Ukupno preminuli | Novi preminuli | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 717 | 34 | 70%
7.studeni | 752 | 35 | 133%
8.studeni | 794 | 42 | 163%
9.studeni | 832 | 38 | 19%
10.studeni | 865 | 33 | -3%
11.studeni | 893 | 28 | 8%
12.studeni | 925 | 32 | 10%
13.studeni | 968 | 43 | 26%
14.studeni | 1006 | 38 | 9%
15.studeni | 1049 | 43 | 2%
16.studeni | 1082 | 33 | -13%
17.studeni | 1113 | 31 | -6%
18.studeni | 1151 | 38 | 36%
19.studeni | 1200 | 49 | 53%

### Zaključak

Zaključak je da je broj novih preminulih ubrzano rastao `kroz cijeli listopad i početak studenog` da bi zadnjih tjedan dana `počeo stagnirati`. To znači da je `epidemija smanjila ubrzavanje uz trend prema stagnaciji krajem listopada`, ako se uzme u obzir da smrti kasne i do tri tjedna za zarazama. Takav zaključak se poklapa s podacima o broju hospitaliziranih i broju osoba na respiratoru.

## Promjena broja novih slučajeva - Hrvatska

Metrika koja nam govori o razmjerima epidemije. Problem je, naravno, što se nikako ne može "uloviti" sve zaražene te se računa da ih je u stvarnosti možda i 10 puta više. Dodatno, ako se značajno promijeni broj testiranih, porast će i broj zaraženih jer on uglavnom proporcionalno ovisi o broju testiranih. Ipak, u Hrvatskoj se ne testira velik broj nasumično odabranih ljudi pa se može reći da je ova metrika kroz vrijeme jednako reprezentativna, osobito u jesenskom valu epidemije.

### Graf

![image](/1911/1911_promjena_slucajeva_ukupno.png)

### Tablica protekla dva tjedna

Datum | Ukupno slučajeva | Novi slučajevi | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 62305 | 2890 | 4%
7.studeni | 64704 | 2399 | -13%
8.studeni | 67247 | 2543 | 17%
9.studeni | 68776 | 1529 | 31%
10.studeni | 70243 | 1467 | 3%
11.studeni | 72840 | 2597 | 5%
12.studeni | 75922 | 3082 | 8%
13.studeni | 78978 | 3056 | 6%
14.studeni | 81844 | 2866 | 19%
15.studeni | 84206 | 2365 | -7%
16.studeni | 85519 | 1313 | -14%
17.studeni | 87464 | 1945 | 33%
18.studeni | 90715 | 3251 | 25%
19.studeni | 93879 | 3164 | 3%

### Zaključak

Zaključak je da je na razini države `epidemija u listopadu eksplodirala` i velik broj ljudi se zarazio. To je dovelo i do znatno većih stopa preminulih početkom studenog. Ipak, taj rast je `početkom studenog praktički nestao i počela je stagnacija`. Bitno je reći da se u pojedinim danima ta stagnacija `pretvara u usporavanje`, što znači da broj novih zaraženih opada. Ukoliko se ovakav trend održi ili produbi, prema kraju studenog bi broj novih preminulih također trebao početi opadati.

## Promjena broja novih slučajeva - Zagreb

Za Zagreb se može smatrati da je nešto ispred ostatka zemlje po razvoju epidemije, ponajviše zato što u njemu živi najviše ljudi, najveća je interakcija, a to sve dovodi do povećane vjerojatnosti za brzo širenje zaraze, ali potom i njezino usporavanje.

### Graf

![image](/1911/1911_promjena_slucajeva_zg.png)

### Tablica protekla dva tjedna

Datum | Ukupno slučajeva | Novi slučajevi | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 16148 | 664 | -11%
7.studeni | 16723 | 575 | -26%
8.studeni | 17184 | 461 | -33%
9.studeni | 17500 | 316 | -2%
10.studeni | 17868 | 368 | 31%
11.studeni | 18489 | 621 | -8%
12.studeni | 19194 | 705 | 8%
13.studeni | 19847 | 653 | -2%
14.studeni | 20401 | 554 | -4%
15.studeni | 20764 | 363 | -21%
16.studeni | 21055 | 291 | -8%
17.studeni | 21476 | 421 | 14%
18.studeni | 22080 | 604 | -3%
19.studeni | 22689 | 609 | -14%

### Zaključak

Zaključak je da je u Zagrebu nakon `velikog rasta u listopadu`, epidemija počela `stagnirati početkom studenog` te uz pad broja zaraženih na tjednoj razini `nerijetko i usporavati`, tj. broj novih zaraženih opada.

## Promjena broja aktivnih slučajeva

Metrika koja nam govori o brzini širenja epidemije, vrlo slično kao promjena broja slučajeva. Dobar je prikaz omjera zaraženih i onih koji su ozdravili. Ako je graf u pozitivnom području, više ljudi se zarazilo, a ako je u negativnom, više ljudi je ozdravilo na tjednoj razini.

### Graf

![image](/1911/1911_promjena_aktivnih.png)

### Tablica protekla dva tjedna

Datum | Ukupno aktivnih | Novi aktivni | Promjena u odnosu na 7 dana ranije
:---  | :---: | :---: | :---: 
6.studeni | 15567 | 211 | 3%
7.studeni | 15542 | -25 | -3%
8.studeni | 15678 | 136 | -1%
9.studeni | 14942 | -736 | 1%
10.studeni | 14524 | -418 | 3%
11.studeni | 15513 | 989 | 5%
12.studeni | 16348 | 835 | 6%
13.studeni | 16746 | 398 | 8%
14.studeni | 17090 | 344 | 10%
15.studeni | 16926 | -164 | 8%
16.studeni | 15699 | -1227 | 5%
17.studeni | 15371 | -328 | 6%
18.studeni | 16891 | 1520 | 9%
19.studeni | 17814 | 923 | 9%

### Zaključak

Zaključak je vrlo sličan onome o promjeni broja slučajeva. `U listopadu se vrlo velik broj ljudi zarazio` uz ubrzavanje širenja epidemije, ali ulaskom u studeni `epidemija je počela stagnirati` uz znatno manju promjenu broja aktivnih slučajeva.

## Županije - Prosječna tjedna promjena broja novih slučajeva

Za jednostavniji pregled na razini županija odabrana je prosječna tjedna promjena broja novih slučajeva. Na temelju nje se vidi kako pojedine županije stoje u proteklih tjedan dana. Bijela boja je indikator da epidemija stagnira ili čak usporava, a što je tamnija crvena boja to epidemija više ubrzava (kako je prikazano na skali uz kartu). Za ovu metriku vrijede ista pravila kao i za sve prethodne, kao što je opisano u uvodu teksta.

> Izračun se vrši tako da se za svaku županiju odredi postotna promjena broja novih slučajeva za svaki dan u odnosu na tjedan dana ranije, a zatim se izračuna prosjek za te vrijednosti u proteklih tjedan dana

### Karta

![image](/1911/1911_prosjecna_promjena.png)

### Tablica

Županija | Prosječna tjedna promjena
:---  | :---:
Istarska | 5%
Karlovačka | 12%
Zadarska | 61%
Primorsko-goranska | 40% 
Vukovarsko-srijemska | 8%
Šibensko-kninska | 61%
Osječko-baranjska | 25%
Splitsko-dalmatinska | 49%
Bjelovarsko-bilogorska | 88%
Brodsko-posavska | -5%
Dubrovačko-neretvanska | -5%
Zagrebačka | 8%
Grad Zagreb | -5%
Koprivničko-križevačka | 57% 
Krapinsko-zagorska | 15%
Ličko-senjska | 88%
Međimurska | -3%
Požeško-slavonska | 51%
Sisačko-moslavačka | 54%
Varaždinska | 10%
Virovitičko-podravska | 158%

### Zaključak

S karte je jasno vidljivo da županije s velikim brojem slučajeva zadnjih tjedan dana stagniraju, a nova znatna širenja se događaju u županijama koje su do sada imale manji broj slučajeva. Epidemija značajno ubrzava u `velikom dijelu Slavonije, u Lici te primorju (osim juga i Istre)`. `Sjeverozapad države je uz dio Slavonije (Posavina) i Dalmacije (jug)` ušao u fazu stagnacije epidemije ili je na putu prema tome.

## Bonus - Udio pozitivnih testova

Metrika koja nam može govoriti o razmjeru epidemije, ali se mora uzeti u obzir broj testiranja. Ukoliko se testira malo, očekivano je da je ta brojka veća, pogotovo ako je epidemija jače raširena među populacijom. 

> Izračun se vrši tako da se broj zaraženih podijeli s brojem testiranih.

### Graf

![image](/1911/1911_udio_pozitivnih_testova.png)

### Tablica protekla dva tjedna

Datum | Ukupno testova | Novi testovi | Udio pozitivnih
:---  | :---: | :---: | :---: 
6.studeni | 541605 | 9317 | 31%
7.studeni | 550229 | 8624 | 28%
8.studeni | 559016 | 8787 | 29%
9.studeni | 564686 | 5670 | 27%
10.studeni | 572489 | 7803 | 19%
11.studeni | 582170 | 9681 | 27%
12.studeni | 592326 | 10156 | 30%
13.studeni | 601743 | 9417 | 32%
14.studeni | 611357 | 9614 | 30%
15.studeni | 619532 | 8175 | 29%
16.studeni | 624393 | 4861 | 27%
17.studeni | 631655 | 7262 | 27%
18.studeni | 640781 | 9126 | 36%
19.studeni | 649551 | 8770 | 36%

### Zaključak

Zaključak je da Hrvatska ili `premalo testira i ima velik broj zaraženih` ili `da se većina slučajeva "ulovi"`. S obzirom na dosadašnja iskustva, `izglednija je prva opcija`. Ipak, ranije su navedeni znatno bolji načini za praćenje brzine širenja epidemije.

## Izvori:

[Koronavirus.hr - twitter](https://twitter.com/koronavirus_hr)

[Velebit AI - Covid-19](https://covid19hr.velebit.ai/d/zL99n2rZz/covid-19-hrvatska?orgId=3)

[Our world in data - COVID-19](https://ourworldindata.org/coronavirus)

[Worldometer - Coronavirus](https://www.worldometers.info/coronavirus)
