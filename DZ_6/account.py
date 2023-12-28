# реализовать класс Account: абстракция базового поведения банковского аккаунта:
# ● создание банковского аккаунта с параметрами: имя, стартовый баланс с которым зарегистрирован аккаунт, история
# операций;
# ● реализация двух методов, которые позволяют положить деньги на счет,
# или снять деньги с счета;
# ● продумать, как можно было бы хранить историю поступления или снятия
# денег, чтобы с ней можно было удобно работать.

import logging


class Account:
    def __init__(self, name: str, start_balance: float):
        self.name = name
        self.start_balance = start_balance
        self.history = None
        logging.basicConfig(
                            filename=f'{self.name}.log',
                            format='[%(asctime)s]: %(message)s',
                            level=logging.INFO
        )

    def run_point(self):
        print(f'Hello, citizen {self.name}! \nYour balance now is: {self.start_balance:.2f}')
        try:
            self.citizen_choice: int = int(input('For add money press digit 1. For delete money press digit 2. Show history: press digit 3. Your choice: '))
        except Exception:
            print('It is not digit, please, try again.')
            self.run_point()
        finally:
            match self.citizen_choice:
                case 1:
                    print('Your chose 1. Let is add some money!')
                    self.add_money()
                case 2:
                    print('Your chose 2. Let is delete some money!')
                    self.take_off_money()
                case 3:
                    print('Your chose 3. Let is see history!\n')
                    with open(f'{self.name}.log', 'r') as file:
                        for line in file:
                            print(line, end='')
                case _:
                    print('Unknown digit.')
        self.cycle()

    def add_money(self) -> None:
        try:
            self.got_money: float = float(input('Add some money (for example: 0000.00): '))
        except Exception:
            print(f'Type of input for add is not float! Try again.')
            self.add_money()

        self.start_balance += self.got_money
        print(f'Balance now after added: {self.start_balance:.2f}')
        logging.info(f'Citizen {self.name} increased your balance by {self.got_money:.2f} \nNow his balance is: {self.start_balance:.2f}')
        self.cycle()

    def take_off_money(self):
        try:
            self.lose_money: float = float(input('Input some money for withdraw (for example: 0000.00): '))
        except Exception:
            print(f'Type of input for delete is not float! Try again.')
            self.take_off_money()

        if self.lose_money > self.start_balance:
            print('Sorry! Not enough money on your balance!')
        else:
            self.start_balance -= self.lose_money
            print(f'Balance now after withdraw: {self.start_balance:.2f}')
            logging.info(f'Citizen {self.name} reduced your balance by {self.lose_money:.2f} \nNow his balance is: {self.start_balance:.2f}')
        self.cycle()

    def cycle(self):
        self.result: str = input('\nDo you want to continue operation? Write y if yes and n if no: ')
        if self.result == 'y':
            self.run_point()
        elif self.result == 'n':
            print('End operation.')
            exit()
        else:
            print('Unknown choice.')
            exit()


citizen = Account('Патрис Лумумба', 100000.00)
citizen.run_point()
citizen.cycle()
