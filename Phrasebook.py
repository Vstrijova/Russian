import streamlit as st
from PIL import Image
from gtts import gTTS


st.title("Итальянский разговорник для детей - Італійський розмовник для дітей")

language = st.radio( "Выберите язык - Виберіть мову" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин'))
  if placechoice == 'Площадка для игр':
    col1, col2 = st.columns(2)
    col1.subheader("Русский")
    data = ("1. Пойдем в парк" , "2. Давай играть в прятки", "3. Давай покатаемся на качелях")
    col1.write(data)
      
    
  
