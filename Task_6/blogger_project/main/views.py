from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .data import BloggersData  # Імпортуємо наш клас з даними

# Допоміжна функція для створення HTML-таблиці (вимога завдання)
def render_table(data_dict):
    rows = ""
    for key, value in data_dict.items():
        rows += f"<tr><td style='padding:5px; border:1px solid #ccc'><b>{key}</b></td><td style='padding:5px; border:1px solid #ccc'>{value}</td></tr>"
    return f"<table style='border-collapse: collapse; width: 50%;'>{rows}</table>"

# 1. Головна сторінка [cite: 485]
def home(request):
    html = """
    <h1>Світ Блогерів</h1>
    <p>Ласкаво просимо на інформаційну платформу!</p>
    <a href='/bloggers/'>Переглянути список блогерів</a> <br>
    <a href='/news/'>Новини (Тест переадресації)</a>
    """
    return HttpResponse(html)

# 2. Список профілів (Таблиця з посиланнями) [cite: 486, 508-511]
def blogger_list(request):
    bloggers = BloggersData.get_all()
    rows = ""
    for b in bloggers:
        # Ім'я є посиланням на детальну сторінку
        link = f"<a href='/bloggers/{b['id']}/'>{b['name']}</a>"
        rows += f"""
        <tr>
            <td style='border:1px solid black; padding:10px'>{link}</td>
            <td style='border:1px solid black; padding:10px'>{b['category']}</td>
        </tr>
        """
    
    html = f"""
    <h1>Наші Блогери</h1>
    <table style='border-collapse: collapse; width: 60%; border: 1px solid black;'>
        <tr style='background-color: #f2f2f2;'>
            <th style='padding:10px; text-align:left'>Ім'я</th>
            <th style='padding:10px; text-align:left'>Категорія</th>
        </tr>
        {rows}
    </table>
    <br><a href='/'>На головну</a>
    """
    return HttpResponse(html)

# 3. Деталі профілю [cite: 487]
def blogger_detail(request, id):
    blogger = BloggersData.get_by_id(id)
    
    # Обробка 404 помилки [cite: 502]
    if blogger is None:
        raise Http404("Блогера з таким ID не знайдено :(")

    table = render_table(blogger)
    html = f"""
    <h1>Профіль: {blogger['name']}</h1>
    {table}
    <br>
    <a href='/bloggers/'>Назад до списку</a>
    """
    return HttpResponse(html)

# 4. Новини з переадресацією [cite: 501]
def news(request):
    # Завдання вимагає переадресацію на головну
    return HttpResponseRedirect("/")