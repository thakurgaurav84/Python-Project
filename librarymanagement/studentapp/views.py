from django.shortcuts import render
import pymysql

# Create your views here.
def home(request):
    return render (request,'studentapp/index.html')
def slogin(request):
    return render(request,'studentapp/student.html')
def sregister(request):
    return render(request,'studentapp/sregister.html')

def RegisterAction(request):
    f=request.POST['fname']
    m=request.POST['mobile']
    r=request.POST['rollno']
    p=request.POST['pwd']
    c=pymysql.connect(host='localhost',user='root',password='aurora@',database='aurora')
    cur=c.cursor()
    cur.execute("select * from student where rollno='"+r+"'")
    d=cur.fetchone()
    print(d)
    if d is not None:
        context={'data':'rollno Already exist try with other...!!'}
        return render(request,'studentapp/sregister.html',context)
    else:
        i=cur.execute("insert into student values('"+f+"','"+m+"','"+r+"','"+p+"')")
        c.commit()
    if i>0:
        context={'data':'Registration Succesful....!!!'}
        return render(request,'studentapp/sregister.html',context)
    else:
        context={'data':'Registration failed....!!!'}
        return render(request,'studentapp/sregister.html',context)

def LoginAction (request):
    r=request.POST['rollno']
    p=request.POST['pwd']
    
    con=pymysql.connect(host='localhost',user='root',password='aurora@',database='aurora')
    cur=con.cursor()
    cur.execute("select * from student where rollno='"+r+"' and password='"+p+"'")
    d=cur.fetchone()

    if d is not None:
        request.session['rollno']=r
        return render(request, 'studentapp/studenthome.html')

    else:
        context={'data':'Login failed..!!'}
        return render(request, 'studentapp/student.html',context)

def studenthome (request):
    return render(request, 'studentapp/studenthome.html')


def login (request):
    return render(request, 'libraryapp/login.html')

def liblogaction(request):
    u=request.POST['username']
    p=request.POST['pwd']
    if u=='admin' and p=='admin':


        return render(request, 'libraryapp/libhome.html')
    else:
        context={'data':'Login Failed..!!'}
        return render (request, 'libraryapp/login.html',context)

def libhome (request):
     return render(request, 'libraryapp/libhome.html')


def addbooks (request):
    return render

def LibLogAction(request):
    u=request.POST['uname']
    p=request.POST['pwd']

    if u=='Admin' and p=='Admin':
        return render(request,'LibrarianApp/LibHome.html')
    else:
        context={'data':'Login Failed..!!'}
        return render(request,'LibrarianApp/Login.html',context)
        
        
def libhome(request):
    return render(request,'libraryapp/libhome.html')
    

def AddBooks(request):
    return render(request,'Libraryapp/addbooks.html')
    
def AddBookAction(request):
    f=request.POST['rno']
    m=request.POST['bname']
    r=request.POST['author']
    
    con=pymysql.connect(host='localhost',user='root',password='aurora@',database='aurora')
    cur=con.cursor()
    cur.execute("select * from books where bname='"+m+"' and author='"+r+"'")
    d=cur.fetchone()
    print(d)
    if d is not None:
        context={'data':'This Book Already Exist..!!'}
        return render(request,'libraryapp/addbooks.html',context)
    else:
        i=cur.execute("insert into books values('"+f+"','"+m+"','"+r+"')")
        con.commit()
    if i>0:
        context={'data':'Book Added Sucessfully..!!'}
        return render(request,'libraryapp/addbooks.html',context)
    else:
        context={'data':'Adding failed..!!'}
        return render(request,'libraryapp/addbooks.html',context)
    
def ViewBooks(request):

    con=pymysql.connect(host='localhost',user='root',password='aurora@',database='aurora')
    cur=con.cursor()
    cur.execute("select * from books")
    data=cur.fetchall()
    strdata="<table border='1'><tr><th>Rack No</th><th>Book Name</th><th>Author</th></tr>"
    for d in data:
        strdata+="<tr><td>"+d[0]+"</td><td>"+d[1]+"</td><td>"+d[2]+"</td></tr>"
    strdata+="</table>"
    context={'table':strdata}
    return render(request,'libraryapp/viewbooks.html',context)

def SearchBook(request):
    return render(request,'studentapp/searchbook.html')
    
def searchbookaction (request):
    m = request.POST['bname']
    con = pymysql.connect(host='localhost', user='root', password='aurora@', database='aurora')
    cur = con.cursor()
    cur.execute("select * from books where bname like %s", ("%"+m+"%",))
    results = cur.fetchall()
    context = {'results': results}
    return render(request, 'studentapp/searchresults.html', context)

    

