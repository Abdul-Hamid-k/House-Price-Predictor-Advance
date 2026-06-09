import pandas as pd
import numpy as np

from data_loader import data_loader


# Columns where NaN = "No Feature" (structural)
NONE_COLS = [
    'PoolQC', 'MiscFeature', 'Alley', 'Fence',
    'FireplaceQu', 'GarageType', 'GarageFinish',
    'GarageQual', 'GarageCond', 'BsmtQual',
    'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
    'BsmtFinType2', 'MasVnrType'
]

ZERO_COLS = [
    'GarageYrBlt', 'GarageArea', 'GarageCars',
    'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
    'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath',
    'MasVnrArea'
]

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Structural: fill with "None" / 0
    for col in NONE_COLS:
        if col in df.columns:
            df[col] = df[col].fillna("None")
    for col in ZERO_COLS:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # LotFrontage: impute by neighborhood median
    df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(lambda x: x.fillna(x.median()))

    # Remaining categoricals: mode
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

