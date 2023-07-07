from collections import Counter

def Check_str(st):
    li=[]
    for i in st:
        li.append(i) # creating list of char

    c=Counter(li) #creating a Dict for key as each char and value as frequency
    li=sorted(list(c.values()))
    li.pop(-1)
    li.append(sorted(list(c.values()))[-1]-1)

    if len(set(list(c.values()))) == 1: # if all charrecter occur same time this will trigger
            return True
    elif len(set(li)) == 1 : # any one charecter occure one time extra this till trigger
            return True
    else:
          return False
    
print(Check_str(st=input("Enter the string you want to check the Validetion : ")))

    

