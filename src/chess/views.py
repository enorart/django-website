from django.shortcuts import render
from django.http import JsonResponse

#BD
from chess.models import User

#classe des échecs (backend)
from chess.chess_classes.ChessBoard import ChessBoard

# Create your views here.
def index(request):
    return render(request, 'chess/index.html')

def info(request):
    users=User.objects.all()
    return render(request, 'chess/info.html',context={"users":users})       #gabarit pour les users
    
def chessboard(request):
    chessboard=ChessBoard().pieces
    chessboard_0 = chessboard[0]
    chessboard_1 = chessboard[1]
    chessboard_2 = chessboard[2]
    chessboard_3 = chessboard[3]
    chessboard_4 = chessboard[4]
    chessboard_5 = chessboard[5]
    chessboard_6 = chessboard[6]
    chessboard_7 = chessboard[7]
    return render(request, 'chess/chessboard.html',context={"chessboard":chessboard, 
                                                            "chessboard_0":chessboard_0,
                                                            "chessboard_1":chessboard_1,
                                                            "chessboard_2":chessboard_2,
                                                            "chessboard_3":chessboard_3,
                                                            "chessboard_4":chessboard_4,
                                                            "chessboard_5":chessboard_5,
                                                            "chessboard_6":chessboard_6,
                                                            "chessboard_7":chessboard_7})


def validate_move(request):
    print(request.POST.get('row'))
    print(request.POST.get('col'))

    return JsonResponse({'success':True,})
