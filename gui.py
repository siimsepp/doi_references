import tkinter as tk

# Impordime projekti osaks oleva faili, mis tegeleb doi-viidete leidmisega
import doi_viited

"""
Programm aitab teadusartikli koostamisel aega kokku hoida. Paljud teadusajakirjad
nõuavad autoritelt doi-viidete lisamist viidetele. Käsitööna on see aeganõudev ja
väga tüütu töö. See programm küsib kasutajalt viiteid ja otsib neile ise doi,
kasutades selleks internetipäringut.
"""


def getvalue():
    """
    Funktsiooni ülesandeks on krabada kasutaja sisestatud viited ja sööta
    nad teisest failist imporditud funktsioonile kirjutame_failid_doiga, mis
    vastutab, et viited saaksid koos doi'ga failidesse kirjutatud. Doi leidmiseks
    kasutab ta funktsiooni doi_tegija.
    """
    viited = viited_sisse.get()
    doi_viited.kirjutame_failid_doiga(viited)


raam = tk.Tk()
raam.title("doi lisamine teadusartiklite viidetele")
raam.geometry("600x730")

viited_sisse = tk.StringVar(raam)

tekst1 = tk.Text(raam, height=1, borderwidth=0, fg='red', font="menlo 17")
tekst1.insert(1.0, "Sisesta tekstikasti viited.\nViidete eraldajaks 'enter':")
tekst1.configure(state="disabled")
tekst1.place(x=50, y=50, width=500, height=50)

sisestus = tk.Entry(raam, textvariable=viited_sisse)
sisestus.place(x=50, y=100, width=500, height=40)

nupp = tk.Button(raam, text='Käivita programm', command=getvalue)
nupp.place(x=50, y=150, width=180, height=40)

tekst2 = tk.Text(raam, height=1, borderwidth=0, fg='green', font="menlo 15")
tekst2.insert(1.0, "Näide, mille saab tekstikasti kopeerida,\net kontrollida programmi tööd:")
tekst2.configure(state="disabled")
tekst2.place(x=50, y=200, width=500, height=40)

tekst3 = tk.Text(raam, height=1, borderwidth=0, font="menlo 12")
tekst3.insert(1.0, """
Marechal, L., Semple, S., Majolo, B. & Maclarnon, A. (2016). Assessing the effects of tourist provisioning on the health of wild barbary macaques in Morocco. PLoS ONE 11, e0155920.\n
Meillere, A., Brischoux, F., Ribout, C. & Angelier, F. (2015). Traffic noise exposure affects telomere length in nestling house sparrows. Biology Letters 11, 20150559.\n
Vineis, P. & Husgafvel-Pursiainen, K. (2005). Air pollution and cancer: biomarker studies in human populations. Carcinogenesis 26(11), 1846-55.
""")
tekst3.configure(state="normal")
tekst3.place(x=50, y=240, width=500, height=200)

tekst4 = tk.Text(raam, height=1, borderwidth=0, fg='blue', font="menlo 15")
tekst4.insert(1.0, """
Programm kirjutab programmifailiga samasse kausta\ntxt- ja docx-laiendiga failid, mis sisaldavad\ntekstikasti kopeeritud viiteid koos doi'ga.\n
Viidete varustamine doi'ga võtab aega, sest iga viite jaoks tuleb teha päring internetis.\n
Aega kulub umbes 7 sekundit viite kohta.\nSeega 100 viitega artiklile doi-viidete leidmine\nvõtab programmil üle 10 minuti.
""")
tekst4.configure(state="disabled")
tekst4.place(x=50, y=440, width=500, height=240)

raam.mainloop()
