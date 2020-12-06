# 06. prosinac 2020. - Pregled epidemiološke situacije

## Način mjerenja

U sljedećem tekstu nisu navedeni klasični podaci kakvi se viđaju svakog dana u vijestima te je zbog toga potrebno objasniti korištene metrike. S obzirom da se na velikom broju grafova promatra dinamika epidemije, to znači da je bitna promjena brzine njezinog širenja. Ovakav način prikaza koristan je jer daje dublji uvid u epidemiju te se na temelju njega mogu uočiti trendovi i raditi prognoze.

Ugrubo, postoje tri opcije za brzinu širenja epidemije:

1. **Epidemija ubrzava** - broj novih slučajeva raste na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 2000 novih slučajeva u tjednu 8.-14. studenog)
2. **Epidemija stagnira** - broj novih slučajeva ostaje isti na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 1000 novih slučajeva u tjednu 8.-14. studenog)
3. **Epidemija usporava** - broj novih slučajeva pada na tjednoj razini (npr. 1000 novih slučajeva u tjednu 1.-7. studenog i 500 novih slučajeva u tjednu 8.-14. studenog)

Ovakva kretanja najbolje je pratiti izračunom **postotne promjene broja (npr. novih slučajeva) na tjednoj razini u odnosu na tjedan ranije**. 

Primjer izračuna za 14. studeni:

> ((Ukupan broj slučajeva u tjednu 8.-14. studenog) - (Ukupan broj slučajeva u tjednu 1.-7. studenog)) / (Ukupan broj slučajeva u tjednu 1.-7. studenog) × 100%

Za prvu opciju takav izračun će dati 100%, za drugu 0% te za treću opciju -50%. Da bi epidemija završila, potreban je duži period njezinog usporavanja, tj. pada broja zaraženih. To dovodi i do sve manjeg broja preminulih. Ukoliko epidemija ubrzava, broj zaraženih raste, a kao posljedica toga i broj preminulih (s vremenskim odmakom) te se epidemija pogoršava. Ako epidemija stagnira, broj zaraženih je otprilike konstantan, a takav je i broj preminulih.

Zašto izračun na tjednoj razini? Zato što je tjedan dana dovoljno velik uzorak da se počnu uočavati trendovi. Izračunom za sedam dana uglavnom se poništavaju dnevne oscilacije nastale radi smanjenog/povećanog obujma testiranja, neradnih dana, praznika i sl. Ipak, ovakvim izračunom se trendovi uočavaju nešto sporije, npr. potrebno je nekoliko dana dobrih rezultata da bi se uočio pozitivan trend na grafu. S druge strane, kad se određeni trend uoči, onda je i njegova težina veća.

Podatke se može podijeliti u dvije grupe:

1. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv u oba smjera u budućnosti** - hospitalizirani, na respiratoru i aktivno oboljeli
2. **Podaci koji izražavaju broj osoba u određenom stanju, promjenjiv samo prema gore u budućnosti** - broj zaraženih i broj preminulih

Stoga su za prvu grupu dovoljno dobri podaci o kumulativnom broju, dok su za drugu grupu korisniji podaci o promjeni broja, sve gledano kao **tjedna postotna promjena broja u odnosu na tjedan ranije**

## Tjedna promjena broja hospitaliziranih osoba

Vrlo važna metrika koja mnogo govori o brzini širenja epidemije, znatno točnije od broja novih slučajeva. Razlog tome je jednostavan - određeni udio zaraženih će svakako završiti u bolnici. Dnevne brojke kasne za zarazama otprilike 10-14 dana, što je vrijeme potrebno da se dobiju prvi simptomi i nakon toga se razvije dovoljno ozbiljan oblik bolesti za odlazak u bolnicu.

### Graf

![image](/06_12_2020/0612_promjena_hospitaliziranih.png)

### Tablica protekla dva tjedna

Datum | Ukupno hospitalizirani | Tjedna promjena
:---  | :---: | :---: 
23.studeni | 2060 | 20%
24.studeni | 2093 | 19%
25.studeni | 2136 | 17%
26.studeni | 2171 | 16%
27.studeni | 2240 | 15%
28.studeni | 2221 | 14%
29.studeni | 2273 | 13%
30.studeni | 2358 | 13%
1.prosinac | 2351 | 13%
2.prosinac | 2408 | 13%
3.prosinac | 2501 | 13%
4.prosinac | 2427 | 13%
5.prosinac | 2514 | 13%
6.prosinac | 2543 | 13%

### Zaključak

Broj hospitaliziranih osoba je nakon smanjivanja stopa porasta kroz cijeli studeni u `zadnjih tjedan dana zaustavio taj trend na 13%`. To znači da broj hospitaliziranih i dalje ubrzano raste. Moguće je da ovo treba pripisati sezonalnosti bolesti te da u ovo doba godine znatno veći udio zaraženih završava u bolnici, iako broj zaraženih u stvari ne raste proporcionalno. U svakom slučaju, trend zasad nije povoljan i može se očekivati dodatan (manji) porast dnevnog broja preminulih osoba.

## Tjedna promjena broja osoba na respiratoru

Također vrlo važna metrika koja mnogo govori o brzini širenja epidemije, s naglaskom da i ovdje zaključci o zarazama vrijede 10-14 dana unazad. To je tako jer je potrebno jedan do dva tjedna da pacijent nakon zaraze dobije prve simptome i zatim razvije tako ozbiljan oblik bolesti da završi na respiratoru.

### Graf

![image](/06_12_2020/0612_promjena_respirator.png)

### Tablica protekla dva tjedna

Datum | Ukupno na respiratoru | Tjedna promjena
:---  | :---: | :---:
23.studeni | 235 | 17%
24.studeni | 244 | 19%
25.studeni | 240 | 19%
26.studeni | 252 | 20%
27.studeni | 266 | 20%
28.studeni | 262 | 21%
29.studeni | 260 | 21%
30.studeni | 255 | 19%
1.prosinac | 245 | 16%
2.prosinac | 252 | 14%
3.prosinac | 258 | 11%
4.prosinac | 262 | 7%
5.prosinac | 259 | 4%
6.prosinac | 264 | 2%

### Zaključak

Broj osoba na respiratoru je nakon konstantnog porasta protekli tjedan ovaj tjedan ponovno započeo `smanjivati stope porasta` i time zadnjih dana došao do vrijednosti bliskih stagnaciji. Ovo je pozitivan pomak i naznačava da broj osoba na respiratoru već tjedan dana ostaje otprilike isti. Nažalost, to je značajnim dijelom tako jer velik broj osoba s respiratora premine i samo ih zamjene novi, ali ukoliko se ovakav trend nastavi onda bi to značilo da ipak sve manje osoba završava na respiratoru. Ukoliko bi se povukla paralela s kretanjem epidemije, zaključak bi bio da je prije otprilike dva tjedna epidemija došla do vrhunca. Ipak, možda je prerano za ovakav zaključak i treba pričekati još barem tjedan dana da se dobar trend nastavi.

## Tjedna promjena broja novih preminulih osoba

Važna metrika koja mnogo govori o razmjerima epidemije, također točnije od broja slučajeva. Naglasak je da je sadašnje stanje posljedica zaraza od prije otprilike tri tjedna - vrijeme potrebno da se razviju simptomi, osoba završi na intenzivnoj njezi i na kraju premine.

### Graf

![image](/06_12_2020/0612_promjena_preminulih.png)

### Tablica protekla dva tjedna

Datum | Novi preminuli | Tjedna promjena
:---  | :---: | :---: 
23.studeni | 45 | 26%
24.studeni | 47 | 34%
25.studeni | 56 | 36%
26.studeni | 51 | 28%
27.studeni | 48 | 19%
28.studeni | 55 | 18%
29.studeni | 57 | 18%
30.studeni | 74 | 23%
1.prosinac | 75 | 25%
2.prosinac | 55 | 19%
3.prosinac | 48 | 17%
4.prosinac | 68 | 26%
5.prosinac | 70 | 27%
6.prosinac | 72 | 29%

### Zaključak

Broj novih preminulih osoba uz povremene oscilacije nažalost i dalje `ima trend porasta`. S obzirom na broj hospitaliziranih i osoba na respiratoru, ovakvo ponašanje krivulje je očekivano. To također upućuje da je epidemija ubrzavala širenje prije otprilike tri tjedna, dakle sredinom studenog. Ipak, moguće je da broj zaraženih nije proporcionalno rastao (tj. da je rastao u manjoj mjeri) jer se radi o sezonalnoj bolesti koja uzrokuje veći broj preminulih u hladnom dijelu godine.

## Tjedna promjena broja novih slučajeva - Hrvatska

Metrika koja govori o razmjerima epidemije sa zakašnjenjem od 5-7 dana, koliko je potrebno da osoba dobije simptome, testira se i dobije rezultat testa. Problem je, naravno, što se nikako ne može "uloviti" sve zaražene. Računa se da je u toplijem dijelu godine broj neregistriranih slučajeva bio i do nekoliko desetaka puta veći od službenih brojki jer je bolest sezonalna i u tom dijelu godine uzrokuje velik udio asimptomatskih ili vrlo blagih slučajeva koji se ne testiraju. Dolaskom hladnijeg dijela godine registrira se sve veći udio zaraženih jer su sve učestaliji teži slučajevi koji završavaju na testiranju pa je stvarna brojka na dnevnoj razini trenutno samo nekoliko puta veća od službene. 

### Graf

![image](/06_12_2020/0612_promjena_slucajeva_ukupno.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---:
23.studeni | 1973 | 20%
24.studeni | 2323 | 19%
25.studeni | 3603 | 17%
26.studeni | 4009 | 21%
27.studeni | 4080 | 28%
28.studeni | 3987 | 25%
29.studeni | 2919 | 17%
30.studeni | 1830 | 13%
1.prosinac | 2900 | 14%
2.prosinac | 3539 | 11%
3.prosinac | 4534 | 9%
4.prosinac | 3955 | 3%
5.prosinac | 4084 | 2%
6.prosinac | 2899 | 4%

### Zaključak

Na razini države epidemija je ubrzavala širenje kroz cijeli studeni i velik broj ljudi se zarazio. Na sreću, proteklih tjedan dana dolazi do `pada stopa ubrzavanja širenja epidemije`, a zadnjih par dana te vrijednosti su `bliske stagnaciji`. To može upućivati da je Hrvatska krajem studenog prošla vrh epidemije, ali potreban je duži ovakav trend da bi se to tvrdilo sa sigurnošću.

## Tjedna promjena broja novih slučajeva - Zagreb

Za Zagreb se može smatrati da je (uz još nekoliko županija) nešto ispred ostatka zemlje po razvoju epidemije, ponajviše zato što u njemu živi najviše ljudi, najveća je interakcija, a to sve dovodi do povećane vjerojatnosti za brzo širenje zaraze, ali potom i njezino ranije usporavanje.

### Graf

![image](/06_12_2020/0612_promjena_slucajeva_zg.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---:
23.studeni | 343 | 12%
24.studeni | 445 | 11%
25.studeni | 595 | 11%
26.studeni | 611 | 14%
27.studeni | 607 | 15%
28.studeni | 647 | 2%
29.studeni | 349 | -8%
30.studeni | 236 | -12%
1.prosinac | 506 | -11%
2.prosinac | 639 | -10%
3.prosinac | 669 | -9%
4.prosinac | 740 | -5%
5.prosinac | 675 | 0%
6.prosinac | 384 | 7%

### Zaključak

Zagreb je `velik dio studenog i početak prosinca proveo uz trend usporavanja širenja epidemije`. To potvrđuje tvrdnju da je Zagreb ispred ostatka zemlje gdje je zabilježeno ubrzavanje širenja epidemije, često značajno. Za očekivati je povremene kraće periode pozitivnih stopa brzine širenja epidemije, ali ukoliko se gleda šira slika, Zagreb već duže vrijeme stoji dobro po pitanju brzine širenja epidemije te broj oboljelih polagano opada.

## Tjedna promjena broja aktivnih slučajeva

Metrika koja govori o brzini širenja epidemije, vrlo slično kao promjena broja slučajeva. Ugrubo je dobar prikaz omjera zaraženih i onih koji su ozdravili. Ako je graf u pozitivnom području, više ljudi se zarazilo, a ako je u negativnom, više ljudi je ozdravilo na tjednoj razini.

### Graf

![image](/06_12_2020/0612_promjena_aktivnih.png)

### Tablica protekla dva tjedna

Datum | Ukupno aktivnih | Tjedna promjena
:---  | :---: | :---:
23.studeni | 19275 | 12%
24.studeni | 19161 | 15%
25.studeni | 20691 | 17%
26.studeni | 21725 | 19%
27.studeni | 22408 | 21%
28.studeni | 23573 | 22%
29.studeni | 23062 | 22%
30.studeni | 21457 | 20%
1.prosinac | 21250 | 18%
2.prosinac | 22610 | 16%
3.prosinac | 23942 | 15%
4.prosinac | 24190 | 12%
5.prosinac | 24190 | 9%
6.prosinac | 23740 | 8%

### Zaključak

Stope rasta broja aktivnih slučajeva su nakon povećavanja kroz velik dio studenog `u posljednjih tjedan dana dobile trend opadanja`, te bi uskoro moglo doći do stagnacije. To također može upućivati na zaključak da je epidemija dosegnula vrhunac krajem studenog. Ipak, i dalje se radi o pozitivnih stopama što znači da se i dalje veći broj ljudi razboli nego što ozdravi na tjednoj razini.

## Tjedna promjena broja novih slučajeva prema dobi

Metrika koja govori o brzini širenja epidemije među različitim uzrastima. Situacija koja bi dovela do usporavanja epidemije je da su sve (ili većina) vrijednosti negativne, a ukoliko to nije moguće, bilo bi dobro da je veći porast koncentriran na lijevu stranu grafa jer su mladi daleko manje ugroženi od starijih osoba (osobito 70+ godina).

### Graf

![image](/29_11_2020/2911_promjena_dob.png)

### Tablica

Raspon godina | Tjedna promjena
:---  | :---:
0-9 | 29%
10-19 | 13%
20-29 | 14%
30-39 | 13%
40-49 | 11%
50-59 | 3%
60-69 | 18%
70-79 | 12%
80-89 | 20%
90+ | 71%

### Zaključak

S grafa je vidljivo da epidemija `ubrzava širenje po svim dobnim skupinama`. Posebno je alarmantan podatak o vrlo velikom tjednom porastu broja slučajeva kod osoba starijih od 90 godina. Posljedica bi mogla biti da u idućim danima i tjednima dođe do dodatnog porasta broja hospitaliziranih i preminulih.

## Tjedna promjena broja novih slučajeva kod osoba starijih od 60 godina

Metrika koja govori o brzini širenja epidemije među osobama starijim od 60 godina, tj. u rizičnoj skupini. S obzirom da je najveći udio preminulih iz ove skupine, prema navedenom grafu može se prognozirati porast/pad broja preminulih u sljedećim danima i tjednima. Vrijednosti na ovome grafu moraju biti što manje kako bi i dnevni broj preminulih počeo padati.

### Graf

![image](/29_11_2020/2911_promjena_60.png)

### Tablica protekla dva tjedna

Datum | Novi slučajevi | Tjedna promjena
:---  | :---: | :---: 
16.studeni | 491 | 5%
17.studeni | 634 | 8%
18.studeni | 703 | 10%
19.studeni | 632 | 8%
20.studeni | 744 | 5%
21.studeni | 779 | 13%
22.studeni | 360 | 19%
23.studeni | 544 | 15%
24.studeni | 791 | 17%
25.studeni | 890 | 20%
26.studeni | 862 | 26%
27.studeni | 931 | 29%
28.studeni | 639 | 18%
29.studeni | 453 | 18%

### Zaključak

Epidemija je među najugroženijima `polako ubrzavala širenje kroz cijeli studeni`. Zadnjih desetak dana ponovno se uočavaju veće stope rasta broja slučajeva, a to bi nažalost moglo uzrokovati dodatan rast broja hospitaliziranih i preminulih osoba u idućim danima i tjednima.

## Županije - Tjedna promjena broja novih slučajeva

Ova karta daje brz i jednostavan uvid u epidemiološko stanje županija u proteklih tjedan dana u odnosu na tjedan ranije. Plava boja je indikator da epidemija usporava, bijela da stagnira, a crvena da epidemija ubrzava (kako je prikazano na skali uz kartu). Za ovu metriku vrijede ista pravila kao i za sve prethodne, kao što je opisano u uvodu teksta.

### Karta

![image](/29_11_2020/2911_promjena_karta.png)

### Tablica

Županija | Tjedna promjena
:---  | :---:
Istarska | 18%
Karlovačka | 110%
Zadarska | 43%
Primorsko-goranska | 29% 
Vukovarsko-srijemska | 4%
Šibensko-kninska | 38%
Osječko-baranjska | 1%
Splitsko-dalmatinska | 26%
Bjelovarsko-bilogorska | 40%
Brodsko-posavska | 38%
Dubrovačko-neretvanska | -4%
Zagrebačka | 4%
Grad Zagreb | -8%
Koprivničko-križevačka | 21% 
Krapinsko-zagorska | 22%
Ličko-senjska | 22%
Međimurska | 25%
Požeško-slavonska | -3%
Sisačko-moslavačka | 27%
Varaždinska | 34%
Virovitičko-podravska | 40%

### Zaključak

S karte je jasno vidljivo da epidemija `u većini županija ubrzava širenje`. `Iznimka su grad Zagreb, istok i jug zemlje`. Uz već objašnjeni Zagreb, za istok zemlje može biti slučaj da se dosta ljudi zarazilo tijekom ljeta pa su ti krajevi također ispred ostatka temlje po epidemiološkoj situaciji.

## Županije - Broj preminulih osoba na 100 000 stanovnika

Na sljedećoj karti se dobro vidi koje su županije jače, a koje slabije pogođene prema ukupnom broju preminulih na 100 000 ljudi. Svjetlija crvena boja je indikator manjeg, a tamnija indikator većeg broja preminulih na 100 000 stanovnika.

Način izračuna:

> (Ukupan broj preminulih)/(Broj stanovnika/100000)

### Karta

![image](/29_11_2020/2911_preminuli_karta.png)

### Tablica

Županija | Broj preminulih na 100 000 stanovnika
:---  | :---:
Istarska | 12
Karlovačka | 58
Zadarska | 19
Primorsko-goranska | 25 
Vukovarsko-srijemska | 25
Šibensko-kninska | 26
Osječko-baranjska | 79
Splitsko-dalmatinska | 34
Bjelovarsko-bilogorska | 33
Brodsko-posavska | 24
Dubrovačko-neretvanska | 31
Zagrebačka | 3
Grad Zagreb | 65
Koprivničko-križevačka | 45 
Krapinsko-zagorska | 71
Ličko-senjska | 59
Međimurska | 54
Požeško-slavonska | 22
Sisačko-moslavačka | 19
Varaždinska | 52
Virovitičko-podravska | 17

### Zaključak

S karte je jasno vidljivo koje su županije do sada teže bile pogođene, tj. gdje je veći udio umrlih. Nije jasno zašto neki prolaze lošije od drugih, ali se može otprilike reći da je kod pogođenijih najvjerojatnije i veći udio zaraženih te da su ispred ostalih po razvoju epidemije.

## Županije - Udio preminulih u ukupnom broju slučajeva (CFR)

Na sljedećoj karti prikazan je postotni udio ukupnog broja preminulih u ukupnom broju slučajeva za svaku županiju. Ova metrika daje dobar uvid o "lovljenju" ukupnog broja zaraza po županijama. Sve iznad 0.5% (pogotovo značajno) upućuje da je registrirani broj slučajeva znatno manji od stvarnog broja zaraženih.

> Izračun se vrši tako da se ukupan broj preminulih podijeli s ukupnim brojem registriranih slučajeva

### Karta

![image](/29_11_2020/2911_CFR_karta.png)

### Tablica

Županija | CFR
:---  | :---:
Istarska | 0.79%
Karlovačka | 2.37%
Zadarska | 0.92%
Primorsko-goranska | 0.99% 
Vukovarsko-srijemska | 1.02%
Šibensko-kninska | 1.15%
Osječko-baranjska | 2.86%
Splitsko-dalmatinska | 0.95%
Bjelovarsko-bilogorska | 1.72%
Brodsko-posavska | 0.88%
Dubrovačko-neretvanska | 1.20%
Zagrebačka | 0.11%
Grad Zagreb | 1.82%
Koprivničko-križevačka | 1.86% 
Krapinsko-zagorska | 1.81%
Ličko-senjska | 2.13%
Međimurska | 1.12%
Požeško-slavonska | 1.19%
Sisačko-moslavačka | 0.92%
Varaždinska | 1.11%
Virovitičko-podravska | 0.78%

### Zaključak

S karte je vidljivo da većina županija ima `prilično visok CFR`. Primjerice, u Osječko-baranjskoj županiji je to blizu 3% te se bez pretjerivanja može reći da je broj zaraženih tamo u stvari barem 5 puta veći nego što je registrirani broj slučajeva. Jedina županija koja odskače prema nižem od očekivanog je Zagrebačka, vjerojatno jer ozbiljno oboljeli idu u bolnicu u Zagreb te se onda i tamo vode kao preminuli ukoliko dođe do takve situacije.

## Preminule osobe u jesenskom valu epidemije

Na sljedećem grafu prikazan je ukupan broj preminulih osoba prema dobi u jesenskom valu epidemije, počevši od 1. rujna.

### Graf

![image](/29_11_2020/2911_preminuli_dob_jesen.png)

### Zaključak

Kao što je očekivano, najveći broj preminulih su osobe starije od 60 godina, a najveća koncentracija je između `77 i 87 godina`. Prosječna dob osoba preminulih u jesenskom valu epidemije je `77 godina`. Broj preminulih muškaraca (893) je znatno veći od broja preminulih žena (627). Muškarci u prosjeku umiru skoro četiri godine mlađi.

## Udio pozitivnih testova

Metrika koja može govoriti o razmjeru epidemije, ali se mora uzeti u obzir broj testiranja. Ukoliko se testira malo, očekivano je da je ta brojka veća, pogotovo ako je epidemija jače raširena među populacijom.

> Izračun se vrši tako da se broj zaraženih za svaki dan podijeli s brojem testiranih.

### Graf

![image](/29_11_2020/2911_udio_pozitivnih_testova.png)

### Tablica protekla dva tjedna

Datum | Broj testiranih | Udio pozitivnih
:---  | :---: | :---:
23.studeni | 6139 | 32%
24.studeni | 8944 | 26%
25.studeni | 10194 | 35%
26.studeni | 11487 | 35%
27.studeni | 11091 | 37%
28.studeni | 11282 | 35%
29.studeni | 8217 | 36%
30.studeni | 5027 | 36%
1.prosinac | 9668 | 30%
2.prosinac | 10077 | 35%
3.prosinac | 11166 | 41%
4.prosinac | 10626 | 37%
5.prosinac | 10662 | 38%
6.prosinac | 9340 | 31%

### Zaključak

Udio pozitivnih testova konstantno raste te je već duže vrijeme uz manje oscilacije `dosegnuo maksimum od otprilike 35%`. Postoje dva moguća objašnjenja: 1. Dobro se "lovi" većina slučajeva te se testiraju velikim dijelom samo zaraženi, 2. Raširenost epidemije među populacijom znatno premašuje kapacitete testiranja. Iako je na početku puno točnija bila druga pretpostavka, dolaskom sve hladnijeg vremena (time i rasta udjela ozbiljnije bolesnih) i povećanjem kapaciteta testiranja moguće je da i prva teza zadnje vrijeme donekle drži vodu.

## Dobno-spolna piramida potvrđenih slučajeva u jesenskom valu epidemije

Animirani prikaz broja slučajeva prema spolu u različitim dobnim skupinama kroz jesenski val epidemije. Daje dobar uvid u zaraženost pojedinih skupina kroz vrijeme.

### Graf

![image](/29_11_2020/2911_dob_spol_piramida.gif)

### Tablica od početka epidemije

Raspon godina | Muškarci | Žene
:---  | :---: | :---:
0-4 | 569 | 492
5-9 | 880 | 788
10-14 | 2055 | 1954
15-19 | 3677 | 3605
20-24 | 4631 | 4636
25-29 | 5255 | 5384
30-34 | 5581 | 5566
35-39 | 5447 | 6204
40-44 | 5744 | 6414
45-49 | 5421 | 6024
50-54 | 5098 | 5771
55-59 | 4804 | 5308
60-64 | 4374 | 3986
65-69 | 3065 | 2592
70-74 | 2264 | 2194
75-79 | 1430 | 1784
80-84 | 1114 | 1649
85-89 | 605 | 1153
90+ | 202 | 682

### Zaključak

Zanimljiva je činjenica da je do sada potvrđeno primjetno `više slučajeva kod žena` (razlika otprilike 4000). Iako je više potvrđenih slučajeva kod žena u ugroženim skupinama, preminulih muškaraca je znatno više. Za ovo su moguća dva objašnjenja, prvo da virus uzrokuje znatno veću smrtnost kod muškaraca, a drugo, vjerojatnije, da se žene u slučaju oboljenja češće odlučuju na testiranje.

## Izvori:

[Koronavirus.hr - twitter](https://twitter.com/koronavirus_hr)

[Koronavirus.hr - strojno čitljivi podaci](https://www.koronavirus.hr/otvoreni-strojno-citljivi-podaci/526)

[Velebit AI - Covid-19](https://covid19hr.velebit.ai/d/zL99n2rZz/covid-19-hrvatska?orgId=3)

[Our world in data - COVID-19](https://ourworldindata.org/coronavirus)

[Worldometer - Coronavirus](https://www.worldometers.info/coronavirus)

-----

Podaci će se osvježavati jednom tjedno, najvjerojatnije nedjeljom u poslijepodnevnim satima

Podaci o broju zaraženih po dobi i spolu mogu se razlikovati od ostalih podataka jer su za njih izvor strojno čitljivi podaci koji nemaju isti interval osvježavanja kao ostali podaci (npr. službeni Twitter račun)
