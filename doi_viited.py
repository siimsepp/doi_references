import re
import requests
import urllib.request
import urllib.parse
from docx import Document

# Teen uue dokumendiobjekti, mis on vajalik Wordi faili kirjutamiseks
document = Document()


def kirjutame_viite_wordi_faili(doiga_viide):
    document.add_paragraph(doiga_viide)
    document.save('Viited_koos_doiga.docx')


def kirjutame_viite_txt_faili(doiga_viide):
    with open('viited_doi.txt', 'a', encoding='utf-8') as f:
        f.write(doiga_viide + '\n')


def doi_tegija(otsing):
    """Funktsioon võtab argumendina sisse viite tekstina, viib selle kujule,
       mida saab URL-ina kasutada, teeb päringu veebilehel crossref.org, see-
       juures varjates oma identiteeti (Pythoni asemel esineb brauserina). Loeb
       sisse otsingu vastusena saadud veebilehe lähtekoodi, otsib sealt
       regulaaravaldise abil esimese doi-viite ning puhastab selle soovitud
       kujule. Lõpuks tagastab esialgse viite koos selle järel oleva doi'ga.
    """
    global otsing_doi
    # viime viite kujule, mida saab kasutada otsinguna (kaotame tühikud jne)
    url_encode = urllib.parse.quote_plus(otsing)
    # url moodustub veebilehest, selle järel olev ?q= näitab, et teeme
    # päringu ning seejärel tuleb vajalikul kujul viide
    url = 'https://search.crossref.org/?q={}'.format(url_encode)
    # kuna paljud veebilehed on külalislahked vaid inimeste vastu, siis
    # esinemegi brauserit kasutava inimesena
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    # esitame päringu veebilehele
    paring = urllib.request.Request(url, headers=headers)
    vastus = urllib.request.urlopen(paring)
    # loeme sisse vastuse ja teisendame tekstiks
    vastus_andmed = str(vastus.read())
    # regex vastavalt veebilehe vormistusele, et saada kätte kõige esimene doi-viide
    leia_doi = re.search("(doi%2Fhttp%3A%2F%2Fdx\.doi\.org.+?)\&amp;", vastus_andmed).group()
    # teeme url'i tagasi tekstiks
    url_decode = urllib.parse.unquote_plus(leia_doi)
    # eemaldame ebavajalikud osad
    puhas = url_decode.replace('doi/http://dx.', '')
    puhas = puhas.replace('&amp;', '')
    # vormistame vastuse kujul: esialgne viide + doi
    otsing_doi = '{} {}'.format(otsing, puhas)
    return otsing_doi


def kirjutame_failid_doiga(viited):
    # kirjutame üle faili, sest hiljem me lisame failile viide haaval, mitte ei
    # kirjuta üle, aga kõigepealt tahame puhast faili. Seega tühjendame faili, mis
    # ilmselt sisaldab eelmise kasutuskorra viiteid.
    with open('viited_doi.txt', 'w', encoding='utf-8') as fw:
        fw.write('')
    # teeme viidetest listi (eraldajaks peab olema newline)
    viited = viited.split('\n')
    # Eemaldan tühja stringi listi lõpust. Kui seda mitte teha, siis kirjutatakse
    # viimane viide faili kahekordselt
    viited = [viide for viide in viited if viide != '']
    # käivitame doi-tegemise funktsiooni iga viite jaoks ja söödame talle sisse viite
    for viide in viited:
        doiga_viide = doi_tegija(viide)
        # kirjutame viited viide haaval koos doi'ga uude puhastatud txt- ja docx-faili
        kirjutame_viite_txt_faili(doiga_viide)
        kirjutame_viite_wordi_faili(doiga_viide)
