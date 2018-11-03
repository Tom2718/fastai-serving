from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadFileForm
import datamodels

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img_name = save_image(request.FILES['image'])
            pred, prob = predict(img_name)
            return render(request, 'web/results.html', {'pred': pred, 'prob': prob})
    form = UploadFileForm()
    return render(request, 'web/index.html', {'form': form})

# Should use separate view
def results(request):
    return render(request, 'web/results.html', {'result': result})