s = "aaaabbcaa"
counter = 0
predbukva = s[0]
for i in s:
    if i == predbukva:
        counter += 1
    else:
        print (predbukva + str(counter), end = "")
    counter = 1
    predbukva = i
print (predbukva + str(counter))
              
    
        
    