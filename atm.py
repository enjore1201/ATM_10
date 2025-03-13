#balance : 통장에 들어있는 기본 금액을 담는 변수
#1. 입금, 2.출금, 3.영수증, 4.종료 => 글자를 입력 받을지(입금,출금..) / 숫자를 입력받을지(1,2,3,...)
#숫자로 원하는 기능을 입력할 수 있게 만들어주세요 그리고 사용자가 입력한 기능은 num 변수를 담아주세요
#deposite_amount
#withdraw_amount
#영수증 기능에는 사용되는 데이터타입은 list -> [["입금", 5000, 8000]],[["출금", 3000, 5000]],["출금", 2000, 3000]
#영수증 기능 구현을 위한 빈 리스트 선언

receipts = []

balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해주세요(1. 입금 2.송금 3.영수증 4.종료)")
    if num =="1":
        deposite_amount = input("입금할 금액을 입력해주세요")
        if deposite_amount.isdigit() and int(deposite_amount) > 0:
            balance += int(deposite_amount)
            print(f'입금하신 금액{deposite_amount}원이고, 현재 잔액{balance}원 입니다')
            
            
            #영수증에 데이터 넣기
            receipts.append(("입금",deposite_amount, balance))
        else:
            print('ㅗ')
    if num == "2":
        withdraw_amount = input("출금할 금액을 입력해주세요 : ")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount
            print(f'출금하신 금액{withdraw_amount}원이고, 현재 잔액{balance}원 입니다')
    
            receipts.append(("출금", withdraw_amount, balance))
        else:
            print('ㅗ')
    if num =="3":
        if receipts:
            print('===영수증===')
            for i in receipts:
                print(f"{i[0]} : {i[1]}원 | 잔액 {i[2]}원")
        else:
            print("ㅗㅗ")
    if num =="4":
        print("서비스를 종료합니다")
        break