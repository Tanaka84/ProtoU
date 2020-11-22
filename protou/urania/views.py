from django.shortcuts import render, reverse
from django.http import HttpResponse
import random
from django.db.models import Count
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView
from .models import Word, Voter, Vote
# Create your views here.

class CreateWord(CreateView):
    model = Word
    fields = ['word', 'emocion']
    template_name = 'urania/word_form.html'

    def get_success_url(request):
        return reverse('new_word')

def votando(request):
    if request.method != "POST":
        #get queryset
        qs = Word.objects.annotate(num_vote=Count('vote')).order_by('num_vote')[:10]
        #pass it as a context
        cxt = {'words': qs}
        #Save the word list sent to the user
        word_list_for_user = [str(word.id) for word in qs]
        string_of_words = (',').join(word_list_for_user)
        try:
            voter = Voter(user = request.user, attempts = 0 , current_words = string_of_words)     
            voter.save()
            return render(request, 'urania/word_vote.html', cxt )
        except:
            Voter.objects.filter(user = request.user).update(current_words = string_of_words)
            return render(request, 'urania/word_vote.html', cxt )
    else:
        results = request.POST['votos'].split(",")
        results = [x.split(':') for x in results]
        ##Get voted words
        list_of_voted_words = [x[0] for x in results]
        string_of_voted_words = (',').join(list_of_voted_words)
        if string_of_voted_words ==  Voter.objects.get(user = request.user).current_words:
            for result in range(len(results)):
                vote = Vote(vote = results[result][1], user = request.user, word = Word.objects.get(id = results[result][0])) 
                Voter.objects.filter(user = request.user).update(attempts = Voter.objects.get(user = request.user).attempts+1, current_words = "")
                vote.save()
                return HttpResponse("<body>gracias jalabola!</body>")
        else:
            Voter.objects.filter(user = request.user).update(attempts = Voter.objects.get(user = request.user).attempts+1, current_words = "")
            return HttpResponse("<body>NO ME VAS A FANTEAR!</body>")
        