from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_toko': 'Indo Shop',
        'npm' : '2406410494',
        'name': 'Edlyn Marva    ',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)