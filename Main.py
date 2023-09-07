# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash
from dash import Dash,html,dcc
import dash_bootstrap_components as dbc


# Load data into a pandas dataframe
df = pd.read_csv('customer_orders.csv')

# Data Exploration
print(df.head())    # Print first 5 rows of data
print(df.info())    # Print column names, data types, and non-null counts

# Data Cleaning and Preprocessing
df.dropna(inplace=True)    # Remove rows with missing values
df.drop_duplicates(inplace=True)    # Remove duplicate rows
df['order_date'] = pd.to_datetime(df['order_date'])    # Convert order_date to datetime format

# Data Analysis
# Create a scatter plot of order amount vs. customer age
plt.figure(figsize=(8,6))
sns.scatterplot(x='customer_age', y='order_amount', data=df)
plt.title('Order Amount vs. Customer Age')
plt.show()

# Create a bar plot of order count by shipping address
plt.figure(figsize=(8,6))
sns.countplot(x='shipping_address', data=df)
plt.title('Order Count by Shipping Address')
plt.show()

# Create a pie chart of order amount by payment method
order_amt_by_pay_method = df.groupby('payment_method')['order_amount'].sum()
plt.figure(figsize=(8,6))
plt.pie(order_amt_by_pay_method, labels=order_amt_by_pay_method.index, autopct='%1.1f%%')
plt.title('Order Amount by Payment Method')
plt.show()

# # Dashboard Implementation
# Create the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Customer Orders Dashboard'), width={'size': 12})
    ]),
    dbc.Row([
        dbc.Col(html.Div('Visualizing insights from customer orders data.'), width={'size': 12})
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='order-amount-vs-age',
            figure=px.scatter(df, x='customer_age', y='order_amount', color='payment_method')
        ), width={'size': 6}),
        dbc.Col(dcc.Graph(
            id='order-count-by-shipping-address',
            figure=px.bar(df, x='shipping_address', title='Order Count by Shipping Address')
        ), width={'size': 6})
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='order-amount-by-payment-method',
            figure=px.pie(df, values='order_amount', names='payment_method', title='Order Amount by Payment Method')
        ), width={'size': 6}),
        dbc.Col(dcc.Graph(
            id='order-amount-over-time',
            figure=px.line(df, x='order_date', y='order_amount', title='Order Amount Over Time')
        ), width={'size': 6})
    ])]
, fluid=True)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)




'''
The first step in data analytics is to understand the dataset and the questions that you want to answer. Once you have a clear understanding of what you want to achieve, you can begin the process of analyzing the data.

Here are the steps to perform data analytics and create a dashboard:

1.Data Exploration:
The first step is to explore the dataset to understand its structure, data types, and values. This step involves checking the missing data, outliers, and exploring the distribution of the data.

2.Data Cleaning and Preprocessing:
After exploring the data, you need to clean the data by removing missing values, duplicates, and outliers. This step is important to ensure that the data is accurate and suitable for analysis. You may also need to transform the data to a suitable format for analysis.

3.Data Analysis:
The next step is to perform data analysis to gain insights into the data. You can use different data analysis techniques such as regression, clustering, or classification, depending on the questions you want to answer. The goal of data analysis is to identify patterns, relationships, and trends in the data.

4.Dashboard Design:
After performing data analysis, you can design a dashboard to visualize the insights you have gained. The dashboard should be designed in a way that is easy to understand and use. The dashboard can include different types of charts, tables, and graphs that help to communicate the insights.

5.Dashboard Implementation:
Finally, you can implement the dashboard using a suitable tool such as Power BI, Tableau, or Excel. The dashboard should be interactive and allow users to explore the data and gain insights. You can also add filters, drill-down capabilities, and other features to enhance the dashboard.

In conclusion, performing data analytics and creating a dashboard requires a thorough understanding of the data and the questions you want to answer. By following the above steps, you can gain insights into the data and create a dashboard that communicates those insights effectively.

Overall, by following the above steps, we can gain insights into the customer orders data and create a dashboard that effectively communicates those insights. The dashboard can be used by different stakeholders such as the marketing team, sales team, or customer support team to make data-driven decisions.
'''
