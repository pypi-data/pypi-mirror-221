from django.db import models
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from annotation.models import Author, Book
from queryset_annotations.base import BaseAnnotation, BaseContextManager
from queryset_annotations.drf.views import AnnotatedQuerysetMixin
from queryset_annotations.proxy.model import BaseProxyModel


class BookCountAnnotation(BaseAnnotation):
    name = "book_count"
    output_field = models.IntegerField()

    def get_expression(self, *, context_manager: BaseContextManager = None):
        return models.Count("books", distinct=True)


class AuthorProxyModel(BaseProxyModel):
    book_count = BookCountAnnotation()

    class Meta:
        model = Author


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AuthorProxyModel
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorViewSet(AnnotatedQuerysetMixin, ModelViewSet):
    annotation_context_class = BaseContextManager
    annotated_model = AuthorProxyModel
    serializer_class = AuthorSerializer

    def get_queryset(self):
        context_manager = self.annotation_context_class(self.get_serializer_context())
        return self.queryset.get_annotated_queryset(context_manager=context_manager)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
