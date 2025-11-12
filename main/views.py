from re import search

from django.shortcuts import render
from pyexpat.errors import messages

from main.models import Incorrect
from .models import *


def index_view(request):
    correct = None
    incorrects = None
    message = None
    search = request.GET.get('search')
    if search:
        search = search.lower()
        corrects = Correct.objects.filter(word=search)
        if corrects.exists():
            correct = corrects.first()
            incorrects = correct.incorrect_set.all()  # <-- to‘g‘ri nom
        else:
            incorrects = Incorrect.objects.filter(word=search)
            if incorrects.exists():
                incorrect = incorrects.first()
                correct = incorrect.correct
                incorrects = correct.incorrect_set.all()
            else:
                if 'x' not in search and 'h' not in search:
                    message = "So'z tarkibida h yoki x mavjud emas!"
                else:
                    message = "Afsus bunday so'z mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
        'search': search
    }
    return render(request, 'index.html', context)


