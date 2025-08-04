# football_data_warehouse/scripts/pipelines/combine_leagues.py
import pandas as pd
import os
import glob
from pathlib import Path
import sys

def main():
    # Get the absolute path of the current script
    script_dir = Path(__file__).parent.resolve()
    
    # Calculate the CORRECT project root path (two levels up from script)
    project_root = script_dir.parent.parent
    
    # Set directory paths
    processed_dir = project_root / "data" / "Processed_data"
    final_data_dir = project_root / "data" / "Final_data"
    
    # Print paths for debugging
    print(f"🔍 Processed data directory: {processed_dir}")
    print(f"💾 Final data directory: {final_data_dir}")
    
    # Create final data directory if it doesn't exist
    final_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Verify processed directory exists
    if not processed_dir.exists():
        print(f"❌ Processed data directory does not exist: {processed_dir}")
        print("Please run the processing pipelines first")
        return
    
    # Find all CSV files in the processed directory
    csv_files = glob.glob(str(processed_dir / "*.csv"))
    
    if not csv_files:
        print(f"❌ No CSV files found in: {processed_dir}")
        print("Files in directory:")
        for f in processed_dir.iterdir():
            print(f" - {f.name}")
        return
    
    print(f"📁 Found {len(csv_files)} league files to combine")
    
    # Initialize list to store dataframes
    all_leagues = []
    
    for file_path in csv_files:
        try:
            # Extract league name from filename
            filename = Path(file_path).stem
            league_name = filename.replace("_merged_squad_stats", "")
            
            # Read CSV file
            df = pd.read_csv(file_path)
            
            # Add league name column
            df.insert(0, "League", league_name)
            
            all_leagues.append(df)
            print(f"✅ Loaded {filename} with {len(df)} teams")
            
        except Exception as e:
            print(f"❌ Error processing {Path(file_path).name}: {str(e)}")
            import traceback
            traceback.print_exc()
    
    if not all_leagues:
        print("❌ No valid data to combine")
        return
    
    # Concatenate all dataframes
    combined_df = pd.concat(all_leagues, ignore_index=True)
    
    # MODIFICATION START: Drop 'League' and rename 'Squad' to 'team'
    # Drop League column if it exists
    if 'League' in combined_df.columns:
        combined_df.drop(columns=['League'], inplace=True)
    
    # Rename Squad column to team if it exists
    if 'Squad' in combined_df.columns:
        combined_df.rename(columns={'Squad': 'team'}, inplace=True)
    # MODIFICATION END
    
    # Save combined data
    output_path = final_data_dir / "Combined_Leagues_Stats.csv"
    combined_df.to_csv(output_path, index=False)
    
    print(f"\n🏆 Successfully combined {len(all_leagues)} leagues")
    print(f"📊 Total teams: {len(combined_df)}")
    print(f"💾 Saved to: {output_path}")

if __name__ == "__main__":
    print("=" * 60)
    print("🏁 STARTING LEAGUE DATA COMBINATION PROCESS")
    print("=" * 60)
    main()
    print("=" * 60)
    print("🏁 PROCESS COMPLETE")
    print("=" * 60)