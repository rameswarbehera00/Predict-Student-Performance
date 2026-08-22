import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
maths = pd.read_excel("Maths.csv")
portuguese = pd.read_excel("Portuguese.csv")


x = maths[["G1", "G2"]]
y = maths["G3"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=20
)

print("X train:", x_train.shape)
print("X test:", x_test.shape)
print("Y train:", y_train.shape)
print("Y test:", y_test.shape)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred[:10])

r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual G3")
plt.ylabel("Predicted G3")
plt.title("Actual vs Predicted Final Grades")
plt.show()

new_student = [[12, 14]]

prediction = model.predict(new_student)

print("Predicted Final Grade:", prediction[0])