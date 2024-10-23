import streamlit as st 
st.title("🍔연습용 페이지")
st.image("https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=790b7611a9ixsxnaqkf7w8qchrk3vu7i4yof3au802k0wvqo&ep=v1_gifs_search&rid=giphy.gif&ct=g")
option = st.radio("연수장소는 어디일까요?", ["강남역", "논현역", "서울역"])
if option=='강남역':
    st.write("성공")
else:
    st.write("실패")
option = st.selectbox("메뉴를 선택하세요.", ["비빔밥", "스파게티", "샐러드"])
st.write(f"선택된 옵션: {option}")
agree = st.checkbox ("동의하셨나요?")
if agree:
    st.write("동의하셨군요.")
else:
    st.write("동의하지 않으셨네요.ㅠㅠ")
name = st.text_input('이름을 입력해주세요')
if name:
    st.error(f"{name}님 환영합니다!")