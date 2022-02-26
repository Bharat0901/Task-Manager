import sys
try:
    creation1=open("pending.txt","x")
    creation1.close()
except:
    pass

try:
    creation2=open("done.txt","x")
    creation2.close()
except:
    pass

def HELP():
    print("""$ ./task help
            Usage :-
            $ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
            $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
            $ ./task del INDEX            # Delete the incomplete item with the given index
            $ ./task done INDEX           # Mark the incomplete item with the given index as complete
            $ ./task help                 # Show usage
            $ ./task report               # Statistics """)
def ls():
    f=open("pending.txt","r")
    l1=f.read().split()
    l1 = [l1[i:i+2] for i in range(0,len(l1),2)]
    l1.sort()
    #print(l1)
    if len(l1)!=0:
        for n,i in enumerate(l1):
            print("{}. {} {}".format(n+1,i[1],[int(i[0])]))
    f.close()
def AdD():
    f=open("pending.txt","a+")
    priority=sys.argv[2]
    work=sys.argv[3]
    data='{} "{task}" '.format(priority,task=work)
    f.write(data)
    f.close()
    print("Added task: {} with priority {}".format(work,priority))
def DeL():
    l=open("pending.txt","r+")
    l1=l.read().split()
    l1 = [l1[i:i+2] for i in range(0,len(l1),2)]
    l1.sort()
    l.close()
    #print(l1)
    if len(l1)!=0:
        for ind,line in enumerate(l1):
            if ind==(int(sys.argv[2])-1):
                print("Deleted item with index {}".format(sys.argv[2]))
                l1.remove(line)
                break
        else:
            print("Error: item with index {} does not exist. Nothing deleted.".format(sys.argv[2]))
        #print(l1) 
        
    else:
        print("Error: item with index {} does not exist. Nothing deleted.".format(sys.argv[2]))
    l=open("pending.txt","w")
    for q in l1:
        data="{} {task} ".format(q[0],task=q[1])
        l.write(data)
    l.close()
def DoNe():
    l=open("pending.txt","r")
    d=open("done.txt","a+")
    l1=l.read().split()
    l1 = [l1[i:i+2] for i in range(0,len(l1),2)]
    l1.sort()
    for _ in range(1):
        if len(l1)!=0:
            for ind,line in enumerate(l1):
                if ind==(int(sys.argv[2])-1):
                    print("Marked item as done.")
                    l1.remove(line)
                    break
            else:
                l.close();d.close()
                print("Error: no incomplete item with index {} exists.".format(sys.argv[2]))
                break
            l.close()
            datad="{} {task} ".format(line[0],task=line[1])
            d.writelines(datad)
            d.close()
            l=open("pending.txt","w")
            l1.sort()
            for q in l1:
                data="{} {task} ".format(q[0],task=q[1])
                l.write(data)
            l.close()
        
        else:
            l.close();d.close()
            print("Error: no incomplete item with index {} exists.".format(sys.argv[2]))  
def ReporT():
    l=open("pending.txt","r")
    d=open("done.txt","r")
    l1=l.read().split()
    l1 = [l1[i:i+2] for i in range(0,len(l1),2)]
    do=d.read().split()
    do = [do[i:i+2] for i in range(0,len(do),2)]
    do.sort()
    print("Pending : {}".format(len(l1)))
    for n1,i in enumerate(l1):
            print("{}. {} {}".format(n1+1,i[1],[int(i[0])]))
    print("\n")
    print("Completed : {}".format(len(do)))
    for n2,j in enumerate(do):
            print("{}. {} {}".format(n2+1,j[1],[int(j[0])]))
    l.close()
    d.close()
try:
    if sys.argv[1]=='help':  
        HELP()    
    elif sys.argv[1]=="ls":  
        ls()
    elif sys.argv[1]=="add":
        AdD()
    elif sys.argv[1]=="del":
        DeL()
    elif sys.argv[1]=="done":
        DoNe()
    elif sys.argv[1]=="report":
        ReporT()
except:
    HELP()