from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Piss
import json
import zlib

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

            text = zlib.compress(text.encode())
            
            # Create an instance of the model with the submitted data
            new_entry = Piss(longitude=longitude, latitude=latitude, text=text)
            
            # Save the new entry to the database
            new_entry.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error_message': str(e)})

    return JsonResponse({'status': 'error'})

def decompress(str):
    try:
        d = zlib.decompress(str['text']).decode()
        str['text'] = d
        return str
    except:
        return str

def fetch_data(request):
    data = list(Piss.objects.values())
    decompressedData = [decompress(d) for d in data]  # Retrieve all data from the Piss model
    return JsonResponse({'data': decompressedData})