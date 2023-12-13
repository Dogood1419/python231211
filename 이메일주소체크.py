# 정규 표현식을 이용한 이메일 주소 체크
# 챗GPT 이용

import re

def check_email(email):
    # 이메일 주소를 체크하는 정규표현식
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.search() 함수를 사용하여 이메일 주소 체크
    match = re.search(pattern, email)
    
    if match:
        return True
    else:
        return False

# 샘플 이메일 주소 10개
sample_emails = [
    "user@example.com",
    "john.doe123@gmail.com",
    "info@company.net",
    "support@website.org",
    "test_email@yahoo.co.kr",
    "invalid.email@.domain.com",
    "user@123.45.67.89",
    "admin@localhost",
    "user@domain_with_underscore.com",
    "no_at_symbol_domain.com"
]

# 각각의 이메일 주소에 대해 체크하고 결과 출력
for email in sample_emails:
    result = check_email(email)
    print(f"{email}: {result}")


# 한글로 주석을 추가
