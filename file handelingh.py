print("********************************")
print("*     FILE HANDALING     *")
print("********************************")
import os
while True:
     def f():
         print("1.create the file")
         print("2.read the file")
         print("3.list the file")
         print("4.edit the file")
         print("6.delete the file")
         print("7.stop program")
     a=input("enter the choice:")
     match a:
          case "1": 
            print("creating a file")
            name=input("enter the file name:")
            name=name+".txt"
            file=open(name,"w")
            file.write("welcome")
            print("____________________")
            print("file created successfully")
            print("____________________")
            f()
          case "2":
            print("read the file")
            name=input("enter file name:")
            name=name+".txt"
            file=open(name,"r")
            print("____________________")
            print(file.read())
            print("____________________")
            f()
          case "3":
            print("listing the file")
            print("____________________")
            path="D:\Supriya"
            file=os.listdir(path)
            for file in file:
                 print(file)
                 print("____________________")
                 f()
          case "4":
            print("editing the file")
            name=input("enter file name:")
            name=name+".txt"
            file=open(name,"a")
            print(file.write("D:\Supriya"))
            print("____________________")
            print("edited the file")
            print("____________________")
          case "5":
            print("deleting the file")
            name=input("enter file name:")
            name=name+".txt"
            os.remove(name)
            print("____________________")
            print("file",name,"deleted successfully")
            print("____________________")
          case "6":
            print("stop the program")
            break
print("end")
                
       
        





