from django.shortcuts import render , redirect

# Create your views here.# packages/views.py
from datetime import datetime
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Package
from .serializers import PackageSerializer
from .forms import PackageForm , SignUpForm , SignInForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, 'index.html')
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

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
    search_fields = "__all__"
    def get_permissions(self):
        if self.action == 'list':
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [permissions.IsAdminUser]
        return [permission() for permission in permissions_classes]

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
# def signup_success(request):

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