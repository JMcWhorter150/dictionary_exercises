# random demo code goes here
# Nest your dictionaries!

bars = {
    'Lloyds': {
        'item': 'Cheap bourbon',
        'day' : 'Tuesday'
    },
    'Manuels' : {
        'item' : 'The Dogzilla',
        'day' : 'Wednesday',
        'fact': 'Python meetup on Thursdays'
    },
    'The Imperial': {
        'item': 'Philly',
        'day' : ['Tuesday', 'Friday']
        #using a list because the days don't need individual labels
    }
}

places = {
    'US': {
        'Georgia': {
            'Atlanta': {
                'work': 'DigitalCrafts',
                'cats': ['Oakley', 'Milla']
            },
            'Savannah': {
                'coffee': 'That place that time'
            }
        },
        'Tennessee': {
            'Nashville': {
                'lunch': 'Hattie B'
            }
        }
    },
    'Europe': {
        'Germany': {
            'Berlin': {
                'lunch': 'The Reichstag'
            },
            'Munich': {
                'snack': 'Hofbrauhaus'
            }
        }
    }
}

movies = [
    {
        'title': 'Avengers: End Game',
        'release date': '2019',
    },
    {
        'title': 'Avengers: Infinity dolars',
        'release date': '2018'
    }
]
# movies[1]['release date']
charges = [
    {
    'vendor': 'Kula',
    'amount': 6.36,
    },
    {
    'vendor': 'Kula',
    'amount': 9.11,
    },
    {
    'vendor': 'Barnes and Noble',
    'amount': 16.49,
    },
    {
    'vendor': 'Kula',
    'amount': 3.99,
    },
    {
    'vendor': 'Lloyds',
    'amount': 14.99,
    }
]


# Bad ways to store complicated information:
# best_item_at_bars = [
#     'Cheap bourbon', # at Lloyd's
#     'The Dogzilla', # at Manuel's
#     'Best staff ever' # The Imperial
# ]

# day_least_crowded = [
#     'Tuesday',
#     'Wednesday',
# ]

# print(f"At {bars[0]}, they have a good {best_item_at_bars}")
