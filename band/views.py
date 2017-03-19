from django.shortcuts import render
from models import Band


def band(request, band_id):
    band = Band.objects.get(pk=band_id)
    return render(request, 'band/band.html', {'band': band})
