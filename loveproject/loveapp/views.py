from django.shortcuts import render
from .models import Couple
import random

def index(request):
    error = None
    all_couples = Couple.objects.all().order_by('-created_at')  # latest first

    if request.method == 'POST':
        name_a = request.POST.get('name_a', '').strip()
        name_b = request.POST.get('name_b', '').strip()
        photo_a = request.FILES.get('photo_a')
        photo_b = request.FILES.get('photo_b')

        if not name_a and not photo_a:
            error = "Please enter a name or upload a photo for Person A."
        elif not name_b and not photo_b:
            error = "Please enter a name or upload a photo for Person B."
        else:
            # Simple logic for love percentage
            percent = random.randint(50, 100)

            # Sentence / tips (you can expand these)
            sentence = f"{name_a or 'Person A'} & {name_b or 'Person B'}: {percent}%"
            tips = "💡 Keep loving and improving your relationship!"

            # Save to database including photos
            couple = Couple.objects.create(
                name_a=name_a if name_a else None,
                name_b=name_b if name_b else None,
                photo_a=photo_a if photo_a else None,
                photo_b=photo_b if photo_b else None,
                percent=percent,
                sentence=sentence,
                tips=tips,
                score=percent
            )

            return render(request, 'result.html', {
                'sentence': sentence,
                'percent': percent,
                'tips': tips,
                'score': percent,
                'all_couples': all_couples
            })

    return render(request, 'index.html', {
        'error': error,
        'all_couples': all_couples
    })
