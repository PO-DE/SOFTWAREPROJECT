from django.db.models import Q
from django.shortcuts import render , redirect
from datetime import datetime
from rest_framework import viewsets, permissions
from .models import Package, Booking
from .forms import PackageForm, SignUpForm, SignInForm, SearchForm, ForgotPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate ,logout
from .serializers import BookingSerializer
from django.http import HttpResponseForbidden
# ------------------------------------------------------
from django.shortcuts import render, get_object_or_404
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


@login_required()
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get_queryset(self):
        queryset = Booking.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = queryset.filter(
                Q(customer_name__icontains=query) | Q(customer_email__icontains=query)
            )
        return queryset

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
def Logout(request):
    logout(request)
    return redirect('index')

# @login_required(login_url='signin')
def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

# @login_required()
def package_detail(request, package_id):
    package = Package.objects.get(pk=package_id)

    destination = package.destination

    # dictionary used for list of images
    destination_images = {
        'Mumbai': ['mumbai1.jpg', 'mumbai2.jpg', 'mumbai3.jpg', 'mumbai4.jpg'],
        'Toronto': ['toronto1.jpg', 'toronto2.jpg', 'toronto3.jpg', 'toronto4.jpg'],
        'Vancouver': ['vancouver1.jpg', 'vancouver2.jpg', 'vancouver3.jpg', 'vancouver4.jpg'],
        'Newyork': ['newyork1.jpg', 'newyork2.jpg', 'newyork3.jpg', 'newyork4.jpg'],
        'Paris': ['paris1.jpg', 'paris2.jpg', 'paris3.jpg', 'paris4.jpg'],
        'Mississauga': ['mississauga1.jpg', 'mississauga2.jpg', 'mississauga3.jpg', 'mississauga4.jpg'],
        'Calgary': ['calgary1.jpg', 'calgary2.jpg', 'calgary3.jpg', 'calgary4.jpg'],
        'Alberta': ['alberta1.jpg', 'alberta2.jpg', 'alberta3.jpg', 'alberta4.jpg'],
        'Regina': ['regina1.jpg', 'regina2.jpg', 'regina3.jpg', 'regina4.jpg'],
        'Hamilton': ['hamilton1.jpg', 'hamilton2.jpg', 'hamilton3.jpg', 'hamilton4.jpg']
    }

    # Check if the destination is in the dictionary
    if destination in destination_images:
        image_list = destination_images[destination]
        context = {'package': package, destination.lower() + '_images': image_list}
    else:
        # Handle other destinations
        context = {'package': package}

    return render(request, 'package_detail.html', context)


@login_required
def package_create(request):
    if not request.user.is_superuser and not (
            request.user.has_perm('management.view_package')
            or request.user.has_perm('management.add_package')
    ):
        return HttpResponseForbidden("You are not authorized to view this page")
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm()
    return render(request, 'package_form.html', {'form': form})


def search_results(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = results = Package.objects.filter(destination__icontains=query) | Package.objects.filter(source__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

def forgotpassword(request):
    if request.method == 'POST':
        # Handle form submission if needed
        pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgotpassword.html', {'form': form})


