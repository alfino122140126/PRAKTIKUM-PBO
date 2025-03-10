import random
import time

class Robot:
    def __init__(self, name, hp=100, attack=15):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense_active = False
    
    def basic_attack(self, enemy):
        if random.random() <= 0.8:
            damage = self.attack
            
            if enemy.defense_active:
                blocked_damage = damage // 2 
                actual_damage = damage - blocked_damage
                hp_gained = blocked_damage // 2
                
                enemy.hp = min(enemy.max_hp, enemy.hp + hp_gained)
                print(f"{enemy.name} menahan {blocked_damage} damage dan mendapatkan {hp_gained} HP!")
                
                enemy.defense_active = False
                
                if actual_damage > 0:
                    enemy.hp = max(0, enemy.hp - actual_damage)
                    print(f"{self.name} menyerang {enemy.name} dan mengurangi {actual_damage} HP!")
            else:
                enemy.hp = max(0, enemy.hp - damage)
                print(f"{self.name} menyerang {enemy.name} dan mengurangi {damage} HP!")
                
            return damage
        else:
            print(f"{self.name} mencoba menyerang {enemy.name} tetapi meleset!")
            return 0
    
    def special_attack(self, enemy):
        if random.random() <= 0.6:
            damage = int(self.attack * 1.8)

            if enemy.defense_active:
                blocked_damage = damage // 3
                actual_damage = damage - blocked_damage
                hp_gained = blocked_damage // 2
                
                enemy.hp = min(enemy.max_hp, enemy.hp + hp_gained)
                print(f"{enemy.name} menahan {blocked_damage} damage dan mendapatkan {hp_gained} HP!")
                
                enemy.defense_active = False
                enemy.hp = max(0, enemy.hp - actual_damage)
                print(f"{self.name} menggunakan PLASMA CANNON dan menyerang {enemy.name} dengan {actual_damage} damage!")
            else:
                enemy.hp = max(0, enemy.hp - damage)
                print(f"{self.name} menggunakan PLASMA CANNON dan menyerang {enemy.name} dengan {damage} damage!")
            
            return True
        else:
            print(f"{self.name} gagal menggunakan PLASMA CANNON!")
            return False
    
    def activate_defense(self):
        self.defense_active = True
        print(f"{self.name} mengaktifkan mode PERTAHANAN!")
        return True
    
    def is_alive(self):
        return self.hp > 0
    
    def status(self):
        status_text = f"{self.name}: HP={self.hp}/{self.max_hp}"
        if self.defense_active:
            status_text += " [DEFENSE]"
        return status_text


class Game:
    def __init__(self, robot1, robot2, max_rounds=15):
        self.robot1 = robot1
        self.robot2 = robot2
        self.current_round = 0
        self.max_rounds = max_rounds
    
    def display_status(self):
        print("\n" + "-"*40)
        print(f"RONDE {self.current_round}")
        print(self.robot1.status())
        print(self.robot2.status())
        print("-"*40)
    
    def player_turn(self, robot, enemy):
        print(f"\nPilih tindakan untuk {robot.name}:")
        print("1. Basic Attack")
        print("2. Plasma Cannon")
        print("3. Bertahan")
        
        while True:
            choice = input("Pilihan (1-3): ")
            if choice in ["1", "2", "3"]:
                choice = int(choice)
                break
            else:
                print("Masukkan angka 1-3!")
        
        if choice == 1:
            robot.basic_attack(enemy)
        elif choice == 2:
            robot.special_attack(enemy)
        elif choice == 3:
            robot.activate_defense()
    
    def ai_turn(self, robot, enemy):
        print(f"\nGiliran {robot.name}:")

        if robot.hp < robot.max_hp * 0.4 and random.random() < 0.6: 
            robot.activate_defense()
        elif random.random() < 0.3: 
            robot.special_attack(enemy)
        elif random.random() < 0.3: 
            robot.activate_defense()
        else: 
            robot.basic_attack(enemy)
    
    def play(self, player_robot=1):
        print("\n" + "="*40)
        print("PERTARUNGAN JAEGER DIMULAI!")
        print("="*40)
        
        while self.current_round < self.max_rounds:
            self.current_round += 1
            self.display_status()

            if player_robot == 1:
                self.player_turn(self.robot1, self.robot2)

                if not self.robot2.is_alive():
                    print(f"\n{self.robot2.name} hancur!")
                    print(f"{self.robot1.name} memenangkan pertarungan!")
                    break

                self.ai_turn(self.robot2, self.robot1)

                if not self.robot1.is_alive():
                    print(f"\n{self.robot1.name} hancur!")
                    print(f"{self.robot2.name} memenangkan pertarungan!")
                    break
            else:
                self.ai_turn(self.robot1, self.robot2)

                if not self.robot2.is_alive():
                    print(f"\n{self.robot2.name} hancur!")
                    print(f"{self.robot1.name} memenangkan pertarungan!")
                    break

                self.player_turn(self.robot2, self.robot1)

                if not self.robot1.is_alive():
                    print(f"\n{self.robot1.name} hancur!")
                    print(f"{self.robot2.name} memenangkan pertarungan!")
                    break

        if self.current_round >= self.max_rounds:
            print("\nPertarungan berakhir karena mencapai batas maksimum ronde!")
            if self.robot1.hp > self.robot2.hp:
                print(f"{self.robot1.name} menang berdasarkan HP tersisa!")
            elif self.robot2.hp > self.robot1.hp:
                print(f"{self.robot2.name} menang berdasarkan HP tersisa!")
            else:
                print("Pertarungan berakhir seri!")
        
        print("\n" + "="*40)
        print("PERTARUNGAN SELESAI")
        print("="*40)


def main():
    robot1 = Robot("Gipsy Danger", hp=120, attack=20)
    robot2 = Robot("Striker Eureka", hp=100, attack=25)

    game = Game(robot1, robot2, max_rounds=15)

    print("Pilih Jaeger yang ingin Anda kendalikan:")
    print("1. Gipsy Danger")
    print("2. Striker Eureka")
    
    player_choice = 0
    while player_choice not in [1, 2]:
        choice = input("(1/2): ")
        if choice in ["1", "2"]:
            player_choice = int(choice)
        else:
            print("Pilihan tidak valid, masukkan 1 atau 2.")

    game.play(player_choice)


if __name__ == "__main__":
    main()