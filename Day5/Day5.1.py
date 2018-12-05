with open("in_k.txt",'r') as f:
    inputs = f.readline()

counter=0

while counter <len(inputs)-2:
    if abs(ord(inputs[counter])-ord(inputs[counter+1]))==32:
        inputs = inputs.replace(inputs[counter:counter+2],"",1)
        if counter>0:
            counter-=1
    else:
        counter+=1
print(len(inputs))
