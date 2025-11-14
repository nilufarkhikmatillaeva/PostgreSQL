import json

cards = {
    '9860020345367543': {
        'name': 'Xamidova Feruza',
        'balance': 500000.0,
        'account_number': '9860020345367543',
        'expiry_date': '12/27',
        'bank_name': 'Ipoteka',
        'pin':'3344',
        'sms_xizmati':'yoniq',
    },
    '9860253412356400':{
        'name':'Yoldoshbayev Ibrohim',
        'balance': 5000000.0,
        'account_number':'9860253412356400',
        'expiry_date': '12/26',
        'bank_name': 'Ipoteka',
        'pin':'1232',
        'sms_xizmati':"ochiq"
    }
}

with open('bank.json','w') as f:
    data=json.dump(cards,f,indent=4)



def load_cards():
    try:
        with open('bank.json','r') as f:
            return json.load(f)
    except:
        return {}

def check_card(cards):
    account_number=input('Enter account number: ')
    card=cards.get(account_number)
    if not card:
        print('Karta mavjud emas')
        return None
    tries=0
    while tries<3:
        pin=input('Pin kodni kiriting:')
        if pin==card['pin']:
            print('Pin kod togri')
            return card

        else:
            tries+=1
            print('Pin kod notogri',3-tries,'ta urinish qoldi')
    print('3 ta xato urinish. Kirish rad etildi')
    return None

def show_balance(card):
    print('Balans:',card['balance'])

def deposit(card):
    try:
        amount=float(input('Summmani kiriting:').strip())
        card['balance']+=amount
        print('Yangi balans:',card['balance'])
        with open('bank.json', 'w') as f:
            json.dump(cards, f, indent=4)

    except:
        print('Iltimos,raqam kiriting')

def withdraw(card):
    try:
        amount = float(input('Summani kiriting:').strip())
        if amount>card['balance']:
            print('Hisobda pul yetarli emas')
        else:
            card['balance']-=amount
            print('Yangi balans:',card['balance'])
            with open('bank.json', 'w') as f:
                json.dump(cards, f, indent=4)

    except:
        print('Iltimos,raqam kiriting')

def enable_sms(card):
    card['sms_xizmati']='yoniq'
    print('Sms xizmati ulandi')
    with open('bank.json', 'w') as f:
        json.dump(cards, f, indent=4)


def disable_sms(card):
    card['sms_xizmati']='ochiq'
    print('Sms xizmati ochirildi')
    with open('bank.json', 'w') as f:
        json.dump(cards, f, indent=4)


def add_card(cards):
    name=input('Name:')
    balance=float(input('Balance:'))
    account_number=input('Karta raqami:')
    expiry_date=input('Expiry date:')
    bank_name=input('Bank name:')
    pin=input('Pin:')
    s={
        account_number:{
            'name':name,
            'balance':balance,
            'account_number':account_number,
            'expiry_date':expiry_date,
            'bank_name':bank_name,
            'pin':pin,
            'sms_xizmati':'ochiq'
        }
    }
    cards.update(s)
    with open('bank.json', 'w') as f:
        json.dump(cards, f, indent=4)


def card_menu(card):
    while True:
        kod=input(' 1.Balansni korish \n 2.Hisobni toldirish \n 3.Pul yechib olish \n 4.Sms xizmatini yoqish \n 5.Sms xizmatini ochirish \n 6.Karta qoshish \n 7.Chiqish')
        if kod=='1':
            show_balance(card)
        elif kod=='2':
            deposit(card)
        elif kod=='3':
            withdraw(card)
        elif kod=='4':
            enable_sms(card)
        elif kod=='5':
            disable_sms(card)
        elif kod=='6':
            add_card(cards)
        elif kod=='7':
            break

with open('bank.json','w') as f:
    json.dump(cards,f,indent=4)

cards = load_cards()           # load all cards
card = check_card(cards)       # login
if card:
    card_menu(card)


