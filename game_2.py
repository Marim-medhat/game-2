list=[10,20,30,
      40,50,60,
      70,80,90]
print (list)
x=5
while x==5:
    print('player 1 entre your position and odd numper from 1to9')
    p=int(input('pos'))
    n=int(input('num'))
    for i in range (len(list)):
        if n==list[i]:
            print('error,try again')
            n=int(input('num'))
    if n%2!=0 and n<=9:         
        for i in range (len(list)):
            if list[i]==p:
                list[i]=n
        print("|",list[0],"|",list[1],"|",list[2],"|")
        print("|",list[3],"|",list[4],"|",list[5],"|")
        print("|",list[6],"|",list[7],"|",list[8],"|")
    else:
        print('error,try again')
        n=int(input('num'))
        for i in range (len(list)):
          if n==list[i]:
             print('error,try again')
             n=int(input('num'))
        for i in range (len(list)):
           if list[i]==p:
               list[i]=n
        print("|",list[0],"|",list[1],"|",list[2],"|")
        print("|",list[3],"|",list[4],"|",list[5],"|")
        print("|",list[6],"|",list[7],"|",list[8],"|")
    if list[0]+list[1]+list[2]==15 or list[8]+list[0]+list[4]==15 or list[3]+list[4]+list[5]==15 or list[6]+list[7]+list[8]==15 or list[6]+list[2]+list[4]==15 or list[1]+list[7]+list[4]==15 or list[6]+list[3]+list[0]==15 or list[2]+list[5]+list[8]==15:
           print("you win")
           break
    print('player 2 entre your position and even numper from 0to9')
    p=int(input('pos')) 
    n=int(input('num'))
    for i in range (len(list)):
            if n==list[i]:
                print('error,try again')
                n=int(input('num'))
    if n%2==0 and n<=9 :
        for i in range (len(list)):
             if list[i]==p:
                list[i]=n
        print("|",list[0],"|",list[1],"|",list[2],"|")
        print("|",list[3],"|",list[4],"|",list[5],"|")
        print("|",list[6],"|",list[7],"|",list[8],"|")
    else:
        print('error,try again')
        n=int(input('num'))
        for i in range (len(list)):
          if n==list[i]:
             print('error,try again')
             n=int(input('num')) 
        for i in range (len(list)):
            if list[i]==p:
                list[i]=n
        print("|",list[0],"|",list[1],"|",list[2],"|")
        print("|",list[3],"|",list[4],"|",list[5],"|")
        print("|",list[6],"|",list[7],"|",list[8],"|")
    if list[0]+list[1]+list[2]==15 or list[8]+list[0]+list[4]==15 or list[3]+list[4]+list[5]==15 or list[6]+list[7]+list[8]==15 or list[6]+list[2]+list[4]==15 or list[1]+list[7]+list[4]==15 or list[6]+list[3]+list[0]==15 or list[2]+list[5]+list[8]==15:
            print("you win")
            break
