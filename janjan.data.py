from tkinter import*
import sqlite3

root=Tk()
root.title('My LESTER Project')
root.geometry("500x500")

conn=sqlite3.connect('mydata.db')

c = conn.cursor()
'''
c.execute ("""CREATE TABLE "mydata" (
	"f_name"	TEXT,
	"l_name"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT

)""")
'''

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)


submit_btn+Button(root,text="Add record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
                
def sumbit():

    conn=sqlite3.connect("C:/Users/STUDENTS/janjan.data.py")
c=conn.cusor()

c. execute("INSERT INTO stuentinfo VALUES(:f_name ,l_name,:age,:address,:email)",
           ({
               
 'f_name':f_name.geet(),
 'l_name':l_name.geet(),
 'age':age.get()
 'address':address.get(),
 'email':email.get()
 
 })
        
    
conn.commit()
conn.close()
           
root.mainloop()
