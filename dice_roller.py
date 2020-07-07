import random
def main():
  player_n = int(input('Numero de jugadores'))
  dice_rolls = int(input('How many dice would you like to roll?'))
  dice_size = int(input('How many sides are the dice?'))
  dice_sum = []
  player_name = []
  mayor = 0
  player_win = 0
  for p in range (0,player_n):
    player_name.append("")
    dice_sum.append(0)
    player_name[p] = str(input('what is team name?'))
    for x in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      dice_sum[p] = dice_sum[p] + roll
      print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum[p]}')
    if dice_sum[p] > mayor:
      mayor = dice_sum[p]
      player_win = p
  print(f'El jugador ganador es {player_win}')
  print(f'El jugador ganador es {player_name[player_win]}')
  print(f'You have rolled a total of {dice_sum[player_win]}')
  print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()