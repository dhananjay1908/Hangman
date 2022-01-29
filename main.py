import random
names = ["dhanno","chirag","lohiya","bong","chintu","gaurav","moyonk","ask","akash"]
x = random.choice(names)

ans = []
for i in range(len(x)):
    ans.append("_")
print(*ans)
print(" ")

hangman = [
  '''  +---+
  |   |
      |
      |
      |
      |
=========''','''  +---+
  |   |
  O   |
      |
      |
      |
=========''','''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
count=0
figure=0
print(hangman[0])
test = []
while True:
  if count==len(x):
    print("YOU WON!!")
    break
  elif figure==len(hangman)-1:
    print("YOU LOSE!!")
    break
  else:
    check=0
    y = input("guess a word: ")
    z=0
    for char in test:
      if y==char:
        z+=1

    if z!=0:
      print("ALREADY USED!")
      continue
    else:
      for i in range(len(x)):
        if y==x[i]:
          ans[i]=y
          count+=1
          check+=1
      if check==0:
        figure+=1
        print("INCORRECT!")
        print(f'LIVES REAMINING = {6-figure}')
      else:
        print("CORRECT!")
        print(f'LIVES REAMINING = {6-figure}')
        
    test.append(y) 
    print(*ans)
    print(hangman[figure])
  