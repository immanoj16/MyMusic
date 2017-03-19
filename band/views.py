from django.shortcuts import render


def band(request, band_id):
    return render(request, 'band/band.html')
