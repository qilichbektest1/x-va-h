from django.shortcuts import render
from main.models import Incorrect
from .models import Correct

def index_view(request):
    correct = None
    incorrects = None
    message = None
    query = request.GET.get('search')

    if query:
        query = query.lower()
        corrects = Correct.objects.filter(word=query)
        if corrects.exists():
            correct = corrects.first()
            incorrects = correct.incorrect_set.all()
        else:
            incorrects_qs = Incorrect.objects.filter(word=query)
            if incorrects_qs.exists():
                incorrect = incorrects_qs.first()
                correct = incorrect.correct
                incorrects = correct.incorrect_set.all()
            else:
                if 'x' not in query and 'h' not in query:
                    message = "So'z tarkibida h yoki x mavjud emas!"
                else:
                    message = "Afsus bunday so'z mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
        'search': query
    }
    return render(request, 'index.html', context)
