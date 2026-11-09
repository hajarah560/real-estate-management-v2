from django.shortcuts import render
from .models import Client, Employee, Land, Building, Lease, Payment


def dashboard(request):
    return render(request, 'realestate_dashboard.html', {
        'client_count': Client.objects.count(),
        'employee_count': Employee.objects.count(),
        'land_count': Land.objects.count(),
        'building_count': Building.objects.count(),
        'lease_count': Lease.objects.count(),
        'payment_count': Payment.objects.count(),
        'recent_payments': Payment.objects.select_related('client', 'employee').order_by('-id')[:5],
    })
