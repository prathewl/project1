data=[]
def insert_data():
   title=input("enter the title")
   amount=input("enter the amount")
   date=input("enter the date")
   #print(title+" "+amount+" "+date)
   data.append((title,amount,date))
def display_data():
   for index,item in enumerate(data):
         print(str(index+1)+ " "+item[0]+" "+item[1]+" "+item[2])
def delete_data():
    display_data()
    index=int(input("enter the index of the data you want to delete"))
    if 0<index<=len(data):
       delete_item=data.pop(index-11)
       print(f"data deleted record: {delete_item[0]} | {delete_item[1]} | {delete_item[2]} ")
    else:
      print("invalid index")
   
def update_data():
      display_data()
      index=int(input("enter the index of the data you want to update"))
      if 0<index<=len(data):
         title=input("enter new tittle (leave empty to unchange)")
         amount=input("enter new amount (leave empty to unchange)")
         date=input("enter new date (leave empty to unchange)")
         old_title,old_amount,old_date=data(index=1)
         data[index-1]=(
            title or old_title,
            amount or old_amount,
            date or old_date
         )
         print("data updated successfully")  
      else:
        print("invalid index")  
            

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
 if(opt==3):
    delete_data()
 if(opt==4):
    update_data()
   
 y=int(input("Do you want to continue? press 0 for yes"))
