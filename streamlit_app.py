import streamlit as st

st.title("👏 Streamlit 연수실습")
st.subheader("저의 페이지에 오신 것을 환영합니다.")
st.write("by 김영란")
st.link_button("ran의 짓허브 페이지 바로 가기", "https://github.com/jinroran")
st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=790b7611pzi5w2kd372m1gnx20291ogyh91p7k6ci82fbpsz&ep=v1_gifs_search&rid=giphy.gif&ct=g")
st.video("https://youtu.be/DoJvGOsq4NQ?si=fK8R_pw2AdbQsA_y")