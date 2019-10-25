SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_price(tickets_total):
    return (tickets_total * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    
    print("There are {0} tickets available".format(tickets_remaining)) 
    user_name = input('Please enter your name: ')
    
    try:

        tickets_to_buy = input('Hello {0}, how many tickets would you like to buy? '.format(user_name))
        tickets_to_buy = int(tickets_to_buy)
        if tickets_to_buy > tickets_remaining:
            raise ValueError('We only have {0} tickets available'.format(tickets_remaining))
        if tickets_to_buy == 0:
            raise ValueError('You need to buy at least 1 ticket to proceed')
            continue
    except ValueError as err:
        print('Oops that\'s not a valid entry: {0}.'.format(err))
    else:
        tickets_total = calculate_price(tickets_to_buy)
        print('The tickets total is ${0}'.format(tickets_total))
        process_sale = input('Would you like to purchase tickets? YES/NO ')
        if process_sale.lower() == 'yes':
            print('SOLD!')
            tickets_remaining -= tickets_to_buy
        else:
            print('Thnk you anyways, {0}'.format(user_name))
    

# Notify user that tickets are sold out
if tickets_remaining <= 0:
   print('We sold out! There are: {0} tickets left.'.format(tickets_remaining))
