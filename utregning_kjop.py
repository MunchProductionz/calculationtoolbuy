import entries_kjop
from formating import f2

def utregning_kjop ():
    oversikt = []

    #Inputs

    #Entries
    entries = kjop()
    sum_entries = 0
    sum_antall = 0
    for order in entries:
        sum_entries += float(order[0])*int(order[1])
        sum_antall += int(order[1])
    
    antall = sum_antall
    avg_entry = sum_entries / antall
    avg_entry_f = formating.f2(avg_entry)

    print()
    
    #Stoploss
    stoploss = float(input('Stoploss-pris per aksje: '))
    stoploss_f = f2(stoploss)

    #Kapital
    kapital = float(input('Tilgjengelig kapital: '))

    print()
    print()

    

    #Utregning
    
    #Ordrestorrelse
    ordrestorrelse = avg_entry * antall
    ordrestorrelse_f = formating.f0(ordrestorrelse)
    ordrestorrelse_prosent = ordrestorrelse / kapital
    ordrestorrelse_prosent_f = formating.f2(ordrestorrelse_prosent)

    #Risiko %
    risiko_prosent = (1 - (stoploss / avg_entry)) * 100         #risiko_prosent = (1 - (stoploss /avg_entry)) * 100
    risiko_prosent_f = formating.f2(risiko_prosent)
    risiko = (risiko_prosent / 100) * ordrestorrelse            #risiko = (risiko_prosent / 100) * ordrestorrelse
    risiko_f = formating.f0(risiko)         

    #Risiko av total %
    risiko_total_prosent = risiko_prosent * ordrestorrelse_prosent
    risiko_total_prosent_f = formating.f2(risiko_total_prosent)


    #Outputs
    oversikt.append(ordrestorrelse_f)
    oversikt.append(ordrestorrelse_prosent_f)
    oversikt.append(risiko_f)
    oversikt.append(risiko_prosent_f)
    oversikt.append(risiko_total_prosent_f)
    oversikt.append(avg_entry_f)
    oversikt.append(stoploss_f)
    oversikt.append(antall)

    return oversikt