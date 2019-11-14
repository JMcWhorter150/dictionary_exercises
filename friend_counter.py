ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

def countFriends(dictionary):
    friends_count = len(dictionary['friends'])
    dictionary['friends_count'] = friends_count
    return dictionary

countFriends(ramit)
print(ramit['friends_count'])
print(ramit.keys())