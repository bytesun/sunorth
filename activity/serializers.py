from rest_framework.serializers import (Serializer,ModelSerializer,)

from .models import (Activity)

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ('subject','description','start','end','organizer')