
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Sample dataset
    data = {
        "Name": ["Ali", "Sara", "Reza", "Mina"],
        "Score": [85, 92, 78, 90]
    }
    df = pd.DataFrame(data)

    # Print statistics
    print("📊 Student Data")
    print(df)
    print("\nAverage Score:", df["Score"].mean())

    # Plot scores
    df.plot(x="Name", y="Score", kind="bar", title="Student Scores", legend=False)
    plt.ylabel("Score")
    plt.show()

if __name__ == "__main__":
    analyze_data()
