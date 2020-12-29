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