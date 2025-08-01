# football_data_warehouse/scripts/pipelines/process_pipelines.py
import os
import importlib.util
import sys
from pathlib import Path

def run_script(script_name):
    """Dynamically import and execute a processing script"""
    # Get the directory of the current script
    current_dir = Path(__file__).parent.resolve()
    
    # Path to the process directory containing the league scripts
    process_dir = current_dir / "process"
    script_path = process_dir / script_name
    
    if not script_path.exists():
        print(f"⚠️ Script not found: {script_path}")
        return
    
    # Create a module name from the script path
    module_name = script_name.replace(".py", "")
    
    try:
        # Import the module dynamically
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        # Execute the main function if it exists
        if hasattr(module, 'main'):
            print(f"🚀 Running {script_name}...")
            module.main()
            print(f"✅ Completed {script_name}\n")
        else:
            print(f"⚠️ {script_name} has no main() function to execute")
    except Exception as e:
        print(f"❌ Error running {script_name}: {str(e)}\n")
        # Print the exception traceback for debugging
        import traceback
        traceback.print_exc()

def main():
    """Main function to run all processing pipelines"""
    # List of script filenames
    scripts = [
        "process_brazil_serie_a_data.py",
        "process_eredivisie_data.py",
        "process_la_liga_data.py",
        "process_bundesliga_data.py",
        "process_championship_data.py",
        "process_premier_league_data.py",
        "process_ligue_1_data.py",
        "process_primeira_liga_data.py",
        "process_serie_a_data.py",
        "process_serie_b_data.py"
    ]
    
    print("=" * 60)
    print("🏁 STARTING DATA PROCESSING PIPELINES")
    print("=" * 60)
    
    # Execute each script in sequence
    for script in scripts:
        run_script(script)
    
    print("=" * 60)
    print("🏁 ALL PROCESSING PIPELINES COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    main()