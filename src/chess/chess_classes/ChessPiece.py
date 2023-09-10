#import des bibliotheques
from abc import ABC, abstractmethod                 #pour les classes abstraites    


class PieceRole:
    """Classe qui représente le rôle d'une pièce d'échec\n
    Son nom, son label (pour l'affichage) et son poids (toujours utile si on veut mettre une IA plus tard)"""
    def __init__(self, name, label, weight):
        self.name=name
        self.label=label
        self.weight=weight


class PieceRolePawn(PieceRole):
    """Classe qui représente le role du pion"""
    def __init__(self):
        PieceRole.__init__(self, "P", "Pawn", 1)


class PieceRoleRook(PieceRole):
    """Classe qui représente le role de la tour"""
    def __init__(self):
        PieceRole.__init__(self, "R", "Rook", 5)


class PieceRoleHorse(PieceRole):
    """Classe qui représente le role du cavalier"""
    def __init__(self):
        PieceRole.__init__(self, "H", "Horse", 3)


class PieceRoleBishop(PieceRole):
    """Classe qui représente le role du fou"""
    def __init__(self):
        PieceRole.__init__(self, "B", "Bishop", 3)


class PieceRoleQueen(PieceRole):    
    """Classe qui représente le role de la reine"""
    def __init__(self):
        PieceRole.__init__(self, "Q", "Queen", 9)


class PieceRoleKing(PieceRole): 
    """Classe qui représente le role du roi"""
    def __init__(self):
        PieceRole.__init__(self, "K", "King", 0)


class ChessPiece(ABC):
    """Classe qui représente une pièce d'échec"""

    def __init__(self, board, name, role, picture, side):
        self.board=board
        self.name=name
        self.role=role
        self.picture=picture
        self.side=side

    def __str__(self):
        return self.name
    
    @abstractmethod     #méthode abstraite
    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Méthode abstraite qui vérifie si le déplacement est valide => Blueprint
        """
        ...

    #validation des mouvements en général => concernent toutes les pièces
    def valid_move_generic(self, src_x, src_y, dest_x, dest_y):
        """Méthode qui vérifie si le déplacement est valide pour une pièce générique\n
        Point de vérification :
        - la case de destination est vide ou occupée par une pièce adverse
        - la case de destination est dans le plateau
        - la case de destination est différente de la case de départ\n
        Retourne True si c'est le cas, False sinon
        """
      
        if dest_x < 0 or dest_x > 7 or dest_y < 0 or dest_y > 7:        #si la case de destination est en dehors du plateau
            return False
        elif src_x == dest_x and src_y == dest_y:     #si on ne bouge pas
            return False
         #si la case de destination est occupée par une pièce de notre camp
        elif self.board.pieces[dest_x][dest_y] != None:  
            if self.board.pieces[dest_x][dest_y].side == self.side:
                return False
        return True
    
    #validation des mouvements spécifiques => horizontaux, verticaux, diagonaux
    def _check_direction_horizontal(self, src_x, src_y, dest_x, dest_y):
        """Methode qui vérifie si le déplacement est horizontal, donc si l'ordonné (y) reste la même"""
        if src_y == dest_y:
            return True
        return False
    

    def _check_direction_vertical(self, src_x, src_y, dest_x, dest_y):
        """Methode qui vérifie si le déplacement est vertical, donc si l'abscisse (x) reste la même"""
        if src_x == dest_x:
            return True      
        return False
    
    def _check_direction_diagonal(self, src_x, src_y, dest_x, dest_y):
        """Methode qui vérifie si le déplacement est diagonal, donc si le abs(delta abscisse) = abs(delta ordonnée)"""
        if abs(src_x - dest_x) == abs(src_y - dest_y):
            return True
        return False
    
    #chemin libre => les pièces ne peuvent pas sauter par dessus d'autres pièces (sauf le cavalier)
    def _clear_direction_horizontal(self, src_x, src_y, dest_x, dest_y):
        """Méthode qui vérifie si la trajectoire est libre pour un déplacement horizontal\n
        On vérifie que les cases de la trajectoire entre le départ et l'arrivée car pour le départ c'est logique que c'est libre et pour l'arrivé on le vérifie déjà avec _valid_move_generic"""
        
        if not self._check_direction_horizontal(src_x, src_y, dest_x, dest_y):      
            return False   #si ce n'est pas un déplacement horizontal, ça ne sert à rien de vérifier si les cases sont libres, le mouvement n'est déjà pas valide

        if src_x > dest_x:
            for i in range(dest_x+1, src_x):
                if self.board.pieces[i][src_y]!=None :    #si il y a une pièce entre 
                    return False
        else:
            for i in range(src_x+1, dest_x):
                if self.board.pieces[i][src_y]!=None:       #si il y a une pièce entre
                    return False
        return True
    
    def _clear_direction_vertical(self, src_x, src_y, dest_x, dest_y):
        """Méthode qui vérifie si la trajectoire est libre pour un déplacement vertical"""

        if not self._check_direction_vertical(src_x, src_y, dest_x, dest_y):
            return False  #si ce n'est pas un déplacement vertical, ça ne sert à rien de vérifier si les cases sont libres, le mouvement n'est déjà pas valide

        if src_y > dest_y:
            for i in range(dest_y+1, src_y):
                if self.board.pieces[src_x][i]!=None:     #si il y a une pièce entre
                    return False
        else:
            for i in range(src_y+1, dest_y):
                if self.board.pieces[src_x][i]!=None:       #si il y a une pièce entre
                    return False
        return True
    
    def _clear_direction_diagonal(self, src_x, src_y, dest_x, dest_y):
        """Méthode qui verifie si la trajectoire est libre pour un déplacement diagonal"""

        if not self._check_direction_diagonal(src_x, src_y, dest_x, dest_y):
            return False  #si ce n'est pas un déplacement diagonal, ça ne sert à rien de vérifier si les cases sont libres, le mouvement n'est déjà pas valide

        if src_x > dest_x:
            if src_y > dest_y:      #diagonale haut gauche
                for i in range(1, src_x - dest_x):
                    if self.board.pieces[dest_x + i][dest_y + i]!=None:           
                        return False
            else:            #diagonale bas gauche
                for i in range(1, src_x - dest_x):
                    if self.board.pieces[dest_x + i][dest_y - i]!=None:
                        return False
        else:
            if src_y > dest_y:      #diagonale haut droite
                for i in range(1, dest_x - src_x):
                    if self.board.pieces[src_x + i][src_y - i]!=None:
                        return False
            else:       #diagonale bas droite
                for i in range(1, dest_x - src_x):
                    if self.board.pieces[src_x + i][src_y + i]!=None:
                        return False
        return True
    
    def _king_checked(self, k_x, k_y):
        """Méthode qui vérifie si le roi est en échec"""

        for i in range(8):      #on parcourt toutes les cases du plateau
            for j in range(8):
                if self.board.pieces[i][j] != None:     #si la case n'est pas vide
                    if self.board.pieces[i][j].side != self.side:     #si la pièce est de l'autre camp
                        if self.board.pieces[i][j].valid_move_generic(i,j, k_x, k_y)==True and self.board.pieces[i][j].specific_valid_move(i,j, k_x, k_y)==True:     #si la pièce peut manger le roi
                            print("Le roi est en échec à cause de la pièce", self.board.pieces[i][j], "en", i, j)
                            return True
        return False

class PiecePawn(ChessPiece):
    """Classe qui représente le pion"""

    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRolePawn(), f'chess/{side}_pawn.png', side)

    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique du pion\n
        Feature :\n
            - le pion peut avancer d'une case vers l'avant\n
            - le pion peut avancer de deux cases vers l'avant si c'est son premier coup\n
            - le pion peut manger en diagonale\n
        Non implémenté :\n
            - la prise en passant\n
        """
             
        if self.side == "white":    #si c'est un pion blanc
          
            if dest_y == src_y - 1 and abs(dest_x - src_x) == 1:     #si le pion mange en diagonale
                if self.board.pieces[dest_x][dest_y]!=None:          
                    if self.board.pieces[dest_x][dest_y].side != self.side:
                        return True
            
            if src_y == 6:          #si c'est le premier coup du pion
                if dest_y == src_y - 1 or dest_y == src_y - 2:        #si le pion avance d'une ou deux cases
                    if self._clear_direction_vertical(src_x, src_y, dest_x, dest_y):        #si la trajectoire est libre
                        if self.board.pieces[dest_x][dest_y]!=None:     #si la case n'est pas vide
                            if self.board.pieces[dest_x][dest_y].side != self.side:     #le pion est bloqué si il y a une pièce sur la case devant lui
                                return False  
                        return True
            
            else:                   #si ce n'est pas le premier coup du pion
                if dest_y == src_y - 1:     #si le pion avance d'une case
                        if self.board.pieces[dest_x][dest_y]!=None:     #si la case n'est pas vide
                            if self.board.pieces[dest_x][dest_y].side != self.side:     #le pion est bloqué si il y a une pièce sur la case devant lui
                                return False           
                        return True
        
        else:                       #si c'est un pion noir
            
            if dest_y == src_y + 1 and abs(dest_x - src_x) == 1:     #si le pion mange en diagonale
                if self.board.pieces[dest_x][dest_y]!=None:         
                    if self.board.pieces[dest_x][dest_y].side != self.side:
                        return True
            
            
            if src_y == 1:          #si c'est le premier coup du pion
                if dest_y == src_y + 1 or dest_y == src_y + 2:        #si le pion avance d'une ou deux cases
                    if self._clear_direction_vertical(src_x, src_y, dest_x, dest_y):
                        if self.board.pieces[dest_x][dest_y]!=None:     #si la case n'est pas vide
                            if self.board.pieces[dest_x][dest_y].side != self.side:     #le pion est bloqué si il y a une pièce sur la case devant lui
                                return False
                        return True
            else:                   #si ce n'est pas le premier coup du pion
                if dest_y == src_y + 1:     #si le pion avance d'une case
                        if self.board.pieces[dest_x][dest_y]!=None:     #si la case n'est pas vide
                            if self.board.pieces[dest_x][dest_y].side != self.side:     #le pion est bloqué si il y a une pièce sur la case devant lui
                                return False
                        return True
        return False
    

class PieceRook(ChessPiece):
    """Classe qui représente la tour"""
    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRoleRook(), f'chess/{side}_rook.png', side)

    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique de la tour\n
        Feature :\n
            - la tour peut se déplacer horizontalement et verticalement\n
        Non implémenté :\n
            - le roque (petit)\n
        """

        if self._check_direction_horizontal(src_x, src_y, dest_x, dest_y):      #si le déplacement est horizontal
            if self._clear_direction_horizontal(src_x, src_y, dest_x, dest_y):    #si la trajectoire est libre
                return True
        elif self._check_direction_vertical(src_x, src_y, dest_x, dest_y):      #si le déplacement est vertical
            if self._clear_direction_vertical(src_x, src_y, dest_x, dest_y):    #si la trajectoire est libre
                return True
        return False
    
class PieceBishop(ChessPiece):
    """Classe qui représente le fou"""
    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRoleBishop(), f'chess/{side}_bishop.png', side)

    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique du fou\n
        Feature :\n
            - le fou peut se déplacer en diagonale\n
        """

        if self._check_direction_diagonal(src_x, src_y, dest_x, dest_y):      #si le déplacement est diagonal
            if self._clear_direction_diagonal(src_x, src_y, dest_x, dest_y):    #si la trajectoire est libre
                return True
        return False
    
class PieceQueen(ChessPiece):
    """Classe qui représente la reine"""
    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRoleQueen(), f'chess/{side}_queen.png', side)

    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique de la reine\n
        Feature :\n
            - la reine peut se déplacer horizontalement, verticalement et en diagonale\n
        Non implémenté : \n
            - le roque (grand)\n
        """

        if self._check_direction_horizontal(src_x, src_y, dest_x, dest_y):      #si le déplacement est horizontal
            if self._check_direction_horizontal(src_x, src_y, dest_x, dest_y):  #si la trajectoire est libre
                return True
        elif self._check_direction_vertical(src_x,src_y,dest_x,dest_y):     #si le déplacement est vertical
            if self._clear_direction_vertical(src_x, src_y, dest_x, dest_y):   #si la trajectoire est libre
                return True
        elif self._check_direction_diagonal(src_x, src_y, dest_x, dest_y):    #si le déplacement est diagonal
            if self._clear_direction_diagonal(src_x, src_y, dest_x, dest_y):    #si la trajectoire est libre
                return True
        return False

class PieceHorse(ChessPiece):
    """Classe qui représente le cavalier"""
    
    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRoleHorse(), f'chess/{side}_horse.png', side)
    
    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique du cavalier\n
        Feature :\n
            - le cavalier peut se déplacer en L\n
            - il peut sauter les pièces entre son départ et son arrivée\n
        """
    
        if abs(dest_x - src_x) == 2 and abs(dest_y - src_y) == 1:     #si le déplacement est en L
            return True
        elif abs(dest_x - src_x) == 1 and abs(dest_y - src_y) == 2:   #si le déplacement est en L
            return True
        return False

class PieceKing(ChessPiece):
    """Classe qui représente le roi"""

    def __init__(self, board, name, side):
        super().__init__(board, name, PieceRoleKing(), f'chess/{side}_king.png', side)
      
    def specific_valid_move(self, src_x, src_y, dest_x, dest_y):
        """Mouvement spécifique du roi\n
        Feature :\n
            - le roi peut se déplacer d'une case dans toute les directions
            - il ne peut pas se mettre en échec\n
        Non implémenté :\n
            - le roque (grand et petit)\n
        """
        if self._king_checked(dest_x, dest_y) == False:     #si ce mvt ne met pas le roi en échec
            if abs(dest_x - src_x) <= 1 and abs(dest_y - src_y) <= 1:       #si le déplacement est d'une case
                return True
            return False
        else :
            return False
        

    

        
    
    