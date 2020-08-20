

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return "brak"



def find_address(text):
    address = find_between(text, 'położonej', 'dla')
    address = address.replace(',', '')
    return address



def find_estimated_sum(text):
    estimated_sum = find_between(text, 'oszacowania wynosi', 'zł')

    estimated_sum=' '.join(estimated_sum.split())
    estimated_sum=estimated_sum.replace(' ','')

    return estimated_sum


def find_starting_price(text):
    starting_price = find_between(text, 'równa', 'sumy')
    starting_price = ' '.join(starting_price.split())

    return starting_price

def find_auction_date(text):
    auction_date = find_between(text, 'w dniu', 'o')
    auction_date = ' '.join(auction_date.split())
    return auction_date