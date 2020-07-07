import random
def main():
  dados_rolls = 10
  dice_sum = 0
  for i in range(0,dados_rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()