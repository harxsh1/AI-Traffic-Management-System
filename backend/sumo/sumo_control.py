import subprocess

def run_sumo(lane_counts):
    print("Launching SUMO (FINAL SAFE MODE)...")

    sumo_gui = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"

    try:
        subprocess.Popen([sumo_gui])
        print("SUMO Opened Successfully")
    except Exception as e:
        print("SUMO Error:", e)