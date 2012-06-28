import main.settings as django_settings

def settings(request):
    """
    Context processor that adds django.settings to the context
    """    
    return {'settings': django_settings}