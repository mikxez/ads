from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad, Category
from .forms import AdForm, LoginForm, RegisterForm
from django.contrib.auth import login, logout

def ad_list(request):
    ads = Ad.objects.all()
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    if category_id:
        ads = ads.filter(category__id=category_id)

    if query:
        ads = ads.filter(title__icontains=query) | ads.filter(description__icontains=query)

    categories = Category.objects.all()

    context = {
        'ads': ads,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    }
    return render(request, 'ads/ad_list.html', context)

def ad_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})
def ad_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    ad = get_object_or_404(Ad, pk=pk, user=request.user)

    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form})

def ad_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    ad = get_object_or_404(Ad, pk=pk, user=request.user)

    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('ad_list')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ad_list')
    else:
        form = LoginForm()

    return render(request, 'ads/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('ad_list')
    else:
        return redirect('ad_list')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('ad_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ad_list')
    else:
        form = RegisterForm()

    return render(request, 'ads/register.html', {'form': form})