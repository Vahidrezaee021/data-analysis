
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    data = {
        "Name": ["Ali", "Sara", "Reza", "Mina"],
        "Score": [85, 92, 78, 90]
    }
    df = pd.DataFrame(data)

    print("📊 Student Data")
    print(df)
    print("\nAverage Score:", df["Score"].mean())

    df.plot(x="Name", y="Score", kind="bar", title="Student Scores", legend=False)
    plt.ylabel("Score")
    plt.show()

if __name__ == "__main__":
    analyze_data()
