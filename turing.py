'''Une emulation de machine de turing

Exemple : voir siracuse.py

Auteur : fredThx
'''


class Turing:
    '''Une machine de T.
    '''
    droite = 1
    R = 1
    D = 1
    gauche = -1
    G = -1
    L = -1
    b = " "

    def __init__(self, etats = None, data = None, start_right = False):
        '''
        - etats :   {1:TEtat(...), 2:...}
        - data  :   [...] ou "   00111"
        '''
        self.etat = 0
        if start_right:
            self.indice = len(data)-1
        else:
            self.indice = 0
        i=0
        self.data = {}
        for c in data or []:
            if c == " ":
                self.data[i] = None
            else:
                self.data[i] = c
            i += 1
        self.etats = etats or {}

    def __str__(self):
        text=f"Etat : {self.etat+1}  => "
        for i in range(min(self.indice,min(self.data.keys())), max(self.indice,max(self.data.keys()))+1):
            if i == self.indice:
                text += f"({self.read(i)})|"
            else:
                text += f" {self.read(i)} |"
        return text

    def read(self, indice=None):
        '''Lit la case active ou la valeur de l'indice si renseigné'''
        if indice is None:
            return self.data.get(self.indice, self.b)
        else:
            return self.data.get(indice, self.b)

    def write(self, value):
        '''Ecrit value dans la case active'''
        if value in [None,self.b]:
            del self.data[self.indice]
        else:
            self.data[self.indice]=value

    def move(self, deplacement):
        ''' Déplace la curseur à droite (+1) ou à gauche (-1)'''
        self.indice += deplacement

    def set_etat(self, etat):
        '''Chaneg d'état '''
        self.etat = etat

    def run_once(self, verb = True):
        result =  self.etats[self.etat].do(self)
        if verb:
            print(self)
        return result

    def run(self, verb = True):
        n=0
        if verb:
            print(self)
        while self.run_once(verb):
            n +=1
            if verb:
                print(f"fin étape {n}")
        print(f"Fin du calcul en {n} étapes")


class TEtat:
    '''Le code d'un état
    '''
    def __init__(self, indice, actions = None):
        self.indice = indice
        self.actions = actions
        assert len(self.actions) == len(set(self.actions)), f"Erreur : actions en doublons : {self.actions}"

    def do(self, machine):
        '''Execute les actions'''
        for action in self.actions:
            result = action.do(machine)
            if result:
                return result
    def __str__(self):
        txt = f"Etat {self.indice} :\n"
        for action in self.actions:
            txt += f"\t{str(action)}\n"
        return txt


class TAction:
    '''Une action : Si Lecture X => Ecriture, Déplacement, Etat+1
    '''
    def __init__(self, lecture, ecriture=None, deplacement=None, etat=None):
        self.lecture = str(lecture)
        if ecriture is None:
            self.ecriture = None
        else:
            self.ecriture = str(ecriture)
        self.deplacement = deplacement
        self.etat = etat

    def __str__(self):
        return f"TAction: {self.lecture}=>{self.ecriture} | {self.deplacement} | {self.etat} "

    def do(self, machine):
        '''Execute l'action est retourne True si l'action a été réalisée
        '''
        if machine.read() == self.lecture:
            change = False
            if self.ecriture:
                #print(f"Write {self.ecriture} ({type(self.ecriture)})on {machine}")
                machine.write(self.ecriture)
                change = True
            if self.deplacement:
                machine.move(self.deplacement)
                change = True
            if self.etat:
                machine.set_etat(self.etat-1)
                change = True
            if change:
                return True

"""
    def xread(self):
        if self.etat == 0:
            if self.data.get(self.indice) != None:
                self.indice += 1
                self.etat = 0
            else:
                self.indice -= 1
                self.etat = 1
        elif self.etat == 1:
            if self.data.get(self.indice) == None:
                self.data[self.indice] = 1
                self.etat = 3 #terminé
            elif self.data.get(self.indice) < "9":
                self.data[self.indice] = chr(ord(self.data.get(self.indice)) + 1)
                self.indice -=1
                self.etat = 2
            elif self.data.get(self.indice) == "9":
                self.data[self.indice] = 0
                self.indice -=1
                self.etat = 1
        elif self.etat == 2:
            if self.data.get(self.indice) != None:
                self.indice -=1
                self.etat = 2
            else:
                self.etat = 3 #terminé
"""
