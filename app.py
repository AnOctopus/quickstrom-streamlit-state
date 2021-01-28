import streamlit as st

state = st.beta_session_state(entries=["foo"])

st.write(state.entries)
