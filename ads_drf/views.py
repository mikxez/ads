from rest_framework import generics, permissions
from app.models import Ad, Category
from .serializers import AdSerializer, CategorySerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdListApiView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Ad.objects.all()
        category = self.request.query_params.get('category')
        query = self.request.query_params.get('q')

        if category:
            queryset = queryset.filter(category__id=category)
        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(description__icontains=query)

        return queryset


class AdDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
