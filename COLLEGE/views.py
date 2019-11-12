from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
def home(request):
    print('homepage')


def login(request):
    pass


from .models import Post


# ob1 = Post()
# ob2 = Post()
# ob3 = Post()
#
# ob1.name = 'arya'
# ob1.age = '22'
# ob1.date = '12.12.12'
#
# ob2.name='rishika'
# ob2.age='23'
# ob2.date='11.11.11'
#
# ob3.name='athulya'
# ob3.age='22'
# ob3.date='9.9.9'

# objects=[ob1,ob2,ob3]

def home(request):
    objects = Post.objects.all()
    recent=Post.objects.order_by('-date')[0:3]
    return render(request, 'marketing-index.html', {'ob': objects}),


def my(request):
    if request.method =='POST':
        a=request.POST['firstname']
        b=request.POST['lastname']
        user=auth.authenticate(username=a,password=b)
        if user is not None:
         auth.login(request,user)
         return redirect('COLLEGE:home')
        else:
          messages.error(request,'login error')
        return redirect('COLLEGE:login')
        print(request.POST)
        # return render(request,'marketing-index.html')
        return redirect('COLLEGE:home')
    return render(request, 'my.html')
def logout(request):
    auth.logout(request)
    return redirect('COLLEGE:home')
# def register(request):
#     return render(request, 'register.html')
def register(request):
    if request.method =='POST':
        a=request.POST['username']
        b=request.POST['email']
        c=request.POST['psw']
        d=request.POST['psw-repeat']
        if c==d:
            if User.objects.filter(username=a):
                messages.error(request,'username already exist')
                return redirect('COLLEGE:register')
            elif User.objects.filter(email=b):
                messages.error(request,'email exist')
            else:
              v=User.objects.create_user(username=a,email=b,password=c,is_staff=1,is_superuser=1)
              v.save()
        else:
            messages.error(request,'error')
            return redirect('COLLEGE:register')
        auth.login(request,v)
        print(a,b,c)
        return redirect('COLLEGE:home')
    return render(request,'register.html')



def index(request):
    if request.method =='POST':
        a=request.POST['username']
        b=request.POST['lastname']
        return render(request,'marketing-index.html')
    objects = Post.objects.all()
    recent = Post.objects.order_by('-date')[0:3]
    return render(request, 'marketing-index.html', {'obj': objects,
                                                    'res':recent})
def listing(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 2)

    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, 'marketing-index.html', {'objects': objects})