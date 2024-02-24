from django.shortcuts import render , redirect

# Create your views here.# packages/views.py
from datetime import datetime
from rest_framework import viewsets, permissions
from .models import Package
from .forms import PackageForm , SignUpForm , SignInForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate ,logout
from django.views.generic import ListView , DetailView

def index(request):
    return render(request, 'index.html')
# class PackageView(ListView):
#     model = Post
@login_required()
def packages(request):
    form = PackageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        source=request.POST.get('source')
        destination=request.POST.get('destination')
        seats=request.POST.get('seats')
        room=request.POST.get('room')
        # hotels = request.POST.get('hotels')

        package=Package.objects.create(source=source, destination=destination, seats=seats, room =room,date = datetime.now())
        package.save()
    # if form.is_valid():
    #     form.save()
    # context = {'title': 'welcome', 'form': form}
    return render(request,'package.html')

# class PackageViewSet(viewsets.ModelViewSet):
#     queryset = Package.objects.all()
#     serializer_class = PackageSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = "__all__"
#     search_fields = "__all__"
#     def get_permissions(self):
#         if self.action == 'list':
#             permissions_classes = [permissions.AllowAny]
#         else:
#             permissions_classes = [permissions.IsAdminUser]
#         return [permission() for permission in permissions_classes]

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after signing up
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired URL name for the home page

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with your desired URL name for the home page
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})
@login_required(login_url='signin')
def logout(request):
    logout(request)
    return redirect('index')
# copy from chatgpt 24-02-2024
@login_required(login_url='signin')
def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

@login_required()
def package_detail(request, pk):
    package = Package.objects.get(pk=pk)
    return render(request, 'package_detail.html', {'package': package})

@login_required()
def package_create(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm()
    return render(request, 'package_form.html', {'form': form})