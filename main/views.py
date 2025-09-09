from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'ElevenKick',
        'name': 'Flora Cahaya Putri',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)