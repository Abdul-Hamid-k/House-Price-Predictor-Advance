import pandas as pd
from src.config import DATA_RAW

def data_loader():
  df = pd.read_csv(DATA_RAW/"test.csv")

  return df