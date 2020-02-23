with open('demo.txt') as prof:
    vowels = ('a', 'e', 'i', 'o', 'u')

    keimeno = prof.read().split(' ')
    keimeno = list(set(keimeno))
    keimeno.sort(key=len, reverse=True)
    i=0
    newList = []
    for i in range(5):
        newList.append(keimeno[i])
        i+=1

    for lexi in newList:
        newlexi = "".join(reversed(lexi))
        for letter in newlexi:
            if letter in vowels:
                newlexi = newlexi.replace(letter, "")

        print(newlexi)


    prof.close()
