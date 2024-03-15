order = {
    'size': 'tall',
    'notes': 'no whip',
    'drink': 'mocha latte',
    'serve': 'for here'
}

match order:
    case {'size': 'tall', 'serve': 'for here', **resto}:
        drink = f"{resto['drink']} {resto['notes']}"
        print(drink)
    case _:
        print("No se encontro la orden")