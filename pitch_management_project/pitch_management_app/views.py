# Create your views here.
import logging
from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import PitchForm
from .models import Pitch

log = logging.getLogger(__name__)


def pitchList(request):
    pitches = Pitch.objects.all()
    return render(request, "pitch-list.html", {"pitches": pitches})


def pitchCreate(request):
    if request.method == "POST":
        form = PitchForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("pitch-list")
            except:
                pass
    else:
        form = PitchForm()
    return render(request, "pitch-create.html", {"form": form})


def pitchUpdate(request, id):
    pitch = Pitch.objects.get(id=id)

    form = PitchForm(
        initial={
            "name": pitch.name,
            "location": pitch.location,
            "last_maintenance_date": pitch.last_maintenance_date,
            "next_maintenance_date": pitch.next_maintenance_date,
            "current_condition": pitch.current_condition,
            "weather": pitch.weather,
            "turf_type": pitch.turf_type,
        }
    )
    if request.method == "POST":
        form = PitchForm(request.POST, instance=pitch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect("/pitch_manage/pitch-list")
            except Exception as e:
                pass
    return render(request, "pitch-update.html", {"form": form})


def pitchDelete(request, id):
    pitch = Pitch.objects.get(id=id)
    try:
        pitch.delete()
    except:
        pass
    return redirect("/pitch_manage/pitch-list")


def get_weather_data(pitch_id):
    pitch = get_object_or_404(Pitch, id=pitch_id)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={pitch.location}&appid={settings.OPENWEATHERMAP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data


@csrf_exempt
@require_POST
def update_pitch_data_with_weather(request, pitch_id):
    pitch = get_object_or_404(Pitch, id=pitch_id)
    weather_data = get_weather_data(pitch_id)
    if weather_data:
        pitch.weather = weather_data.get("weather")[0].get("main")
        if pitch.weather == "Rain":
            if pitch.turf_type == "natural":
                maintence_day = 3
                condition = 3

            elif pitch.turf_type == "artificial":
                maintence_day = 5
                condition = 5

            elif pitch.turf_type == "hybrid":
                maintence_day = 4
                condition = 4

            pitch.next_maintenance_date = datetime.now() + timedelta(days=maintence_day)
            pitch.current_condition = condition
        else:
            pitch.next_maintenance_date = pitch.last_maintenance_date + timedelta(
                days=settings.REGULAR_MAINTENANCE_DAY
            )
        pitch.save()
        return JsonResponse({"message": "Pitch updated successfully"})
    else:
        return JsonResponse({"message": "something went wrong"})


def pitchlist(request):

    pitch = Pitch.objects.filter(next_maintenance_date__gte=datetime.now()).order_by(
        "next_maintenance_date"
    )
    context = {"pitches": pitch}
    return render(request, "pitchlist.html", context)
