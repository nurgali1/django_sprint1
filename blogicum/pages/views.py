from django.shortcuts import render


def about(requests):
    return render(requests, 'pages/about.html')


def rules(requests):
    return render(requests, 'pages/rules.html')
