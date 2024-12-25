choices = ["가위, 바위, 보"]

user1_choice = input("user1: 가위, 바위, 보 중 하나를 선택하세요: ")
print(f"user1이 선택한 값: {user1_choice}")
if user1_choice not in choices:
    print("가위 바위 보 중 선택하세요.")

user2_choice = input("user1: 가위, 바위, 보 중 하나를 선택하세요: ")
print(f"user1이 선택한 값: {user1_choice}")
if user2_choice not in choices:
    print("가위 바위 보 중 선택하세요.")

if  (
    (user1_choice == "바위" and user2_choice == "가위") or
    (user1_choice == "가위" and user2_choice == "보") or
    (user1_choice == "보" and user2_choice == "바위")
):
    print("user1이 이겼습니다.")
elif user1_choice == user2_choice:
    print("비겼습니다.")
else:
    print("user2가 이겼습니다.")