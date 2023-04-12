from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/solarsystem')
def solarystem():

    return jsonify(
        {'id': 0,
         'name':'Mercury',
         'image': 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTFFRKg1XEC7kNu58XVZi9vPh6F9ii0FhevCdEAUKyMEtSdx4HLLLNBMacXXX0Y0gLv',
         'description': 'A Merkúr a Naprendszer legbelső és legkisebb bolygója,[8] a Nap körüli keringési ideje 88 nap. A Merkúr a Földről nézve fényesnek látszik, magnitúdója −2,0 és 5,5 között változik, azonban nehéz észlelni, mert a Földről nézve a Naptól mérhető legnagyobb szögtávolsága csak 28,3°. Reggel vagy este szürkületkor lehet megfigyelni.A Merkúrt meglátogató két űreszköz közül az első a Mariner–10 volt, mely 1974–75-ben a bolygó felszínének csupán 45%-át térképezte fel. A második a MESSENGER, amely további 30%-ot mutatott meg a bolygó felszínéből, amikor 2008. január 14-én elrepült mellette. Ez az űreszköz 2008. október 6-án és 2009. szeptember 29-én még kétszer elhaladt a bolygó mellett, 2011. március 19-én bolygó körüli pályára állt, mintegy 200 kilométerre a felszíntől – adatokat gyűjt, azokat a Földre továbbítja, miután a maximális magasságba került, 15 000 kilométerre a felszíntől. Ekkortól tovább tanulmányozza és feltérképezi az egész égitestet.A Merkúr sok tekintetben hasonlít a Holdra: felszínét számos kráter borítja, nincs természetes holdja, és nincs állandó légköre. Azonban a Holddal ellentétben nagy, vasat tartalmazó magja van, aminek következtében rendelkezik mágneses mezővel, melynek erőssége a földinek körülbelül 1%-a.[9] Magjának relatív mérete miatt kivételesen nagy a bolygó sűrűsége. Felszíni hőmérséklete 90 és 700 K (-183  és 427 °C) között változik,[10] Ahol a Nap éppen merőlegesen éri a felszínt, ott van a legmelegebb, és a sarkokhoz közeli kráterek mélyén mérik a leghidegebbet.A Merkúr megfigyeléséről szóló feljegyzések legalább az időszámításunk előtti első ezredfordulóig nyúlnak vissza. A babiloniak a Nabu nevet adták neki, hírvivő istenük neve után. Az i.e 4. század előtt a görög csillagászok két bolygónak gondolták aszerint, hogy napkeltekor vagy napnyugtakor volt látható. Előbbi az Apollón, utóbbi a Hermész nevet kapta.[11] Az i.e 4. században felismerték, hogy a két bolygó egy és ugyanaz, onnantól kezdve Hermésznek nevezték.[12] A bolygó magyar neve a rómaiakig nyúlik vissza, akik a bolygót Mercurius római istenről nevezték el, aki a görög Hermész római megfelelője. A Merkúr asztronómiai jele a kör egy kereszt függőleges szárán, a kör tetején egy félkörrel, ami Hermész caduceusának stilizált változata.'
         },

        {'id': 1,
         'name': 'Venus',
         'image': 'https://www.nasa.gov/sites/default/files/thumbnails/image/venus_0.jpg',
         'description': 'A Vénusz a második bolygó a Naptól, keringési ideje 224,7 földi nap. Nevét Venusról, a szépség római istennőjéről kapta. A Hold után a legfényesebb objektum az éjszakai égbolton, legnagyobb látszólagos fényessége -4,6 magnitúdó. Maximális fényességénél még nappal is észrevehető. Mivel a Vénusz kering a Nap körül és közelebb van hozzá, mint a Föld, ezért néhány hónapig a Naptól keletre, később néhány hónapig a Naptól nyugatra látható, változó távolságra. A keringés mindkét szélső pontjának látszólagos távolsága a Naptól, azaz a bolygó legnagyobb kitérése 47,8°, vagyis a Napot legfeljebb három órával követi, illetve előzi meg az égen.'
         },

        {'id': 2,
         'name': 'Earth',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/The_Blue_Marble_%28remastered%29.jpg/800px-The_Blue_Marble_%28remastered%29.jpg',
         'description': 'A Föld (görögül: Γαῖα – Gaia, latinul: Terra vagy Tellus) a Naptól számított harmadik bolygó a Naprendszerben, ahol a legnagyobb átmérőjű, tömegű és sűrűségű Föld-típusú bolygó.Több millió faj, köztük az ember élőhelye is. A Föld a világegyetem egyetlen olyan bolygója, amelyről tudjuk, hogy életet hordoz. Jelenlegi ismereteink szerint 4,44[12]–4,54 milliárd éve alakult ki,[13][14][15][16] és a felszínén mintegy egy milliárd év múlva az élet is megjelent. Azóta a bioszféra jelentősen megváltoztatta az atmoszférát, és más, biotikus összetevőit. Ezzel lehetőség nyílt az aerob organizmusok osztódásos szaporodására, és létrejött az ózonréteg, amely megszűri a Nap felől érkező ultraibolya sugárzást. A Föld felszínét a Föld mágneses mezője védi a nagyenergiájú kozmikus sugárzástól. A Naprendszer külső körülményei a várakozások szerint még mintegy 1,5 milliárd évig támogatják az élet jelenlétét, de ezután a mind fényesebbé váló Nap el fogja tüntetni a bioszférát.'
         },

        {'id': 3,
         'name': 'Mars',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/7/76/Mars_Hubble.jpg',
         'description': 'A Mars a Naptól számított negyedik bolygó a Naprendszerben. Szabad szemmel is könnyedén látható az éjszakai égbolton. A római hadistenről nevezték el, de gyakran hívják „vörös bolygónak” is színe miatt, amit a Mars felszínét meghatározó vas-oxid okoz. A Mars a harmadik legnagyobb kőzetbolygó, számos rendkívüli felszíni képződménnyel.Két természetes holdja van, a Phobos és a Deimos, mindkettő kicsi és szabálytalan alakú, valószínűleg befogott kisbolygók. Továbbá a 2000-es évek elejétől három mesterséges hold kíséri útján: Mars Odyssey, Mars Express és a Mars Reconnaissance Orbiter.'
         },

        {'id': 4,
         'name': 'Jupiter',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Jupiter.jpg/800px-Jupiter.jpg',
         'description': 'A Jupiter az ötödik bolygó a Naptól, és messze a legnagyobb bolygó a Naprendszerben. Óriásbolygó, tömege két és félszerese az összes többi bolygó együttes tömegének. A többi óriásbolygóval (Szaturnusz, Uránusz, Neptunusz) együtt gyakran Jupiter-típusú, vagy külső bolygóknak nevezik.A Földről nézve maximális fényessége -2,94 magnitúdó, ezzel átlagosan a harmadik legfényesebb égitest az éjszakai égbolton, a Hold és a Vénusz után (rövid időre a Mars vetekedhet fényességével pályájának bizonyos pontjain).A Jupiter főként hidrogénből áll, tömegének egynegyedét hélium teszi ki, sziklás magja nehezebb elemeket tartalmazhat. Gyors forgása miatt alakja forgási ellipszoid (lapított gömb). A külső atmoszférája láthatóan számos sávra oszlik a különböző szélességi körökön, turbulenciát és viharokat okozva ezek határain. Kiemelkedő látványosság a Nagy Vörös Folt, egy óriási vihar, amit már a 17. században is megfigyeltek.'
         },

        {'id': 5,
         'name': 'Saturn',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/1920px-Saturn_during_Equinox.jpg',
         'description': 'A Szaturnusz a hatodik bolygó a Naptól számítva, a második legnagyobb a Naprendszerben a Jupiter után. Egyike annak az öt bolygónak, ami a Földről szabad szemmel is látható. A Szaturnusznak látványos, jégből és törmelékekből álló gyűrűrendszere van. Szaturnuszról, a római istenről nevezték el. Jele az isten sarlójának stilizált képe (Unicode: ♄).A Szaturnusz belső magja valószínűleg vas-nikkel összetételű, a magot fémes hidrogén veszi körül, ezután egy közbülső réteg következik, amit folyékony hidrogén és folyékony hélium alkot, és végül a bolygó külső takarója gázokból áll. A Szaturnusz légkörének halvány-sárgás színezete van, ezt a benne található ammóniakristályok okozzák.'
         },

        {'id': 6,
         'name': 'Uranus',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg',
         'description': 'Az Uránusz a Naprendszer hetedik bolygója. Óriásbolygó, a harmadik legnagyobb átmérőjű és a negyedik legnagyobb tömegű.Az Uránusz felfedezését 1781. március 13-ától számítjuk, mert ekkor pillantotta meg először Sir William Herschel. Azóta tudjuk, hogy a bolygót előzőleg 1690 és 1771 között legalább hússzor regisztrálták, de mindannyiszor csillagnak vélték. Az elmozdulását pedig mérési hibának. Herschel eleinte nem volt tisztában vele, hogy a Naprendszer egy eddig ismeretlen bolygóját fedezte fel, először üstökösként azonosította az égitestet.'
         },

        {'id': 7,
         'name': 'Neptune',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/6/63/Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg',
         'description': 'A Neptunusz a Naptól számítva a nyolcadik, legkülső bolygó a Naprendszerben. Csillagrendszerünk négy óriásbolygója közül a méretét tekintve az utolsó, a tömegét nézve viszont az Uránuszt megelőzve a harmadik legnagyobb. Színe miatt Neptunusról, a tengerek római istenéről nevezték el. Jele az isten háromágú szigonyát jelképezi (Unicode: ♆). 14 ismert holdja van, ezek közül a két ismertebb a Nereida és a Triton.'
         },

        {'id': 8,
         'name': 'Pluto',
         'image': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Pluto_by_LORRI_and_Ralph%2C_13_July_2015.jpg',
         'description': 'A Pluto törpebolygó, 2006. augusztus 24-éig a Naprendszer kilencedik, legkisebb bolygójaként tartották számon, ma pedig (az Eris után) a második legnagyobb törpebolygónak számít. Azóta a Neptunusz a Naprendszer legtávolabbi bolygója. A Föld holdjánál kisebb, magas hőmérsékleten összetömörült anyagokból álló, nitrogén–metán–szén-monoxid légkörű törpebolygó.Bolygó besorolását azért vesztette el, mert a Kuiper-övben egy olyan égitestet fedeztek fel, amely közel ugyanakkora. Ez az Eris törpebolygó, melynek felfedezése után a Nemzetközi Csillagászati Unió új bolygó-meghatározást alkotott, amely az Erist – és így a Plutót is – a bolygóktól külön kategóriába helyezi.'
         },

    )

if __name__ == '__main__':
    app.run(debug=True)