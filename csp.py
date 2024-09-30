x=[1,2,3]
y=list(range(10))
counter=0
for i in x:
    for j in y:
        if i+j>=5:
            print([i,j],end=" ")
            counter+=1

print(f"\nFound {counter} Solutions")