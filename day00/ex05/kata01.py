languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

keys = list(languages.keys())
values = list(languages.values())


for i in range(0, len(keys)):
     print("{} was created by {}".format(keys[i], values[i]))
    
