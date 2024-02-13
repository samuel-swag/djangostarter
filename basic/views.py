from django.shortcuts import render
from django.http import Http404
from .models import Computed

# Create your views here.

# Computation function
def compute(request, value):
    try:
        input = int(value)
        precomputed = Computed.objects.filter(input=input)
        if precomputed.count() != 0:  
            # This was already computed, so look up answer
            answer = precomputed[0].output
        else:
            # Compute the answer
            answer = input * input
            # Save it into the database
            computed = Computed(input=input, output=answer)
            computed.save()
    except:
        raise Http404(f"Invalid input: {value}")

    return render (
        request,
        "basic/compute.html",
        {
            'input': input,
            'output': answer
        }
    )