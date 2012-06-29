from annoying.decorators import render_to
from contacts.models import PersonalInfo


@render_to('contacts.html')
def contacts(request):
    try:
        contact_info = PersonalInfo.objects.get(id='1')
    except PersonalInfo.DoesNotExist:
        contact_info = None
    return {'contact_info': contact_info}
