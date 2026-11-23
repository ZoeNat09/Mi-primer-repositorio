from django.http import HttpResponse

def saludo(request):#primera vista, se le puede asignar cualquier nombre
return HttpResponse("hola mundo")

