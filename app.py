import streamlit as st
from openai import OpenAI
import os

st.title("🚨미니 응급실👨‍⚕️👩‍⚕️")
st.write("아픈 증상을 입력하면 질병과 응급처치를 안내해드립니다!")

user_symptom = st.text_area("현재 느끼는 증상을 입력하세요")

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

if st.button("증상 분석하기"):
    if not user_symptom.strip():
        st.warning("증상을 입력해주세요!")
    else:
        st.info("증상을 분석하고 있습니다...🩺")

        prompt = f"""
        사용자가 입력한 증상: {user_symptom}

        아래 기준으로 한국어로 정리해줘:

        1. 가능한 질병 3~5개 (각 질병 추정 이유 포함)
        2. 응급도 (낮음 / 중간 / 높음)
        3. 지금 당장 해야 할 응급처치 3가지
        4. 병원 방문이 필요한 상황인지 여부

        깔끔한 bullet point 스타일로 출력해줘.
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4.1-mini",
        )

        result = response.choices[0].message.content

        st.subheader("🚨분석 결과🩺")
        st.write(result)