import streamlit as st
import plotly.express as px
import pandas as pd

# Load your retail sales data
retail_data = pd.read_csv("https://raw.githubusercontent.com/carolistical/final-rep/main/retail_sales_data.csv")

# Create a Streamlit app
st.title('Retail Sales Data Analysis')

# Section 1: Show Data and Plot Bar Chart
st.header('Bar Chart - Retail Sales Data (Section 1)')

# Show data checkbox
show_data_1 = st.checkbox("Show data (Section 1)")
if show_data_1:
    st.write(retail_data)
    st.write("This data is aggregated information of a retail store selling three categories of products: Electronics, Clothing, and Beauty, to both female and male customers, across different quarters, recording revenue, quantity, and product prices.")

# Plot barchart checkbox
plot_barchart = st.checkbox("Plot Barchart (Section 1)")
if plot_barchart:
    # Create a slider to select a month
    selected_month = st.slider('Select a month', min_value=1, max_value=12)

    # Filter the DataFrame for the selected month
    filtered_df = retail_data[retail_data['month'] == selected_month]

    # Calculate total revenue per category
    category_revenue = filtered_df.groupby('Category')['Revenue'].sum().reset_index()

    # Create the bar chart
    bar = px.bar(category_revenue, x='Category', y='Revenue', color='Category', title=f'Bar Chart for Month {selected_month}', labels={'Revenue': 'Total Revenue'})

    # Show the bar chart
    st.plotly_chart(bar)

    # Explanation of problem and observation
    st.write("Problem: Retail store wants to understand demand and customer behavior spanning the months of the year 2023.")
    st.write("Finding: Clothes are more in demand in the beginning of the year, and electronics are in demand in the middle of the year.")

# Section 2: Grouped Bar Chart
st.header('Grouped Bar Chart - Retail sales data (Section 2)')

# Filter data for the specified categories
selected_categories = st.multiselect("Select Categories", retail_data["Category"].unique())
filtered_data = retail_data[retail_data["Category"].isin(selected_categories)]

# Create a grouped bar chart using Plotly Express, Group the bars by gender
fig = px.bar(filtered_data, x="Category", y=["Total Amount Female", "Total Amount Male"], color="Gender", barmode="group", labels={"value": "Revenue"})

# Customizing the chart layout
fig.update_layout(title="Revenue by Category and Gender", xaxis_title="Category", yaxis_title="Revenue")

# Explain Problem
st.write("Problem: Retail store wants to get a more in-depth understanding of which gender generates more revenue, so they can tailor more products towards them.")

# Explain Finding
st.write("Finding: Beauty category is dominated by women.")
st.write("Clothing category is dominated by men.")
st.write("Electronics category is slightly dominated by women.")

# Display the chart in the Streamlit app
st.plotly_chart(fig)
