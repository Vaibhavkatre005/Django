from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import job_post


job_title=[
    'Job 01',
    'job 02',
    'Job 03'
]
job_discription=[
    'This is the job discription for Job 01',
    'This is the job discription for Job 02',
    'This is the job discription for Job 03'
]
class TempValue:
    value=50
    num=12
 
# def hello(request):
#     template=loader.get_template('app/hello.html')
#     list=['first_item', 'second_item']
#     temp=TempValue()
#     context={'name': 'Django', 'list_item': list, 'temp_value': temp}
#     return HttpResponse(template.render(context, request))

def hello(request):
    # template=loader.get_template('app/hello.html')
    list=['first_item', 'second_item']
    temp=TempValue()
    isAuth=False
    context={'name': 'Django', 'list_item': list,'isAuth':isAuth , 'temp_value': temp}
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)




# Create your views here.
def home_page(request):
    # output=''
    # for i in job_title:
    #     job_id=job_title.index(i)
    #     # url=f'job/{str(job_id)}'
    #     url=(reverse('job_url', args=(job_id, )))
    #     output+=(f'<h1><a href={url}> {i}</a></h1>      <h3>{job_discription[job_id]}</h3>')
        
    # return HttpResponse(f"{output}")
    # # return HttpResponse("<h1>Hello World</h1><ul><li> J1 </li> <li>J2</li></ul>")
    jobs=job_post.objects.all()
    context={'jobs':jobs}
    return render(request, "app/index.html", context)
   

# def jobPage(request, id):
#     # print(id)
#     # id=id+1
#     if id > 2:
#         return redirect(reverse('home_page'))
#     # print(type(id))
#     # a=('this is a job page ',id)
#     # link= 'https://www.google.com'


#     return_html=f'<h1>{job_title[id-1]}</h1> <h3>{job_discription[id-1]}</h3>'
#     return HttpResponse(return_html)

def jobPage(request, id):
    jobs=job_post.objects.get(id=id )
    try:
        # return_html=f'<h1>{job_title[id-1]}</h1> <h3>{job_discription[id-1]}</h3>'
        # return HttpResponse(return_html)

        #old method
        #context={"job_title":job_title[id],'job_description':job_discription[id]}
        #return render(request, 'app\job_details.html', context)

        #fetching from DB
        context={"jobs":jobs}
        return render(request, 'app\job_details.html', context)
    except:
        return HttpResponseNotFound("Not found")

    
