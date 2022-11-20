from django.shortcuts import render, HttpResponse

def home(request):
    html_response = "<h1>Mi Web Personal</h1>"
    for i in range(10):
        html_response += "<p>Esto es la portada</p>"
    return HttpResponse(html_response)

def about(request):
    return HttpResponse("""
                    <h1>Mi Web Personal</h1>
                    <h2>Acerca de</h2>
                    <p>Me llamo Héctor y me encanta Django!</p>
                    """)

