# 게임시나리오 : 스타크래프트 시뮬레이션

#Unit 부모클래스 선언
class Unit:
    def __init__(self, name, energy, is_fly):
        self.name = name
        self.energy = energy
        self.is_fly = is_fly

    def get_tribe(self):
        print(self.name + 'is a basic tribe!!')

    def get_energy(self):
        if self.energy > 0:
            print(self.name + '의 현재는 에너지는 ', self.energy,'입니다!')
        else:
            print(self.name + '유닛은 전사했습니다. ㅜㅜ')
        #return self.energy



# 테란종족 클래스
class Terran(Unit):
    def get_tribe(self):
        print(self.name + 'is a Terran !!')
    def be_attactted(self):
        self.energy -= 3

# 프로토스 종족  클래스
class Protoss(Unit):
    def get_tribe(self):
        print(self.name + 'is a Protoss !!')
    def be_attactted(self):
        self.energy -= 2

# 저그종족 클래스
class Zerg(Unit):
    def get_tribe(self):
        print(self.name + 'is a Zerg !!')
    def be_attactted(self):
        self.energy -= 4


# 종족별유닛생성
marine  = Terran('마린', 15, False)
corsair = Protoss('커세어', 20, True)
hydra   = Zerg('히드라', 10,False)

print('현재의에너지!!! \n-------------------')
marine.get_energy()
corsair.get_energy()
hydra.get_energy()

# 게임어택시뮬레이션
for x in range (3):
    marine.be_attactted()
    corsair.be_attactted()
    hydra.be_attactted()

    print('\n*', x+1, '차공격받은후의에너지!!! \n----------------------------')
    marine.get_energy()
    corsair.get_energy()
    hydra.get_energy()

print('\nGame Over !!!')