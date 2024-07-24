from django.shortcuts import render,HttpResponse
from app.models import Contact
from django.contrib import messages
# Create your views here.
def index2(request):
    return render(request,"index2.html")

def analyze(request):
    #Get The text
    text=request.GET.get('text','default')

    #Analyze the text
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')

    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
        
        analysed=""
        for char in text:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analysed}
        text=analysed
        # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analysed=""
        for char in text:
            analysed+=char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analysed}
        text=analysed
        # return render(request,'analyze.html',params)
    if(newlineremover=="on"):
        analysed=""
        for char in text:
            if char!='\n' and char!='\r':
                analysed=analysed+char
        params={'purpose':'Removed NewLines','analyzed_text':analysed}
        text=analysed
        # return render(request,'analyze.html',params)
    if(extraspaceremover=="on"):
        analysed=""
        for index,char in enumerate(text):
            if text[index]==' ' and text[index+1]==' ':
                pass
            else:
                analysed=analysed+char
        params={'purpose':'Extra Spaces Remover','analyzed_text':analysed}
        text=analysed
        # return render(request,'analyze.html',params)
    elif(charcount=="on"):
        count=0
        for char in text:
            if char==' ' or char  in punctuations:
                pass
            else:
                count+=1

        params={'purpose':'Extra Spaces Remover','analyzed_text':count}
        return render(request,'analyze.html',params)
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcount!="on" ):
        return HttpResponse("Error")
    return render(request,"analyze.html",params )

def contact(request):
    if request.method=="POST":
        FirstName=request.POST.get("FirstName")
        LastName=request.POST.get("LastName")
        Email=request.POST.get("Email")
        Phone=request.POST.get("Phone")
        desc=request.POST.get("desc")
        City=request.POST.get("City")
        inputState=request.POST.get("inputState")
        inputZip=request.POST.get("inputZip")
        contact=Contact(FirstName=FirstName,LastName=LastName,Email=Email,Phone=Phone,desc=desc,City=City,inputState=inputState,inputZip=inputZip)
        contact.save()
        messages.success(request, "Your message has been sent...")
    return render(request,"contact.html")


def about(request):
    return render(request,'about.html')