from django.shortcuts import render, redirect
from obrazkiapp.models import Picture, Rectangle, Tag
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


# Main page.
def show_main(request):
    page_number = request.GET.get("page", 1)
    tags = Tag.objects.get_queryset()
    if request.method == 'POST':
        merged_tags = ""
        order = request.POST.get("Radio", "id")
        if order == 'None':
            order = "id"
        tags = []
        for tag in Tag.objects.get_queryset():
            if tag.name in request.POST:
                tags.append(tag.name)
        if len(tags) == 0:
            tags = [tag.name for tag in Tag.objects.get_queryset()]
        else:
            for tag in tags:
                merged_tags += tag + "."
    else:
        order = request.GET.get("order", "id")
        merged_tags = request.GET.get("merged_tags", "")
        if len(merged_tags) > 0:
            tags = []
            word = ""
            for sign in merged_tags:
                if sign != ".":
                    word = word + sign
                else:
                    tags.append(word)
                    word = ""
        else:
            tags = [tag.name for tag in Tag.objects.get_queryset()]
    pics_list = []
    for pict in Picture.objects.get_queryset().order_by(order):
        if any(tag.name in tags for tag in Tag.objects.filter(picture=pict)):
            pics_list.append(pict)

    paginator = Paginator(pics_list, 6)
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        return render(request, 'Obrazkolandia_out.html', {'all_pics': page_obj, 'order': order, 'all_tags': Tag.objects.get_queryset() , 'merged_tags': merged_tags})
    else:
        return render(request, 'Obrazkolandia.html', {'all_pics': page_obj, 'order': order, 'all_tags': Tag.objects.get_queryset() , 'merged_tags': merged_tags})


# Login.
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


# Logout.
def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:9000/obrazki')


# Shows control panel of user.
def show_panel(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            merged_tags = ""
            order = request.POST.get("Radio", "id")
            if order == 'None':
                order = "id"
            tags = []
            for tag in Tag.objects.get_queryset():
                if tag.name in request.POST:
                    tags.append(tag.name)
            if len(tags) == 0:
                tags = [tag.name for tag in Tag.objects.get_queryset()]
            else:
                for tag in tags:
                    merged_tags += tag + "."
        else:
            order = request.GET.get("order", "id")
            merged_tags = request.GET.get("merged_tags", "")
            if len(merged_tags) > 0:
                tags = []
                word = ""
                for sign in merged_tags:
                    if sign != ".":
                        word = word + sign
                    else:
                        tags.append(word)
                        word = ""
            else:
                tags = [tag.name for tag in Tag.objects.get_queryset()]
        pics_list = []
        print(tags)
        for pic in Picture.objects.get_queryset().order_by(order):
            if request.user in pic.users.all() and any(tag.name in tags for tag in Tag.objects.filter(picture=pic)):
                pics_list.append(pic)
        paginator = Paginator(pics_list, 6)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        print("własna!")
        return render(request, 'Obrazkolandia_własna.html', {'all_pics': page_obj, 'order': order, 'all_tags': Tag.objects.get_queryset() , 'merged_tags': merged_tags})
    else:
        return redirect('login')


# Main page of picture.
def pict_site(request, pict_name):
    if Picture.objects.filter(name=pict_name).exists():
        pict = Picture.objects.filter(name=pict_name).get()
        return render(request, 'pict.html', {'pict': pict})
    else:
        return render(request, '404.html')


# Add new rectangle.
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
                return render(request, 'pict_modify.html', {'pict': pict})
        else:
            return render(request, '404.html')
    else:
        return redirect('login')



# Deletion of rectangle.
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
                return redirect('http://127.0.0.1:9000/obrazki/panel/' + pict_name)
            else:
                return render(request, '404.html')
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')