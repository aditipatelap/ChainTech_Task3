import random

from django.shortcuts import render

def random_quote(request):
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Innovation distinguishes between a leader and a follower. – Steve Jobs",
        "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
        "Stay hungry, stay foolish. – Steve Jobs",
        "Design is not just what it looks like and feels like. Design is how it works. – Steve Jobs"
    ]
    quote = random.choice(quotes)
    context = {
        'quote': quote,
    }
    return render(request, 'myapp/index.html', context)