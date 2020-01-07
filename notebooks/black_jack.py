import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files

deck_df = pd.read_csv('notebooks/deck.csv')
hand_df = pd.read_csv('notebooks/hand.csv')

# Make points histogram

hand_sum = hand_df['Points'].sum()
print(hand_sum)
