import streamlit as st

def main():
    st.title("Graph Control Panel")

    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Pie"])
    data = st.text_input("Enter data, separated by commas")
    data = list(map(int, data.split(",")))

    if chart_type == "Line":
        st.line_chart(data)
    elif chart_type == "Bar":
        st.bar_chart(data)
    else:
        st.pie_chart(data)

if __name__ == "__main__":
    main()