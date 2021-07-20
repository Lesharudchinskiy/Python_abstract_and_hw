f_langs = {'kirill': 'js', 'lexa': 'py', 'stifler': 'py', 'rob': 'java'}
vote = ['sanya', 'nik', 'rob', 'lexa']
for name in vote:
    if name in f_langs.keys():
        print('Thank you ' + name.title() + ' for voting!')
    else:
        print(name.title() + ', do you want to vote for favorite lang?')