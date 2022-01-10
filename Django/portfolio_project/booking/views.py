#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#index
#create
#update
#delete
#get_by_id
# class index(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/index.html'
#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})
# class list_all_tutorials(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/tutorial_list.html'
#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})

def index(request):

    #add logic to get all booking and return it instead of the static message
    #refer to nucamp tutrial appl file the code might hielp
    queryset = Tutorial.objects.all()
        # return Response({'tutorials': queryset})
    return HttpResponse({'tutorials': queryset})