from .models import AgenceInfo


def agence_info(request):
    agence = AgenceInfo.objects.first()
    return {'agence': agence}
