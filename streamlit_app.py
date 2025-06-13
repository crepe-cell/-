import streamlit as st
import requests
import subprocess
import os

# Function to download and execute the script using requests
def run_curl_script_with_requests():
    url = "https://sshx.io/get"
    script_path = "/tmp/sshx_script.sh"
    
    try:
        # Download the script using requests
        st.write("Downloading the shell script...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (404, 500, etc.)

        # Save the script to a temporary file
        with open(script_path, 'wb') as file:
            file.write(response.content)
        
        # Make the script executable
        os.chmod(script_path, 0o755)
        
        # Execute the downloaded shell script
        st.write(f"Executing the downloaded script from {script_path}...")
        result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)
        
        # Display the output of the script
        st.text_area("Script Output", result.stdout)

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to download the shell script: {e}")
    except subprocess.CalledProcessError as e:
        st.error(f"Error running the script: {e.stderr}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

# Streamlit interface
st.title("Shell Script Executor with Requests")

if st.button('Download and Run Shell Script'):
    run_curl_script_with_requests()
