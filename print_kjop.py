def print_kjop (liste):

    #Inputs
    ordrestorrelse_f = liste[0]
    ordrestorrelse_prosent_f = liste[1]
    risiko = liste[2]
    risiko_prosent_f = liste[3]
    risiko_total_f = liste[4]

    #Outputs
    print(f'Kjopssum: {ordrestorrelse_f} kr')
    print(f'Kjopssum av kapital: {ordrestorrelse_prosent_f}%')
    print()
    print(f'Risiko ved handel: {risiko} kr')
    print(f'Risiko ved handel: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_f}%')