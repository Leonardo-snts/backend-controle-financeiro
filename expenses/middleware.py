# expenses/middleware.py
def debug_middleware(get_response):
    def middleware(request):
        # Imprimir informações úteis para depuração
        print("Debugging Middleware Ativado")
        print("FILES RECEBIDOS:", request.FILES)
        print("POST DATA:", request.POST)
        print("CONTENT-TYPE:", request.content_type)
        response = get_response(request)
        return response
    return middleware
