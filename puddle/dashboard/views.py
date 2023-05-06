from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item

# Create your views here.


@login_required
def index(request):
    user = request.user
    items = Item.objects.filter(created_by=user)

    return render(request, 'dashboard/index.html', {
        'items': items,
        'user': user
    })
