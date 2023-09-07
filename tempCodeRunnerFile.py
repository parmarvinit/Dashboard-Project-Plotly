# Data Analysis
# Create a scatter plot of order amount vs. customer age
plt.figure(figsize=(8,6))
sns.scatterplot(x='customer_age', y='order_amount', data=df)
plt.title('Order Amount vs. Customer Age')
plt.show()