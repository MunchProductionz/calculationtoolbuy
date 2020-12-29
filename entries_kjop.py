#order = [price, amount]
#orders = [[price_1, amount_1], [price_2, amount_2], ...]

def kjop ():
    print('Vennligst skriv inn ønsket ordre.')
    print('Skriv inn ordre på formen "<pris> <antall>".')
    print()

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