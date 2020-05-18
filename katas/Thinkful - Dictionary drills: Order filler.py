def fillable(stock, merch, quantity):
    return merch in stock and stock[merch] >= quantity
    
stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}
print(fillable(stock, 'football', 4))

