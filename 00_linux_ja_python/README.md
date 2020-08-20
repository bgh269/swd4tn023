# Ohjelmistokehityksen teknologioita


Aloitustunnille ehkä pieni motivointipuhe Gitistä ja Dockerista. Docker on hyödynnettävissä myöhemmillä viikoilla tehtävien yhtenäistämiseksi kaikille: versiot, riippuvuudet, komennot yms. saadaan yhtenäisiksi kaikille. Huonolla tuurilla opiskelijoilta voi kulua koko viikko yrittäessään tunkata toimivaa Python- tai Node-kehitysympäristöä omalle koneelleen. Vaihtoehtoisesti voimme suositella jo heti alussa asentamaan itselleen VirtualBoxin ja Ubuntun, johon voimme tarjota "standardoidut" ohjeet riippuvuuksien asentamiseksi versioineen.

Käytetäänkö kehitystyökaluna VS Codea?

**Case**

Saman Python-koodin suorittaminen kahdella eri koneella tuottaa eri vastauksen, joka johtuu siitä, että koneille on asennettu eri versiot Pythonista. Dockerin avulla suoritettaessa eri koneilla saadaan samat tulokset, koska kontin sisällä Pythonin versio on yhteinen.

Gitin käytöstä tunnilla tehtävät esimerkit koodataan omaan kehityshaaraansa, josta tehdään committeja esimerkin aikana. Lopuksi kehityshaara yhdistetään masteriin. &rarr; Saadan Gittiä tuotua esiin konkreettisen esimerkin kautta.


## Esitietovaatimukset tietorakenteisiin ja algoritmeihin

* Toimiva kehitysympäristö (asennettuna Python ja editori, mielellään Docker tai VirtualBox)
* Alustava käsitys Pythonista (https://www.w3schools.com/python/)

Aloitustunnilla voitaisiin antaa jokin lämmittelytehtävä, jotta ainakin ehto- ja toistorakenteet sekä listat olisivat opiskelijoille tuttuja ennen ensimmäistä _varsinaista_ aihetta.


<!-- 

# CSC Pilvipalvelut

https://www.csc.fi/web/education/pilvipalvelut

# CSC Pouta

https://docs.csc.fi/cloud/pouta/

# CSC Rahti

https://docs.csc.fi/cloud/rahti/rahti-what-is/ -->


# VirtualBoxin asennus

## Terminaalin avaaminen

Näppäinyhdistelmä `CTRL + ALT + T`.

## Gitin asennus

```shell

$ sudo apt install git
$ git clone  https://github.com/haagahelia/swd4tn023.git

```

## Pythonin "asennus"

```shell
$ sudo apt install python3-pip
```

## Visual Studio Coden asennus

Ubuntu Software &rarr; Visual Studio Code &rarr; install

Extensions: 

1. Python // koodieditori
1. Pylint // koodin tarkistus
1. Rope // refaktorointi
1. autopep8 // koodin muotoilu

User settings &rarr; **Format on save** ja **Format on paste**.