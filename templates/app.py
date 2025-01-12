import __init__
from views.view import SubscriptionService
from models.database import engine
from datetime import datetime 
from decimal import Decimal
from models.model import Subscription

class UI:
    def __init__(self):
        self.ss = SubscriptionService(engine)

    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Pagar uma assinatura
            [4] -> Valor total
            [5] -> Gastos últimos 12 meses
            [6] -> Sair
            ''')
            choice = int(input('Escolha uma opção: '))
            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.pay_subscription()
            elif choice == 4:
                self.total_value()
            elif choice == 5:
                self.ss.gen_chart()
            else:
                break

    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data da Assinatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))

        obj = Subscription( 
            empresa = empresa,
            site = site,
            data_assinatura=data_assinatura,
            valor=valor,
            status=1,
        )
        
        self.ss.create(obj)
        
        print('Assinatura adicionada com sucesso!')

    def delete_subscription(self):
        lista = self.ss.list_all()
        #Todo quando excluir a assinatura, excluir todos os pagamentos dela (no caso inativar)- ok
        print('Escolha qual assinatura deseja excluir:')

        for i in lista:
            print(f'[{i.id}] -> {i.empresa}')

        choice = int(input('Escolha a assinatura: '))
        self.ss.delete(choice)
        
        print('Assinatura excluída com sucesso!')

    
    def pay_subscription(self):

        lista = self.ss.list_all()

        for i in lista:
            print (f'[{i.id}] --> {i.empresa}  | valor: {i.valor:.2f}')
        
        while True:
        
            choice = int(input('Escolha qual assinatura deseja pagar \n' \
                               'Voltar ao menu, tecle [0] \n' \
                                 'Assinatura: ' ))
            if choice == 0:
                break
            else:
                for n in lista:
                    if choice ==n.id:
                        print(f'Assinatura escolhida é {n.empresa}')
                        ok = True
                        try:
                            self.ss.pay(n)
                            print('Assinatura foi paga com sucesso!')
                        except Exception as e:
                            print(f"Ocorreu um erro: {e}")
                            
                return
            
            


    def total_value(self):
        print(f'Seu valor total mensal de assinatura é {self.ss.total_value()}')

#if __name__=='main':
UI().start()