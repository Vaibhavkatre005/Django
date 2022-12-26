from django.shortcuts import render

# Create your views here.
def subscribe(request):
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']

        print("POST REQUEST, Name: ",fname,lname)
        if fname=='':
            fnamereq="first name required"

    context={'fnamereq': fnamereq}
    return render(request, 'subscribe/subscribe.html', context)