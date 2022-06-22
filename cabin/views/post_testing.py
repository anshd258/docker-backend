from django.shortcuts import render,redirect


def PostTesting(request):
    return render(request, 'post_testing.html')
