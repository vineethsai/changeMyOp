from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import hashlib
from django.contrib.auth.models import User
from .models import Like, Dislike, Opinion, Comment


def home(request):
    """
    routes to home page on GET request
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, "index.html", status=200)
    else:
        return HttpResponse("Method not allowed on /.", status=405)


def specificUser(request, user_id):
    """
    Displays a single user's information and their picture on GET request
    :param request: request object
    :param user_id: user_id provided by parent call
    :return:
    """
    if request.method == "GET":
        if request.user.is_authenticated:
            user = User.objects.get(pk=user_id)
            email = user.email.lower().encode()
            gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email).hexdigest()
            ops = Opinion.objects.get(author=user)
            total_likes = Like.objects.get(user=user)
            return HttpResponse([user, ops.text, total_likes, gravatar_url])
        else:
            return HttpResponseRedirect("/auth/signin")
    else:
        return HttpResponse("Method not allowed on main/users/.", status=405)


def opinions(request):
    """
    Displays a single user's information and their picture on GET request
    :param request: request object
    :param user_id: user_id provided by parent call
    :return:
    """
    if request.method == "GET":
        ops = Opinion.objects.all()
        likes = Like.objects.all()
        dislikes = Dislike.objects.all()
        return HttpResponse([ops, likes, dislikes])
    else:
        return HttpResponse("Method not allowed on main/users/.", status=405)

def specific_opinions(request, op_id):
    """
    Displays a single user's information and their picture on GET request
    :param request: request object
    :param user_id: user_id provided by parent call
    :return:
    """
    if request.method == "GET":
        try:
            ops = Opinion.objects.get(pk=op_id)
        except Opinion.DoesNotExist:
            return HttpResponse("Opinion does not exist", status=404)
        try:
            likes = Like.objects.get(opinion=ops) if Like.objects.get(opinion=ops) is not None else 0
            dislikes = Dislike.objects.get(opinion=ops) if Dislike.objects.get(opinion=ops) is not None else 0
            return HttpResponse([ops.text, likes, dislikes])
        except Dislike.DoesNotExist:
            likes = Like.objects.get(opinion=ops) if Like.objects.get(opinion=ops) is not None else 0
            return HttpResponse([ops.text, likes])
        except Like.DoesNotExist:
            dislikes = Dislike.objects.get(opinion=ops) if Dislike.objects.get(opinion=ops) is not None else 0
            return HttpResponse([ops.text, dislikes])
    else:
        return HttpResponse("Method not allowed on main/users/.", status=405)