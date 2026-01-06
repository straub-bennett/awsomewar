x = True

while x == True:
    try:
        user_input = input('would you like to play war? (yes/no): ')
        if user_input.lower() == 'no':
            break
        if user_input.lower() == 'yes':
            print('Starting a new game of war...')
            x = False
            # Here you would add the logic to start a poker game
    except:
        print('An error occurred. Please try again.')
y = True
while y == True:
    country = input('What country do you want to play as?  (Prussia/easy, England/medium,Austria/hard, Ottoman Empire/insane): ')
    if country.lower() == 'prussia' or country.lower() == 'easy':
        print('You have chosen Prussia with easy difficulty.')
        y = False
        money = 30000
        army = 10000
        stability = 35
    elif country.lower() == 'england' or country.lower() == 'medium':
        print('You have chosen England with medium difficulty.')
        y = False
        money = 25000
        army = 7000
        stability
    elif country.lower() == 'austria' or country.lower() == 'hard':
        print('You have chosen Austria with hard difficulty.')
        y = False
        money = 20000
        army = 4000
        stability = 10
    elif country.lower() == 'ottoman empire' or country.lower() == 'insane':
        print('You have chosen Ottoman Empire with insane difficulty.')
        y = False
        money = 15000
        army = 1000
        stability = 5
    else:
        print('Invalid choice. Please try again')
        continue
print(f'You start with ${money} and {army} soldiers. Good luck!')
yes = u_input
