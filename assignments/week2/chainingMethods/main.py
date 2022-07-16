class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\nMember? {self.is_reward_member}\nGold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_reward_member == False:
            self.is_reward_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name} is already enrolled.")
        return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print(f"{self.first_name} has insufficient points.")
        return self

user_Angela = User("Angela", "Bereski", "angelakbereski@gmail.com", 35)

user_Angela.display_info().enroll().spend_points(50).display_info().enroll()

user_Kyle = User("Kyle", "Ogilvie", "kogilvie686@gmail.com", 37)

user_Marshall = User("Marshall", "Hoke", "m.p.hoke@gmail.com", 34)

user_Kyle.enroll().spend_points(80).display_info()

user_Marshall.display_info().spend_points(40)