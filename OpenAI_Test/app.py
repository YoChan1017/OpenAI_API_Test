# .env 파일을 사용하는 예제
from dotenv import load_dotenv
import os
import openai

# 환경변수 파일 로드
load_dotenv()

# API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 여행지 입력 받기
destination = input("여행지 입력: ")

# OpenAI API 요청 설정
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"설명없이 추천 관광지명만 3곳을 알려줘. 여행지는 '{destination}'이야."}
    ],
    max_tokens=50
)

# 응답 출력
recommended_spots = response.choices[0].message['content']
print(f"{destination}에서 추천하는 관광지 3곳:\n{recommended_spots}")
