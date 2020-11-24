# 22. studeni 2020. - Pregled epidemiološke situacije

## Način mjerenja

U sljedećem tekstu nisu navedeni klasični podaci kakvi se viđaju svakog dana u vijestima te je zbog toga potrebno objasniti korištene metrike. S obzirom da se na velikom broju grafova promatra dinamika epidemije, to znači da je bitna promjena brzine njezinog širenja. Ovakav način prikaza koristan je jer daje dublji uvid u epidemiju te se na temelju njega mogu uočiti trendovi i raditi prognoze.

Ugrubo, postoje tri opcije za brzinu širenja epidemije:

1. **Epidemija ubrzava** - broj novih slučajeva raste na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 2000 novih slučajeva u tjednu 8.-14. studenog)
2. **Epidemija stagnira** - broj novih slučajeva ostaje isti na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 1000 novih slučajeva u tjednu 8.-14. studenog)
3. **Epidemija usporava** - broj novih slučajeva pada na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 500 novih slučajeva u tjednu 8.-14. studenog)

Ovakva kretanja najbolje je pratiti izračunom **postotne promjene broja (npr. zaraženih) na tjednoj razini u odnosu na tjedan ranije**. 

> Primjer izračuna za 14. studeni:
> ((Ukupan broj novih zaraženih u tjednu 8.-14. studenog) - (Ukupan broj novih zaraženih u tjednu 1.-7. studenog)) / (Ukupan broj novih zaraženih u tjednu 1.-7. studenog) × 100%

Za prvu opciju takav izračun će dati 100%, za drugu 0% te za treću opciju -50%. Da bi epidemija završila, potreban je duži period njezinog usporavanja, tj. pada broja zaraženih. To dovodi i do sve manjeg broja preminulih. Ukoliko epidemija ubrzava, broj zaraženih raste, a kao posljedica toga i broj preminulih (s vremenskim odmakom) te se epidemija pogoršava. Ako epidemija stagnira, broj zaraženih je otprilike konstantan, a takav je i broj preminulih.

Zašto izračun na tjednoj razini? Zato što je tjedan dana dovoljno velik uzorak da se počnu uočavati trendovi. Izračunom za sedam dana uglavnom se poništavaju dnevne oscilacije nastale radi smanjenog/povećanog obujma testiranja, neradnih dana, praznika i sl. Ipak, ovakvim izračunom se trendovi uočavaju nešto sporije, npr. potrebno je nekoliko dana dobrih rezultata da bi se uočio pozitivan trend na grafu. S druge strane, kad se određeni trend uoči, onda je i njegova težina veća.

Podatke se može podijeliti u dvije grupe:

1. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv u oba smjera u budućnosti** - hospitalizirani, na respiratoru i aktivno oboljeli
2. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv samo prema gore u budućnosti** - broj zaraženih i broj preminulih

Stoga su za prvu grupu dovoljno dobri podaci o kumulativnom broju, dok su za drugu grupu korisniji podaci o promjeni broja, sve gledano kao **tjedna postotna promjena broja u odnosu na tjedan ranije**

## Tjedna promjena broja hospitaliziranih osoba

Vrlo važna metrika koja mnogo govori o brzini širenja epidemije, znatno točnije od broja novih slučajeva. Razlog tome je jednostavan - određeni udio zaraženih će svakako završiti u bolnici. Dnevne brojke su posljedica zaraza od prije 7-10 dana, što je vrijeme potrebno da se dobiju prvi simptomi i nakon toga se razvije dovoljno ozbiljan oblik bolesti za odlazak u bolnicu.

### Graf

![image](/22_11_2020/2211_promjena_hospitaliziranih.png)

### Tablica protekla dva tjedna

Datum | Ukupno hospitalizirani | Tjedna promjena
:---  | :---: | :---: 
9.studeni | 1451 | 29%
10.studeni | 1513 | 28%
11.studeni | 1545 | 28%
12.studeni | 1598 | 27%
13.studeni | 1620 | 26%
14.studeni | 1655 | 26%
15.studeni | 1710 | 25%
16.studeni | 1816 | 25%
17.studeni | 1827 | 24%
18.studeni | 1878 | 23%
19.studeni | 1944 | 23%
20.studeni | 1992 | 23%
21.studeni | 1981 | 22%
22.studeni | 2013 | 21%

### Zaključak

Broj hospitaliziranih je `ubrazano rastao kroz cijeli listopad` da bi se početkom studenog `ubrzavanje krenulo smanjivati uz daljnji trend prema stagnaciji`.

## Tjedna promjena broja osoba na respiratoru

Također vrlo važna metrika koja mnogo govori o brzini širenja epidemije, s razlikom što zaključci vrijede 7-14 dana unazad. To je tako jer je potrebno jedan do dva tjedna da pacijent nakon zaraze dobije prve simptome i zatim razvije tako ozbiljan oblik bolesti da završi na respiratoru.

### Graf

![image](/22_11_2020/2211_promjena_respirator.png)

### Tablica protekla dva tjedna

Datum | Ukupno na respiratoru | Tjedna promjena
:---  | :---: | :---:
9.studeni | 142 | 71%
10.studeni | 167 | 64%
11.studeni | 178 | 61%
12.studeni | 178 | 57%
13.studeni | 179 | 50%
14.studeni | 184 | 48%
15.studeni | 194 | 43%
16.studeni | 191 | 41%
17.studeni | 196 | 36%
18.studeni | 205 | 30%
19.studeni | 204 | 26%
20.studeni | 217 | 25%
21.studeni | 213 | 21%
22.studeni | 223 | 19%

### Zaključak

Broj osoba na respiratoru `u dva je vala ubrzano rastao`, a zadnjih desetak dana `ubrzavanje se smanjuje i ima tendenciju prema stagnaciji`.

## Tjedna promjena broja novih preminulih osoba

Važna metrika koja mnogo govori o razmjerima epidemije, također točnije od broja slučajeva. Naglasak je da je sadašnje stanje posljedica zaraza od prije otprilike tri tjedna - vrijeme potrebno da se razviju simptomi, osoba završi na intenzivnoj njezi i na kraju premine.

### Graf

![image](/22_11_2020/2211_promjena_preminulih.png)

### Tablica protekla dva tjedna

Datum | Novi preminuli | Tjedna promjena
:---  | :---: | :---: 
9.studeni | 38 | 68%
10.studeni | 33 | 50%
11.studeni | 28 | 48%
12.studeni | 32 | 41%
13.studeni | 43 | 35%
14.studeni | 38 | 23%
15.studeni | 43 | 10%
16.studeni | 33 | 5%
17.studeni | 31 | 5%
18.studeni | 38 | 8%
19.studeni | 49 | 14%
20.studeni | 57 | 15%
21.studeni | 47 | 17%
22.studeni | 49 | 19%

### Zaključak

Broj novih preminulih `ubrzano je rastao kroz cijeli listopad i početak studenog` da bi zatim na neko vrijeme `došao blizu stagnacije`. Nažalost, u zadnjih nekoliko dana ponovno je prisutno `ubrzavanje rasta` broja preminulih osoba.

## Tjedna promjena broja novih slučajeva - Hrvatska

Metrika koja govori o razmjerima epidemije. Problem je, naravno, što se nikako ne može "uloviti" sve zaražene te se računa da ih je u stvarnosti možda i 10 puta više. Dodatno, ako se značajno promijeni broj testiranih, porast će i broj zaraženih jer on uglavnom proporcionalno ovisi o broju testiranih. Ipak, u Hrvatskoj se ne testira velik broj nasumično odabranih ljudi pa se može reći da je ova metrika kroz vrijeme jednako reprezentativna, osobito u jesenskom valu epidemije.

### Graf

![image](/22_11_2020/2211_promjena_slucajeva_ukupno.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---:
9.studeni | 1529 | 4%
10.studeni | 1467 | 4%
11.studeni | 2597 | 5%
12.studeni | 3082 | 6%
13.studeni | 3056 | 6%
14.studeni | 2866 | 11%
15.studeni | 2365 | 8%
16.studeni | 1313 | 4%
17.studeni | 1945 | 7%
18.studeni | 3251 | 10%
19.studeni | 3164 | 9%
20.studeni | 2958 | 7%
21.studeni | 3573 | 8%
22.studeni | 3308 | 15%

### Zaključak

Na razini države epidemija je `značajno ubrzavala širenje kroz cijeli listopad` i velik broj ljudi se zarazio. To je dovelo i do znatno većih stopa preminulih početkom studenog. Taj veliki rast je `početkom studenog praktički nestao` i uspostavio se `trend blizak stagnaciji`. S druge strane, bitno je reći da čak i uz ovako male stope ubrazavanja, brzina širenja epidemije i dalje raste te je, nažalost, prema kraju studenog za očekivati dodatan manji porast broja preminulih.

## Tjedna promjena broja novih slučajeva - Zagreb

Za Zagreb se može smatrati da je (uz još nekoliko županija) nešto ispred ostatka zemlje po razvoju epidemije, ponajviše zato što u njemu živi najviše ljudi, najveća je interakcija, a to sve dovodi do povećane vjerojatnosti za brzo širenje zaraze, ali potom i njezino ranije usporavanje.

### Graf

![image](/22_11_2020/2211_promjena_slucajeva_zg.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---:
9.studeni | 316 | -14%
10.studeni | 368 | -12%
11.studeni | 621 | -13%
12.studeni | 705 | -10%
13.studeni | 653 | -9%
14.studeni | 554 | -5%
15.studeni | 363 | -1%
16.studeni | 291 | -2%
17.studeni | 421 | -3%
18.studeni | 604 | -2%
19.studeni | 609 | -6%
20.studeni | 624 | -6%
21.studeni | 822 | 2%
22.studeni | 560 | 10%

### Zaključak

U Zagrebu je nakon `velikog ubrzavanja širenja epidemije u listopadu`, brzo došla `faza stagnacije`, a zatim i `usporavanja brzine širenja` epidemije. 

## Tjedna promjena broja aktivnih slučajeva

Metrika koja govori o brzini širenja epidemije, vrlo slično kao promjena broja slučajeva. Ugrubo je dobar prikaz omjera zaraženih i onih koji su ozdravili. Ako je graf u pozitivnom području, više ljudi se zarazilo, a ako je u negativnom, više ljudi je ozdravilo na tjednoj razini.

### Graf

![image](/22_11_2020/2211_promjena_aktivnih.png)

### Tablica protekla dva tjedna

Datum | Ukupno aktivnih | Tjedna promjena
:---  | :---: | :---:
9.studeni | 14942 | 6%
10.studeni | 14524 | 4%
11.studeni | 15513 | 2%
12.studeni | 16348 | 2%
13.studeni | 16746 | 3%
14.studeni | 17090 | 5%
15.studeni | 16926 | 6%
16.studeni | 15699 | 6%
17.studeni | 15371 | 7%
18.studeni | 16891 | 7%
19.studeni | 17814 | 8%
20.studeni | 18193 | 8%
21.studeni | 19079 | 8%
22.studeni | 19985 | 10%

### Zaključak

`Kroz cijeli listopad epidemija je značajno ubrzavala` svoje širenje, ali ulaskom u studeni `epidemija je tek u blagom ubrzavanju ili stagnaciji` uz znatno manju promjenu broja aktivnih slučajeva.

## Tjedna promjena broja novih slučajeva prema dobi

Metrika koja govori o brzini širenja epidemije među različitim uzrastima. Situacija koja bi dovela do usporavanja epidemije je da su sve (ili većina) vrijednosti negativne, a ukoliko to nije moguće, bilo bi dobro da je veći porast koncentriran na lijevu stranu grafa jer su mladi daleko manje ugroženi od starijih osoba (osobito 70+ godina).

### Graf

![image](/22_11_2020/2211_promjena_dob.png)

### Tablica

Raspon godina | Tjedna promjena
:---  | :---:
0-9 | 35%
10-19 | 25%
20-29 | 19%
30-39 | 19%
40-49 | 25%
50-59 | 22%
60-69 | 20%
70-79 | 12%
80-89 | 24%
90+ | 29%

### Zaključak

S grafa je vidljivo da epidemija `ubrzava širenje po svim dobnim skupinama`. Manji broj testiranih i/ili manji broj ljudi u skupini može biti objašnjenje zašto su `prva i zadnja skupina najpogođenije`.

## Tjedna promjena broja novih slučajeva kod osoba starijih od 60 godina

Metrika koja govori o brzini širenja epidemije među osobama starijim od 60 godina, tj. u rizičnoj skupini. S obzirom da je najveći udio preminulih iz ove skupine, prema navedenom grafu može se prognozirati porast/pad broja preminulih u sljedećim danima i tjednima. Vrijednosti na ovome grafu moraju biti što manje kako bi i dnevni broj preminulih počeo padati.

### Graf

![image](/22_11_2020/2211_promjena_60.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---: 
9.studeni | 158 | 25%
10.studeni | 262 | 19%
11.studeni | 319 | 10%
12.studeni | 281 | 11%
13.studeni | 353 | 16%
14.studeni | 272 | 7%
15.studeni | 119 | 0%
16.studeni | 242 | 5%
17.studeni | 302 | 8%
18.studeni | 330 | 10%
19.studeni | 316 | 8%
20.studeni | 350 | 5%
21.studeni | 361 | 13%
22.studeni | 158 | 19%

### Zaključak

Epidemija je među najugroženijima `znatno ubrzavala širenje krajem listopada`. Do sredine studenog nastupila je `faza stagnacije uz povremene oscilacije` prema ubrzavanju.

## Županije - Tjedna promjena broja novih slučajeva

Ova karta daje brz i jednostavan uvid u epidemiološko stanje županija u proteklih tjedan dana u odnosu na tjedan ranije. Plava boja je indikator da epidemija usporava, bijela da stagnira, a crvena da epidemija ubrzava (kako je prikazano na skali uz kartu). Za ovu metriku vrijede ista pravila kao i za sve prethodne, kao što je opisano u uvodu teksta.

### Karta

![image](/22_11_2020/2211_promjena_karta.png)

### Tablica

Županija | Tjedna promjena
:---  | :---:
Istarska | 3%
Karlovačka | -3%
Zadarska | 67%
Primorsko-goranska | 15% 
Vukovarsko-srijemska | -14%
Šibensko-kninska | 31%
Osječko-baranjska | 30%
Splitsko-dalmatinska | 18%
Bjelovarsko-bilogorska | 3%
Brodsko-posavska | -6%
Dubrovačko-neretvanska | -9%
Zagrebačka | 27%
Grad Zagreb | 10%
Koprivničko-križevačka | 45% 
Krapinsko-zagorska | 19%
Ličko-senjska | 69%
Međimurska | 13%
Požeško-slavonska | 37%
Sisačko-moslavačka | 45%
Varaždinska | 0%
Virovitičko-podravska | 15%

### Zaključak

S karte je jasno vidljivo da epidemija `u većini županija ubrzava širenje`. Na dan izračuna najlošije stoje Zadarska i Ličko-senjska županija. Na tjednoj razini epidemija usporava u Posavini i na krajnjem jugu zemlje.

## Županije - Broj preminulih osoba na 1000 stanovnika

Na sljedećoj karti se dobro vidi koje su županije jače, a koje manje pogođene prema ukupnom broju preminulih na 1000 ljudi. Svjetlija crvena boja je indikator manjeg, a tamnija indikator većeg broja preminulih na 1000 stanovnika.

> Način izračuna:
> (Ukupan broj preminulih)/(Broj stanovnika/1000)

### Karta

![image](/22_11_2020/2211_preminuli_karta.png)

### Tablica

Županija | Broj preminulih na 1000 stanovnika
:---  | :---:
Istarska | 0.11
Karlovačka | 0.48
Zadarska | 0.12
Primorsko-goranska | 0.19 
Vukovarsko-srijemska | 0.23
Šibensko-kninska | 0.21
Osječko-baranjska | 0.63
Splitsko-dalmatinska | 0.31
Bjelovarsko-bilogorska | 0.28
Brodsko-posavska | 0.15
Dubrovačko-neretvanska | 0.24
Zagrebačka | 0.03
Grad Zagreb | 0.53
Koprivničko-križevačka | 0.31 
Krapinsko-zagorska | 0.44
Ličko-senjska | 0.43
Međimurska | 0.45
Požeško-slavonska | 0.14
Sisačko-moslavačka | 0.15
Varaždinska | 0.35
Virovitičko-podravska | 0.13

### Zaključak

S karte je jasno vidljivo koje su županije do sada teže bile pogođene, tj. gdje je veći udio umrlih. Nije jasno zašto neki prolaze lošije od drugih, ali se može otprilike reći da je kod pogođenijih najvjerojatnije i veći udio zaraženih te da su ispred ostalih po razvoju epidemije.

## Županije - Udio preminulih u ukupnom broju slučajeva (CFR)

Na sljedećoj karti prikazan je postotni udio ukupnog broja preminulih u ukupnom broju slučajeva za svaku županiju. Ova metrika daje dobar uvid o "lovljenju" ukupnog broja zaraza po županijama. S obzirom da se smatra da taj broj treba biti oko 0.15%, sve iznad te brojke (pogotovo značajno) upućuje da je registrirani broj slučajeva znatno manji od stvarnog broja zaraženih.

> Izračun se vrši tako da se ukupan broj preminulih podijeli s ukupnim brojem registriranih slučajeva

### Karta

![image](/22_11_2020/2211_CFR_karta.png)

### Tablica

Županija | CFR
:---  | :---:
Istarska | 0.83%
Karlovačka | 2.62%
Zadarska | 0.79%
Primorsko-goranska | 0.98% 
Vukovarsko-srijemska | 1.07%
Šibensko-kninska | 1.20%
Osječko-baranjska | 2.73%
Splitsko-dalmatinska | 1.03%
Bjelovarsko-bilogorska | 1.86%
Brodsko-posavska | 0.70%
Dubrovačko-neretvanska | 1.04%
Zagrebačka | 0.13%
Grad Zagreb | 1.70%
Koprivničko-križevačka | 1.76% 
Krapinsko-zagorska | 1.37%
Ličko-senjska | 2.02%
Međimurska | 1.19%
Požeško-slavonska | 0.89%
Sisačko-moslavačka | 0.91%
Varaždinska | 3.96%
Virovitičko-podravska | 0.75%

### Zaključak

S karte je vidljivo da većina županija ima `prilično visok CFR`. Primjerice, u Varaždinskoj županiji je to skoro 4% te se bez pretjerivanja može reći da je broj zaraženih u stvari barem 10 puta veći nego što je registrirani broj slučajeva. Jedina županija koja ima realan broj je Zagrebačka, možda radi većeg opsega testiranja, ali moguće i zato što bolesni idu u Zagreb te se tamo registriraju kao preminuli ukoliko dođe do takve situacije.

## Udio pozitivnih testova

Metrika koja može govoriti o razmjeru epidemije, ali se mora uzeti u obzir broj testiranja. Ukoliko se testira malo, očekivano je da je ta brojka veća, pogotovo ako je epidemija jače raširena među populacijom.

> Izračun se vrši tako da se broj zaraženih podijeli s brojem testiranih.

### Graf

![image](/22_11_2020/2211_udio_pozitivnih_testova.png)

### Tablica protekla dva tjedna

Datum | Broj testiranih | Udio pozitivnih
:---  | :---: | :---:
9.studeni | 5670 | 27%
10.studeni | 7803 | 19%
11.studeni | 9681 | 27%
12.studeni | 10156 | 30%
13.studeni | 9417 | 32%
14.studeni | 9614 | 30%
15.studeni | 8175 | 29%
16.studeni | 4861 | 27%
17.studeni | 7262 | 27%
18.studeni | 9126 | 36%
19.studeni | 8770 | 36%
20.studeni | 8321 | 36%
21.studeni | 9877 | 36%
22.studeni | 9216 | 36%

### Zaključak

Udio pozitivnih testova konstantno raste te je zadnjih nekoliko dana `dosegnuo maksimum`. Postoje dva moguća objašnjenja: 1. Dobro se "lovi" većina slučajeva te se testiraju velikim dijelom samo zaraženi, 2. Raširenost epidemije među populacijom znatno premašuje kapacitete testiranja.

## Dobno-spolna piramida potvrđenih slučajeva od početka epidemije

Prikaz broja slučajeva prema spolu u različitim dobnim skupinama.

### Graf

![image](/22_11_2020/2211_dob_spol_piramida.png)

### Tablica

Raspon godina | Muškarci | Žene
:---  | :---: | :---:
0-4 | 477 | 412
5-9 | 690 | 617
10-14 | 1639 | 1589
15-19 | 3014 | 2999
20-24 | 3923 | 3914
25-29 | 4458 | 4452
30-34 | 4672 | 4578
35-39 | 4485 | 5061
40-44 | 4705 | 5197
45-49 | 4455 | 5010
50-54 | 4218 | 4807
55-59 | 3955 | 4390
60-64 | 3533 | 3221
65-69 | 2460 | 2122
70-74 | 1828 | 1796
75-79 | 1200 | 1467
80-84 | 902 | 1339
85-89 | 503 | 913
90+ | 158 | 521

### Zaključak

Zanimljiva je činjenica da je do sada potvrđeno primjetno `više slučajeva kod žena` (razlika otprilike 3000). U skladu s time, veći dio dobnih skupina ima više slučajeva kod žena, s naglaskom na najstarije skupine.

## Izvori:

[Koronavirus.hr - twitter](https://twitter.com/koronavirus_hr)

[Koronavirus.hr - strojno čitljivi podaci](https://www.koronavirus.hr/otvoreni-strojno-citljivi-podaci/526)

[Velebit AI - Covid-19](https://covid19hr.velebit.ai/d/zL99n2rZz/covid-19-hrvatska?orgId=3)

[Our world in data - COVID-19](https://ourworldindata.org/coronavirus)

[Worldometer - Coronavirus](https://www.worldometers.info/coronavirus)

-----

Podaci će se osvježavati jednom tjedno, najvjerojatnije nedjeljom u poslijepodnevnim satima

Podaci o broju zaraženih po dobi i spolu mogu sse razlikovati od ostalih podataka jer su za njih izvor strojno čitljivi podaci koji nemaju isti interval osvježavanja kao ostali podaci (npr. službeni Twitter račun)
