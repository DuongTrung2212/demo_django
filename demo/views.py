from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Lesson
from .serializers import CourseSerializers, LessonSerializers
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializers
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializers

    @action(methods=["post"], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializers(l, context={"request": request}).data, status=status.HTTP_200_OK)
        # permission_classes = [permissions.IsAuthenticated]

        # def get_permissions(self):
        #     if self.action == 'list':
        #         return [permissions.AllowAny()]
        #     return [permissions.IsAuthenticated()]
