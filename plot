import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class GameSessionLogger:
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.records = []

    def log_round(self, round_number: int, score: int):
        self.records.append({
            "player": self.player_name,
            "round": round_number,
            "score": score,
            "timestamp": datetime.now()
        })

    def to_dataframe(self):
        return pd.DataFrame(self.records)

    def plot(self):
        df = self.to_dataframe()
        if df.empty:
            return

        ax = df.plot(x="round", y="score", marker="o", legend=False)
        ax.set_xlabel("Round")
        ax.set_ylabel("Score (fruits eaten)")
        ax.set_title(f"Snake Scores - {self.player_name}")
        plt.xticks(df["round"])
        plt.grid(True)
        plt.show()