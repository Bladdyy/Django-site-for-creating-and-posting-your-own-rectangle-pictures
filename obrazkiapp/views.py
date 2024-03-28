from django.shortcuts import render, redirect
from obrazkiapp.models import Picture, Rectangle
from django.contrib.auth import authenticate, login, logout

def show_main(request):
    pics_list = Picture.objects.all()
    if request.user.is_authenticated:
        return render(request, 'Obrazkolandia_out.html', {'all_pics': pics_list})
    else:
        return render(request, 'Obrazkolandia.html', {'all_pics': pics_list})


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:9000/obrazki')
        else:
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:9000/obrazki')


def show_panel(request):
    if request.user.is_authenticated:
        pics_list = []
        for pic in Picture.objects.all():
            if request.user in pic.users.all():
                pics_list.append(pic)
        return render(request, 'Obrazkolandia_własna.html', {'all_pics': pics_list, 'usr': request.user})
    else:
        return redirect('login')


def pict_site(request, pict_name):
    if Picture.objects.filter(name=pict_name).exists():
        pict = Picture.objects.filter(name=pict_name).get()
        rect_list = Rectangle.objects.filter(picture=pict)
        return render(request, 'pict.html', {'pict': pict, 'rectangles': rect_list})
    else:
        return render(request, '404.html')


def pict_modify(request, pict_name):
    if request.user.is_authenticated:
        pics_list = []
        for pic in Picture.objects.all():
            if request.user in pic.users.all():
                pics_list.append(pic.name)
        if pict_name in pics_list:
            pict = Picture.objects.filter(name=pict_name).get()
            if request.method == 'POST':
                x = request.POST["X"]
                y = request.POST["Y"]
                height = request.POST["height"]
                width = request.POST["width"]
                color = request.POST["color"]
                new_rect = Rectangle(x=x, y=y, width=width, height=height, color=color, picture=pict)
                new_rect.save()
                rect_list = Rectangle.objects.filter(picture=pict)
                return redirect('http://127.0.0.1:9000/obrazki/panel/' + pict_name)
            else:
                rect_list = Rectangle.objects.filter(picture=pict)
                return render(request, 'pict_modify.html', {'pict': pict, 'rectangles': rect_list})
        else:
            print(pict_name)
            return render(request, '404.html')
    else:
        return redirect('login')


def rect_delete(request, pict_name, rect_id):
    if request.user.is_authenticated:
        pics_list = []
        for pic in Picture.objects.all():
            if request.user in pic.users.all():
                pics_list.append(pic.name)
        if pict_name in pics_list:
            pict = Picture.objects.filter(name=pict_name).get()
            rects = [rect.id for rect in Rectangle.objects.filter(picture=pict)]
            if rect_id in rects:
                Rectangle.objects.filter(id=rect_id).delete()
                print(rect_id)
                return redirect('http://127.0.0.1:9000/obrazki/panel/' + pict_name)
            else:
                return render(request, '404.html')
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')