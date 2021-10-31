from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Goal
# from .serializers import GoalSerializer
# from rest_framework import viewsets


# class GoalViewSet(viewsets.ModelViewSet):
#     queryset = Goal.objects.all()
#     serializer_class = GoalSerializer


def goali_app_view(request):
    all_goals = Goal.objects.all()
    return render(request, 'goal_list.html', {'all_goals': all_goals})


def add_goal_view(request):
    name = request.POST['name']
    description = request.POST['description']
    new_goal = Goal(name=name, description=description)
    new_goal.save()
    return HttpResponseRedirect('/goali_app/')


def delete_goal_view(request, goal_id):
    removed_goal = Goal.objects.get(id=goal_id)
    removed_goal.delete()
    return HttpResponseRedirect('/goali_app/')
    
