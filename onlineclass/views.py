#https://blog.finxter.com/how-to-embed-a-python-interpreter-in-your-website/
from django.shortcuts import render,redirect #for connect one html page to anoter
from .models import Register 
from .models import questions as question       #import table 
from .models import student_data as students #database class import file in models.py 
from .models import  user_submit as user    #database class import file from models.py (databse)
from .models import upload_doc as Upload
from django.http import HttpResponse #http request and response file 
from datetime import datetime
from .forms import student #forms.py  file imort 
from django.core.mail import send_mail #for send mail
from django.conf import settings
from englisttohindi.englisttohindi import EngtoHindi        #english to hindi translator module import 
import nltk          #import nltk is for antonyms and synonyms 
from nltk.corpus import wordnet  #it is a part of nltk module 
# message to be translated


# Create your views here.
now = datetime.now()

today_time= now.strftime("%H:%M:%S")
print("Current Time =", today_time)

studentname=""




def admin(request):            #admin login 
    print("pass")
    account = Register()
    account.img = 'admin.jpg'
    name="Admin "
    student_data = students.objects.all()
    
    return render(request,'admin.html',{'account':account,'today_time':today_time,'name':name,'student_data': student_data})

def qupload(request):                  #question upload function 
    account = Register()
    account.img = 'admin.jpg'
    name="Admin "
    if request.method=="POST":
        question_id = int(request.POST.get('question_id'))
        question_name = request.POST.get('question_name')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        answers = request.POST.get('answer')
        qus = question()                        #object creattion of question class from models.py table name questons 
        qus.question_id = question_id
        qus.question_name=question_name
        qus.option_1 = option_1
        qus.option_2 =option_2
        qus.option_3 =option_3
        qus.option_4 =option_4
        qus.answer=answers
        qus.save()
        print("Question Uploaded")
        return render(request,'qupload.html')

       
       


    return render(request,'qupload.html',{'account':account,'name':name,'today_time':today_time})

def admlogin(request):                             #admin login page 
    name ="Admin"
    account = Register()
    account.img = 'admin.jpg'
    student_data = students.objects.all()        #all data fetch from table stduent_data (databases) 
   
    if request.method=='POST':
        username = request.POST.get('uname')
        password = int(request.POST.get('your_pass'))
        if((username =="devraj") and (password ==1234)):
            return render(request,'admin.html',{'account':account,'today_time':today_time,'name':name,'student_data':student_data})

                       
    return render(request,'admlogin.html')
     

def index(request):
    reg=""

    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile =request.POST.get('mobile')
        pass1 = request.POST.get('pass')
        pass2 = request.POST.get('re_pass')
        request.session['mobile'] = mobile #session start 
        request.session['user_name'] = name
        print(name,email,pass1,pass2)
        reg = Register()
        reg.username = name
        reg.email = email
        reg.mobile = mobile
        reg.password = pass1
        reg.save()
        subject = 'welcome to our company '  
        message = 'hello user'
        email_form = settings.EMAIL_HOST_USER
        receipt_list = [email,]
        send_mail(subject,email_form,message,receipt_list)                
        return redirect('userdetails')
        
    
    
    register = Register()
    register.img = 'signin.jpg' 
    print("suessfull regster")
    return render(request,'index.html')
# this login funtion is for hyper link like one page to another move

def login(request):
    account = Register()
    account.img = 'img.jpg' 
    user_names=""
    passwords =""
    if request.method == 'POST':
        user_names = request.POST.get('uname')
        passwords = request.POST.get('your_pass')
    request.session['u_name'] = user_names

    logi = Register.objects.filter(username=user_names,password=passwords) #all data fetch from register database
    #logi = Register.objects.all() 
    print(logi)
    for data in logi:
        users = data.username    #username fetch from register database
        mobiles = data.mobile   #mobile data fetch from register database  
        print("username is  : ",users)
        try:
            if(user_names == users):
                print("same")
                user_data = student.objects.filter(user_name=user_names)
            
                return render(request,'Dashboard.html',{'user_data':user_data,'today':today_time,'account':account})
                break
            
        except NameError:
            print("error",NameError)
            return render(request,'Dashboard.html')
            

            
    return render(request,'login.html')


        
   



def Dashboard(request):
    user_name_data = request.session['u_name']
    user_data = student.objects.filter(user_name=user_name_data)
    
    account = Register()
    account.img = 'account.jpg'
    return render(request,'DashBoard.html',{'account':account,'today_time':today_time,'user_data':user_data})
        


#def Dashboard(request): #hyper link code (go to Dashboard.html page )
    #return render(request,'Dashboard.html')

def exampage(request):  #hyper link code (go to exampage.html)
    st_name =""
    answers = []        #list created for accestion all answer and store into answers
    user_name = request.session['u_name']   
    print("user_name is :",user_name)                           #user_name session access from login.html user_name filed
    user_data = student.objects.filter(user_name=user_name)                               # all data fetch from the student table
    
    questions_fetch = question.objects.filter(question_id=101)      #question fetch from questions database
    for data in user_data:
        st_name = data.st_name
   
    account = Register()
    account.img = 'account.jpg'

     
    q1 = question.objects.all()                                          #question fetch from database
    user_submit = user.objects.all()         #user_submit data fetch 
      
    for i in user_submit:
        if(i.student_name == user_name):
            user_name =user_name
    print("name is .....:", user_name)
    if(i.student_name == user_name): 
        Desc = "You are Already Completed the Exam:"
        return render(request,'exampage.html',{'account':account,'today_time':today_time,'Desc':Desc})  
    else:
        if request.method =='POST':
            answers.append(request.POST.get('101'))
            answers.append(request.POST.get('102'))
            answers.append(request.POST.get('103'))
            answers.append(request.POST.get('104'))
            answers.append(request.POST.get('105'))
            print("answers",answers)            
            if(answers[1] is not None):
                res = user()
                res.student_name =user_name 
                res.student_mobile = 74855
                res.answer = answers
                res.save()
            

                        #return redirect('exampage',{'account':account,'today_time':today_time,'user_data':user_data,'questions_fetch':questions_fetch})                
                return render(request,'ResultPage.html',{'account':account,'today_time':today_time,'user_data':user_data})  
            else:
                return render(request,'exampage.html',{'account':account,'today_time':today_time,'user_data':user_data,'q1':q1})
        
    Exam_Start = "To start the exam Click Submit Button : "
    return render(request,'exampage.html',{'account':account,'today_time':today_time,'user_data':user_data,'questions_fetch':questions_fetch,'Exam_Start':Exam_Start})    

def Resultpage(request):  #hyper link code (go to Resultpage.html)
    u_name= request.session['u_name']                       #session User_name Data access 
    user_data = student.objects.filter(user_name=u_name)       #Data Fetch From the student_data table from onlineclass Database
    account = Register()
    account.img = 'account.jpg'
    
    #All questio fetch from questions table in onlineexam database and store into lst_answer 
    question_answer = question.objects.all()                   
    set_answer =[]
    for i in question_answer:
        set_answer.append(i.answer)
    len_answer = len(set_answer)
    correct_answer =0
    #All answer fetch from user_submit table and store the result into user_answer list 
    #fetched data and did some operation and find the correct result of the user submitted exam paper end here
    #exam_did_data = user.objects.filter(student_name=u_name)  
    try:
        exam_did_data = user.objects.filter(student_name=u_name) 
        user_answer1 =""
        user_answer =""
        for i in exam_did_data:
            user_answer1= i.answer
        len_result = len(user_answer1)
        for i in range(1,len_result-1):
            if(user_answer1[i]=="'"):
                continue
            else:
                user_answer +=user_answer1[i]
        user_answer = list(user_answer.split(", "))
        print("special :",user_answer)

        for i in range(0,len_answer-1):
            if(user_answer[i]==set_answer[i]):
                correct_answer +=1

        # fetched data and did some operation and find the correct result of the user submitted exam paper end here
    
        Desc = "Your Result is out of 5 : is "
        return render(request,'Resultpage.html',{'account':account,'user_data':user_data,'today_time':today_time,'correct_answer':correct_answer,'Desc':Desc})
    except:
        Desc = "You Are not gave the exam yet : Please Do the Exam "
        return render(request,'Resultpage.html',{'account':account,'user_data':user_data,'today_time':today_time,'Desc':Desc})

    
    
    
    

def loginpage(request): #hyper link code (go to login.html page ) 
    
    return render(request,'login.html')

def upload(request):
   
    if request.method == 'POST':
        item_name = request.POST.get('i_name')
        item_amount = int(request.POST.get('amount'))
        item_desc = request.POST.get('desc')
        image = request.POST.get('image')
        print("item_name is :",item_name )
        print("path is :",image,item_desc,item_amount)
        upl = Upload()
        print("check 1")
    
        upl.item_name = item_name
        upl.item_amount =item_amount
        upl.item_desc = item_desc
        upl.images = image
        upl.save()
    logis = Upload.objects.all()
    print("logis:",logis)
    #return render(request,'upload.html')   
    return render(request,'showitem.html',{'logis':logis})

def userdetails(request):
    print("call userdetails")
    st_mobile = request.session['mobile']
    user_names = request.session['user_name']

    try:
        if request.method == 'POST':
            name = request.POST.get('st_name')
            mobile =  st_mobile
            college_name = request.POST.get('college')
            branch = request.POST.get('branch')
            semester = int(request.POST.get('semester'))
            usn = request.POST.get('usn')
            image = "IMG.JPG"
            sign ="SIGN.JPG"
            print(name,mobile,college_name,branch,semester,usn,image,sign)
            #stds = students.objects.all()
            #for i in stds:
                #if(i.user_name != user_names):
            std = students()
            std.user_name = user_names
            std.st_name=name
            std.mobile=mobile
            std.college=college_name
            std.branch=branch
            std.semester=semester
            std.photo=image
            std.signature=sign
            std.usn = usn
            std.save()

            return render(request,'login.html')
    except NameError:
            print("NameError")
     
    return render(request,'userdetails.html')


def stringresult(request):
    account = Register()
    account.img = 'account.jpg'
    s_mobile = request.session['mobile']
    user_data = student.objects.filter(mobile=s_mobile) 
    return render(request,'stringresult.html',{'today':today_time,'account':account,'user_data':user_data})

def StringCalc(request):
    account = Register()
    account.img = 'account.jpg'
    s_name = request.session['u_name']
    user_data = student.objects.filter(user_name =s_name)     # Data Fetch from Database student Data table 


    if request.method=="POST":
        data_desc ="The actual Data is : "
        result = ""
        data = request.POST.get('string')
        print("String is : ",data)
        if 'Translate' in request.POST:
            print("Translate ")
            desc  = "The result of the given Data is  : "
            con = EngtoHindi(data)
            result =con.convert
        
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})

        if 'Synonyms' in request.POST:
            synonyms = []
            for syn in wordnet.synsets(data):
                for i in syn.lemmas():
                    synonyms.append(i.name())

            con = EngtoHindi(synonyms)
            desc  = "The Synonyms of the given Data is  : "
            
            result =set(synonyms)
           # result_in_hindi = result.convert

            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'Antonyms' in request.POST:
            antonyms = []
            for any in wordnet.synsets(data):
                for i in any.lemmas():
                    if i.antonyms():
                        antonyms.append(i.antonyms()[0].name())


            desc  = "The Antonyms of the given Data is : "
            
            result =set(antonyms)
        
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'special_char' in request.POST:
            print("special_char")
            desc = "The All special charater of given Data is : "
            for i in data:
                if(i.isalpha()):
                    continue
                elif(i.isdigit()):
                    continue
                else:
                    result += i
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'find_string' in request.POST:           # strt operation on more then one submit buttion in form
            desc ="The All alphabet character is :"
            

            for i in data:
                if(i.isalpha()):
                    result +=i
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})

        
        if 'vowel' in request.POST:             #vowel check 
            desc = "The vowel of given data is  :"
            vowel = "aeiouaEIOU"
            for i in data:
                if(i in vowel):
                    result +=i

                

            
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'consonent' in request.POST:
           
            desc = "The consonent of the given data is  : "
            vowel = "AEIOUaeiou"
            for i in data:
                if(i not in vowel):
                    result +=i
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'Count_word' in request.POST:
            
            desc = "The count of each character of given Data is   : "
            all_freq = {}
            for i in data:
                if i in all_freq:
                    all_freq[i] +=1
                else:
                    all_freq[i] = 1
            result = all_freq
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'sort_string' in request.POST:
            print("sort_string")
            #return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'find_number' in request.POST:
            desc = "The number of given data is  : "
            for i in data:
                if(i.isdigit()):
                    result +=i
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        if 'number_operation' in request.POST:
            desc  = "The result of the given Data is  : "
            result =eval(data)
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})
        
        if 'sort_number' in request.POST:
            desc = 'The sort of number  of the givem data is : '
            lst = []
            for i in data:
                if(i.isdigit()):
                    result +=i
            
        
            for i in result:        #convert into the list
                lst.append(int(i))
            length_list = len(lst)
            for i in range(0,length_list):          #sort the data in to increasing order
                for j in range(i+1,length_list):
                    if(lst[i]>lst[j]):
                        lst[i],lst[j] = lst[j],lst[i]
                        
            

            result = lst
                
            return render(request,'stringresult.html',{'data_desc':data_desc,'data':data,'desc':desc,'result':result})

        return render(request,'stringresult.html')

    return render(request,'StringCalc.html',{'today_time':today_time,'account':account,'user_data':user_data})

def OnlineCompiler(request):
    user_name_data = request.session['u_name']
    user_data = student.objects.filter(user_name=user_name_data)
    
    account = Register()
    account.img = 'account.jpg'
    return render(request,'OnlineCompiler.html',{'account':account,'today_time':today_time,'user_data':user_data})