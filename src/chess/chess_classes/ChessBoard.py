from chess.chess_classes.ChessPiece import *

class ChessBoard:

    def __init__(self):
        self.pieces = [[None for y in range(8)] for x in range(8)]
        self.pieces=self.load_grid()
    
    def load_grid(self):
        """Placement initial des pièces sur le plateau de jeu\n
        [abscisse][ordonnée] allant de 0 à 7"""
        for i in range(8):
            self.pieces[i][1]=PiecePawn(self,f"p{i+1}","black")     
            self.pieces[i][6]=PiecePawn(self,f"p{i+1}","white")
        self.pieces[0][0]=PieceRook(self, "r1","black")     
        self.pieces[7][0]=PieceRook(self, "r2","black")
        self.pieces[0][7]=PieceRook(self, "r1","white")
        self.pieces[7][7]=PieceRook(self, "r2","white")
        self.pieces[1][0]=PieceHorse(self, "h1", "black")       
        self.pieces[6][0]=PieceHorse(self, "h2", "black")
        self.pieces[1][7]=PieceHorse(self, "h1","white")
        self.pieces[6][7]=PieceHorse(self, "h2","white")
        self.pieces[2][0]=PieceBishop(self, "b1","black")       
        self.pieces[5][0]=PieceBishop(self, "b2","black")
        self.pieces[2][7]=PieceBishop(self, "b1", "white")
        self.pieces[5][7]=PieceBishop(self, "b2","white")
        self.pieces[3][0]=PieceQueen(self, "q","black")     
        self.pieces[3][7]=PieceQueen(self, "q","white")
        self.pieces[4][0]=PieceKing(self, "k","black")
        self.pieces[4][7]=PieceKing(self, "k","white")      
        return self.pieces
    
# objet_board=ChessBoard()

# #choix de la pièce
# objet_piece=objet_board.pieces[5][5]
# print(objet_piece)
# print(objet_piece.side)


# #position des rois :
# wk_x=4
# wk_y=7

# bk_x=4
# bk_y=0

# print(objet_piece._king_checked(5,5))

#attention pour les conditions de mouvement bien appeler les deux fonctions
# src_x=4
# src_y=3
# dst_x=4
# dst_y=5

# print(objet_piece.valid_move_generic(src_x,src_y,dst_x,dst_y))
# objet_board.pieces[dst_x][dst_y]=PieceKing(objet_board,"k","black")
# objet_board.pieces[src_x][src_y]=None

# print(objet_piece.specific_valid_move(src_x,src_y,dst_x,dst_y))




