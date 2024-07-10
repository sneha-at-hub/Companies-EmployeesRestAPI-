from django.http import JsonResponse, HttpResponse

def home_page(request):
    print("Home Page")
    friends = [
        'Diwash',
        'Smriti',
        'Srishak'
    ]
    
    return JsonResponse(friends, safe=False)