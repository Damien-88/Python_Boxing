from datetime import time

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
        self.technique = ""
        self.jab_hit = self.name + " Jab Hit +5 "
        self.jab_blocked = self.name + " Jab Blocked +5 "
        self.jab_dodged = self.name + " Jab Dodged +5 "
        self.punch_hit = self.name + " Punch Hit +10 "
        self.punch_blocked = self.name + " Punch Blocked +10 "
        self.punch_dodged = self.name + " Punch Dodged +10 "
        self.hook_hit = self.name + " Hook Hit +15 "
        self.hook_blocked = self.name + " Hook Blocked +15 "
        self.hook_dodged = self.name + " Hook Dodged +15 "
        self.uppercut_hit = self.name + " Uppercut Hit +20 "
        self.uppercut_blocked = self.name + " Uppercut Blocked +20 "
        self.uppercut_dodged = self.name + " Uppercut Dodged +20 "

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

    def weight_categories(self):

        if self.weight > 200:
            self.weight_class = " Heavyweight "
        elif self.weight > 175:
            self.weight_class = " Cruiserweight "
        elif self.weight > 168:
            self.weight_class = " Light Heaveyweight "
        elif self.weight > 160:
            self.weight_class = " Super Middleweight "
        elif self.weight > 154:
            self.weight_class = " Middleweight "
        elif self.weight > 147:
            self.weight_class = " Super Welterweight "
        elif self.weight > 140:
            self.weight_class = " Welterweight "
        elif self.weight > 135:
            self.weight_class = " Super Lightweight "
        elif self.weight > 130:
            self.weight_class = " Lightweight "
        elif self.weight > 126:
            self.weight_class = " Super Featerweight "
        elif self.weight > 122:
            self.weight_class = " Featerweight "
        elif self.weight > 118:
            self.weight_class = " Super Bantamweight "
        elif self.weight > 115:
            self.weight_class = " Bantamweight "
        elif self.weight > 112:
            self.weight_class = " Super Flyweight "
        elif self.weight > 105:
            self.weight_class = " Flyweight "
        else:
            self.weight_class = " Too Light "

        return self.weight_class

    def jab(self, location):

        self.technique = "jab"
        self.area = location

        if self.right_handed:
            self.side = "left"
        else:
            self.side = "right"

    def punch(self, location):

        self.technique = "punch"
        self.area = location

        if self.right_handed:
            self.side = "right"
        else:
            self.side = "left"

    def upper_cut(self, hand):

        self.technique = "upper_cut"
        self.area = "high"
        self.side = hand

    def hook(self, location, hand):

        self.technique = "hook"
        self.area = location
        self.side = hand

    def block(self, location):
        self.technique = "block"
        self.area = location
        self.side = "null"

    def dodge(self, direction):
        self.technique = "dodge"
        self.area = "null"
        self.side = direction

    def hit(self, other_fighter, multiple, add):
        self.hits.append(5 * multiple)
        self.stamina -= (2 + add)
        other_fighter.hp -= 5 * multiple
        other_fighter.stamina -= 5 * multiple

    def blocked(self, other_fighter, multiple, add):
        self.stamina -= (2 + add)
        other_fighter.blocks.append(5 * multiple)
        other_fighter.stamina -= (2 + add)

    def counter(self, other_fighter, multiple):
        self.stamina -= 5 * multiple
        other_fighter.stamina -= 5 * multiple

    def hit_or_blocked(self, other_fighter):

        if self.technique == "jab":

            if other_fighter.technique == "block":
                if self.area != other_fighter.area:
                    self.hit(other_fighter, 1, 0)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.jab_blocked

            elif other_fighter.technique == "dodge":
                if self.side != other_fighter.side:
                    self.hit(other_fighter, 1, 0)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.jab_dodged

            else:
                if self.area != other_fighter.area:
                    if other_fighter.technique == "punch":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 2, 3)
                        return self.technique_hit + other_fighter.punch_hit
                    elif other_fighter.technique == "hook":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 3, 8)
                        return self.technique_hit + other_fighter.hook_hit
                    elif other_fighter.technique == "upper cut":
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 4, 13)
                        return self.technique_hit + other_fighter.uppercut_hit
                    else:
                        self.hit(other_fighter, 1, 0)
                        other_fighter.hit(self, 1, 0)
                        return self.technique_hit + other_fighter.technique_hit
                else:
                    if self.side != other_fighter.side:
                        if other_fighter.technique == "punch":
                            self.hit(other_fighter, 1, 0)
                            other_fighter.hit(self, 2, 3)
                            return self.technique_hit + other_fighter.punch_hit
                        elif other_fighter.technique == "hook":
                            self.hit(other_fighter, 1, 0)
                            other_fighter.hit(self, 3, 8)
                            return self.technique_hit + other_fighter.hook_hit
                        elif other_fighter.technique == "upper cut":
                            self.hit(other_fighter, 1, 0)
                            other_fighter.hit(self, 4, 13)
                            return self.technique_hit + other_fighter.uppercut_hit
                        else:
                            self.hit(other_fighter, 1, 0)
                            other_fighter.hit(self, 1, 0)
                            return self.technique_hit + other_fighter.technique_hit
                    else:
                        self.counter(other_fighter, 1)
                        return self.technique.capitalize() + "countered"

        elif self.technique == "punch":

            if other_fighter.technique == "block":
                if self.area != other_fighter.area:
                    self.hit(other_fighter, 2, 3)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.punch_blocked

            elif other_fighter.technique == "dodge":
                if self.side != other_fighter.side:
                    self.hit(other_fighter, 2, 3)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 1, 0)
                    return other_fighter.punch_dodged

            else:
                if self.area != other_fighter.area:
                    if other_fighter.technique == "jab":
                        self.hit(other_fighter, 2, 3)
                        other_fighter.hit(self, 1, 0)
                        return self.technique_hit + other_fighter.jab_hit
                    elif other_fighter.technique == "hook":
                        self.hit(other_fighter, 2, 3)
                        other_fighter.hit(self, 3, 8)
                        return self.technique_hit + other_fighter.hook_hit
                    elif other_fighter.technique == "upper cut":
                        self.hit(other_fighter, 2, 3)
                        other_fighter.hit(self, 4, 13)
                        return self.technique_hit + other_fighter.uppercut_hit
                    else:
                        self.hit(other_fighter, 2, 3)
                        other_fighter.hit(self, 2, 3)
                        return self.technique_hit + other_fighter.technique_hit
                else:
                    if self.side != other_fighter.side:
                        if other_fighter.technique == "jab":
                            self.hit(other_fighter, 2, 3)
                            other_fighter.hit(self, 1, 0)
                            return self.technique_hit + other_fighter.jab_hit
                        elif other_fighter.technique == "hook":
                            self.hit(other_fighter, 2, 3)
                            other_fighter.hit(self, 3, 8)
                            return self.technique_hit + other_fighter.hook_hit
                        elif other_fighter.technique == "upper cut":
                            self.hit(other_fighter, 2, 3)
                            other_fighter.hit(self, 4, 13)
                            return self.technique_hit + other_fighter.uppercut_hit
                        else:
                            self.hit(other_fighter, 2, 3)
                            other_fighter.hit(self, 2, 3)
                            return self.technique_hit + other_fighter.technique_hit
                    else:
                        self.counter(other_fighter, 1)
                        return self.technique.capitalize() + "countered"

        elif self.technique == "hook":

            if other_fighter.technique == "block":
                if self.area != other_fighter.area:
                    self.hit(other_fighter, 3, 8)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 2, 3)
                    return other_fighter.hook_blocked

            elif other_fighter.technique == "dodge":
                if self.side != other_fighter.side:
                    self.hit(other_fighter, 3, 8)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 2, 3)
                    return other_fighter.hook_dodged

            else:
                if self.area != other_fighter.area:
                    if other_fighter.technique == "punch":
                        self.hit(other_fighter, 3, 8)
                        other_fighter.hit(self, 2, 3)
                        return self.technique_hit + other_fighter.punch_hit
                    elif other_fighter.technique == "jab":
                        self.hit(other_fighter, 3, 8)
                        other_fighter.hit(self, 1, 0)
                        return self.technique_hit + other_fighter.jab_hit
                    elif other_fighter.technique == "upper cut":
                        self.hit(other_fighter, 3, 8)
                        other_fighter.hit(self, 4, 13)
                        return self.technique_hit + other_fighter.uppercut_hit
                    else:
                        self.hit(other_fighter, 3, 8)
                        other_fighter.hit(self, 3, 8)
                        return self.technique_hit + other_fighter.technique_hit
                else:
                    if self.side != other_fighter.side:
                        if other_fighter.technique == "punch":
                            self.hit(other_fighter, 3, 8)
                            other_fighter.hit(self, 2, 3)
                            return self.technique_hit + other_fighter.punch_hit
                        elif other_fighter.technique == "jab":
                            self.hit(other_fighter, 3, 8)
                            other_fighter.hit(self, 1, 0)
                            return self.technique_hit + other_fighter.jab_hit
                        elif other_fighter.technique == "upper cut":
                            self.hit(other_fighter, 3, 8)
                            other_fighter.hit(self, 4, 13)
                            return self.technique_hit + other_fighter.uppercut_hit
                        else:
                            self.hit(other_fighter, 3, 8)
                            other_fighter.hit(self, 3, 8)
                            return self.technique_hit + other_fighter.technique_hit
                    else:
                        self.counter(other_fighter, 2)
                        return self.technique.capitalize() + "countered"

        elif self.technique == "upper_cut":

            if other_fighter.technique == "block":
                if self.area != other_fighter.area:
                    self.hit(other_fighter, 4, 13)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 2, 3)
                    return other_fighter.uppercut_blocked

            elif other_fighter.technique == "dodge":
                if self.side != other_fighter.side:
                    self.hit(other_fighter, 4, 13)
                    return self.technique_hit
                else:
                    self.blocked(other_fighter, 2, 3)
                    return other_fighter.uppercut_dodged

            else:
                if self.area != other_fighter.area:
                    if other_fighter.technique == "punch":
                        self.hit(other_fighter, 4, 13)
                        other_fighter.hit(self, 2, 3)
                        return self.technique_hit + other_fighter.punch_hit
                    elif other_fighter.technique == "hook":
                        self.hit(other_fighter, 4, 13)
                        other_fighter.hit(self, 3, 13)
                        return self.technique_hit + other_fighter.hook_hit
                    elif other_fighter.technique == "jab":
                        self.hit(other_fighter, 4, 13)
                        other_fighter.hit(self, 1, 0)
                        return self.technique_hit + other_fighter.jab_hit
                    else:
                        self.hit(other_fighter, 4, 13)
                        other_fighter.hit(self, 4, 13)
                        return self.technique_hit + other_fighter.technique_hit
                else:
                    if self.side != other_fighter.side:
                        if other_fighter.technique == "punch":
                            self.hit(other_fighter, 4, 13)
                            other_fighter.hit(self, 2, 3)
                            return self.technique_hit + other_fighter.punch_hit
                        elif other_fighter.technique == "hook":
                            self.hit(other_fighter, 4, 13)
                            other_fighter.hit(self, 3, 8)
                            return self.technique_hit + other_fighter.hook_hit
                        elif other_fighter.technique == "jab":
                            self.hit(other_fighter, 4, 13)
                            other_fighter.hit(self, 1, 0)
                            return self.technique_hit + other_fighter.jab_hit
                        else:
                            self.hit(other_fighter, 4, 13)
                            other_fighter.hit(self, 4, 13)
                            return self.technique_hit + other_fighter.technique_hit
                    else:
                        self.counter(other_fighter, 2)
                        return self.technique.capitalize() + "countered"

        elif self.technique == "block":

            if other_fighter.technique == "block":
                
                return "Double Block"

            elif other_fighter.technique == "dodge":
                
                return "Block Dodge"

            elif self.area != other_fighter.area:
                if other_fighter.technique == "jab":
                    other_fighter.hit(self, 1, 0)
                    return other_fighter.jab_hit
                elif other_fighter.technique == "punch":
                    other_fighter.hit(self, 2, 3)
                    return other_fighter.punch_hit
                elif other_fighter.technique == "hook":
                    other_fighter.hit(self, 3, 8)
                    return self.technique_hit + other_fighter.jab_hit
                elif other_fighter.technique == "upper cut":
                    other_fighter.hit(self, 4, 13)
                    return other_fighter.uppercut_hit
                else:
                    return "Miss"
            
            else:
                if other_fighter.technique == "jab":
                    other_fighter.blocked(self, 1, 0)
                    return self.jab_blocked
                elif other_fighter.technique == "punch":
                    other_fighter.blocked(self, 1, 0)
                    return self.punch_blocked
                elif other_fighter.technique == "hook":
                    other_fighter.blocked(self, 2, 3)
                    return self.hook_blocked
                else:
                    other_fighter.blocked(self, 2, 3)
                    return self.uppercut_blocked

        elif self.technique == "dodge":

            if other_fighter.technique == "block":
                
                return "Dodge Block"

            elif other_fighter.technique == "dodge":
                
                return "Double Dodge"

            elif self.area != other_fighter.area:
                if other_fighter.technique == "jab":
                    other_fighter.hit(self, 1, 0)
                    return other_fighter.jab_hit
                elif other_fighter.technique == "punch":
                    other_fighter.hit(self, 2, 3)
                    return other_fighter.punch_hit
                elif other_fighter.technique == "hook":
                    other_fighter.hit(self, 3, 8)
                    return self.technique_hit + other_fighter.jab_hit
                elif other_fighter.technique == "upper cut":
                    other_fighter.hit(self, 4, 13)
                    return other_fighter.uppercut_hit
                else:
                    return "Miss"
            
            else:
                if other_fighter.technique == "jab":
                    other_fighter.blocked(self, 1, 0)
                    return self.jab_dodged
                elif other_fighter.technique == "punch":
                    other_fighter.blocked(self, 1, 0)
                    return self.punch_dodged
                elif other_fighter.technique == "hook":
                    other_fighter.blocked(self, 2, 3)
                    return self.hook_dodged
                else:
                    other_fighter.blocked(self, 2, 3)
                    return self.uppercut_dodged

        else:

            return "Miss"

    def rest(self, rounds):
        if rounds.round == 2:
            if self.hp < 0.75 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2)):
                self.hp = 0.75 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2))
            else:
                self.hp = 100 + (self.level * 10 + self.wins * 5 - self.losses * 2)
        elif rounds.round >= 3:
            if self.hp < 0.5 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2)):
                self.hp = 0.5 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2))
            elif self.hp < 0.75 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2)):
                self.hp = 0.75 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2))

    def dazed(self):
        return "Dazed"

    def down(self):
        count = 10
        if self.hp > 0.2 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2)):
            count = 7
        elif self.hp > 0.1 * (100 + (self.level * 10 + self.wins * 5 - self.losses * 2)):
            count = 5
        elif self.hp > 10:
            count = 2
        else:
            count = 0
        self.hp -= 10
        return count

    def tko(self):
        self.concious = False
        return self.name + " is KO'd"

    def match_end(self, other_fighter):
        if self.concious and other_fighter.concious:
            for hit in self.hits:
                self.score += hit
            for block in self.blocks:
                self.score += block
            for h in other_fighter.hits:
                other_fighter.score += h
            for b in other_fighter.blocks:
                other_fighter.score += b
            if self.score > other_fighter.score:
                self.wins += 1
                self.level += 1
                other_fighter.losses += 1
                return self.name + " WINS!"
            elif other_fighter.score > self.score:
                other_fighter.wins += 1
                other_fighter.level += 1
                self.losses += 1
                return other_fighter.name + "WINS!"
            else:
                return "Draw"

class Rounds:

    def __init__(self):
        self.round = 1

    def __repr__(self):
        return "ROUND: " + str(self.round)

    def round_change(self):
        self.round += 1
        return self.timer(180)
            
    def cool_down(self):
        return self.timer(30)

    def timer(start, boxer_1, boxer_2):
        while start:
            mins, secs = divmod(start, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end = "\r")
            time.sleep(1)
            start -= 1
            if boxer_1.concious == False or boxer_2.concious == False:
                break

boxer_1 = Boxer("Bob", 177, "6' 1\"", 28)

boxer_2 = Boxer("Ted", 182, "5' 10\"", 36, False)