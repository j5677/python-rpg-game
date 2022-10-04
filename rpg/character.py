
class Character():
    def __init__(self):
        self.name = 'player'
        self.strength = 0
        self.intelligence = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = 'human'
        self.Class = 'fighter'
        self.level = 1
        self.hitPointMax = 100
        self.movement = 0
        self.armor = 0
        self.xp = 0
        self.type = 0
        self.currentWeapon = 'dagger'
        self.currentArmor = 'leather'

    def SetCurrentWeapon(self):
        pass

    def RollToHit(self):
        pass

    def rollForDamage(self):
        pass

    def getAC(self):
        pass

    def getMovement(self):
        pass

    def getAbilityBonuses(self):
        pass
    