## "Moderni JavaScript"

Case: Erittäin yksinkertaistettu valmis full-stack JavaScript-sovellus, jossa frontissa natiivi JS:ää ja backendissä Node natiivilla http-moduulilla (ilman Express:iä tai muita työkaluja). Tutkitaan konkreettisesti, miten koodin suoritus etenee frontista Nodelle ja takaisin. Käytetään Chromen DevToolsia ja debuggeria ja "kokeillaan kaikki komennot" myös Chromen konsolissa &rarr; nähdään promise-oliot, niiden tilat, suoritusjärjestys yms.

**ES6:n ilmaisuvoimaisimmat syntaksit**: Miten JavaScriptiä luetaan?!

Updated: haetaan runkoa osoitteesta http://es6-features.org/

Nuolifunktioiden "kertaus", case: map ja reduce.

JSLint-koodityylit

Testaaminen

- asynkronisuuden käsite ja vertailu esim. Javan rinnakkaiseen suoritusmalliin
- Promise-olioiden periaatteet
- promise-olioden käytön harjoittelu selaimessa fetch-funktion avulla
- vilkaisu eri ratkaisumallien eroihin:
	- Fetch, jQuery, XMLHttpRequest...
- selainohjelmointi ja Chromen DevTools

#### Mahdollinen case: ShoppingListExample?

- JS-pohjainen ShoppingListExample? 
- Projektin kirjoittaminen JavaScriptillä?
- toimivaa materiaalia? https://github.com/haagahelia/ShoppingListExample#esimerkkiprojektin-javascript-osuus


#### Toinen mahdollinen case: chat tai muu reaaliaikainen sovellus websocketeilla?

Jos halutaan tehdä jotain ihan muuta kuin tähän asti, voidaan käyttää myös muita kuin HTTP-protokollaa...

#### Node
- require vs. import -syntaksi
- spread & rest -syntaksi
- async/await + koodin kääntäminen Babel-työkalun avulla
	- vrt. JSX-koodin kääntäminen
	- myös riippuvuuksien hallinta

### Seminaariharjoitus

- tunnilla ja tehtävissä käsitellyn koodin jatkokehittäminen siten, että data tallennetaan MongoDB:llä pysyvään muistiin?
- oman node-moduulin julkaiseminen NPM:ssä?
- ohjelmistoprojekti II -kurssin projektin rakentaminen npm-moduuleina (julkaisu GitHubissa riittää?)





---

Node ja NPM

* Miksi buildataan? Mitä vaiheita?
* Riippuvuuksien hallinta: hyödyt ja haitat?
    * vaihtoehtoinen tapa: selainten perinteinen malli
* Tietoturva


Tehtävä kaikille:



Seminaarioptio: 

* oman NPM-paketin julkaiseminen


https://www.w3schools.com/nodejs/default.asp

https://nodejs.org/en/knowledge/getting-started/npm/what-is-npm/

