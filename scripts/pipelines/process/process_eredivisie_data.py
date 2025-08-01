import pandas as pd
import numpy as np
from functools import reduce
import os

def process_standard_stats(df, is_opponent=False):
    """Process standard stats dataframe"""
    drop_cols = ['# Pl', 'Age', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 'G-PK']
    divide_cols = ['PK', 'PKatt', 'CrdY', 'CrdR', 'PrgC', 'PrgP']
    base_col = 'MP'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_goalkeeping_stats(df, is_opponent=False):
    """Process goalkeeping stats dataframe"""
    drop_cols = ['# Pl', 'Starts', 'Min', '90s', 'GA', 'CS']
    divide_cols = ['SoTA','Saves', 'W', 'D', 'L', 'PKatt', 'PKA', 'PKsv','PKm']
    base_col = 'MP'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_advanced_gk_stats(df, is_opponent=False):
    """Process advanced goalkeeping stats dataframe"""
    drop_cols = ['# Pl', 'GA', 'PKA', '#OPA']
    divide_cols = ['FK', 'CK', 'OG', 'Cmp', 'Att', 'Cmp%', 'Att (GK)', 'Thr', 'Att.1', 'Opp', 'Stp']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_shooting_stats(df, is_opponent=False):
    """Process shooting stats dataframe"""
    drop_cols = ['# Pl', 'Sh', 'SoT', 'FK', 'PK', 'PKatt', 'xG', 'npxG']
    divide_cols = ['Gls']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_passing_stats(df, is_opponent=False):
    """Process passing stats dataframe"""
    drop_cols = ['# Pl', 'Cmp', 'Att', 'Cmp%', 'Cmp.1', 'Att.1', 'Cmp%.1', 
                 'Cmp.2', 'Att.2', 'Cmp%.2', 'Cmp.3', 'Att.3', 'Cmp%.3', 
                 'Ast', 'xAG', 'xA', 'A-xAG', 'PrgP']
    divide_cols = ['TotDist', 'PrgDist', 'KP', '1/3', 'PPA', 'CrsPA']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_pass_types_stats(df, is_opponent=False):
    """Process pass types stats dataframe"""
    drop_cols = ['# Pl', 'Att']
    divide_cols = ['Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 
                   'In', 'Out', 'Str', 'Cmp', 'Off', 'Blocks']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_gsc_stats(df, is_opponent=False):
    """Process goal/shot creation stats dataframe"""
    drop_cols = ['# Pl', 'SCA', 'GCA']
    divide_cols = ['PassLive', 'PassDead', 'TO', 'Sh', 'Fld', 'Def', 
                   'PassLive.1', 'PassDead.1', 'TO.1', 'Sh.1', 'Fld.1', 'Def.1']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_defensive_stats(df, is_opponent=False):
    """Process defensive actions stats dataframe"""
    drop_cols = ['# Pl']
    divide_cols = ['Tkl', 'TklW', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 'Tkl.1', 
                   'Att', 'Tkl%', 'Lost', 'Blocks', 'Sh', 'Pass', 'Int', 
                   'Tkl+Int', 'Clr', 'Err']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_possession_stats(df, is_opponent=False):
    """Process possession stats dataframe"""
    drop_cols = ['# Pl', 'Live', 'Poss', 'Touches', 'Def Pen', 'Def 3rd', 'Carries', 'TotDist']
    divide_cols = ['Mid 3rd', 'Att 3rd', 'Att Pen', 'Att', 'Succ', 'Tkld', 'Carries', 
                   'TotDist', 'PrgDist', 'PrgC', '1/3', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def process_misc_stats(df, is_opponent=False):
    """Process miscellaneous stats dataframe"""
    drop_cols = ['# Pl', 'CrdY', 'CrdR', '2CrdY', 'Crs', 'Int', 'Recov', 'Lost', 'OG', 'TklW', 'PKwon', 'PKcon']
    divide_cols = ['Fls', 'Fld', 'Off', 'Crs', 'Int', 'OG', 'Recov', 'Won']
    base_col = '90s'
    
    for col in divide_cols:
        new_col = f'{col}_per_90'
        df[new_col] = df[col] / df[base_col]
        df.loc[df[base_col] == 0, new_col] = 0
    
    df.drop(columns=drop_cols + divide_cols, inplace=True)
    
    if is_opponent:
        df['Squad'] = df['Squad'].str.replace('^vs ', '', regex=True)
        rename_dict = {col: f"{col}_against" for col in df.columns if col != 'Squad'}
        df.rename(columns=rename_dict, inplace=True)
    
    return df

def main():
    # Get the absolute path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Calculate the project root path (three levels up from script)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir, os.pardir))
    
    # Set data paths relative to project root
    raw_data_dir = os.path.join(project_root, "data", "Raw_data", "Eredivisie_data")
    processed_dir = os.path.join(project_root, "data", "Processed_data")
    
    # Create processed directory if it doesn't exist
    os.makedirs(processed_dir, exist_ok=True)
    
    # Read all data files using absolute paths
    Eredivisie_1 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Standard_Stats.csv"), skiprows=1)
    Eredivisie_2 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Standard_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_3 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Goalkeeping_Stats.csv"), skiprows=1)
    Eredivisie_4 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Goalkeeping_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_5 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Advanced_Goalkeeping_Stats.csv"), skiprows=1)
    Eredivisie_6 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Advanced_Goalkeeping_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_7 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Shooting_Stats.csv"), skiprows=1)
    Eredivisie_8 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Shooting_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_9 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Passing_Stats.csv"), skiprows=1)
    Eredivisie_10 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Passing_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_11 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Pass_Types_Stats.csv"), skiprows=1)
    Eredivisie_12 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Pass_Types_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_13 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Goal_Shot_Creation_Stats.csv"), skiprows=1)
    Eredivisie_14 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Goal_Shot_Creation_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_15 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Defensive_Actions_Stats.csv"), skiprows=1)
    Eredivisie_16 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Defensive_Actions_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_17 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Possession_Stats.csv"), skiprows=1)
    Eredivisie_18 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Possession_Stats(opponent stats).csv"), skiprows=1)
    Eredivisie_21 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Miscellaneous_Stats.csv"), skiprows=1)
    Eredivisie_22 = pd.read_csv(os.path.join(raw_data_dir, "Squad_Miscellaneous_Stats(opponent stats).csv"), skiprows=1)

    # Process and merge all stats categories
    Eredivisie_Squad_Standard_Stats_df = pd.merge(
        process_standard_stats(Eredivisie_1),
        process_standard_stats(Eredivisie_2, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Goalkeeping_Stats_df = pd.merge(
        process_goalkeeping_stats(Eredivisie_3),
        process_goalkeeping_stats(Eredivisie_4, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Advanced_Goalkeeping_Stats_df = pd.merge(
        process_advanced_gk_stats(Eredivisie_5),
        process_advanced_gk_stats(Eredivisie_6, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Shooting_Stats_df = pd.merge(
        process_shooting_stats(Eredivisie_7),
        process_shooting_stats(Eredivisie_8, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Passing_Stats_df = pd.merge(
        process_passing_stats(Eredivisie_9),
        process_passing_stats(Eredivisie_10, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Pass_Types_Stats_df = pd.merge(
        process_pass_types_stats(Eredivisie_11),
        process_pass_types_stats(Eredivisie_12, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Goal_Shot_Creation_Stats_df = pd.merge(
        process_gsc_stats(Eredivisie_13),
        process_gsc_stats(Eredivisie_14, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Defensive_Actions_Stats_df = pd.merge(
        process_defensive_stats(Eredivisie_15),
        process_defensive_stats(Eredivisie_16, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Possession_Stats_df = pd.merge(
        process_possession_stats(Eredivisie_17),
        process_possession_stats(Eredivisie_18, is_opponent=True),
        on='Squad',
        how='inner'
    )

    Eredivisie_Squad_Miscellaneous_Stats_df = pd.merge(
        process_misc_stats(Eredivisie_21),
        process_misc_stats(Eredivisie_22, is_opponent=True),
        on='Squad',
        how='inner'
    )

    # Prepare for final merge
    dataframes = [
        Eredivisie_Squad_Standard_Stats_df,
        Eredivisie_Squad_Goalkeeping_Stats_df,
        Eredivisie_Squad_Advanced_Goalkeeping_Stats_df,
        Eredivisie_Squad_Shooting_Stats_df,
        Eredivisie_Squad_Passing_Stats_df,
        Eredivisie_Squad_Pass_Types_Stats_df,
        Eredivisie_Squad_Goal_Shot_Creation_Stats_df,
        Eredivisie_Squad_Defensive_Actions_Stats_df,
        Eredivisie_Squad_Possession_Stats_df,
        Eredivisie_Squad_Miscellaneous_Stats_df
    ]
    
    columns_to_drop = ['MP', 'MP_against', '90s', '90s_against']
    prefixes = [
        "Standard_", "Goalkeeping_", "AdvGoalkeeping_", "Shooting_", 
        "Passing_", "PassTypes_", "GSC_", "Defense_", "Possession_", "Miscellaneous_"
    ]

    processed_dfs = []
    for df, prefix in zip(dataframes, prefixes):
        df_clean = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore')
        df_clean = df_clean.rename(columns={
            col: prefix + col if col != 'Squad' else col 
            for col in df_clean.columns
        })
        processed_dfs.append(df_clean)

    # Final merge and save to Processed_data directory
    merged_df = reduce(
        lambda left, right: pd.merge(left, right, on='Squad', how='outer'),
        processed_dfs
    )

    output_path = os.path.join(processed_dir, "Eredivisie_merged_squad_stats.csv")
    merged_df.to_csv(output_path, index=False)
    print(f"✅ Eredivisie merged data saved to {output_path}")

if __name__ == "__main__":
    main()