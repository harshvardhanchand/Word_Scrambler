from django.shortcuts import render
from .models import DictionaryWord
from .utils import find_matches

# Create your views here.


def index(request):
    return render(request, 'word_scrambler_app/index.html')

def search_results(request):
    word = request.GET.get('word')
    matches = find_matches(word, DictionaryWord.objects.all())
    context = {'word': word, 'matches': matches}
    return render(request, 'word_scrambler_app/search_results.html', context)