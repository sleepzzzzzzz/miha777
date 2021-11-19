from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import InputForm
from .models import inputname
import json


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Take data from the initial form
            name_input = form.cleaned_data['name0']
            # Convert to json type
            text = json.dumps(name_input, ensure_ascii=False)
            # Create object
            inputname.objects.create(text=text, field='name0')

            # Loop take data from other form
            for count in range(1, len(request.POST) - 1):
                label = 'name' + str(count)
                input_value = request.POST[label]
                # Check for empty field
                if input_value:
                    text = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(label)
                    inputname.objects.create(text=text, field=field)
                count += 1

        return redirect(reverse('form_name:done'))


    else:
        form = InputForm()
        context = {
            'form': form
        }
    return render(request, 'form_name/index.html', context)


def done(request):
    # Take data from the db
    data = inputname.objects.all().values('id', 'field', 'text')
    json_list = list(data)
    context = {
        'json_list': json_list
    }
    return render(request, 'form_name/done.html',context)
# Create your views here.
