with open('TEST.txt') as egg:
  for word in egg.read().split(' '):
    if len(word)>3:
      #w=list(i)


      print(word[-1:] + word[1:-1] + word[:1] +'ay')
egg.close
