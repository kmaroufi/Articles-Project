class CreateOrUpdateModelMixin:
    def create_or_update(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Exception:
            return self.create(request, *args, **kwargs)