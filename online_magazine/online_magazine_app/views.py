from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

from online_magazine_app.models import UserDetails, Article, UserLike
from .forms import CustomUserCreationForm,CustomAuthenticationForm, PublishArticleForm, UserLikeForm

def home(request):
    return render(request, 'templates/home.html',{})

def user_profile(request):
    user = request.user
    return render(request, 'templates/user_profile.html',{'user':user})


@csrf_exempt
def register(request):
    data = json.loads(request.body.decode('utf-8'))

    if request.method == 'POST':
        form = CustomUserCreationForm(data)

        if form.is_valid():
            user_details = UserDetails(
                username = form.cleaned_data['username'],
                user_id = form.cleaned_data['user_id'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                bio = form.cleaned_data['bio']
            )

            user_details.save()
           # return redirect('login')  
            return JsonResponse({'success': True, 'message': 'Registration successful'})

    else:
        print("Form is not valid.")
        form = CustomUserCreationForm()
        return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

    #return render(request, 'templates/register.html', {'form': form})

@csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
        form = CustomAuthenticationForm(data)
        if form.is_valid():
            user_details = form.cleaned_data
            return JsonResponse({'success': True, 'username': user_details.username})
        else:
            return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)
    else:
        form = CustomAuthenticationForm()

    #return render(request, 'templates/login.html',{'form': form})
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=400)   

@csrf_exempt
def publish(request, user_id):
    data = json.loads(request.body.decode('utf-8'))
    form = PublishArticleForm(data)

    if form.is_valid():
            # Get the form data
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            date = form.cleaned_data['date']
            author_id = form.cleaned_data['author_id']
            author = UserDetails.objects.get(user_id=author_id)

            # Save the data to the database
            Article.objects.create(
                title=title,
                content=content,
                publication_date=date,
                author_id=author.user_id
            )

            # Redirect to a success page or do something else
            #return redirect('user_profile')
            return JsonResponse({'success': True})
    #return render(request, 'templates/publish.html', {'user_id': user_id})
    return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)

def search(request):
    searchstring = request.GET.get('searchstring', '')
    search_type = request.GET.get('type','')

    if search_type == 'title':
        search_results = Article.objects.filter(title__icontains=searchstring)
    elif search_type == 'author':
        user_details_queryset = UserDetails.objects.filter(username__icontains=searchstring)
        search_results = Article.objects.filter(author_id__in=user_details_queryset.values('user_id'))
    else:
        search_results=[]    

    #return render(request, 'search_results.html', {'query': request.GET.get('query', ''), 'results': search_results, 'search_type': search_type})
    results_list = [{'title': article.title, 'author': article.author.username, 'userid': article.author_id, 'content': article.content} for article in search_results]
    return JsonResponse({'query': searchstring, 'results': results_list, 'search_type': search_type})

def myarticle(request, user_id):
    articles = Article.objects.filter(author_id=user_id)

    articles_list = []
    for article in articles:
        likes_count = UserLike.objects.filter(article_id=article.id).count()

        articles_data = {
              'title': article.title,
              'content': article.content,
              'publication_date': article.publication_date.isoformat(), 
              'author': article.author.username,
              'categories': [], 
              'likes': likes_count  
            }
        articles_list.append(articles_data)

    return JsonResponse({'articles': articles_list})
    
@csrf_exempt 
def add_like(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
        form = UserLikeForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors.as_json()}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)    



