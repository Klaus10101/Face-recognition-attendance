import datetime
import csv
x = datetime.datetime.now()
names = [] 
def stu():
    with open ("nameslist.txt","r") as file:
        data=file.read()
        x=data.split()
        return x
    
def present():
    with open("present.txt","r") as pr_stu:
        a=pr_stu.read().split()
        return a
    
def add(d,rows): 
    
   
    filename = 'att.csv'

    with open(filename, 'a+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows([[f"Date:  {d}"]])
        csvwriter.writerows("\n")
        csvwriter.writerows([["Names","","Presence"]])
        csvwriter.writerows("\n")
        csvwriter.writerows(rows)
        csvwriter.writerows("\n")

