import  streamlit as st

st.set_page_config(page_title="BANK APP", layout='centered')


st.markdown('<div class="main-title">Bank App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A Safe and Secure Banking App</div>' , unsafe_allow_html=True)
st.markdown('<div class="box-1">Savings</div>', unsafe_allow_html=True)
st.markdown('<div class="box-2">current</div>', unsafe_allow_html=True)


st.markdown("""
<style>
.main-title{
font-size:40px !important;
font-weight:700;
color:#1F4E79;
text-align:center;
}
.sub-title{
font-size:20px !important;
color:rgb(255,255,255);
text-align:center;
}
.box-1{
width:200px;
height:150px;
background-color:rgb(255,0,0);
color:#000;
justify-content:center;
align-items:center;
display:flex;
font-size:30px;
font-style:italics;
position:absolute;
top:140px;
}
.box-1:hover{
background-color:#E2F;
color:#FFF;
}
.box-2{
width:200px;
height:150px;
background-color:rgb(0,0,0);
color:#fff;
justify-content:center;
align-items:center;
display:flex;
font-size:30px;
font-style:italics;
position:absolute;
left:350px;
top:123px;
}
.box-2:hover{
background-color:#fff;
color:#000;
}

</style>
""", unsafe_allow_html=True)