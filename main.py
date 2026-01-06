x = True
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 20)
dice3 = random.randint(1, 50)

while x == True:
    try:
        user_input = input('would you like to play war? (yes/no): ')
        if user_input.lower() == 'no':
            break
        if user_input.lower() == 'yes':
            print('Starting a new game of war...')
            x = False
    except:
        print('An error occurred. Please try again.')
y = True
while y == True:
    country = input('What country do you want to play as?  (Prussia/easy, Austrian empire/hard, Ottoman Empire/insane): ')
    if country.lower() == 'prussia' or country.lower() == 'easy':
        print('You have chosen Prussia with easy difficulty.')
        y = False
        money = 30000
        army = 10000
        stability = 35
        culture = 'German'
        Neighbors = ['Austria-Hungary', 'Russia', 'France', 'Denmark', 'Switzerland']
    elif country.lower() == 'austria' or country.lower() == 'hard':
        print('You have chosen Austria with hard difficulty.')
        y = False
        money = 20000
        army = 4000
        stability = 10
        culture = 'austrian/hungarian'
        Neighbors = ['Prussia', 'Russia', 'Italy', 'Ottoman Empire']   
    elif country.lower() == 'ottoman empire' or country.lower() == 'insane':
        print('You have chosen Ottoman Empire with insane difficulty.')
        y = False
        money = 15000
        army = 1000
        stability = 5
        culture = 'Turkish'
        Neighbors = ['Russia', 'Austria-Hungary', 'Italy', 'Bulgaria', 'Greece']
    else:
        print('Invalid choice. Please try again')
        continue
print(f'You start with ${money}, {army} soldiers, and {stability} stability. Good luck!')
print('loading...')
tutorial = input('Would you like a quick tutorial? (yes/no): ')
if tutorial.lower() == 'yes':
    print('In this game, you will manage your country by making strategic decisions to grow your economy, build your army, and maintain stability. Your goal is to become the hegimon of Europe and Asia. The game is turn based, and each turn you will have to make a stratigic desicion to grow your economy, militry, or stability. your economy represents how well you can do other actions such as recruting an army, or increaseing stabiliy, which pretty much represetns the health of your country. Your military represents how well you can defend yourself from other countries or attack them. Good luck and have fun!')
else: 
    print('Skipping tutorial...')
    game_start = True
while game_start == True:
random_event = random.randint(1, 5)
    if random_event == 1:
        print('Random event: ')
