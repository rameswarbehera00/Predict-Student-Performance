from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def main():
    project_dir = Path(__file__).resolve().parent
    maths = pd.read_excel(project_dir / "Maths.xlsx")

    features = maths[["G1", "G2"]]
    target = maths["G3"]
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=20
    )

    print("X train:", x_train.shape)
    print("X test:", x_test.shape)
    print("Y train:", y_train.shape)
    print("Y test:", y_test.shape)

    model = LinearRegression()
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    print(predictions[:10])

    r2 = r2_score(y_test, predictions)
    print("R² Score:", r2)

    mae = mean_absolute_error(y_test, predictions)
    print("Mean Absolute Error:", mae)

    figure, axis = plt.subplots()
    axis.scatter(y_test, predictions)
    axis.set_xlabel("Actual G3")
    axis.set_ylabel("Predicted G3")
    axis.set_title("Actual vs Predicted Final Grades")
    figure.savefig(project_dir / "actual_vs_final.png", bbox_inches="tight")
    plt.close(figure)
    print("Plot saved to:", project_dir / "actual_vs_final.png")

    new_student = pd.DataFrame({"G1": [12], "G2": [14]})
    prediction = model.predict(new_student)
    print("Predicted Final Grade:", prediction[0])


if __name__ == "__main__":
    main()
