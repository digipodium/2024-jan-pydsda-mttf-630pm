import streamlit as st
import plotly.express as px
import numpy as np
st.title('My first app in streamlit')
st.info("streamlit allows us to build apps")
st.warning("This is a warning")

def fibonacci(start,stop):
    x = [start, start+1]
    for i in range(stop):
        x.append(x[-1] + x[-2])
    return x

start = st.slider('Start', 0, 100)
stop = st.slider('Stop', 0, 100)
data = np.array(fibonacci(start,stop))
sin = np.sin(data)
fig = px.area(x=data, y=sin)
st.plotly_chart(fig, 
                use_container_width=True)