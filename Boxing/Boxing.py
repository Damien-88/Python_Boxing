class Boxer:

    def __init__(self, new_name, new_weight, new_height, new_age, new_right_handed = True):
        
        self.name = new_name
        self.weight = new_weight
        self.height = new_height
        self.age = new_age
        self.weight_class = ""
        self.wins = 0
        self.losses = 0
        self.level = 1
        self.hp = 100 + (self.level * 10 + self.wins * 5 - self.losses * 2)
        self.stamina = 100 + (self.level * 10 + self.wins * 5 - self.losses * 2)
        self.concious = True
        self.right_handed = new_right_handed
        self.hits = []
        self.blocks = []
        self.score = 0
        self.area = ""
        self.side = ""
        self.type = ""

    def __repr__(self):
        
        return """
        Name: {}
        Class: {}
        Weight: {}
        Height: {}
        Age: {}
        Wins: {}
        Losses: {}
        """.format(
            self.name, self.weight_class, self.weight, self.height, self.age, self.wins, 
            self.losses
            )

    def jab(self, location, hand):

        self.type = "jab"
        self.area = location
        self.side = hand


    def punch(self, other_boxer, location, hand):

        self.type = "punch"
        self.area = location
        self.side = hand

    def upper_cut(self, other_boxer, hand):

        self.type = "upper_cut"
        self.area = "high"
        self.side = hand

    def hook(self, other_boxer, location, hand):

        self.type = "hook"
        self.area = location
        self.side = hand

    def block(self, other_boxer, location):
        self.type = "block"
        self.area = location
        self.side = "null"

    def dodge(self, other_boxer, direction):
        self.type = "dodge"
        self.area = "null"
        self.side = direction

    def hit(self, other_fighter, multiple, add):
        self.hits.append(5 * multiple)
        self.stamina -= (2 + add) * multiple 
        other_fighter.hp -= 5 * multiple
        other_fighter.stamina -= 5 * multiple

    def blocked(self, other_fighter, multiple, add):
        self.stamina -= (2 + add) * multiple
        other_fighter.blocks.append(5 * multiple)
        other_fighter.stamina -= (2 + add) * multiple

    def counter(self, other_fighter, multiple):
        self.stamina -= 5 * multiple
        other_fighter.stamina -= 5 * multiple

    def hit_or_blocked(self, other_fighter):

        if self.type == other_fighter.type:
            pass

        elif self.type == "jab":

            if other_fighter.type == "block":
                if self.area != other_fighter.area:
                    self.hit(other_fighter, 1, 0)
                    return self.name + " Hit +5"
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.name + "Blocked +5"
            elif other_fighter.type == "dodge":
                if self.side != other_fighter.side:
                    self.hit(other_fighter, 1, 0)
                    return self.name + " Hit +5"
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.name + "Dodged +5"
            else:
                if self.area != other_fighter.area:
                    if other_fighter.area == "punch":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 2, 3)
                    elif other_fighter.area == "hook":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 3, 3)
                    elif other_fighter.area == "upper cut":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 4, 3)
                else:
                    if self.side != other_fighter.side:
                        pass
                    else:
                        self.counter(other_fighter, 1)

        elif self.type == "punch":
            if other_fighter.type == "block":
                pass
            elif other_fighter.type == "dodge":
                pass
            else:
                pass
        elif self.type == "upper_cut":
            if other_fighter.type == "block":
                pass
            elif other_fighter.type == "dodge":
                pass
            else:
                pass
        elif self.type == "hook":
            if other_fighter.type == "block":
                pass
            elif other_fighter.type == "dodge":
                pass
            else:
                pass
        elif self.type == "block":
            pass
        elif self.type == "dodge":
            pass
        else:
            return "Nothing"

    def hold(self, other_boxer, ref):
        pass

    def rest(self, ring):
        pass

    def dazed(self, other_boxer, ref):
        pass

    def tko(self, other_boxer, ref):
        pass

    def win(self, other_boxer, ref):
        pass


class Referee:

    def __init__(self):
        pass

    def begin_round(self):
        pass

    def break_up(self, boxer_one, boxer_two):
        pass

    def count(self):
        pass

    def call_match(self):
        pass

    def match_time(self):
        pass

class Ring:

    def __init__(self):
        pass