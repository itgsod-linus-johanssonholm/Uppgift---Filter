#encoding: UTF-8

def filter(array,value):

    lenght = len(array)

    newlist = []
    for i in range(lenght):
        print array[i]
        if array[i] == value:
           newlist.append(value)



    return newlist


array =["bosse", "daniel", "edvard", "bosse", "bosse"]
value = "bosse"

print filter(array,value)