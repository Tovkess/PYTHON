from django.http import HttpResponse

def list_singers():
    return [
        {'id': 1, 'name': 'Океан Ельзи', 'genre': 'Рок', 'lead_singer': 'Святослав Вакарчук'},
        {'id': 2, 'name': 'Бумбокс', 'genre': 'Хіп-хоп', 'lead_singer': 'Андрій Хливнюк'},
        {'id': 3, 'name': 'DZIDZIO', 'genre': 'Поп', 'lead_singer': 'Михайло Хома'},
        {'id': 4, 'name': 'ТНМК', 'genre': 'Хіп-хоп', 'lead_singer': 'Фоззі'},
        {'id': 5, 'name': 'Тартак', 'genre': 'Рок', 'lead_singer': 'Сашко Положинський'}
    ]

def popular_singers(request):
    html = "<h1>Популярні співаки України</h1><ul>"
    for s in list_singers():
        # Зверніть увагу: посилання залишається тим самим
        html += f"<li><a href='/singer/?id={s['id']}'>{s['name']}</a> - {s['genre']}</li>"
    html += "</ul>"
    return HttpResponse(html)

def singer_card(request):
    singer_id = request.GET.get('id')
    if singer_id:
        singer_id = int(singer_id)
        singer = next((s for s in list_singers() if s['id'] == singer_id), None)
        if singer:
            return HttpResponse(f"<h1>{singer['name']}</h1><p>Жанр: {singer['genre']}</p><p>Вокаліст: {singer['lead_singer']}</p><br><a href='/'>Назад</a>")
    return HttpResponse("Співака не знайдено")