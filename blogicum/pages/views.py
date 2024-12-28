from django.shortcuts import render


# Обработка ошибки 404
def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


# Обработка ошибки 403
def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


# Обработка ошибки 500
def internal_server_error(request):
    return render(request, 'pages/500.html', status=500)
