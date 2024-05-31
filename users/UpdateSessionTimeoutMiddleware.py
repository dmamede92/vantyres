from django.utils import timezone


class UpdateSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Define o tempo de expiração da sessão se ainda não estiver definido
            if 'last_activity' not in request.session:
                request.session['last_activity'] = timezone.now().isoformat()

            # Atualiza o tempo de expiração da sessão em cada solicitação
            request.session['last_activity'] = timezone.now().isoformat()

        response = self.get_response(request)
        return response
