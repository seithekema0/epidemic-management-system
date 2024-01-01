## PROJECT ON EPIDIMIC MANAGEMENT SYSTEM CLASS XII(SCIENCE)

import mysql.connector as a

mydb=a.connect(host="localhost",user="root",password="amit",database="information")
print(mydb)

mycursor=mydb.cursor()
def menu():
    print("==================================================================================")
    print("------------------------------------MAIN MENU-------------------------------------")
    print("==================================================================================")
    print("KVS QUARANTINE CENTER")
    print("----------------------")
    print("1.Insert new entrant details")
    print("2.Update test results")
    print("3.Display all data")
    print("4.Display positive patients details")
    print("5.Update discharge details")
    print("6.Display particular paitent details")
    print("7.Quit")
    print("----------------------")
    n=int(input("Enter your choice ="))

    if n==1:
        newpatient()

    elif n==2:
        updateresults()

    elif n==3:
        alldata()

    elif n==4:
        positivedata()

    elif n==5:
        discdetail()

    elif n==6:
        patdetail()

    elif n==7:
        print("==================================================================================")
        print("----------------------------------VISIT AGAIN!!!----------------------------------")
        print("==================================================================================")
               
        
    else:
        print("====INVALID INPUT PLEASE TRY AGAIN====")

    menu()

# FUNCTION 1(Insert new entrant details)

def newpatient():
    l1=[]
    z = True
    
    while z:
        
        a=int(input("Enter patient id ="))
        b=input("Enter name of patient =")
        c=int(input("Enter patient age ="))
        d=input("Enter date of arrival(in YYYY-MM-DD formate) =")
        e=input("Enter the mode of transport used =")
        f=input("IS the patient symptomatic?(Yes or No) =")
            
        h=input("Enter test result(positive or negative) =")
    
        l1.append([a,b,c,d,e,f,h])
        
        
        
            
        sql=("insert into patient(P_ID,NAME,AGE,DATE_OF_ARRIVAL,MODE_OF_TRANSPORT,SYMPTOMATIC,TEST_RESULT) values(%s,%s,%s,%s,%s,%s,%s)")
        mycursor.executemany(sql,l1)
        mydb.commit()
    
    
        print("==================================================================================")
        print("------------------------------UPDATED SUCCESSFULLY!!!-----------------------------")
        print("==================================================================================")
        
        isContinue=(input("press y to add more or press n to stop: ")).lower()
        
        if isContinue=='n':
            break
    
    menu()

        
    


    

# FUNCTION 2(Update test results)

def updateresults():
    l2=[]
    
    a=int(input("Enter patient id ="))
    b=input("Enter date of testing(in YYYY-MM-DD formate) =")
    l2.append(b)
    c=input("Enter test result =")
    l2.append(c)

        
            
    l2.append(a)
    sql=("update patient set DATE_OF_TESTING=%s,TEST_RESULT=%s where P_ID=%s")
    
    mycursor.execute(sql,l2)
    mydb.commit()
    print("==================================================================================")
    print("------------------------------UPDATED SUCCESSFULLY!!!-----------------------------")
    print("==================================================================================")

    menu()

        
            
            
# FUNCTION 3(Display all data)  


def alldata():
    print("=======================================================")
    print("=====================PATIENT DETAILS===================")
    print("=======================================================")
    sql=("select * from patient")
    mycursor.execute(sql)
    a=mycursor.fetchall()
    for i in a:
        print(i)

    print("=======================================================")
    print("=======================================================")
    print("=======================================================")

    menu()



# FUNCTION 4(Display positive patients details)


def positivedata():
    l3=[]
    print("=======================================================")
    print("==============POSITIVE PATIENT DETAILS=================")
    print("=======================================================")
    sql=("select * from patient where TEST_RESULT='positive'")
    mycursor.execute(sql)
    a=mycursor.fetchall()
    l3.append(a)
    for i in l3:

        print(i)

    print("=======================================================")
    print("=======================================================")
    print("=======================================================")

    menu()


# FUNCTION 5(Update discharge details)


def discdetail():
    l4=[]
    a=int(input("Enter patient id ="))
    b=input("Enter discharge date(in YYYY-MM-DD formate) =")
    l4.append(b)
    l4.append(a)
    sql=("update patient set discharge_date=%s where P_ID=%s")
    mycursor.execute(sql,l4)
    mydb.commit()
    
    print("==================================================================================")
    print("------------------------------UPDATED SUCCESSFULLY!!!-----------------------------")
    print("==================================================================================")

    menu()
    




# FUNCTION 6(Display particular paitent details)


def patdetail():
    l5=[]
    a=int(input("Enter patient id ="))
    l5.append(a)
    sql=("select * from patient where P_ID=%s")
    mycursor.execute(sql,l5)
    b=mycursor.fetchall()
    print(b)
    print("=======================================================")
    print("=======================================================")
    print("=======================================================")

    menu()


menu()
