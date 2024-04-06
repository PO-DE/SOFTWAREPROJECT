from django.shortcuts import render
from management.package.models import Package

def index(request):
    try:
        package_alberta = Package.objects.get(pk=5)  # Replace with the actual ID
        package_toronto = Package.objects.get(pk=4)  # Replace with the actual ID
        package_mumbai = Package.objects.get(pk=7)  # Replace with the actual ID
    except Package.DoesNotExist:
        package_alberta = package_toronto = package_mumbai = None

        # Pass them to the context
    context = {
        'package_alberta': package_alberta,
        'package_toronto': package_toronto,
        'package_mumbai': package_mumbai,
    }

    return render(request, 'index.html', context)
    # return render(request, 'index.html')