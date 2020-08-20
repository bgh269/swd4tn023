## Tietorakenteet ja algoritmit

* Mihin tarvitaan tietorakenteita ja algoritmeja?
	* koronasovellus?
	* reittiopas?
	* hakukone?
	* ...
	* Dijkstran algoritmin esittely korkealla tasolla?

* "yleisimmät" tietorakenteet ja niiden käyttötarkoituksia
	* uutena Set ja sen toimintaperiaate
	* konseptin tasolla puut ja verkot
* "yleisimmät" algoritmit ja niiden käyttötarkoituksia
	* hakualgoritmit
	* järjestämisalgoritmit

### Etukäteismateriaali

Katso video: **What Is an Algorithm?**

Opit käsitteet:

* Selection sort (valintajärjestäminen)
* Insertion sort (lisäysjärjestäminen)
* Käsitteet
	* Sorting
	* Searching
	* Shortest path cost

https://youtu.be/PY82qqyWJJs**

---

HYVÄ! Katso video: **What is an algorithm and why should you care?** 

https://youtu.be/CvSOaYi89B4

---

Hyvä! Katso video: **Practical Big-O Notation**

https://youtu.be/e6UZ2kzmmdA

> Big-O notation is how the efficiency of algorithms is typically described. Figuring out the O-notation of an algorithm can look tricky, but as this video shows, for the majority of situations, it's pretty straightforward.

---

Syventävä! Katso video: **Introduction to Big O Notation and Time Complexity**

https://youtu.be/D6xkbGLQesk

### Teoriaosuus ja demo

Lähtötila: käytetään listaa suomen- ja englanninkielisistä sanoista ja tehdään niille erilaisia operaatioita. Eri versioiden yhteydessä otetaan "leikkimielisesti" aikaa ohjelman suorituksesta.

Lineaarisen haun ja binäärihaun visualisointi: https://www.cs.usfca.edu/~galles/visualization/Search.html

#### Sanastot

Tällä kurssilla esitetty esimerkki suomen- ja englanninkielisten sanojen käsittelystä on Antti Laaksosen luennon innoittama. https://www.cs.helsinki.fi/u/ahslaaks/tira19/luento1/

* src/englangi.txt

--- 

* src/suomi.txt

Copyright (C) Kotimaisten kielten tutkimuskeskus 2006
Kotimaisten kielten tutkimuskeskuksen nykysuomen sanalista, versio 1
Julkaistu 15.12.2006

Sanalista julkaistaan GNU LGPL -lisenssillä.
Lisenssiteksti luettavissa osoitteessa http://www.gnu.org/licenses/lgpl.html


#### 1. Mitkä samat sanat esiintyvät sekä suomen- että englanninkielessä?

Kehitetään algoritmi, jolla käydään läpi kaikki suomenkieliset sanat, ja kutakin sanaa kohden etsitään englanninkielisistä sanoista vastinetta. Lopuksi tulostetaan löydetyt yhteiset sanat.

#### 2. Tehokkuuden pohdinta

Pohditaan sitä, kuinka monta operaatiota edellä mainittu algoritmi pahimmillaan vaatii valmistuakseen. Tutustutaan O-notaatioon ja johdetaan algoritmista aikavaatimukseksi O(n*n)

#### 3. Miten algoritmia voidaan muuttaa, jotta haku veisi vähemmän aikaa

Tutustutaan netin lähteistä erilaisiin hakualgoritmeihin. 

Pythonin `x in list` aikavaatimus on O(n): https://wiki.python.org/moin/TimeComplexity

Niiden yhteydessä katsotaan puolitushaun aikavaatimus ja kokeillaan muuttaa alkuperäinen algoritmi hyödyntämään puolitushakua sanojen etsimiseksi englanninkielisestä listasta &rarr; ohjelman suoritus toivottavasti nopeutuu havaittavasti. O(n*log(n))

#### 4. Miten käytetty tietorakenne vaikuttaa ohjelman nopeuteen?

Viimeisenä pohditaan, mitä eri tietorakenteita listojen lisäksi meillä olisi sanojen tallentamiseen. *Opiskelijoiden tulisi tuntea hajautustaulu, jonka avulla haku on nopea.* Kokeillaan toteutusta Pythonin sanakirjan avulla ja katsotaan mikä nopeus on verrattuna alkuperäiseen. Perehdytään jostain hyvästä lähteestä sanakirjan (map) toteutukseen, joka havaitaan hyväksi.

#### 5. Vaihtoehtoinen kolmas tietorakenne ja ongelman muotoilu toisella tavalla

Määritellään ongelma uudelleen joukko-opin näkökulmasta: molemmille kielille yhteiset sanat ovat osajoukko. Käyttämällä Pythonin joukkoja haluttu osajoukko saadaan selville ilman yhtään toisto- tai hakuoperaatiota. Vertaillaan jälleen tuloksia suorituskyvyn ja kompleksisuuden näkökulmasta.

Tutustutaan set-tietorakenteen aikavaatimukseen: `x in set` aikavaatimus on O(1). https://wiki.python.org/moin/TimeComplexity

### Ennakkotehtävä 

https://wiki.python.org/moin/TimeComplexity

Videoiden katsominen

monivalintakysymykset:

1. Iso-O -notaatio kuvaa algoritmin suoritusajan pahinta tapausta suhteessa käsiteltävien alkioiden määrään (n). Perustuen etukäteisaineistoon, aseta seuraavat algoritmin tehokkuutta kuvaavat suureet suuruusjärjestykseen tehokkaimmasta vähiten vähiten tehokkaaseen, eli pienimmästä suoritusajasta suurimpaan:

O(1)
O(n)
O(log(n))
O(n*log(n))
O(n*n)

### Tehtävä 2

* kahden vapaasti valittavan järjestelyalgoritmin toteuttaminen ja niiden vertaileminen kompleksisuuden ja tehokkuuden kannalta
* Sortataan esimerkiksi samankaltaista sanalistaa, jota käsiteltiin johdannossa
* ristinolla-pelin tietorakenteen ja voittajan ratkaisevan algoritmin toteuttaminen
	* moniulotteinen tietorakenne
	* moniulotteisen tietorakenteen läpikäynti
	* annetaan`ko esim. käyttöliittymä valmiina?



### Seminaariharjoitus

Sanaruudukkotehtävä, jossa sanat tulee etsiä ristiin, ylös, alas jne. Syötteenä voidaan antaa sanaruudukko tekstitiedostona.

Tai

Reittejä etsivän algoritmin toteuttaminen hyödyntäen avointa dataa euroopan pääkaupungeista sekä niiden välisistä etäisyyksistä. Syvyyshaku ja rinnakkaishaku.


### Materiaaleja

https://tira-s19.mooc.fi/materiaali

https://www.helsinki.fi/en/unitube/video/d1733eed-b574-46e0-b291-cc25beca4b33



---

> "More importantly one should know when and where to use them. Some examples where you can find direct application of sorting techniques include:
> 
> Sorting by price, popularity etc in e-commerce websites"
>
> https://u.osu.edu/cstutorials/2016/11/21/7-algorithms-and-data-structures-every-programmer-must-know/

https://u.osu.edu/cstutorials/2016/11/21/7-algorithms-and-data-structures-every-programmer-must-know/

https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42

Mikä on hyvä tietorakenne tai algoritmi?

* iso O -notaatio (suorituskyky)
* tilavaatimus


https://github.com/pllk/tirakirja/raw/master/tirakirja.pdf