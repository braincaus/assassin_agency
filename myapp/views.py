from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Hit, Hitman, HitStatus


# Create your views here.


@login_required(login_url='/login/')
def index(request):
    hits = None
    if request.user.is_superuser:
        hits = Hit.objects.filter(status_id=1)
    elif request.user.hitman.active:
        if request.user.hitman.manager is None:
            hits = Hit.objects.filter(hitman__manager=request.user.hitman, status_id=1)
        else:
            hits = Hit.objects.filter(hitman=request.user.hitman, status_id=1)

    return render(request, 'myapp/index.html', locals())


def login_view(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['email'], password=data['password'])
        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'myapp/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login')


@login_required(login_url='/login/')
def create_new_hit_view(request):
    if request.method == 'GET':
        hitmen = Hitman.objects.filter(manager=request.user.hitman, active=True)
        status = HitStatus.objects.all()
        return render(request, 'myapp/hit_new.html', locals())
    elif request.method == 'POST':
        data = request.POST
        hitman = data['hitman']
        target = data['target']
        description = data['description']
        Hit.objects.create(hitman_id=hitman, target=target, description=description, status_id=1)
        return redirect('/')


@login_required(login_url='/login/')
def detail_hit_view(request, pk):
    if request.method == 'GET':
        hitmen = Hitman.objects.filter(active=True)
        status = HitStatus.objects.all()
        edit = True if request.user.is_superuser or request.user.hitman.is_manager else False
        if not request.user.is_superuser and request.user.hitman.is_manager:
            hitmen = hitmen.filter(manager=request.user.hitman)
        hit = get_object_or_404(Hit, pk=pk)
        return render(request, 'myapp/hit_detail.html', locals())
    elif request.method == 'POST':
        data = request.POST
        hitman = data.get('hitman', None)
        status = data['status']
        hit = get_object_or_404(Hit, pk=pk)
        if hitman:
            hit.hitman_id = hitman
        hit.status_id = status
        hit.save()
        return redirect('/')


@login_required(login_url='/login/')
def list_hitmen(request):
    if request.method == 'GET':
        hitmen = Hitman.objects.filter()
        if not request.user.is_superuser and request.user.hitman.is_manager:
            hitmen = hitmen.filter(manager=request.user.hitman)
        return render(request, 'myapp/list_hitman.html', locals())


@login_required(login_url='/login/')
def hitman_detail(request, pk):
    if request.method == 'GET':
        hitman = get_object_or_404(Hitman, pk=pk)
        return render(request, 'myapp/hitman_detail.html', locals())
    elif request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        status = data.get('status')
        hitman = get_object_or_404(Hitman, pk=pk)
        hitman.user.first_name = name
        hitman.user.username = email
        hitman.user.email = email
        hitman.user.save()
        hitman.active = True if status else False
        hitman.save()
        return redirect('/hitmen/')
