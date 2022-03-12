"""
    CSE 231 proj 11 to simulate pokemon battle
"""

from random import randint
import random
import csv


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
        name=str(self.name)
            
        '''
            Retrurn the name of the move for printing
        '''        
        return name
        pass

    def __repr__(self):
        name = str(self.name)
        return name
        pass
        '''
            return name of move for display in shell
        '''
    
    def get_name(self):
        '''
            return name attribute
        '''
        return self.name
        pass
    def get_element(self):
        '''
            this will return the element attribute
        '''
        return self.element
        pass
    
    def get_power(self):
        return self.power
        pass
        '''
            returns the power attribute
        '''
    
    def get_accuracy(self):
        return self.accuracy
        pass
        '''
            Returns the accuracy attribute
        '''
    
    def get_attack_type(self):
        return self.attack_type
        pass
        '''
            Returns the attack type- 1,2,3
        '''

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        

class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        return_str = ""
        return_str+="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(self.name+self.hp+self.patt+self.pdef+self.satt+self.sdef)
        return_str+= "{:<15}{:<15}\n"(self.element1+self.element2)
        if 0<self.get_number_moves():
            return_str+= " "
            for move in self.get_moves():
                return_str+= "{:<15}".format(str(move))
            return return_str
            pass
        '''
            returns parts of the pokemon object in 3 lines. First line has name, hp, pokemon attack and defence
            2nd line has the elements and 3rd has the moves
        '''

    def __repr__(self):
        return_str=""
        return_str+="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(self.name, self.hp, self.patt, self.pdef, self.satt, self.sdef)
        return_str+= "{:<15}{:<15}\n".format(self.element1,self.element2)
        if 0<self.get_number_moves():
            return_str+= " "
            for move in self.get_moves():
                return_str+= "{:<15}".format(str(move))
        return return_str
        pass
        '''
            same as __str__ but for shell
        '''
        
    def get_name(self):
        return self.name
        pass
    
        '''
            returns name attribute
        '''
    def get_element1(self):
        return self.element1
        pass
        '''
            return the element 1 attribute
        '''
    
    def get_element2(self):
        return self.element2
        pass
        '''
            return the element 2 attribute
        '''
    
    def get_hp(self):
        return self.hp
        pass
        '''
            returns hp attribute
        '''
    
    def get_patt(self):
        return self.patt
        pass
        '''
            return patt attribute
        '''

    def get_pdef(self):
        return self.pdef
        pass
        '''
            return the pdef attribute
        '''

    def get_satt(self):
        return self.satt
        pass
        '''
            return the satt attribute
        '''

    def get_sdef(self):
        return self.sdef
        pass
        '''
            return sdef attribute
        '''
        pass
    
    def get_moves(self):
        return self.moves
        pass
        '''
            returns the moves list attribute
        '''

    def get_number_moves(self):
        
        return len(self.moves)
        pass
        '''
            returns number of moves
        '''

    def choose(self,index):
        try:
            return self.moves[index]
        except:
            return None
        return None
        pass
        '''
            indexes and returns the chosen move
        '''
    def show_move_elements(self):
        pass
        '''
            display the element of the move
        '''


    def show_move_power(self):
        pass
        '''
            displays the power of the pokemons move
        '''

    def show_move_accuracy(self):
        pass
        '''
            function to get accuracy of move
        '''

    def add_move(self, move):
        #set x to the number of move function
        #check if x is less than or equal to 3
        #if x <= 3:
        #self.moves.append(move)
        #'''Adds the move parameter to moves list if pokemon has 3 or less moves'''
        number_of_moves = self.get_number_moves()
        if number_of_moves != None and number_of_moves < 4:
            self.moves.append(move) #adds move to list of moves
        pass


    def attack(self, move, opponent):
        '''This method takes the move used by the attacker (self) 
        and deals damage to the opponent (who should also be an instance 
        of class Pokemon). It does not return anything'''
        mp = 0 # the power of the move
        a = 0 #The patt or satt of the attacking Pokemon
        d = 0 #The pdef or sdef of the defending Pokemon
        mdf=1.0 #takes into effect same-type attack bonus (STAB) 
        #if move is super effective or not effective.
        rand2 = randint(1,100)
        mp = move.get_power()
        attype = move.get_attack_type()
        if attype == 2:
            a = self.get_patt()
            d= opponent.get_pdef()
 
            pass
        elif attype ==3:
            a = self.get_satt()
            d= opponent.get_sdef() 
            pass 
        else:
            print( "Invalid attack_type, turn skipped.")
            return None
        if rand2 > move.get_accuracy(): #if rand is greater than the move accuracy you have missed
            print("Move missed!")
            return None
        pass
        elem1 = opponent.get_element1()
        move_elem = move.get_element()
        selfelem1 = self.get_element1()
        elem2 = opponent.get_element2()
        move_elem = move.get_element()
        selfelem2 = self.get_element2()
 
        if elem1 in is_effective_dictionary[move_elem]: #deals the damage
            mdf = mdf*2
        if elem2 in is_effective_dictionary[move_elem]: #deals the damage
            mdf = mdf*2
        if elem1 in not_effective_dictionary[move_elem]: #deals the damage
            mdf = mdf/2
        if elem2 in not_effective_dictionary[move_elem]:#deals the damage
            mdf = mdf/2
        if elem1 in no_effect_dictionary[move_elem]:
            mdf = 0
            return None
        if elem2 in no_effect_dictionary[move_elem]:
            mdf = 0
            return None
        if mdf<1:
            print("Not very effective...")
        elif mdf>1:
            print("It's super effective!!!!")
        if move_elem == selfelem1:
            mdf=mdf*1.5
        elif move_elem == selfelem2:
            mdf=mdf*1.5
            damage = mp*a*20/d/50
            damage = damage+2
            damage = damage*mdf
            damage = int(damage)
            opponent.subtract_hp(damage)
            
        
    def subtract_hp(self,damage):
        self.hp=self.hp-damage
        if self.hp<=0:
            self.hp=0
        else:
            pass
        pass
        '''
            Subracts hp from pokemon
        '''