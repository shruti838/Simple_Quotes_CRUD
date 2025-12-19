from django.shortcuts import render
from django.conf import settings
from .models import Quote
import os

def home(request):
    print("=== DEBUG START ===")
    print("DATABASE PATH:", settings.DATABASES['default']['NAME'])
    print("DB EXISTS:", os.path.exists(settings.DATABASES['default']['NAME']))
    print("QUOTES IN DB:", list(Quote.objects.all()))
    print("=== DEBUG END ===")
    return render(request, 'quotes/home.html', {'quotes': Quote.objects.all()})
