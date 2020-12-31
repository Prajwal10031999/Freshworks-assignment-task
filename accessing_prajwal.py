import codeprajwal as x 
x.create("naruto",25)

x.create("src",70,3600) 

x.read("naruto")

x.read("src")

x.create("naruto",50)

x.modify("naruto",55)
 
x.delete("naruto")


t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
