from formating import f2

def utregning_kjøp ():
    oversikt = []

    #Inputs
    print('Vennligst skriv inn ønsket ordre.')
    entry = float(input('Pris per aksje: '))
    antall = int(input('Antall aksjer: '))
    stoploss = float(input('Stoploss-pris per aksje: '))
    kapital = float(input('Tilgjengelig kapital: '))



    #Utregning
    
    #Ordrestørrelse
    ordrestørrelse = entry * antall
    ordrestørrelse_prosent = ordrestørrelse / kapital
    ordrestørrelse_prosent_f = formating.f2(ordrestørrelse_prosent)

    #Risiko %
    risiko = antall * (entry - stoploss)
    risiko_prosent = 1 - (stoploss / entry)
    risiko_prosent_f = formating.f2(risiko)

    #Risiko av total %
    risiko_total = risiko * ordrestørrelse_prosent
    risiko_total_f = formating.f2(risiko_total)



    #Outputs
    oversikt.append(ordrestørrelse)
    oversikt.append(ordrestørrelse_prosent_f)
    oversikt.append(risiko)
    oversikt.append(risiko_prosent_f)
    oversikt.append(risiko_total_f)

    return oversikt
