CATEGORIES ={
    'Phones': 'katalog/smartfony/',
    'Fridges': 'katalog/holodilniki/',
    'Vacuums': 'katalog/pylesosy/',
    'Computers': 'katalog/noutbuki/',
    'Tv': 'katalog/televizory/',
    'Heater':'katalog/obogrevateli/',
}

def get_value(category):
    for key, value in CATEGORIES.items():
        if key == category:
            return value