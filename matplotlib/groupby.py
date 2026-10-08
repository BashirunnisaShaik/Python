import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({"Month":["Jan","Feb","Mar","Apr","May"],"Sales":[100,150,120,180,200]})
plt.bar(df["Month"],df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()