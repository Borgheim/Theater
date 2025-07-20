from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Actor, Performance, Stage, Director, Casting
from django.db.models import Q, Value
from django.db.models.functions import Concat
from collections import defaultdict
from .forms import ActorForm

@login_required
def search(request):
    """Search for performances, actors, directors, and stages."""
    query_actor = request.GET.get('actor', '').strip()
    query_performance = request.GET.get('performance', '').strip()
    query_director = request.GET.get('director', '').strip()
    stage_name = request.GET.get('stage', '').strip()

    performances = Performance.objects.all()
    actors = []
    directors = []
    actor_roles = defaultdict(list)

    filters = Q()


    if query_actor:
        parts = query_actor.split()
        if len(parts) == 2:
            actors = Actor.objects.filter(
                Q(first_name__icontains=parts[0], last_name__icontains=parts[1]) |
                Q(first_name__icontains=parts[1], last_name__icontains=parts[0])
            )
        else:
            actors = Actor.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name')
            ).filter(full_name__icontains=query_actor)

        filters &= Q(actors__in=actors)


    if query_performance:
        filters &= Q(title__icontains=query_performance)


    if query_director:
        parts = query_director.split()
        if len(parts) == 2:
            directors = Director.objects.filter(
                Q(first_name__icontains=parts[0], last_name__icontains=parts[1]) |
                Q(first_name__icontains=parts[1], last_name__icontains=parts[0])
            )
        else:
            directors = Director.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name')
            ).filter(full_name__icontains=query_director)

        filters &= Q(director__in=directors)


    if stage_name:
        filters &= Q(stage__name__icontains=stage_name)

    performances = performances.filter(filters).distinct()

    if actors:
        castings = Casting.objects.select_related('actor', 'performance', 'role').filter(actor__in=actors)
        for casting in castings:
            actor_roles[casting.actor.id].append((casting.performance, casting.role))

    return render(request, 'theatre/search.html', {
        'query_actor': query_actor,
        'query_performance': query_performance,
        'query_director': query_director,
        'stage_name': stage_name,
        'performances': performances,
        'actors': actors,
        'directors': directors,
        'actor_roles': actor_roles,
    })

@login_required
def add_actor(request):
    """Add a new actor via form."""
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm()
    return render(request, 'theatre/add_actor.html', {'form': form})


def actor_list(request):
    """Display a list of all actors."""
    actors = Actor.objects.all()
    return render(request, 'theatre/actor_list.html', {'actors': actors})

@login_required
def director_list(request):
    """Display a list of all directors."""
    directors = Director.objects.all().order_by('last_name', 'first_name')
    return render(request, 'theatre/directors.html', {'directors': directors})



