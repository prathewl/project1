data=[]
def insert_data():
   title=input("enter the title")
   amount=input("enter the amount")
   date=input("enter the date")
   #print(title+" "+amount+" "+date)
   data.append((title,amount,date))
def display_data():
   for item in data:
      print(item[0]+" "+item[1]+" "+item[2])
y=0
while(y==0): 
 print("1->for insert")
 print("2->for display")
 print("3->for delete")
 print("4->for update")
 opt=int(input("enter the option"))
 if(opt==1):
   insert_data()
 if(opt==2):
   display_data()
   
 y=int(input("Do you want to continue? press 0 for yes"))
