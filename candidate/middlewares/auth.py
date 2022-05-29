from django.shortcuts import redirect


# Middleware for Candidate Model.
def Cauthmiddleware(get_response):
    def middleware(request):
        return_url = request.META['PATH_INFO']
        if not request.session.get('cand_id'):
            return redirect(f'login-candidate?return_url={return_url}')
        response = get_response(request)
        return response

    return middleware