import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value", "Wage", "Height", "Weight"]

st.dataframe(df_filtered[columns], column_config={
    "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
    "Photo": st.column_config.ImageColumn(width=10),
    "Flag": st.column_config.ImageColumn("Country", width=10),
    "Age": st.column_config.Column(width=10),
}, height=600, width=1500)

