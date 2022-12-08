import pandas as pd #pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Currency Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_excel(
    io='try_panda3.xlsx',
    engine='openpyxl',
    # sheet_name='currency',
    # usecols='B:R',
    # nrows=100,
)

# print(df)
st.title(":bar_chart: Sample Data from CSV file")
st.dataframe(df)

#taking user input
# text_input = st.text_input("Enter the currency","")
# st.markdown(f"Currency data for Given input dates is: {text_input}")
st.markdown(f"Currency data for Given input dates is: ")


# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
date = st.sidebar.multiselect(
    "Select the Date:",
    options=df["Date"].dt.date.unique()
)


df_selection = df.query(
    # "Date == @date & Algerian_dinar==@Currency_type "
    "Date == @date"
)

#display dataframe
st.dataframe(df_selection)


###############################################################

# ---- MAINPAGE ----
st.title(":bar_chart: Currency Bar-Chart Dashboard")
st.markdown("##")


#finally Working-->Dont Touch
dt = pd.read_excel('try_panda3.xlsx')
dt = dt.to_dict('records')
print(dt)

# print(type(dt))
currencies = []
for key in dt[0]:
    currencies.append(key)

currencies.remove("Date")
selected_curr = st.selectbox("Select Currency: ",currencies)

dates = []
values = []

for row in dt:
    dates.append(row["Date"])
    print(type(row[selected_curr]))
    values.append(row[selected_curr])

# print(values)
dataframe = pd.DataFrame({
  'date': dates,
  'second column': values
})

dataframe = dataframe.rename(columns={'date':'index'}).set_index('index')

st.bar_chart(dataframe)

#######################################################################

st.title(":bar_chart: Currency Line-Chart Dashboard")
st.markdown("##")
st.line_chart(dataframe)


#######################################
# DATE BY CURRENCY LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["Date"]).sum()[["Algerian_dinar"]].sort_values(by="Algerian_dinar")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Algerian_dinar",
    y=sales_by_product_line.index,
    title="<b>Currency by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

st.plotly_chart(fig_product_sales)
