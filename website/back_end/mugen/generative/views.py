from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import GenerateAudioForm
from .models import GenerateAudioModel
import socket, datetime, os

region, temp, ip, time_now = '', '', '', ''

# Create your views here.
@csrf_protect
def generate_music(request):
    form = GenerateAudioForm()
    global region, temp, ip, time_now
    if request.method == 'POST':
        form = GenerateAudioForm(request.POST)
        
        if form.is_valid():
            from generative.final import main
            region = form.cleaned_data['region']
            region = str(region)
            temp = form.cleaned_data['temp']
            temp = float(temp)
            ip = socket.gethostbyname(socket.gethostname())
            time_now = datetime.datetime.now()
            
            main(region, temp)
            GenerateAudioModel(region=region, temp=temp, ip_address=ip, time=time_now).save()
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if os.path.isfile(os.path.join(BASE_DIR, 'music.mid')):
                pass
            
        # return HttpResponse(f'{region=}\n{temp=}\n{ip=}\n{time_now=}')
            
    return render(request, 'generative/index.html', dict(form=form, region=region, temp=temp, ip=ip, time=time_now))

def output(request):
    if request.method == 'POST':
        region, temp, ip, time_now = '', '', '', ''
    return HttpResponse(f'{region=}\n{temp=}\n{ip=}\n{time_now=}')