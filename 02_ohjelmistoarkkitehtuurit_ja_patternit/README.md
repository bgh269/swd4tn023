## Testaus

* dayOfYear-koodin testaaminen: annettuun koodiin on jätetty kaksi vaikeasti havaittavaa bugia
* Esimerkkikoodi olemassa Javalla, se tulee kääntää Pythonille
* Pythonin standardikirjaston unittest vai PyTest?
	* https://docs.python.org/3/library/unittest.html

### Teoriaosuus

* Testauksen käsitteet korkealla abstraktiotasolla
	* tavoitteet
	* tasot (yksikkö-, integraatio-, järjestelmä- ja hyväksymistestaus)
	* strategiat: eksploratiivinen vs. testisuunnitelmaan perustuva
	* Given, when, then...
	* manuaalinen ja automatisoitu testaus
	* BDD-ajattelu: cucumber ja robot framework
	* Käyttäjätarinat ja hyväksymiskriteerit
	* refaktorointi (esim. valtava Python-funktio)

* Automatisoidun testauksen käsitteet
	* test fixture
	* mock, stub, fake object, spy
	* test case
	* test suite
	* test runner
	* assertoinnit
	* "annotaatiot"
	* "assert ja bdd -syntaksit"

### Tehtävä

Koodataan Pythonilla yksikkötestit annetulle Python-funktiolle. Testit ajetaan lokaalisti tai Dockerin avustuksella. Opettaja esittelee molemmat tavat johdannossa. Kirjoitettujen testien tulee paljastaa annetussa ohjelmassa olevat bugit, jotka korjataan annettuun koodiin.

**Tätä testiä voidaan hyödyntää automaatiovaiheessa siten, että Travis ajaa testit automaattisesti?**


### Vaihe 2: "integraatiotesti"

Vaikeammin testattava koodi, jossa joudutaan mockaamaan jokin riippuvuus. Otetaan paha funktio, joka esim. lukee ja kirjoittaa levyltä ja on "mahdoton testata". Refaktoroidaan tätä jotta saadaan testattua.

Ehdotus: klassisesti vaikeasti testattavaa on päivämääräriippuvainen koodi!

1. Kirjoitetaan testit koodille, joka tulostaa eri kellonaikoina eri tulosteet. Pythonin Mock-oliot.
1. Kirjoitetaan testi, jossa kutsutaan jotain web-osoitetta.


### Seminaariharjoitus:

- Robot framework -testit esim. omalle ohjelmistoprojekti II -kurssin projektille
- Robot framework -aiheinen seminaariesitys
