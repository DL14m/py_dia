from stanze import Stanza 

class Partita: 
    
    def __init__(self): 
        self.stanzaVincente = None
        self.stanzaCorrente = None
        self.lp = 10 

        self.creaStanza()

    def creaStanza(self): 
        parcheggio = Stanza('Parking Area') 
        area_relax = Stanza('Relax Area') 
        segreteria = Stanza('School Office') 
        aula_gialla = Stanza('Yellow Classroom') 
        aula_azzurra = Stanza('Cyan Classroom') 
        presidenza = Stanza('Presidency') 
        corridoio = Stanza('Aisle')
        atrio = Stanza('Lobby')

        parcheggio.impostaStanzaNord(corridoio)
        parcheggio.impostaStanzaOvest(presidenza)
        parcheggio.impostaStanzaSud(atrio)

        corridoio.impostaStanzaNord(atrio)
        corridoio.impostaStanzaEst(parcheggio)
        corridoio.impostaStanzaOvest(aula_gialla)
        corridoio.impostaStanzaSud(presidenza)

        presidenza.impostaStanzaEst(parcheggio)
        presidenza.impostaStanzaSud(segreteria)

        segreteria.impostaStanzaNord(presidenza)
        segreteria.impostaStanzaEst(atrio)

        atrio.impostaStanzaNord(parcheggio)
        atrio.impostaStanzaEst(corridoio)
        atrio.impostaStanzaOvest(segreteria)

        aula_gialla.impostaStanzaOvest(corridoio)
        aula_gialla.impostaStanzaSud(aula_azzurra)

        aula_azzurra.impostaStanzaOvest(aula_gialla)
        aula_azzurra.impostaStanzaOvest(area_relax)
        
        area_relax.impostaStanzaOvest(aula_azzurra)

        self.stanzaCorrente = parcheggio
        area_relax.stanza_vincente = True

        print('Mappa Inizializzata')