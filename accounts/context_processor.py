from .models import Profile

def links(request):
    if request.user.is_authenticated:
        pro_obj = Profile.objects.get(user=request.user)
        pic = pro_obj.image
        return {'pic':pic}
    return {}