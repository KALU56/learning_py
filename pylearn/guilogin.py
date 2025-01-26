###registration form
# which has 
# employ registration from as title
# first name,last name,sex,age,department,highest edication level,habbies,remark,register and clear action
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title("employee registration form")
root.geometry("500x500")

#form title
tk.Label(root,text="fill the following information",font=("Arial",20)).grid(row=0,column=0,columnspan=2)
#form fields
#first name
tk.Label(root,text="first name").grid(row=1,column=0)
first_name=tk.Entry(root)
first_name.grid(row=1,column=1)
#last name
tk.Label(root,text="father name").grid(row=2,column=0)
father_name=tk.Entry(root)
father_name.grid(row=2,column=1)
#sex
tk.Label(root,text="sex").grid(row=3,column=0)
sex=tk.StringVar(value="male")

sex.grid(row=3,column=1)
tk.Radiobutton(root,text="male",value=1,variable=sex,value="male" ).grid(row=3,column=2)
tk.Radiobutton(root,text="female",value=2,variable=sex,value="female").grid(row=3,column=3)
#age
tk.Label(root,text="age").grid(row=4,column=0)
age=tk.IntVar(value=0)
age=tk.Spinbox(root,from_=0,to=100,textvariable=age)
age.grid(row=4,column=1) 
#department
tk.Label(root,text="department").grid(row=5,column=0)
dep=["SE","HR","IT","Marketing","Finance"]
department=tk.Combobox(root,values=dep)
department.set("Select Department")
department.grid(row=5,column=1)
#highest edication level
tk.Label(root,text="highest edication level").grid(row=6,column=0)
highest_education_level=tk.StringVar(value="Select Level")
highest_education_level=tk.Combobox(root,values=["Select Level","B.Tech","M.Tech","B.Sc","M.Sc","B.A","M.A","B.Com","M.Com","B.E","M.E","B.Pharm","M.Pharm","B.Ed","M.Ed","B.Tech","M.Tech","B.Sc","M.Sc","B.A","M.A","B.Com","M.Com","B.E","M.E","B.Pharm","M.Pharm","B.Ed","M.Ed","B.Tech","M.Tech","B.Sc","M.Sc","B.A","M.A","B.Com","M.Com","B.E","M.E","B.Pharm","M.Pharm","B.Ed","M.Ed","B.Tech","M.Tech","B.Sc","M.Sc","B.A","M.A","B.Com","M.Com","B.E","M.E","B.Pharm","M.Pharm","B.Ed","M.Ed"])
highest_education_level.set("Select Level")
highest_education_level.grid(row=6,column=1)

#habbies
tk.Label(root,text="habbies").grid(row=7,column=0)
playing_football=tk.Checkbutton(root,text="playing football") 
playing_football.grid(row=7,column=1)
playing_cricket=tk.Checkbutton(root,text="playing cricket")
playing_cricket.grid(row=7,column=2)
playing_reading=tk.Checkbutton(root,text="playing reading")
playing_reading.grid(row=7,column=3)
playing_writing=tk.Checkbutton(root,text="playing writing")
playing_writing.grid(row=7,column=4)
#remark
tk.Label(root,text="remark").grid(row=8,column=0)
remark=tk.Entry(root)
remark.grid(row=8,column=1)

#submit button
tk.Button(root,text="register").grid(row=9,column=0)
tk.Button(root,text="clear").grid(row=9,column=1)   








