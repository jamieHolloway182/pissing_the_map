from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Piss
import json

def index(request):
    return render(request, "pissmap/index.html")

@csrf_exempt
def add_entry(request):
    if request.method == 'POST':
        try:
            # Extract data from the POST request
            data = json.loads(request.body.decode('utf-8'))
            
            text = data.get('text', '')
            longitude = data.get('longitude', '')
            latitude = data.get('latitude', '')
            
            # Create an instance of the model with the submitted data
            new_entry = Piss(longitude=longitude, latitude=latitude, text=text)
            
            # Save the new entry to the database
            new_entry.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error_message': str(e)})

    return JsonResponse({'status': 'error'})

def fetch_data(request):
    data = list(Piss.objects.values())  # Retrieve all data from the Piss model
    return JsonResponse({'data': data})