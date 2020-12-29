def print_kjøp (liste):

    #Inputs
    ordrestørrelse_f = liste[0]
    ordrestørrelse_prosent_f = liste[1]
    risiko = liste[2]
    risiko_prosent_f = liste[3]
    risiko_total_f = liste[4]

    #Outputs
    print(f'Kjøpssum: {ordrestørrelse_f} kr')
    print(f'Kjøpssum av kapital: {ordrestørrelse_prosent_f}%')
    print(f'Risiko ved handel: {risiko} kr')
    print(f'Risiko ved handel: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_f}%')