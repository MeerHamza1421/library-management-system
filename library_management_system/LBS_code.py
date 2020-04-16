import os       #os module to use remove function to remove file
import logging

'''logging module to use strip function to make string
clean from white spaces and new line character afer reading it from file'''

   #**********************lists of global variables*****************************

MAX_BOOK_ID = 12
DATE_SIZE=10
MAX_COPY_NUMBER=16
MAX_BOOKS=200
MAX_CATEGORIES=30
MAX_BOOK_NAME=60
MAX_CATEGORIE_NAME=20
MAX_CATEGORIE_NUMBER=3

#   ******************************validation functions***********************************

def isvalidbookid(bookid):
    b=0
    c=0
    d=0
    for i in range(3):
        if(bookid[i].isdigit()):
            b+=1
    if b==3:
        if (bookid[3]=='-'):
            for i in range(4,6):
                 if (bookid[i].isupper()):
                     c+=1
        if c==2:
            if (bookid[6]=='-'):
                for i in range(7,12):
                    if (bookid[i].isdigit()):
                        d+=1
    if d==5:
        return True
    else:
        return False
def isvalidcopynumber(bookcopy):
    b = 0
    c = 0
    d = 0
    e = 0
    for i in range(3):
        if (bookcopy[i].isdigit()):
            b += 1
    if b == 3:
        if (bookcopy[3] == '-'):
            for i in range(4, 6):
                if (bookcopy[i].isupper()):
                    c += 1
        if c == 2:
            if (bookcopy[6] == '-'):
                for i in range(7, 12):
                    if (bookcopy[i].isdigit()):
                        d += 1
                if d == 5:
                    if bookcopy[12]=="#":
                        for i in range(13,16):
                            if bookcopy[i].isdigit():
                                e+=1
    if e==3:
        return True
    else:
        return False
def isvalidcategorynumber(categoryid):
    b=0
    for i in range(3):
        if (categoryid[i].isdigit()):
            b += 1
    if b == 3:
        return True
    else:
        return False
def isvalidbookname(bookname):
    x=len(bookname)
    c=0
    for i in range(x):
            if bookname[i].isalnum() or bookname[i] == ' ' or bookname[i] == ':':
                c += 1
    if c == x:
        return True
    else:
        return  False
def isvalidcategoryname(categoryname):
    x = len(categoryname)
    c = 0
    for i in range(x):
        if categoryname[i].isalpha():
            c += 1
    if c == x:
        return True
    else:
        return False
#   *********************************category related functions********************************** '''

def AddCategory(CatergoryNo, CatergoryName, ArraySize, newCategoryId, newCategoryName):
    f=0
    for i in range(ArraySize):
        if CatergoryNo[i] == "0" and CatergoryName[i]== "0":
            CatergoryNo[i]=newCategoryId
            CatergoryName[i]=newCategoryName
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def UpdateCategory (CatergoryNo, CatergoryName, ArraySize, prevCategoryId, newCategoryId, newCategoryName):
    f=0
    for i in range(ArraySize):
        if CatergoryNo[i]==prevCategoryId:
            CatergoryNo[i]=newCategoryId
            CatergoryName[i]=newCategoryName
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def DeleteCategory(CatergoryNo,CatergoryName,ArraySize,CategoryId):
    f=0
    for i in range(ArraySize):
        if CatergoryNo[i]==CategoryId:
            CatergoryNo[i]="0"
            CatergoryName[i]="0"
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def  PrintCategories(CatergoryNo, CatergoryName, ArraySize):
    for i in range(ArraySize):
        if CatergoryNo[i] != " 0" and CatergoryName[i] !="0":
            print(CatergoryNo[i], ":\t", CatergoryName[i])
        else:
            pass
def SaveCategories( CatergoryNo, CatergoryName, ArraySize, fileName):
    file=open(fileName, "w")
    for i in range(ArraySize):
        if CatergoryNo[i] != " 0" and CatergoryName[i] != "0":
            file.write(CatergoryNo[i])
            file.write(" ")
            file.write(CatergoryName[i])
            file.write("\n")
    file.close()
def  LoadCategories(CatergoryNo, CatergoryName, ArraySize, fileName):
    file=open(fileName, "r")
    for i in range(ArraySize):
        CatergoryNo[i]=file.readline(3).strip()
        CatergoryName[i]=file.readline()
        CatergoryName[i]=CatergoryName[i].strip()
        if CatergoryNo[i]=="" and CatergoryName[i]=="":
            CatergoryNo[i]="0"
            CatergoryName[i]="0"
            break
    file.close()

    '''****************************book related functions**********************************'''

def  AddBook(BookId, BookName, Editions, ArraySize, newBookId, newBookName, edition):
    f = 0
    for i in range(ArraySize):
        if BookId[i]=="0" and BookName[i]=="0" and Editions[i]=="0":
            BookId[i]=newBookId
            BookName[i]=newBookName
            Editions[i]=edition
            f = 1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def  UpdateBook(BookId,BookName,Editions,ArraySize,prevBookId,newBookId,newBookName,edition):
    f=0
    for i in range(ArraySize):
        if BookId[i]==prevBookId:
            BookId[i]=newBookId
            BookName[i]=newBookName
            Editions[i]=edition
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def DeleteBook(BookId, BookName, Editions, ArraySize, bookId):
    f=0
    for i in range(ArraySize):
        if BookId[i]==bookId:
            BookId[i]="0"
            BookName[i]="0"
            Editions[i]="0"
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def PrintBooks(BookId,BookName,Editions,ArraySize):
    print("bookid\tbookname\teditions")
    for i in range(ArraySize):
        if BookId[i]!="0" and BookName!=0 and Editions[i]!="0":
            print(BookId[i],"\t",BookName[i],"\t",Editions[i])
        else:
            pass
def SaveBooks(BookId,BookName,Editions,ArraySize,filename):
    file=open(filename,"w")
    for i in range(ArraySize):
        if BookId[i]!="0" and BookName[i]!="0" and Editions[i]!="0":
            file.write(BookId[i])
            file.write("\n")
            file.write(BookName[i])
            file.write("\n")
            file.write(Editions[i])
            file.write("\n")
        else:
            pass
    file.close()
def LoadBooks(BookId,BookName,Editions,ArraySize,filename): #loading sai krni hai
    file=open(filename,"r")
    for i in range(ArraySize):
        BookId[i]=file.readline().strip()
        BookName[i]=file.readline().strip()
        Editions[i]=file.readline().strip()
        if BookId[i]=="" and BookName[i]=="" and Editions[i]=="":
            BookId[i]="0"
            BookName[i]="0"
            Editions[i]="0"
            break
    file.close()

#    *********************************book copy related functions*************************************

def AddBookSample (CopyId, PulishedDates, ArraySize, newCopyId, newPublishDate):
    f=0
    for i in range(ArraySize):
        if CopyId[i]=="0" and PulishedDates[i]=="0":
            CopyId[i]=newCopyId
            PulishedDates[i]=newPublishDate
            f=1
            break
        else:
            pass
    if f==1:
        return True
    else:
        return False
def  UpdateBookSample (CopyId,PulishedDates,ArraySize,prevCopyId,newCopyId,newPublishDate):
    f=0
    for i in range(ArraySize):
        if CopyId[i]==prevCopyId:
            CopyId[i]=newCopyId
            PulishedDates[i]=newPublishDate
            f=1
        else:
            pass
    if f==1:
        return True
    else:
        return False
def  DeleteBookSample (CopyId,PulishedDates,ArraySize,copyId):
    f=0
    for i in range(ArraySize):
       if CopyId[i]==copyId:
           CopyId[i]="0"
           PulishedDates="0"
           f=1
           break
       else:
           pass
    if f==1:
        return True
    else:
        return False
def  PrintBookSamples (CopyId,PulishedDates, ArraySize, BookId):
    print("copyid\tpublihed date")
    for i in range(ArraySize):
        p=CopyId[i]
        f = 0
        if BookId in CopyId[i]:
                print(CopyId[i],"\t",PulishedDates[i])
                p="0"
        else:
            pass
def  SaveBookSamples (CopyId,PulishedDates,ArraySize,fileName):
    file=open(fileName,"w")
    for i in range(ArraySize):
        if CopyId[i]!="0" and PulishedDates[i]!="0":
            file.write(CopyId[i])
            file.write(" ")
            file.write(PulishedDates[i])
            file.write("\n")
        else:
            pass
    file.close()
def LoadBookSamples (CopyId, PulishedDates, ArraySize, fileName):
    file=open(fileName,"r")
    for i in range(ArraySize):
        CopyId[i]=file.readline(MAX_COPY_NUMBER).strip()
        PulishedDates[i]=file.readline().strip()
        if CopyId[i]=="" and PulishedDates[i]=="":
            CopyId[i]="0"
            PulishedDates[i]="0"
            break
    file.close()

#*************************I/O functions**********************************

def printmenu():
    print("** Welcome to University Library Management System **\nChoose the following option\n 1\tCategory Management(A,E,L,D)\n2\tBooks Management(A,E,L,D)\n3\tBook Copies Management(A,E,L,D)\n0\tExit Program(0E)\nChoose the option:\n")
def manioption(mainOption):
    mainOption=int(input("enter the main option:\t"))
    return mainOption
def suboption(subOption):
    subOption=input("enter the suboption for further processing:\t")
    return subOption

#    *************************************************MAIN FUNCTION*****************************************************

catno=[None]*MAX_CATEGORIES
catnam=[None]*MAX_CATEGORIES
bokid=[None]*MAX_BOOKS
boknam=[None]*MAX_BOOKS
edi=[None]*MAX_BOOKS
bokcpy=[None]*MAX_BOOKS
pubdat=[None]*MAX_BOOKS
for i in range(MAX_CATEGORIES):
    catno[i]="0"
    catnam[i]="0"
for i in range(MAX_BOOKS):
    bokid[i]="0"
    boknam[i]="0"
    edi[i] = "0"
for i in range(MAX_BOOKS):
    bokcpy[i]="0"
    pubdat[i]="0"
f=input("enter name of file to get data of categories:\t")
LoadCategories(catno,catnam,MAX_CATEGORIES,f)
os.remove(f)    #you should be careful when giving file name to load data because if you give wrong name then
                # then all your data should be lost because os.remove() remove file after typing its name
                #  and after removing during the time of safe it again create a new file and save data on it
f1=input("enter name of file to get data of books:\t")
LoadBooks(bokid,boknam,edi,MAX_BOOKS,f1)
os.remove(f1)
f2=input("enter name of file to get data of books:\t")
LoadBookSamples(bokcpy,pubdat,MAX_BOOKS,f2)
os.remove(f2)
while(1):
    m=None
    s=None
    printmenu()
    main=manioption(m)
    sub=suboption(s)
    if main==1:
        if sub=="A":
            print("Enter the details of the category")
            newcateid=input("Enter the category Id:\t")
            newcatnam=input("Enter the category name:\t")
            while (not(isvalidcategorynumber(newcateid)) or (not(isvalidcategoryname(newcatnam)))):
                print("you may enter invalid input\n\t******try again********")
                newcateid = input("Enter the category Id:\t")
                newcatnam = input("Enter the category name:\t")
            r=AddCategory(catno,catnam,MAX_CATEGORIES,newcateid,newcatnam)
            if r==True:
                print("category added successfully")
            else:
                print("category not be added")
        elif sub=="E":
            print("Enter the details of the category")
            oldcatid=input("enter previous category which you want to edit/update:\t")
            newcateid=input("enter the new category id:\t")
            newcatnam=input("enter the name of new category:\t")
            while not(isvalidcategorynumber(oldcatid)) or not(isvalidcategorynumber(newcateid)) or not(isvalidcategoryname(newcatnam)):
                print("you may enter invalid input\n\t******try again********")
                oldcatid = input("enter previous category which you want to edit/update:\t")
                newcateid = input("Enter the category Id:\t")
                newcatnam = input("Enter the category name:\t")
            r=UpdateCategory(catno,catnam,MAX_CATEGORIES,oldcatid,newcateid,newcatnam)
            if r==True:
                print("category updated successfully")
            else:
                print("category not be updated may be you enter wrong id or id doesnot exist")
        elif sub=="L":
            PrintCategories(catno,catnam,MAX_CATEGORIES)
        elif sub=="D":
            ncatid=input("enter the id of category you want to delete:\t")
            while (not(isvalidcategorynumber(ncatid))):
                print("you may enter invalid input\n\t******try again********")
                ncatid = input("enter the id of category you want to delete:\t")
            r=DeleteCategory(catno,catnam,MAX_CATEGORIES,ncatid)
            if r==True:
                print("category deleted sucessfully")
            else:
                print("category not deletd you may enter wrong id")
    elif main==2:
        if sub=="A":
            print("enter the details of book")
            newbokid=input("enter the book id:\t")
            newboknam=input("enter the name fo book:\t")
            newedi=input("enter the edition of book:\t")
            while(not(isvalidbookid(newbokid)) or not(isvalidbookname(newboknam))):
                print("you may enter invalid input\n\t******try again********")
                newbokid = input("enter the book id:\t")
                newboknam = input("enter the name fo book:\t")
                newedi = input("enter the edition of book:\t")
            r=AddBook(bokid,boknam,edi,MAX_BOOKS,newbokid,newboknam,newedi)
            if r==True:
                print("book addded succesfully")
            else:
                print("book was not added")
        elif sub=="E":
            print("enter the details of book")
            oldbokid=input("enter the bookid which you want to edit/update")
            newbokid = input("enter the book id:\t")
            newboknam = input("enter the name fo book:\t")
            newedi = input("enter the edition of book:\t")
            while (not (isvalidbookid(newbokid)) or not(isvalidbookid(oldbokid)) or not(isvalidbookname(newboknam))):
                print("you may enter invalid input\n\t******try again********")
                oldbokid = input("enter the bookid which you want to edit/update")
                newbokid = input("enter the book id:\t")
                newboknam = input("enter the name fo book:\t")
                newedi = input("enter the edition of book:\t")
            r=UpdateBook(bokid,boknam,edi,MAX_BOOKS,oldbokid,newbokid,newboknam,newedi)
            if r==True:
                print("book was updated succesfully")
            else:
                print("book not be updated may be you enter wrong id or id doesnot exist ")
        elif sub=="L":
            PrintBooks(bokid,boknam,edi,MAX_BOOKS)
        elif sub=="D":
            nbokid=input("enter the book id you want to delete:\t")
            while not(isvalidbookid(nbokid)):
                print("you may enter invalid input\n\t******try again********")
                nbokid = input("enter the book id you want to delete:\t")
            r=DeleteBook(bokid,bokid,edi,MAX_BOOKS,nbokid)
            if r==True:
                print("book delted succesfully")
            else:
                print("book not be deleted may be you enter wrong id or id doesnot exist ")
    elif main==3:
        if sub=="A":
            print("enter the details of book copy")
            newidcpy = input("enter id of book copy to add:\t")
            newpubdat = input("enter the publishdate of bookcopy:\t")
            while not(isvalidcopynumber(newidcpy)):
                print("you may enter invalid input\n\t******try again********")
                newidcpy = input("enter id of book copy to add:\t")
                newpubdat = input("enter the publishdate of bookcopy:\t")
            r=AddBookSample(bokcpy,pubdat,MAX_BOOKS,newidcpy,newpubdat)
            if r==True:
                print("book copy added successfully")
            else:
                print("book copy not added")
        elif sub=="E":
            print("enter the details of book copy")
            oldbokcpy=input("enter previous id:\t")
            newidcpy = input("enter new id of book copy to add:\t")
            newpubdat = input("enter the new publishdate of bookcopy:\t")
            while not(isvalidcopynumber(newidcpy) or not(isvalidcopynumber(oldbokcpy))):
                print("you may enter invalid input\n\t******try again********")
                oldbokcpy = input("enter previous id:\t")
                newidcpy = input("enter id of book copy to add:\t")
                newpubdat = input("enter the publishdate of bookcopy:\t")
            r=UpdateBookSample(bokcpy,pubdat,MAX_BOOKS,oldbokcpy,newidcpy,newpubdat)
            if r==True:
                print("book copy edited/updated sucessfully")
            else:
                print("book copy not be updated may be you enter wrong id or id doesnot exist ")
        elif sub=="L":
            nbokcpy=input("enter the id which copies you want to load:\t")
            while not(isvalidbookid(nbokcpy)):
                print("you may enter invalid input\n\t******try again********")
                nbokcpy = input("enter the id which copies you want to load:\t")
            PrintBookSamples(bokcpy, pubdat, MAX_BOOKS,nbokcpy)
        elif sub=="D":
            delbokcpy=input("enter the id of book copy you want to delete:\t")
            while not(isvalidcopynumber(delbokcpy)):
                print("you may enter invalid input\n\t******try again********")
                delbokcpy = input("enter the id of book copy you want to delete:\t")
            r=DeleteBookSample(bokcpy,pubdat,MAX_BOOKS,delbokcpy)
            if r==True:
                print("book sample deleted successfully")
            else:
                print("book sample not be deleted may be you enter wrong id or id doesnot exist")
    elif main==0:
        if sub=="E":
             f=input("enter the name of file for categories to save data:\t")
             SaveCategories(catno,catnam,MAX_CATEGORIES,f)
             f1=input("enter the name of file for books to save data\t")
             SaveBooks(bokid,boknam,edi,MAX_BOOKS,f1)
             f2=input("enter the name of file to store bookcopies:\t")
             SaveBookSamples(bokcpy,pubdat,MAX_BOOKS,f2)
             break