def print_kjop (liste):

    #Inputs
    ordrestorrelse_f = liste[0]
    ordrestorrelse_prosent_f = liste[1]
    risiko_f = liste[2]
    risiko_prosent_f = liste[3]
    risiko_total_f = liste[4]
    avg_entry = liste[5]
    antall = liste[6]

    #Outputs
    print(f'Kjopssum: {ordrestorrelse_f} kr')
    print(f'Kjopssum av kapital: {ordrestorrelse_prosent_f}%')
    print()
    print(f'Risiko ved handel: {risiko_f} kr')
    print(f'Risiko ved handel %: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_f}%')
    print()
    print(f'Avg. Entry: {avg_entry} kr')
    print(f'Antall: {antall} kr')