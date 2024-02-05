def unique(list):
    map = {}
    for x in list:
        map[x]=1
    
    for x in map:
        print(x,end=' ')

list = input()
unique(list)