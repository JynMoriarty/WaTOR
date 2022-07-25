from random import randint,choice
import time

class Fish:
    
    def __init__(self,reproduction_time,x,y): 
       
        self.reproduction_time = 0
        self.x = x 
        self.y = y
    def fish_movements(self,monde):
            """ Création de la méthode fish movement 
            parameters : self, grille qui est un attribut grille d'un objet de type Aquartorium
            cette méthode va nous renvoyer une liste des déplacements possibles 'return liste'
            cette méthode contient 4 variables Nord,Sud,Ouest,Est qui represente la position x+1 x-1 y+1 y-1 ces variables sont créer avec des modulos pour que les déplacements
            soit bien dans une grille torique , une variable n qui va s'incrémenter de 1 et qui va s'arreter après qu'elle est vérifier les 4 positions.
            cette méthode retourne 2 liste soit une liste de mouvement de disponible : liste , soit une liste de 0 : liste_null pour dire qu'il n'y a aucun mouvement
            elle retourne en priorité la liste de mouvement si sa len est supérieur à 0.
            """
            Nord = (self.y-1)%monde.ordonne
            Sud = (self.y+1)%monde.ordonne
            Ouest =(self.x-1)%monde.abscisse
            Est = (self.x+1)%monde.abscisse
            n=0
            liste=[]
            liste_null=[]
            while n<=3:
                if monde.grille[Nord][self.x]== None:
                    liste.append(1)
                    n+=1
                else :
                    liste_null.append(0)
                    n+=1
                if monde.grille[Sud][self.x]== None:
                    liste.append(2)
                    n+=1
                else : 
                    liste_null.append(0)
                    n+=1
                if monde.grille[self.y][Ouest]== None:
                    liste.append(3)
                    n+=1
                else : 
                    liste_null.append(0)
                    n+=1
                if monde.grille[self.y][Est]== None:
                    liste.append(4)
                    n+=1
                else : 
                    liste_null.append(0)
                    n+=1
            if len(liste)>0:
                return liste
            else : return liste_null
    def fish_move(self,monde,nRandom,fish_time):
            """création de la méthode de déplacement du poisson 
            parameters : self , grille qui est un attribut grille  d'objet de type Aquartorium,nRandom qui est un int : nombre aléatoire qu'on va obtenir
            En fonction de nRandom le poisson va bouger au nord,sud,ouest,est et time qui est le temps de reproduction du poisson.
            on créer 4 variables Nord,Sud,Ouest,Est qui represente la position  y+1 y-1 x+1 x-1 ces variables sont créer avec des modulos pour que les déplacements
            soit bien dans une grille torique
            si le temps de reproduction du poisson est supérieur à time on enlever son temps de reproduction initiale et on créer un poisson
            si il est inférieur à 5 on bouge notre poisson est la case d'avant est égale à none
            """
            Nord = (self.y-1)%monde.ordonne
            Sud = (self.y+1)%monde.ordonne
            Ouest =(self.x-1)%monde.abscisse
            Est = (self.x+1)%monde.abscisse
            oldxpos = self.x
            oldypos = self.y
            if nRandom == 0 :
                monde.grille[self.y][self.x]=monde.grille[self.y][self.x]
            if nRandom == 1 :
                if monde.grille[Nord][self.x]== None:
                    if self.reproduction_time > fish_time:
                        self.reproduction_time = 0
                        self.y = Nord 
                        monde.grille[Nord][self.x]= self
                        monde.grille[oldypos][oldxpos]=Fish(0,oldxpos,oldypos)
                        
                    else :
                        self.reproduction_time+=1
                        self.y = Nord
                        monde.grille[Nord][self.x]=self
                        monde.grille[oldypos][oldxpos]= None
                        
            if nRandom == 2:
                if monde.grille[Sud][self.x]== None:
                    if  self.reproduction_time > fish_time :
                        self.reproduction_time=0
                        self.y = Sud
                        monde.grille[Sud][self.x]=self
                        monde.grille[oldypos][oldxpos]=Fish(0,oldxpos,oldypos)
                    else :
                        self.reproduction_time+=1
                        self.y= Sud
                        monde.grille[Sud][self.x]=self
                        monde.grille[oldypos][oldxpos]= None
                        
            if nRandom == 3:
                if monde.grille[self.y][Ouest]== None:
                    if self.reproduction_time > fish_time :
                        self.reproduction_time = 0
                        self.x = Ouest
                        monde.grille[self.y][Ouest]=self
                        monde.grille[oldypos][oldxpos]=Fish(0,oldxpos,oldypos)
                    else :
                        self.reproduction_time+=1
                        self.x = Ouest
                        monde.grille[self.y][Ouest]= self
                        monde.grille[oldypos][oldxpos]=None
            if nRandom == 4:
                if monde.grille[self.y][Est]== None:
                    if self.reproduction_time > fish_time :
                        self.reproduction_time = 0
                        self.x = Est
                        monde.grille[self.y][Est]=self
                        monde.grille[oldypos][oldxpos]=Fish(0,oldxpos,oldypos)
                    else :
                        self.reproduction_time += 1
                        self.x = Est
                        monde.grille[self.y][Est]=Fish(self.reproduction_time,Est,self.y)
                        monde.grille[oldypos][oldxpos]= None
                        
    def fish_play(self,monde,fish_time):
        nRandom = 0
        liste = []
        liste = self.fish_movements(monde)
        nRandom=choice(liste)
        self.fish_move(monde,nRandom,fish_time)
class Shark(Fish):

    def __init__(self,reproduction_time,x,y,energy):
        super().__init__(reproduction_time,x,y)
        self.energy = energy
    def shark_movements(self,monde):
        """ méthode qui renvoie deux listes de déplacements possible une qui contient que des cases none et une autre où il y'a des poissons 
        on renvoit la liste cases où il y'a des poissoins en priorité
        on créer 4 variables Nord,Sud,Ouest,Est qui represente la position  y+1 y-1 x+1 x-1 ces variables sont créer avec des modulos pour que les déplacements
        soit bien dans une grille torique
        une variable n qui va s'incrémenter de 1 et qui va s'arreter après qu'elle est vérifier les 4 positions.
        cette méthode retourne 3 liste soit une liste de mouvement de disponible contenant les cases vides : liste , soit une liste de 0 : liste_null pour dire qu'il n'y a aucun mouvement
        soit une liste qui contient la liste des mouvements ou les cases contiennent des poissons : liste_cases_poissons
        cette méthode retourne priorité liste_cases_poisson après liste après liste_null

        """
        Nord = (self.y-1)% monde.ordonne
        Sud = (self.y+1)%monde.ordonne
        Ouest =(self.x-1)%monde.abscisse
        Est = (self.x+1)%monde.abscisse
        n=0
        liste=[]
        liste_cases_poissons= []
        liste_null=[]
        while n<=3:

            if type(monde.grille[Nord][self.x])==Fish:
                liste_cases_poissons.append(1)
                n+=1
            elif monde.grille[Nord][self.x]== None:
                liste.append(1)
                n+=1
            else : 
                liste_null.append(0)
                n+=1
            if type(monde.grille[Sud][self.x])==Fish:
                liste_cases_poissons.append(2)
                n+=1
            elif monde.grille[Sud][self.x]== None:
                liste.append(2)
                n+=1
            else : 
                liste_null.append(0)
                n+=1
            if type(monde.grille[self.y][Ouest])==Fish:
                liste_cases_poissons.append(3)
                n+=1
            elif monde.grille[self.y][Ouest]== None:
                liste.append(3)
                n+=1
            else : 
                liste_null.append(0)
                n+=1
            if type(monde.grille[self.y][Est])==Fish:
                liste_cases_poissons.append(4)
                n+=1
            elif monde.grille[self.y][Est]== None:
                liste.append(4)
                n+=1
            else : 
                liste_null.append(0)
                n+=1
        if len(liste_cases_poissons)>0:
            return liste_cases_poissons
        elif len(liste)>0:
            return liste
        else : 
            return liste_null
    def shark_move(self,monde,nRandom,shark_time,energy):
        """création de la méthode de déplacement du requin
        parameters : self , monde.grille  qui est un attribut monde.grille de l'objet de type Aquartorium,nRandom qui est un int : nombre aléatoire qu'on va obtenir
        En fonction de nRandom le poisson va bouger au nord,sud,ouest,est 
        on créer 4 variables Nord,Sud,Ouest,Est qui represente la position x+1 x-1 y+1 y-1 ces variables sont créer avec des modulos pour que les déplacements
        soit bien dans une monde.grille torique
        si le temps de reproduction du requin est égale à 7 on enlever son énergie on créer un requin
        si il est inférieur on bouge notre requin est la case d'avant est égale à none
        """
        Nord = (self.y-1)%monde.ordonne
        Sud = (self.y+1)%monde.ordonne
        Ouest =(self.x-1)%monde.abscisse
        Est = (self.x+1)%monde.abscisse
        oldxpos = self.x
        oldypos = self.y
        """ Explication de la boucle pour un nrandom à chaque tour on enleve déja un energy à la case ou se situe notre requin si l'energie de notre requin est égale à 0 on le delete on le remplace par None
            si la case adjacente est vide il y'a deux options si il assez de d'energie de reproduction "reproduction_time" , celui ci est reset à zero et on bouge notre requin et on créer un requin la ou il était
            Si la case adjacente est un poisson il y'a deux options qui sont les même hormis que dans les deux cas ont rajoute +2 d'énergie au requin quand il aura manger le poisson
        """
        if nRandom == 0 :
            self.energy-=1
            if self.energy ==0:
                monde.grille[self.y][self.x] = None
            else :monde.grille[self.y][self.x] = self
        if nRandom == 1 :
            self.energy-=1
            if self.energy ==0:
                monde.grille[self.y][self.x] = None  
            elif monde.grille[Nord][self.x]== None:

                if self.reproduction_time > shark_time :   
                    self.reproduction_time =0
                    self.y=Nord
                    monde.grille[Nord][self.x]= self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.y = Nord
                    monde.grille[Nord][self.x]= self
                    monde.grille[oldypos][oldxpos] = None
            elif type(monde.grille[Nord][self.x])==Fish:
                
                
                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.energy += 2
                    if self.energy > energy:
                        self.energy = energy
                    self.y = Nord
                    monde.grille[Nord][self.x]= self
                    monde.grille[oldypos][oldxpos] = Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.energy += 2
                    if self.energy > energy:
                        self.energy = energy
                    self.y = Nord
                    monde.grille[Nord][self.x]= self
                    monde.grille[oldypos][oldxpos] = None
        elif nRandom == 2:
            self.energy-=1
            if self.energy ==0:
                monde.grille[self.y][self.x] = None
            elif monde.grille[Sud][self.x]== None:

                
                if self.reproduction_time > shark_time  : 
                    self.reproduction_time =0
                    self.y = Sud
                    monde.grille[Sud][self.x]= self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.y = Sud
                    monde.grille[Sud][self.x]= self
                    monde.grille[oldypos][oldxpos] = None
            elif type(monde.grille[Sud][self.x]) ==Fish:
                
               
                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.energy +=2
                    if self.energy > energy:
                        self.energy = energy
                    self.y=Sud
                    monde.grille[Sud][self.x]= self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.energy += 2
                    if self.energy > energy:
                        self.energy = energy
                    self.y= Sud
                    monde.grille[Sud][self.x]= self
                    monde.grille[oldypos][oldxpos] = None
                    
                
        elif nRandom == 3:

            self.energy -= 1
            if self.energy == 0:
                monde.grille[self.y][self.x] = None

            elif monde.grille[self.y][Ouest]== None:

                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.x = Ouest
                    monde.grille[self.y][Ouest]=self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)

                else :
                        self.reproduction_time+=1
                        self.x = Ouest
                        monde.grille[self.y][Ouest]=self
                        monde.grille[oldypos][oldxpos]= None
            elif type (monde.grille[self.y][Ouest])==Fish:

                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.energy += 2
                    if self.energy > energy:
                        self.energy = energy
                    self.x = Ouest
                    monde.grille[self.y][Ouest]=self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.energy+=2
                    if self.energy > energy:
                        self.energy = energy
                    self.x= Ouest
                    monde.grille[self.y][Ouest]= self
                    monde.grille[oldypos][oldxpos] = None

        elif nRandom == 4:
            
            self.energy-=1
            if self.energy ==0:
                monde.grille[self.y][self.x] = None
            elif monde.grille[self.y][Est]== None:
                
                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.x = Est
                    monde.grille[self.y][Est]=self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time+=1
                    self.x = Est
                    monde.grille[self.y][Est]=self
                    monde.grille[oldypos][oldxpos]= None
            elif type(monde.grille[self.y][Est]) == Fish:
                
                if self.reproduction_time > shark_time:
                    self.reproduction_time =0
                    self.energy+=2
                    if self.energy > energy:
                        self.energy = energy
                    self.x = Est
                    monde.grille[self.y][Est]=self
                    monde.grille[oldypos][oldxpos]= Shark(0,oldxpos,oldypos,20)
                else :
                    self.reproduction_time +=1
                    self.energy += 2
                    if self.energy > energy:
                        self.energy = energy
                    self.x = Est
                    monde.grille[self.y][Est]= self
                    monde.grille[oldypos][oldxpos] = None
                    
    def shark_play(self,monde,shark_time,energy):
        nRandom = 0
        liste = []
        liste = self.shark_movements(monde)
        nRandom=choice(liste)
        self.shark_move(monde,nRandom,shark_time,energy)

        
class Aquartorium:
    
    def __init__(self,abscisse,ordonne): 
        self.abscisse=abscisse
        self.ordonne=ordonne
        self.grille =[[None for i in range(abscisse)] for _ in range(ordonne)]
    """ méthode init qui initalise les attributs de l'objet Aquartorium 
    parameters : abscisse = abcisse de notre grille et ordonne = ordonne de notre grille
    grille de dimension ordonne,abcisse
    """    


    def affiche_grille(self):
        """ on affiche notre grille et on remplace les objets poissons par des 1 et les objets requins par des 2 sinon par des none
        parameters : objet de type aquartorium
        """
        for i in self.grille :
            ligne_aff = ""
            for j in i:
                if type(j)==Shark:
                    ligne_aff += " 2 "
                elif type (j)==Fish:
                    ligne_aff += " 1 "
                elif j is None:
                    ligne_aff += " 0 "
            print(ligne_aff)
    def peupler(self,sharks_number,fishes_number,energy):
            """ parameters : nb de requins et nb de poisson 
            elle va remplir notre grille de poissons et de requins dans une
            """
            for i in range(sharks_number):
                rdnumberx = randint(0,self.abscisse-1)
                rdnumbery= randint(0,self.ordonne-1)
                while self.grille[rdnumbery][rdnumberx] is not None:
                    rdnumberx = randint(0,self.abscisse-1)
                    rdnumbery= randint(0,self.ordonne-1)
                self.grille[rdnumbery][rdnumberx]=Shark(0,rdnumberx,rdnumbery,energy)
            for i in range(fishes_number):
                rdnumberx = randint(0,self.abscisse-1)
                rdnumbery= randint(0,self.ordonne-1)
                while self.grille[rdnumbery][rdnumberx] is not None:
                    rdnumberx = randint(0,self.ordonne-1)
                    rdnumbery= randint(0,self.abscisse-1)
                self.grille[rdnumbery][rdnumberx]=Fish(0,rdnumberx,rdnumbery)
    def jouer_tour(self,shark_time,fish_time,energy):
        """la fonction jouer tour ne prend aucun parametre et fait jouer un tour c'est à dire qu'elle va faire bouge tous les créatures dans la grille
        """
        for abscisse in self.grille:
            for ordonne in abscisse:
                if type(ordonne) ==Fish:
                    ordonne.fish_play(self,fish_time)  
                elif type(ordonne) == Shark:
                    ordonne.shark_play(self,shark_time,energy)
            

#####################################################
#                   INITIALISATION                  #
#####################################################
fish_time =0
shark_time=0
energy=0
abscisse = int(input("Enter la largeur de la grille  :  "))

while abscisse <2:
    abscisse = int(input("Enter la largeur de la grille  :  "))

ordonne = int(input("Entrer la longueur de la grille  : "))    

while ordonne <2:
    ordonne = int(input("Entrer la longueur de la grille  : "))

fishes_number = int(input("Entrer le nombre de poissons : "))
sharks_number = int(input("Entrer le nombre de requins : "))

if fishes_number !=0:
    fish_time= int(input("Entrer le temps de reproduction des poissons : "))


if sharks_number!=0:
    shark_time = int(input("Entrer le temps de reproduction des requins : "))
    energy = int(input("Entrez l'énergie des requins : "))

tour= int(input("Entrer le Nombre de tour que vous voulez faire : "))

while tour <0 :
    tour= int(input("Entrer le Nombre de tour que vous voulez faire : "))

print("############################################################################")


monde = Aquartorium(abscisse,ordonne)
monde.peupler(sharks_number,fishes_number,energy)
p =0
#####################################################)
#                   DEMARRAGE                       #
#####################################################

while p<tour:
    monde.jouer_tour(shark_time,fish_time,energy)
    monde.affiche_grille()
    time.sleep(1)
    "on affiche la grille à chaque fois qu'un tour complet de la grille à été effectuer : un requin ou un poisson peut bouger plusieurs fois"
    print("############################")
        
    p+=1



#L'écosystème a tendance à pencher en faveur des requins. Comme il était indiqué en cours il n'y avait pas la contrainte de faire bouger que les poissons et les requins
# c'est à dire qu'à chaque fois qu'on boucle dans la grille si un poisson ou un requin bouge vers le bas à la ligne suivante il va rejouer un tour
#l'affichage est fait après un tour complet de la grille si un poisson à la case 0.0 est à la case 5.3 c'est normal.
#Pour les requins qui se mangent entre eux vous pouvez tester une grille de 5x4 avec 0 poissons et 20 requins et
# un temps de reproduction supérieur à leur énergie E ils vont mourrir à tour = E car aucun des requins ne se mangent entre eux
# pour égaliser le rapport de force entre les requins et les poissons je viens de changer l'energie limite des requins à leur energie de base.
   

