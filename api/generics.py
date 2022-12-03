from rest_framework import mixins, generics

from api.mixins import CreateOrUpdateModelMixin


class CreateOrUpdateAPIView(CreateOrUpdateModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create_or_update(request, *args, **kwargs)
