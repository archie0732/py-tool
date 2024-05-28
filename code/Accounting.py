import csv
import os
from datetime import datetime

# 取一個檔案名為transactions.csv的檔案
FILENAME = 'transactions.csv'

# 沒有檔案 ==> 寫入一個 用os
def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Description', 'Amount'])

# 加入帳單
def add_transaction(date, description, amount):
    # mode='a' : 模式 append 
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        # 依序加入 date 描述 $
        writer.writerow([date, description, amount])

# 查看帳單
def view_transactions():
    # 未建檔
    if not os.path.exists(FILENAME):
        print("請先輸入帳目")
        return
    # mode='r': 讀檔模式
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        # for each 找(符合資料)的檔
        for row in reader:
            print(', '.join(row))

# 計算
def calculate_balance():
    # 總金額 = 預設式0
    total = 0.0
    if not os.path.exists(FILENAME):
        print("請先輸入帳目")
        return total
    
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        # 用for each 找檔案裡的所有帳目，並加總
        for row in reader:
            try:
                total += float(row[2])
            except ValueError:
                print(f"發現錯誤: {row}")
    return total

def main():
    # 如未建檔==>建檔
    initialize_csv()

    while True:
        print("\n歡迎使用本計帳功能")
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有交易")
        print("4. 查看餘額")
        print("5. 退出")

        choice = input("輸入您的選擇(數字): ")

        if choice == '1' or choice == '2':
            date_str = input("請輸入日期 (格式:YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print("無效的日期格式，請使用格式 YYYY-MM-DD")
                continue

            description = input("輸入關於收支描述: ")
            try:
                amount = float(input("金額: "))
            except ValueError:
                print("輸入錯誤")
                continue

            if choice == '2':
                amount = -amount  # 支出改負數

            add_transaction(date_str, description, amount)
            print("添加成功!")
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            balance = calculate_balance()
            print(f"目前餘額: {balance}")
        elif choice == '5':
            print("再見!")
            break
        else:
            print("無效的選擇，請重試")

# 執行主函數
if __name__ == "__main__":
    main()
