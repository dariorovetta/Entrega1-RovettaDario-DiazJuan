from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("Login")
    context = {}
    return render(request, "appChats/chatPage.html", context)
