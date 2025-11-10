# 제목
st.title("약수 개수 확인기 🧮")

# 사용자 입력
number = st.number_input("숫자를 입력하세요", min_value=1, step=1)

# 버튼 클릭 시
if st.button("약수 개수 확인"):
    count = 0
    divisors = []

    # 약수 계산
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            divisors.append(i)

    st.write(f"입력한 숫자 {number}의 약수 개수는 **{count}개**입니다.")
    st.write(f"약수: {divisors}")
