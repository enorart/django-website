from django.urls import path

from .views import index, info, chessboard, validate_move

urlpatterns = [
    path('',index, name="chess-index"),
    path('info/',info,name="chess-info"),
    path('chessboard/',chessboard, name="chess-chessboard"),
    path('validate_move/',validate_move, name="chess-validate_move")
]