from django.urls import path

# ------------------------------------------------------------------------------
# temporary
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('🤨')
# ------------------------------------------------------------------------------

urlpatterns = [
    path('', hello_world, name='hello_world'),
]
