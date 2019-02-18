from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def qna(request):
    return render(request,'qna.html')
    
    
def mypage(request):
    return render(request,'mypage.html')
    

def signup(request):
    return render(request,'signup.html')

def notfound(request,noturl):
    return render(request,'notfound.html',{'noturl':noturl})
    
