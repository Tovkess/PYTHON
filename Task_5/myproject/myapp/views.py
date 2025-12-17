from django.http import HttpResponse

def my_table(request):
    html = """
    <html>
    <head><title>Завдання 5</title></head>
    <body>
        <h1>Інформація про студента</h1>
        <table border="1" style="border-collapse: collapse; width: 50%;">
            <tr>
                <th style="padding: 10px; background-color: #ddd;">Параметр</th>
                <th style="padding: 10px; background-color: #ddd;">Значення</th>
            </tr>
            <tr>
                <td style="padding: 10px;">Прізвище та Ім'я</td>
                <td style="padding: 10px;">Гордієнко Андрій</td>
            </tr>
            <tr>
                <td style="padding: 10px;">Група</td>
                <td style="padding: 10px;">КН-31</td>
            </tr>
            <tr>
                <td style="padding: 10px;">Курс</td>
                <td style="padding: 10px;">Python Web (Django)</td>
            </tr>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)