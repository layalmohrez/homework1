#empty list to append reminde of divisions
binary=[]
while True:
    d=int(input('enter decimal: '))
    #decimal to binary algorithm
    while d!=0:
        # append reminde of division 0 or 1
        binary.append(d%2)
        # int devision
        d//=2
    #reverse the list to make output is right
    binary.reverse()
    for i in binary:
        print(i,end='')
    print()
    s=input('do you want to continue? for yes enter y no enter n: ')
    if s=='y':
        #clear list items
        binary=[]
    elif s=="n":
        break
    else:
        print('error, good bye')
        break
