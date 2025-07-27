import pandas as pd
from sklearn.utils import resample

def balance_dataset(df, target_column):
    major_class = df[target_column].value_counts().idxmax()
    df_major = df[df[target_column] == major_class]
    df_minors = [df[df[target_column] == label] for label in df[target_column].unique() if label != major_class]

    resampled_minors = [resample(minor, replace=True, n_samples=len(df_major), random_state=42) for minor in df_minors]
    df_balanced = pd.concat([df_major] + resampled_minors)
    return df_balanced.sample(frac=1).reset_index(drop=True)

if __name__ == '__main__':
    raw_df = pd.read_csv('raw/CICIoT2023.csv')
    balanced = balance_dataset(raw_df, 'Label')
    balanced.to_csv('balanced_stats.csv', index=False)
    print("Dataset balanced and saved.")
