global el
el=[]
def item(): 
    q,*p=input().split()
    global ind,element,l
    l=[int(x) for x in p]
    if len(l)==2:
        ind=l[0]
        element=l[1]
    elif len(l)==1:
        element=l[0]
    
    if q=='print':
        display()
    elif q=='insert' or q=="append":
        datainsert()
    elif q=='sort':
        el.sort()
        print("sorted!")
        display()

    elif q=='remove':
        remove()
    elif q=='pop':
        el.pop()
        print("popped")
        display()
    elif q=='reverse':
        el.reverse()
        print('reversed!')
        display()
    else:
        print("please pass valid input")
        item()

def remove():
    if not l:
        print("pass element to remove")
        display()
    else:
        if element not in el:
            print(f"{l} is not in the list")
            display()
        else:
            el.remove(element)
            display()
            
def datainsert():
    if not l:
        print("Please pass the value to insert!")
    else:
        if len(l)>=2:
            el.insert(ind,element)
            print('Element inserted:')
            display()
        else:
            el.append(element)
            print("Element appended!")
            display()

def display():
    if not el:
        print("Empty\nPlease Insert element")
        item()
    else:
        print(el)
        item()
item()
