#Complete program

#Formating
def f0 (tall):
    return format(tall, '.0f')
def f1 (tall):
    return format(tall, '.1f')
def f2 (tall):
    return format(tall, '.2f')


#Entries_kjop
def kjop ():
    print('Vennligst skriv inn ønsket ordre.')
    print('Skriv inn ordre på formen "<pris> <antall>".')

    orders = []
    order = input('Order 1: ').split()
    orders.append(order)
    counter = 1
    
    while True:
        counter += 1
        order = input(f'Order {counter}: ').split()
        if not order:
            break
        orders.append(order)
        
    return orders


#Utregning_kjop
def utregning_kjop ():
    oversikt = []

    #Inputs

    #Entries
    entries = kjop()
    sum_entries = 0
    sum_antall = 0
    for order in entries:
        sum_entries += float(order[0])*int(order[1])    #Problem
        sum_antall += int(order[1])
    
    antall = sum_antall
    avg_entry = sum_entries / antall
    avg_entry_f = f2(avg_entry)

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
    ordrestorrelse_f = f0(ordrestorrelse)
    ordrestorrelse_prosent = ordrestorrelse / kapital
    ordrestorrelse_prosent_f = f2(ordrestorrelse_prosent)

    #Risiko %
    risiko_prosent = (1 - (stoploss / avg_entry)) * 100         #risiko_prosent = (1 - (stoploss /avg_entry))
    risiko_prosent_f = f2(risiko_prosent)
    risiko = (risiko_prosent / 100) * ordrestorrelse          #risiko = risiko_prosent * ordrestorrelse
    risiko_f = f0(risiko)         

    #Risiko av total %
    risiko_total_prosent = risiko_prosent * ordrestorrelse_prosent
    risiko_total_prosent_f = f2(risiko_total_prosent)


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


#Print_kjop
def print_kjop (liste):

    #Inputs
    ordrestorrelse_f = liste[0]
    ordrestorrelse_prosent_f = liste[1]
    risiko_f = liste[2]
    risiko_prosent_f = liste[3]
    risiko_total_prosent_f = liste[4]
    avg_entry_f = liste[5]
    stoploss_f = liste[6]
    antall = liste[7]

    #Outputs
    print(f'Kjopssum: {ordrestorrelse_f} kr')
    print(f'Kjopssum av kapital: {ordrestorrelse_prosent_f}%')
    print()
    print(f'Risiko ved handel: {risiko_f} kr')
    print(f'Risiko ved handel %: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_prosent_f}%')
    print()
    print(f'Avg. Entry: {avg_entry_f} kr')
    print(f'Stoploss: {stoploss_f} kr')
    print(f'Antall: {antall}')


#Main_kjop
def main ():
    print_kjop(utregning_kjop())
    
main()