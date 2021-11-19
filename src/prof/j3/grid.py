from case import Case

class Grid:
    
    def __init__(self, puzzle = 81*'.'):
        """
            Constructeur par défaut
            Arguments :
                - puzzle : chaine de 81 caractères
            Tests :
            >>> Grid().puzzle == 81*'.', Grid(81*'2').puzzle == 81*'2'
            (True, True)
            >>> Grid().full, Grid(81*'2').full
            (False, True)
        """
        self.puzzle = puzzle
        self.full = self.puzzle.count('.') == 0
        self.initCases()
        self.puzzleNow = self.casesToString()            
        
    def loadFromFile(num):
        """
            Charger un puzzle dans le fichier grids.sud
            Argument :
                - num : numéro du puzzle à charger
            Tests :
            >>> Grid.loadFromFile(0).puzzle[:10]
            '4.....8.5.'
        """
        file = open("grids.sud")
        lines = file.readlines()
        return Grid(lines[num][:-1])
    
    def initCases(self):
        """
            Initialise une liste de 81 cases représentée par l'attribut cases,
            avec leur valeur suivant le puzzle.
            Cette méthode est à appelée lors de l'instanciation de l'objet
            Tests:
            >>> S = Grid()
            >>> S.cases[0].value == None
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.cases[0].value == 4
            True
            >>> S.cases[13].region == 2
            True
        """
        self.cases = []
        
        for i in range(81):
            if self.puzzle[i] == '.':
                self.cases.append(Case(i))
            else:
                self.cases.append(Case(i, int(self.puzzle[i])))
                
                
    def casesToString(self):
        """
            Retourne une chaine de caractère représentant le Sudoku
            Permet de faire la comparaison entre l'état initial du puzzle
            et l'état après ajout de valeurs
            
            Cette méthode est appelée lors de l'instanciation de l'objet. Elle crée alors
            un attribut puzzleNow. Elle est également appelée lors d'un changement d'une
            valeur de case.
        
            Tests :
            >>> S = Grid()
            >>> S.puzzleNow == 81*'.'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.cases[0].value = 5
            >>> S.casesToString()[0] == '5'
            True
        """
        S = ""
        for i in range(81):
            if self.cases[i].value == None:
                S += '.'
            else:
                S += f"(self.cases[i].value)"
        return S
                
    def setValue(self, position, value):
        """
            Méthode permettant de modifier la valeur d'une case à une position donnée.
            Cette méthode doit mettre à jour l'attribut puzzleNow.
            Attention, on ne doit pas pouvoir modifier une valeur qui a été placée initialement.
            
            Tests :
            >>> S = Grid()
            >>> S.setValue(0, 8)
            >>> S.puzzleNow[0] == '8'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(0, 7)
            >>> S.puzzleNow[0] == '7'
            False
        """
        self.cases[position].setValue(value)
        self.puzzleNow = self.casesToString()
        
        pass
                
    def __repr__(self):
        """
            Méthode de représentation d'un Sudoku
        """
        S = ''
        for i in range(81):
            if (i+1)%9==0:
                S += f'|{self.puzzleNow[i]}|\n'
            else:
                S += f'|{self.puzzleNow[i]}'
        return S   
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
