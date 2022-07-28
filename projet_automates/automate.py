# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from parser import *
from itertools import product
from automateBase import AutomateBase



class Automate(AutomateBase):
        
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ (self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        print("Appel fonction succ")
        L=[] #liste finale
        s=[] #liste temporaire
        
        for e in listStates : #on parcours la liste des états de l'automate en question
        	s=s+self.succElem(e,lettre) #Pour chaque état de l'automate on ajoute à la liste temporaire la liste des états successifs par rapport à la lettre demandé

        for i in s : #On veut maintenant, avoir une liste des états sans occurences, on parcours donc la liste temporaire s	
        	if i not in L : #Si l'état dans la liste temporaire n'est pas encore dans la liste finale, on l'ajoute à la liste finale
        		L.append(i)
        return L


    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x   def determinisation(auto) :
   str -> bool
        rend True si auto accepte mot, False sinon"""
        print("Appel fonction accepte")
        
        liste_init=auto.getListInitialStates() #On crée la liste des états initiaux
        Liste_final=auto.getListFinalStates() #On crée la liste des états finaux
        
        #lettre:str
        for lettre in mot: #On parcours le mot pour savoir si l'automate l'accepte
        	liste_init=auto.succ(liste_init,lettre) 
        	print(liste_init)
        if (len(liste_init)==0): #Si à la fin du parcours la taille de la liste vaut zéro c'est qu'il n'y a pas d'état successeur qu'on peut accéder avec la lettre correspondante et donc on retourne false 
        	return False
        #etat=state : int
        for state in liste_init :#Si on arrive ici, c'est qu'il y a des successeurs, on veut donc vérifier si le mot se termine bien, on parcours donc la liste initiale redéfinie précédemment
        	if state in Liste_final : #Il suffit d'avoir un état dans la liste qui soit égale à un état finale de la liste pour que l'automate soit déterministe, sinon il ne l'est pas
        		return True
        return False
       


        				        
        
    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        print("Appel fonction estComplet")
        for i in auto.listStates : #On parcours 
        	liste_transition=auto.getListTransitionsFrom(i)
       		for l in alphabet:
       			if l not in[t.etiquette for t in liste_transition]:
       				return False
        return True


        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        print("Appel fonction estDeterministe")
        if len(auto.getListInitialStates())!=1 : #Si il y a plus d'un état initiale, l'automate ,n'est plus déterministe
        	return False #on parcours la liste des état de l'automate
        for l in auto.listStates: #On parcours les états de l'auto pour voir s'il y a un seul étiquette pour chaque lettres de l'alphabet
        	L=[]
        	for i in auto.getListTransitionsFrom(l):
        		if i.etiquette in L:
        			return False
        		L.append(i.etiquette)
        return True

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        print("Appel fonction completeAutomate")
        if auto.estComplet(auto, alphabet): #On vérifie d'abord si l'automate n'est pas déjà déterministe, si c'est le cas on retourne lui même
        	return auto
        
        newState = State("Puit",False,False) #On crée l'état puis pour compléter l'automate, l'état puis n'est ni un état final, ni un état initial
        newAuto = copy.deepcopy(auto) #On fait une copie de l'automate auto car on ne veut pas modifier l'automate auto
        newAuto.addState(newState) #On ajoute l'état à l'automate copie qui se nomme newAuto
        for i in auto.listStates: #On parcours la liste des états de l'automate de base auto, et on vérifie pour chaque transitions entre 2 états, il y a bien tout l'alphabet
        	Liste_trans=auto.getListTransitionsFrom(i)#On veut la liste des transitions pour comparer l'étiquette de la transition et des lettres de l'alphabet
        	for e1 in alphabet : 
        		for e2 in Liste_trans :
        			if e2.etiquette == e1 : #on compare la lettre de l'alphabet en cours avec tout les étiquettes de la liste des transitions si c'est la même lettre on continue
        				continue
        			t = Transition(i,e1,newState) #sinon on crée une nouvelle transition entre l'état i en cours et l'état puit newState
        			newAuto.addTransition(t) #qu'on rajoute à l'automate newAuto
        		t2 = Transition(newState,e1,newState)#Enfin, on crée et on rajoute une transition entre de l'état puit et lui même avec tout les lettres de l'alphabet pour compléter 
        		newAuto.addTransition(t2)
        		
        			 
        	#t = Transition(i,alphabet,NewState)
        	#newAuto.addTransition(t) 
     
        
        return newAuto
   
        
	
    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        
        if Automate.estDeterministe(auto):
            return auto
        
        Lis=[set(auto.getListInitialStates())]
        Lfs=[]
        Lft=[]
        cpt=0
        alphabet=auto.getAlphabetFromTransitions()
        
        for liste in Lis:
            for lettre in alphabet:
                Lsucc=auto.succ(liste,lettre)      	
                if set(Lsucc) not in Lis:
                    Lis.append(set(Lsucc))
		
         		                              	
        for liste in Lis:
        	nit=True
        	nal=State.isFinalIn(liste)
        	for etat in list(liste):	       			        		     		
        		if not etat.init:
        			nit=False      	       		
        	Lfs.append(State(cpt,nit,nal)) 
        	cpt+=1
        	       
        for j in range(0,len(Lis)):
        	for lettre in alphabet:
        		Lsucc=set(auto.succ(Lis[j],lettre))
        		for i in range(0,len(Lis)):
        			if Lsucc==Lis[i]:
        				Lft.append(Transition(Lfs[j],lettre,Lfs[i]))
        		
        	
        return Automate(Lft,Lfs)
    
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
        print("Appel fonction complémentaire")
        auto_deter = Automate.determinisation(auto) #On determinise l'automate qu'on a passé en argument
        auto_complete = Automate.completeAutomate(auto_deter, alphabet) #On complete l'automate precedemment determiné 

        for state in auto_complete.listStates : #Pour un etat dans la liste d'etats de l'automate complété et determinisé
            state.fin = not(state.fin) #Les etats finaux deviennent non finaux et inversement

        return auto_complete      
   
    @staticmethod
    def intersection (auto0, auto1): 
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        print("Appel fonction intersection")
        new_auto = Automate([],None) #None pour liste de States None cf _init_ dans automate base
        if (len(auto0.listStates) == 0):                                                                       
            return new_auto
        if (len(auto1.listStates) == 0):
            return new_auto                #Si un des automates n'a pas d'etats return l'automate vide directement

        alphabet=[] #On creer l'alphabet, il faut que les lettres soient dans les 2 automates
        for lettre in auto0.getAlphabetFromTransitions(): #Pour une lettre dans l'alphabet du 1ère automate
            if lettre in auto1.getAlphabetFromTransitions(): #Si le second automate possède cette lettre
                alphabet.append(lettre) #on l'ajoute a l'alphabet

        liste_couple_etats = list(product(auto0.getListInitialStates(), auto1.getListInitialStates())) #On creer une liste de couples d'etats, product c'est la fonction produit
        cpt = 0  #compteur pour l'identifiant
        for (s0, s1) in liste_couple_etats: #Pour un couple d'etats dans la liste de couples d'etats
            new_auto.addState(State(cpt, True, s0.fin and s1.fin, label=str((s0.id,s1.id)))) #On ajoute un etat initial et peut etre final si s0 ET s1 sont finaux avec chaine str le couple d'identifiant
            cpt+=1 #on incremente le compteur

        for (s0, s1) in liste_couple_etats: #Pour un couple [...]
            etat_depart = new_auto.listStates[liste_couple_etats.index((s0,s1))] #On creer le couple d'etats d'où part la transition
            for lettre in alphabet: #Pour une lettre dans l'alphabet
                liste_couple_etats_succ = list(product(auto0.succElem(s0,lettre), auto1.succElem(s1,lettre))) #On creer la liste des couples d'etats successeurs 
                for (s2,s3) in liste_couple_etats_succ: #Pour un couple dans la liste des couples d'etats successeurs
                    if (s2,s3)  in liste_couple_etats: #Si le couple est deja dans la liste de couples d'etats 
                        etat_arriver = new_auto.listStates[liste_couple_etats.index((s2,s3))] #On creer le nouveau couple d'etats avec le couple deja dans la liste (celui où arrive la transition)
                    else:  #Si le couple n'est pas deja dans la liste de couples d'etats 
                        liste_couple_etats.append((s2,s3)) #On l'ajoute 
                        etat_arriver = State(cpt, False, s2.fin and s3.fin, label=str((s2.id,s3.id))) #On creer un nouvel etat 
                        new_auto.addState(etat_arriver) #On ajoute le nouvel etat a auto2
                        cpt +=1 #on incremente le compteur
                
                    new_transition = Transition(etat_depart, lettre, etat_arriver) #On creer la nouvelle transition
                    new_auto.addTransition(new_transition) #On ajoute cette transition a new_auto
        return new_auto
        

    @staticmethod
    def union (auto0, auto1): #A refaire
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        print("Appel Fonction union")
        new_auto = Automate([],None) #None pour liste de States None cf _init_ dans automate base
        if (len(auto0.listStates) == 0):                                                                       
            return new_auto
        if (len(auto1.listStates) == 0):
            return new_auto                #Si un des automates n'a pas d'etats return l'automate vide directement

        alphabet=[] #On creer l'alphabet, il faut que les lettres soient dans les 2 automates
        for lettre in auto0.getAlphabetFromTransitions(): #Pour une lettre dans l'alphabet du 1ère automate
            if lettre in auto1.getAlphabetFromTransitions(): #Si le second automate possède cette lettre
                alphabet.append(lettre) #on l'ajoute a l'alphabet

        liste_couple_etats = list(product(auto0.getListInitialStates(), auto1.getListInitialStates())) #On creer une liste de couples d'etats, product c'est la fonction produit
        cpt = 0  #compteur pour l'identifiant
        for (s0, s1) in liste_couple_etats: #Pour un couple d'etats dans la liste de couples d'etats
            new_auto.addState(State(cpt, True, s0.fin or s1.fin, label=str((s0.id,s1.id)))) #On ajoute un etat initial et peut etre final si s0 ET s1 sont finaux avec chaine str le couple d'identifiant
            cpt+=1 #on incremente le compteur

        for (s0, s1) in liste_couple_etats: #Pour un couple [...]
            etat_depart = new_auto.listStates[liste_couple_etats.index((s0,s1))] #On creer le couple d'etats d'où part la transition
            for lettre in alphabet: #Pour une lettre dans l'alphabet
                liste_couple_etats_succ = list(product(auto0.succElem(s0,lettre), auto1.succElem(s1,lettre))) #On creer la liste des couples d'etats successeurs 
                for (s2,s3) in liste_couple_etats_succ: #Pour un couple dans la liste des couples d'etats successeurs
                    if (s2,s3)  in liste_couple_etats: #Si le couple est deja dans la liste de couples d'etats 
                        etat_arriver = new_auto.listStates[liste_couple_etats.index((s2,s3))] #On creer le nouveau couple d'etats avec le couple deja dans la liste (celui où arrive la transition)
                    else:  #Si le couple n'est pas deja dans la liste de couples d'etats 
                        liste_couple_etats.append((s2,s3)) #On l'ajoute 
                        etat_arriver = State(cpt, False, s2.fin or s3.fin, label=str((s2.id,s3.id))) #On creer un nouvel etat 
                        new_auto.addState(etat_arriver) #On ajoute le nouvel etat a auto2
                        cpt +=1 #on incremente le compteur
                
                    new_transition = Transition(etat_depart, lettre, etat_arriver) #On creer la nouvelle transition
                    new_auto.addTransition(new_transition) #On ajoute cette transition a new_auto
        return new_auto

   
   

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        print("Appel fonction concatenation")    
        
        A = copy.deepcopy(auto1)
        
        A0 = copy.deepcopy(auto1)
        
        A1 = copy.deepcopy(auto2)
        
        cpt = 0
        
        L = []
                    
        for s in A0.listStates :
            if(s.init == True) :
                tmp = s.id
            if(s.fin == True) :
                s.fin = False
            cpt = s.id
            
        cpt += 1
        tmp1 = cpt-1   
        for etat in A1.listStates :
            etat.id = cpt
            s = State(cpt, etat.init, etat.fin, etat.label)
            A0.addState(s)
            if(etat.init == True) :
                s1 = State(cpt, etat.init, etat.fin, etat.label)
            cpt += 1
            for transition in A1.listTransitions :
                A0.addTransition(transition)
            for t in A.listTransitions :
                if(t.stateDest.id == tmp or t.stateDest.id == tmp1 and etat.init == True) :
                    A0.addTransition(Transition(t.stateSrc, t.etiquette, s1))
                    
        return A0
        
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        print("Appel fonction etoile")
        return




