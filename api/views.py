from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.db.models import Prefetch
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404

from api.generics import CreateOrUpdateAPIView
from api.mixins import CreateOrUpdateModelMixin
from .serializers import *


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return self.queryset.prefetch_related(Prefetch("ratings",
                                                       queryset=ArticleRating.objects.filter(
                                                           user=self.request.user if type(
                                                               self.request.user) is not AnonymousUser else None)))


class ArticleRatingCreateOrUpdate(LoginRequiredMixin, CreateOrUpdateAPIView):
    queryset = ArticleRating.objects.select_for_update()
    serializer_class = ArticleRatingSerializer
    lookup_field = "article_id"

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg], 'user': self.request.user}
        print(filter_kwargs)
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
