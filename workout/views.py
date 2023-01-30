from django.shortcuts import render
from .forms import PlanForm
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.


def Plan(request):
    """ View to return to the workout request page."""
    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone_number': request.POST['phone_number'],
            'email_address': request.POST['email_address'],
            'plan_type': request.POST['plan_type'],
            'your_goal': request.POST['your_goal'],

        }
        form = PlanForm(form_data)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    "Thanks for submitting your Workout Plan Query." +
                    "One of our Personal Trainer will contact you withing 3 days")
            except ValidationError as e:
                messages.error(request, e.message)

    form = PlanForm()
    context = {
        'form': form,
    }
    return render(request, 'workout/workout.html', context)
