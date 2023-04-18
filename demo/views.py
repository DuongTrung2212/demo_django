from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import Course, Lesson, User
from .serializers import CourseSerializers, LessonSerializers, UserSerializers

# Create your views here.


class UserViewSet(
    viewsets.ModelViewSet,
    generics.CreateAPIView,
    generics.RetrieveAPIView,
):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [
        MultiPartParser,
    ]

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializers

    @action(
        methods=["post"], detail=True, url_path="hide-lesson", url_name="hide-lesson"
    )
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(
            data=LessonSerializers(l, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )
        # permission_classes = [permissions.IsAuthenticated]

        # def get_permissions(self):
        #     if self.action == 'list':
        #         return [permissions.AllowAny()]
        #     return [permissions.IsAuthenticated()]
