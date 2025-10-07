from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Computed
from django.utils import timezone

# Create your views here.

# Computation function
def compute(request, value):
    try:
        input = int(value)
        precomputed = Computed.objects.filter(input=input)
        if precomputed.count() == 0:  # The answer for this input has not been computed
            # Compute the answer
            answer = input * input
            time_computed = timezone.now()
            # Save it into the database
            computed = Computed(
                input=input, 
                output=answer,
                time_computed=time_computed
            )
            computed.save() # Store it into the database
        else: 
            computed = precomputed[0] 
        
        return render (
            request,
            "basic/compute.html",
            {
                'input': input,
                'output': computed.output,
                'time_computed': computed.time_computed.strftime("%m-%d-%Y %H:%M:%S UTC")
            }
        )
    except:
        raise Http404(f"Invalid input: {value}")


def isPrime(request, value):
    try:
        input = int(value)
        divisor = None
        lessthantwo = False
        if input < 2:
            lessthantwo = True
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(input**0.5) + 1):
                if input % i == 0:
                    is_prime = False
                    divisor = i
                    break
        
        return render(
            request,
            "basic/isPrime.html",
            {
                'lessthantwo': lessthantwo,
                'input': input,
                'divisor': divisor,
                'is_prime': is_prime
            }
        )
    except:
        raise Http404(f"Invalid input: {value}")



def evenOdd(request):
    if request.method == 'GET':
        return render(request, "basic/evenodd.html", {})
    else:
        number = int(request.POST['number'])
        return HttpResponse(f"The number is {'even' if number % 2 == 0 else 'odd'}")

# def evenOdd(request, value):
#     try:
#         input = int(value)
#         result = False
#         if input % 2 == 0:
#             result = True
        
#         return render(request, {
#             'result': result,
#             'value': value
#         })
#     except:
#         raise Http404(f"Invalid input: {value}")