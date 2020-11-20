# Pregled dinamike epidemije u posljednjih mjesec dana

## Objašnjenje načina mjerenja

U sljedećem tekstu nisu navedeni klasični podaci kakvi se viđaju svakog dana u vijestima te je zbog toga potrebno objasniti korištene metrike. S obzirom da se promatra dinamika epidemije, to znači da je bitna promjena brzine njezinog širenja. Ovakav način prikaza koristan je jer daje dublji uvid u epidemiju te se na temelju njega mogu uočiti trendovi i raditi prognoze.

Ugrubo, postoje tri opcije za brzinu širenja epidemije:

1. **Epidemija ubrzava** - broj novih slučajeva raste na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 2000 novih slučajeva u tjednu 8.-14. studenog)
2. **Epidemija stagnira** - broj novih slučajeva ostaje isti na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 1000 novih slučajeva u tjednu 8.-14. studenog)
3. **Epidemija usporava** - broj novih slučajeva pada na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 500 novih slučajeva u tjednu 8.-14. studenog)

Ovakva kretanja najbolje je pratiti izračunom **postotne promjene broja (npr. zaraženih) na tjednoj razini u odnosu na tjedan ranije**. 

> Primjer izračuna za 14. studeni:
>
> ((Ukupan broj novih zaraženih u tjednu 8.-14. studenog) - (Ukupan broj novih zaraženih u tjednu 1.-7. studenog)) / (Ukupan broj novih zaraženih u tjednu 1.-7. studenog) × 100%

Za prvu opciju takav izračun će dati 100%, za drugu 0% te za treću opciju -50%. Da bi epidemija završila, potreban je duži period njezinog usporavanja, tj. pada broja zaraženih. To dovodi i do sve manjeg broja preminulih. Ukoliko epidemija ubrzava, broj zaraženih raste, a kao posljedica toga i broj preminulih (s vremenskim odmakom) te se epidemija pogoršava. Ako epidemija stagnira, broj zaraženih je otprilike konstantan, a takav je i broj preminulih.

Zašto izračun na tjednoj razini? Zato što je tjedan dana dovoljno velik uzorak da se počnu uočavati trendovi. Izračunom za sedam dana odjednom uglavnom se poništavaju dnevne oscilacije nastale radi smanjenog/povećanog obujma testiranja, neradnih dana, praznika i sl. Ipak, ovakvim izračunom se trendovi uočavaju nešto sporije, npr. potrebno je nekoliko dana dobrih rezultata da bi se uočio pozitivan trend na grafu. S druge strane, kad se određeni trend uoči, onda je i njegova težina veća.

Podatke se može podijeliti u dvije grupe:

1. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv u oba smjera u budućnosti** - hospitalizirani, na respiratoru i aktivno oboljeli
2. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv samo prema gore u budućnosti** - broj zaraženih i broj preminulih

Stoga su za prvu grupu dovoljno dobri podaci o kumulativnom broju, dok su za drugu grupu korisniji podaci o promjeni broja, sve gledano kao **tjedna postotna promjena broja u odnosu na tjedan ranije**

## Tjedna promjena broja hospitaliziranih osoba

Vrlo važna metrika koja mnogo govori o brzini širenja epidemije, znatno točnije od broja novih slučajeva. Razlog tome je jednostavan - određeni udio zaraženih će svakako završiti u bolnici. Dnevne brojke su posljedica zaraza od prije 7-10 dana, što je vrijeme potrebno da se dobiju prvi simptomi i nakon toga se razvije dovoljno ozbiljan oblik bolesti za odlazak u bolnicu.

### Graf

![image](/20_11_2020/2011_promjena_hospitaliziranih.png)

### Tablica protekla dva tjedna

Datum | Ukupno hospitalizirani | Novi hospitalizirani | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 1330 | 23 | 30%
8.studeni | 1396 | 66 | 29%
9.studeni | 1451 | 55 | 29%
10.studeni | 1513 | 62 | 28%
11.studeni | 1545 | 32 | 28%
12.studeni | 1598 | 53 | 27%
13.studeni | 1620 | 22 | 26%
14.studeni | 1655 | 35 | 26%
15.studeni | 1710 | 55 | 25%
16.studeni | 1816 | 106 | 25%
17.studeni | 1827 | 11 | 24%
18.studeni | 1878 | 51 | 23%
19.studeni | 1944 | 66 | 23%
20.studeni | 1992 | 48 | 23%

### Zaključak

Zaključak je da je broj hospitaliziranih `naglo rastao kroz cijeli listopad` da bi početkom studenog taj `rast krenuo slabjeti uz daljnji trend prema stagnaciji`. To znači da je epidemija nakon `značajnog ubrzavanja` kroz listopad `prestala ubrzavati` krajem tog mjeseca ako se uzme u obzir da hospitalizacije kasne 7-10 dana za zarazama.

## Tjedna promjena broja osoba na respiratoru

Također vrlo važna metrika koja mnogo govori o brzini širenja epidemije, s razlikom što zaključci vrijede 7-14 dana unazad. To je tako jer je potrebno jedan do dva tjedna da pacijent nakon zaraze dobije prve simptome i zatim razvije tako ozbiljan oblik bolesti da završi na respiratoru.

### Graf

![image](/20_11_2020/2011_promjena_respirator.png)

### Tablica protekla dva tjedna

Datum | Ukupno na respiratoru | Novi na respiratoru | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 128 | -7 | 66%
8.studeni | 145 | 17 | 71%
9.studeni | 142 | -3 | 71%
10.studeni | 167 | 25 | 64%
11.studeni | 178 | 11 | 61%
12.studeni | 178 | 0 | 57%
13.studeni | 179 | 1 | 50%
14.studeni | 184 | 5 | 48%
15.studeni | 194 | 10 | 43%
16.studeni | 191 | -3 | 41%
17.studeni | 196 | 5 | 36%
18.studeni | 205 | 9 | 30%
19.studeni | 204 | -1 | 26%
20.studeni | 217 | 13 | 25%

### Zaključak

Zaključak je da je broj osoba na respiratoru u dva navrata `naglo rastao`, a zadnjih desetak dana `rast se smanjuje i ima tendenciju prema stagnaciji`. To također znači da je epidemija `počela smanjivati brzinu širenja krajem listopada`, ako se uzme u obzir da pacijenti završe na respiratoru tek 7-14 dana nakon zaraze. Takav zaključak se poklapa i sa zaključkom o hospitalizacijama.

## Tjedna promjena broja novih preminulih osoba

Važna metrika koja nam mnogo govori o razmjerima epidemije, također točnije od broja slučajeva. Naglasak je da je sadašnje stanje posljedica zaraza od prije otprilike tri tjedna - vrijeme potrebno da se razviju simptomi, osoba završi na intenzivnoj njezi i na kraju premine.

### Graf

![image](/20_11_2020/2011_promjena_preminulih.png)

### Tablica protekla dva tjedna

Datum | Ukupno preminuli | Novi preminuli | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 752 | 35 | 76%
8.studeni | 794 | 42 | 86%
9.studeni | 832 | 38 | 68%
10.studeni | 865 | 33 | 50%
11.studeni | 893 | 28 | 48%
12.studeni | 925 | 32 | 41%
13.studeni | 968 | 43 | 35%
14.studeni | 1006 | 38 | 23%
15.studeni | 1049 | 43 | 10%
16.studeni | 1082 | 33 | 5%
17.studeni | 1113 | 31 | 5%
18.studeni | 1151 | 38 | 8%
19.studeni | 1200 | 49 | 14%
20.studeni | 1257 | 57 | 15%

### Zaključak

Zaključak je da je broj novih preminulih ubrzano rastao `kroz cijeli listopad i početak studenog` da bi zadnjih tjedan dana `došao blizu stagnacije`. To znači da je `epidemija smanjila ubrzavanje uz trend prema stagnaciji krajem listopada`, ako se uzme u obzir da smrti kasne i do tri tjedna za zarazama. Takav zaključak se poklapa s podacima o broju hospitaliziranih i broju osoba na respiratoru.

## Tjedna promjena broja novih slučajeva - Hrvatska

Metrika koja nam govori o razmjerima epidemije. Problem je, naravno, što se nikako ne može "uloviti" sve zaražene te se računa da ih je u stvarnosti možda i 10 puta više. Dodatno, ako se značajno promijeni broj testiranih, porast će i broj zaraženih jer on uglavnom proporcionalno ovisi o broju testiranih. Ipak, u Hrvatskoj se ne testira velik broj nasumično odabranih ljudi pa se može reći da je ova metrika kroz vrijeme jednako reprezentativna, osobito u jesenskom valu epidemije.

### Graf

![image](/20_11_2020/2011_promjena_slucajeva_ukupno.png)

### Tablica protekla dva tjedna

Datum | Ukupno slučajeva | Novi slučajevi | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 64704 | 2399 | 0%
8.studeni | 67247 | 2543 | 4%
9.studeni | 68776 | 1529 | 4%
10.studeni | 70243 | 1467 | 4%
11.studeni | 72840 | 2597 | 5%
12.studeni | 75922 | 3082 | 6%
13.studeni | 78978 | 3056 | 6%
14.studeni | 81844 | 2866 | 11%
15.studeni | 84206 | 2365 | 8%
16.studeni | 85519 | 1313 | 4%
17.studeni | 87464 | 1945 | 7%
18.studeni | 90715 | 3251 | 10%
19.studeni | 93879 | 3164 | 9%
20.studeni | 96837 | 2958 | 7%

### Zaključak

Zaključak je da je na razini države `epidemija u listopadu eksplodirala` i velik broj ljudi se zarazio. To je dovelo i do znatno većih stopa preminulih početkom studenog. Ipak, taj veliki rast je `početkom studenog praktički nestao i uspostavio se trend blizak stagnaciji`. S druge strane, bitno je reći da čak i uz ovako male stope ubrazavanja, epidemija i dalje raste te je, nažalost, prema kraju studenog za očekivati dodatan manji porast broja preminulih.

## Tjedna promjena broja novih slučajeva - Zagreb

Za Zagreb se može smatrati da je nešto ispred ostatka zemlje po razvoju epidemije, ponajviše zato što u njemu živi najviše ljudi, najveća je interakcija, a to sve dovodi do povećane vjerojatnosti za brzo širenje zaraze, ali potom i njezino usporavanje.

### Graf

![image](/20_11_2020/2011_promjena_slucajeva_zg.png)

### Tablica protekla dva tjedna

Datum | Ukupno slučajeva | Novi slučajevi | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 16723 | 575 | -8%
8.studeni | 17184 | 461 | -12%
9.studeni | 17500 | 316 | -14%
10.studeni | 17868 | 368 | -12%
11.studeni | 18489 | 621 | -13%
12.studeni | 19194 | 705 | -10%
13.studeni | 19847 | 653 | -9%
14.studeni | 20401 | 554 | -5%
15.studeni | 20764 | 363 | -1%
16.studeni | 21055 | 291 | -2%
17.studeni | 21476 | 421 | -3%
18.studeni | 22080 | 604 | -2%
19.studeni | 22689 | 609 | -6%
20.studeni | 23313 | 624 | -6%

### Zaključak

Zaključak je da je u Zagrebu nakon `velikog rasta u listopadu`, epidemija brzo došla u `fazu stagnacije početkom studenog`. Uz daljnji pad broja zaraženih na tjednoj razini `epidemija u protekla dva tjedna u Zagrebu usporava` te se sve manje ljudi zaražuje.

## Tjedna promjena broja aktivnih slučajeva

Metrika koja nam govori o brzini širenja epidemije, vrlo slično kao promjena broja slučajeva. Dobar je prikaz omjera zaraženih i onih koji su ozdravili. Ako je graf u pozitivnom području, više ljudi se zarazilo, a ako je u negativnom, više ljudi je ozdravilo na tjednoj razini.

### Graf

![image](/20_11_2020/2011_promjena_aktivnih.png)

### Tablica protekla dva tjedna

Datum | Ukupno aktivnih | Novi aktivni | Tjedna promjena
:---  | :---: | :---: | :---: 
7.studeni | 15542 | -25 | 16%
8.studeni | 15678 | 136 | 10%
9.studeni | 14942 | -736 | 6%
10.studeni | 14524 | -418 | 4%
11.studeni | 15513 | 989 | 2%
12.studeni | 16348 | 835 | 2%
13.studeni | 16746 | 398 | 3%
14.studeni | 17090 | 344 | 5%
15.studeni | 16926 | -164 | 6%
16.studeni | 15699 | -1227 | 6%
17.studeni | 15371 | -328 | 7%
18.studeni | 16891 | 1520 | 7%
19.studeni | 17814 | 923 | 8%
20.studeni | 18193 | 379 | 8%

### Zaključak

Zaključak je vrlo sličan onome o promjeni broja slučajeva. `U listopadu se vrlo velik broj ljudi zarazio` uz ubrzavanje širenja epidemije, ali ulaskom u studeni `epidemija je tek u blagom ubrzavanju ili stagnaciji` uz znatno manju promjenu broja aktivnih slučajeva.

## Županije - Tjedna promjena broja novih slučajeva

Za jednostavniji pregled na razini županija odabrana je tjedna promjena broja novih slučajeva. Na temelju nje se vidi kako pojedine županije stoje u proteklih tjedan dana u odnosu na tjedan ranije. Plava boja je indikator da epidemija usporava, bijela da stagnira, crvena da epidemija ubrzava (kako je prikazano na skali uz kartu). Za ovu metriku vrijede ista pravila kao i za sve prethodne, kao što je opisano u uvodu teksta.

### Karta

![image](/20_11_2020/2011_promjena_karta.png)

### Tablica

Županija | Tjedna promjena
:---  | :---:
Istarska | 6%
Karlovačka | 27%
Zadarska | 61%
Primorsko-goranska | 14% 
Vukovarsko-srijemska | -22%
Šibensko-kninska | 18%
Osječko-baranjska | 11%
Splitsko-dalmatinska | 15%
Bjelovarsko-bilogorska | 4%
Brodsko-posavska | 7%
Dubrovačko-neretvanska | -24%
Zagrebačka | 10%
Grad Zagreb | -6%
Koprivničko-križevačka | 25% 
Krapinsko-zagorska | 28%
Ličko-senjska | 46%
Međimurska | 3%
Požeško-slavonska | 22%
Sisačko-moslavačka | -4%
Varaždinska | 8%
Virovitičko-podravska | 36%

### Zaključak

S karte je jasno vidljivo da većina županija i dalje ima porast broja zaraženih na tjednoj razini. Iznimke su grad Zagreb, istok i jug zemlje gdje epidemija usporava. Treba naglasiti da s obzirom na vrlo mali i/ili promjenjiv broj testiranja, čak niti izračun na tjednoj razini za neke županije nije dovoljno reprezentabilan.

## Bonus - Udio pozitivnih testova

Metrika koja nam može govoriti o razmjeru epidemije, ali se mora uzeti u obzir broj testiranja. Ukoliko se testira malo, očekivano je da je ta brojka veća, pogotovo ako je epidemija jače raširena među populacijom. 

> Izračun se vrši tako da se broj zaraženih podijeli s brojem testiranih.

### Graf

![image](/20_11_2020/2011_udio_pozitivnih_testova.png)

### Tablica protekla dva tjedna

Datum | Ukupno testova | Novi testovi | Udio pozitivnih
:---  | :---: | :---: | :---: 
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
20.studeni | 657872 | 8321 | 36%

### Zaključak

Zaključak je da Hrvatska ili `premalo testira i ima velik broj zaraženih` ili `da se većina slučajeva "ulovi"`. S obzirom na dosadašnja iskustva, `izglednija je prva opcija`. Ipak, ranije su navedeni znatno bolji načini za praćenje brzine širenja epidemije.

## Izvori:

[Koronavirus.hr - twitter](https://twitter.com/koronavirus_hr)

[Velebit AI - Covid-19](https://covid19hr.velebit.ai/d/zL99n2rZz/covid-19-hrvatska?orgId=3)

[Our world in data - COVID-19](https://ourworldindata.org/coronavirus)

[Worldometer - Coronavirus](https://www.worldometers.info/coronavirus)
