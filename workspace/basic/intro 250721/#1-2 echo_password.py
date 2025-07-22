import re

def is_valid_password(password):
    # 각각 조건을 만족하는 정규표현식
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[^\w]', password)  # \w는 알파벳+숫자+언더바, 따라서 [^\w]는 특수문자

    return all([has_lowercase, has_uppercase, has_digit, has_special])

def main():
    while True:
        user_input = input("비밀번호를 입력하세요 (!quit 입력 시 종료): ")
        if user_input == "!quit":
            print("종료합니다.")
            break
        if is_valid_password(user_input):
            print("✅ 유효한 비밀번호입니다.")
        else:
            print("❌ 비밀번호는 소문자, 대문자, 숫자, 기호를 각각 최소 하나 이상 포함해야 합니다.")

if __name__ == "__main__":
    main()
