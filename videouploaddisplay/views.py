from django.shortcuts import render

from djangovideouploaddisplay.settings import MEDIA_ROOT
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
import subprocess

@ensure_csrf_cookie
def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            handle_uploaded_file(file)
            return render(request, "upload-display-video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload-display-video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def do_check(request):
    subprocess.run(['python','./tf-pose-estimation/run_video.py','--model=mobilenet_thin','--resolution=272x480',
                    '--video=model.mp4','--type=model'], stdout=subprocess.PIPE)
    subprocess.run(
        ['python','./tf-pose-estimation/run_video.py','--model=mobilenet_thin','--resolution=272x480',
                    '--video=test.mp4','--type=test'], stdout=subprocess.PIPE)
    scMessage = '评分完成'
    return render(request, 'upload-display-video.html', {'scMessage' : scMessage})

def do_result(request):
    result = subprocess.run(['python', 'process.py'], stdout=subprocess.PIPE)
    result = str(result.stdout).split('\\')[0][2:]
    return render(request, 'upload-display-video.html',{'result': result})

def do_again(request):
    tips = '请再次上传文件'
    subprocess.run(
        ['rm' , 'model.txt'], stdout=subprocess.PIPE)
    subprocess.run(
        ['rm', 'test.txt'], stdout=subprocess.PIPE)
    return render(request, 'upload-display-video.html',{'result': tips})