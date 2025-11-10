# app.py
import streamlit as st

# 제목
st.title("약수 개수 확인기")

# 사용자 입력
number = st.number_input("숫자를 입력하세요", min_value=1, step=1)

if st.button("약수 개수 확인"):
    # 약수 개수 계산
    count = 0
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            divisors.append(i)
    
    st.write(f"{number}의 약수는 {count}개입니다.")
    st.write("약수:", divisors)
