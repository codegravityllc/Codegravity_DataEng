import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connection details
server = 'DESKTOP-1KU88UE'
database = 'Data_Engineer_cg'
username ='DESKTOP-1KU88UE\Pravasis Dhakal'
password = 'NewSecurePassword'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to SQL Server
conn = pyodbc.connect(connection_string)

# Query the data
query = 'SELECT * FROM YourTableName'
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Create visualizations
# Example: Bar chart
df['YourColumn'].value_counts().plot(kind='bar')
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# Example: Line chart
df.plot(x='DateColumn', y='ValueColumn', kind='line')
plt.title('Line Chart Example')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Example: Heatmap (using Seaborn)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()