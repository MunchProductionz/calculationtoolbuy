import entries_kjop
from formating import f2

def utregning_kjøp ():
    oversikt = []

    #Inputs
    print('Vennligst skriv inn ønsket ordre.')

    #Entries
    entries = entries_kjop.kjop()
    antall_entries = len(entries)
    for entry in entries: 
        sum_entries += pris[0]*pris[1]
        sum_antall += pris[1]
    
    avg_entry = sum_entries / antall_entries
    antall = sum_antall

    # entry = float(input('Pris per aksje: '))
    # antall = int(input('Antall aksjer: '))

    #Stoploss / Kapital
    stoploss = float(input('Stoploss-pris per aksje: '))
    kapital = float(input('Tilgjengelig kapital: '))



    #Utregning
    
    #Ordrestørrelse
    ordrestørrelse = avg_entry * antall
    ordrestørrelse_prosent = ordrestørrelse / kapital
    ordrestørrelse_prosent_f = formating.f2(ordrestørrelse_prosent)

    #Risiko %
    risiko = antall * (avg_entry - stoploss)
    risiko_prosent = 1 - (stoploss / avg_entry)
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
    oversikt.append(avg_entry)
    oversikt.append(antall)

    return oversikt
