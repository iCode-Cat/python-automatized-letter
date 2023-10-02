 
names = []
starting_letter = ''
# Push names
with open('./Input/Names/invited_names.txt') as name:
    names = (name.read().split())

# Initial letter
    with open('./Input/Letters/starting_letter.txt') as initial:
           starting_letter = initial.read()

# Write letter with names
for name in names:
    with open(f'Output/{name}.txt', mode='w') as letter:
        letter.write(starting_letter.replace('[name]', name))

        
