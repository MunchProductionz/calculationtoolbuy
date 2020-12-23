from formating import f2

def kjøp ():

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
    print(f'Kjøpsum: {ordrestørrelse}')
    print(f'Kjøpsum av kapital: {ordrestørrelse_prosent_f}%')
    print(f'Risiko ved handel: {risiko} kr')
    print(f'Risiko ved handel: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_f}%')
