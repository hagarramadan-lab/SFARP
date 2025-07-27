import pandas as pd

def extract_features(df):
    df['PPS'] = df['PacketCount'] / df['Duration']
    df['Entropy'] = - (df['PacketSize'].value_counts(normalize=True) * np.log2(df['PacketSize'].value_counts(normalize=True))).sum()
    df['DMP'] = df.duplicated(['MAC', 'IP']).astype(int)
    return df
