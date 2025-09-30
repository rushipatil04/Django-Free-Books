from rest_framework import viewsets, filters, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, Http404
from .models import Book, Subject, Year
from .serializers import BookSerializer, SubjectSerializer, YearSerializer, BookCreateSerializer

class YearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [AllowAny]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['year', 'subject', 'is_public']
    search_fields = ['title', 'author', 'description']
    ordering_fields = ['upload_date', 'title', 'author']
    ordering = ['-upload_date']
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Book.objects.all()
        return Book.objects.filter(is_public=True)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'download', 'preview']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return BookCreateSerializer
        return BookSerializer
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        try:
            book = self.get_object()
            if not book.is_public and not request.user.is_authenticated:
                return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
            
            response = FileResponse(
                book.pdf_file.open(),
                as_attachment=True,
                filename=f"{book.title}.pdf"
            )
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def preview(self, request, pk=None):
        try:
            book = self.get_object()
            if not book.is_public and not request.user.is_authenticated:
                return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
            
            response = FileResponse(
                book.pdf_file.open(),
                content_type='application/pdf'
            )
            response['Content-Disposition'] = 'inline'
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if username and password:
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return Response({
                'success': True,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'is_staff': user.is_staff
                }
            })
    
    return Response({'success': False, 'error': 'Invalid credentials'}, 
                   status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def admin_logout(request):
    logout(request)
    return Response({'success': True})

@api_view(['GET'])
@permission_classes([AllowAny])
def check_auth(request):
    return Response({
        'is_authenticated': request.user.is_authenticated,
        'is_staff': request.user.is_staff if request.user.is_authenticated else False
    })