import entries_kjop
from formating import f2

def utregning_kjop ():
    oversikt = []

    #Inputs

    #Entries
    entries = kjop()
    antall_entries = len(entries)
    sum_entries = 0
    sum_antall = 0
    for order in entries:
        sum_entries += float(order[0])*int(order[1])        #Problem
        sum_antall += int(order[1])
    
    avg_entry = sum_entries / antall_entries
    antall = sum_antall

    print()
    
    #Stoploss / Kapital
    stoploss = float(input('Stoploss-pris per aksje: '))
    kapital = float(input('Tilgjengelig kapital: '))



    #Utregning
    
    #Ordrestorrelse
    ordrestorrelse = avg_entry * antall
    ordrestorrelse_f = formating.f0(ordrestorrelse)
    ordrestorrelse_prosent = ordrestorrelse / kapital
    ordrestorrelse_prosent_f = formating.f2(ordrestorrelse_prosent)

    #Risiko %
    risiko_prosent = 1 - (stoploss / avg_entry)         #risiko_prosent = (1 - (stoploss /avg_entry))
    risiko_prosent_f = formating.f2(risiko_prosent)
    risiko = risiko_prosent * ordrestorrelse          #risiko = risiko_prosent * ordrestorrelse
    risiko_f = formating.f0(risiko)         

    #Risiko av total %
    risiko_total = risiko * ordrestorrelse_prosent
    risiko_total_f = formating.f2(risiko_total)


    #Outputs
    oversikt.append(ordrestorrelse_f)
    oversikt.append(ordrestorrelse_prosent_f)
    oversikt.append(risiko_f)
    oversikt.append(risiko_prosent_f)
    oversikt.append(risiko_total_f)
    oversikt.append(avg_entry)
    oversikt.append(antall)

    return oversikt
