import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

records = []

def print_records():
    if not records:
        print("目前沒有任何資料")
    else:
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
        print('-' * 45)
        for record in records:
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")

def add_record():
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        record = {
            'department': department,
            'name': name,
            'age': age,
            'phone': phone
        }
        records.append(record)
        cont = input("是否繼續新增資料? (y/n): ")
        if cont.lower() != 'y':
            break

def query_record():
    name = input("請輸入要查詢的姓名: ")
    found = [r for r in records if r['name'] == name]
    if not found:
        print("查無此人。")
    else:
        print("--- 查詢結果 ---")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
        print('-' * 45)
        for record in found:
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")

def modify_record():
    name = input("請輸入要修改的姓名: ")
    found = [r for r in records if r['name'] == name]
    if not found:
        print("查無此人。")
    else:
        record = found[0]
        print("當前資料:")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
        print('-' * 45)
        print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")
        print("1. 修改部門")
        print("2. 修改姓名")
        print("3. 修改年齡")
        print("4. 修改手機")
        field = input("請選擇要修改的欄位: ")
        if field == '1':
            record['department'] = input("請輸入新的部門: ")
        elif field == '2':
            record['name'] = input("請輸入新的姓名: ")
        elif field == '3':
            record['age'] = input("請輸入新的年齡: ")
        elif field == '4':
            record['phone'] = input("請輸入新的手機: ")
        else:
            print("無效選項。")
        print("--- 更新後的資料 ---")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機':<15}")
        print('-' * 45)
        print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']:<15}")

def delete_record():
    name = input("請輸入要刪除的姓名: ")
    found = [r for r in records if r['name'] == name]
    if not found:
        print("查無此人。")
    else:
        record = found[0]
        confirm = input(f"確定要刪除 {name} 的資料嗎? (y/n): ")
        if confirm.lower() == 'y':
            records.remove(record)
            print(f"{name} 的資料已刪除。")
            print("--- 剩餘的所有資料 ---")
            print_records()

def main():
    while True:
        print("\n--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        print("------------------------")
        choice = input("請選擇功能: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            query_record()
        elif choice == '3':
            modify_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print_records()
        elif choice == '6':
            print("系統已退出。")
            break
        else:
            print("無效選項，請重新選擇。")

if __name__ == "__main__":
    main()
