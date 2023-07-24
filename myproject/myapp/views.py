from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        link = request.POST["link"]
        # form=ImageForm(data=request.POST,files=request.FLIES)
        # if form.is_valid():
        #     form.save()
        #     obj=form.instance
        #บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age,
            email=email,
            link=link,
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/")
    else :
        return render(request,"form.html")

def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.email = request.POST["email"]
        person.link = request.POST["link"]
        person.save()
        messages.success(request,"อัพเดตข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นทาง
        return redirect("/")
    #ดึงข้อมูลประชากรที่ต้งการแก้
    person = Person.objects.get(id=person_id)
    return render(request,"edit.html",{"person":person})

def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    #เปลี่ยนเส้นทาง
    return redirect("/")