import pandas as pd
import sqlite3

conn = sqlite3.connect("football.db")

fifa = pd.read_csv("fifa_ranking_2022-10-06.csv")
matches = pd.read_csv("matches_1930_2022.csv")          
world_cup = pd.read_csv("world_cup.csv")

fifa.to_sql("fifa_rank", conn, if_exists="replace", index=False)
matches.to_sql("matches", conn, if_exists="replace", index=False)
world_cup.to_sql("world_cup", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

#CSV Dosyalarımızı Database Formatına Çeviriyoruz!
