from django.shortcuts import render
from . import anfisa


def index(request):
    html = ''
    if request.method == 'POST':
        # извлекаем из POST-запроса вопрос пользователя
        query = request.POST['query']

        # допишите ваш код здесь
        answer = anfisa.process_query(query)

        # полученный из anfisa.py ответ оборачиваем в HTML-теги, будет нарядно
        html = f'<mark>{answer}</mark>'

    # подготовьте словарь context, чтобы вывести информацию в шаблон
    context = {
        'response': html,  # сюда передайте HTML-код с ответом Анфисы
        'where': request.path  # передаём абсолютный адрес страницы
    }

    # добавьте словарь context третьим аргументом
    return render(request, 'anfisa/index.html', context)


def about(request):
    # верните результат вызова функции render() с нужными аргументами
    return render(request, 'anfisa/about.html')
