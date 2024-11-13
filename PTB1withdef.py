def PTB1(a,b):
    if a==0 and b == 0:
        return "Vô số nghiệm"
    elif    a==0 and b != 0:
        return "Vô nghiệm"
    else:
        x  = round(-b/a,2)
        return "Nghiệm x là:",x

import random

def tai_xiu():
    print("Chào mừng bạn đến với trò chơi Tài Xỉu!")
    
    # Người chơi nhập mức cược
    balance = int(input("Nhập số tiền cược của bạn: "))
    
    # Chọn tài hoặc xỉu
    choice = input("Chọn tài hoặc xỉu (tài/xỉu): ").lower()
    
    # Tạo số ngẫu nhiên từ 1 đến 6 cho ba viên xúc xắc
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)
    total = dice_1 + dice_2 + dice_3
    
    # Hiển thị kết quả
    print(f"Kết quả của ba viên xúc xắc là: {dice_1}, {dice_2}, {dice_3} (Tổng: {total})")
    
    # Xác định tài/xỉu
    if total >= 11 and total <= 17:
        result = "tài"
    else:
        result = "xỉu"
        
    # So sánh kết quả với lựa chọn của người chơi
    if choice == result:
        print("Chúc mừng! Bạn đã đoán đúng.")
        balance += 100  # Thêm tiền vào tài khoản
    else:
        print("Rất tiếc! Bạn đã đoán sai.")
        balance -= 100  # Trừ tiền khỏi tài khoản

    print(f"Số tiền của bạn hiện tại là: {balance}.")

# Chạy trò chơi
tai_xiu()

