from collections import Counter
#st="check check check that or this"
st=input("Enter a string with some repetitive word : ")
c=Counter(st.split(" "))  # creating a dict of word count
d = max(zip(c.values(), c.keys()))[1] # use Zip function to creat a key value tuple of dict and find the max and return the key name .
print(len(d))


