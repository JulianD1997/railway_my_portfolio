from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method != 'POST':
        return render(request,'index.html',{}) 
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    text_area = request.POST['text__area']
    message = f"""
    Me comunico : {name} con correo de email : {email}
    para informar
    {text_area}
    """
    send_mail(
        subject,
        message,
        email,
        ['juliandevcasallas@gmail.com'],
    )
    return render(request,'index.html',{'name':name})