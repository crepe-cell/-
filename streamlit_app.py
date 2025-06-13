import streamlit as st
import subprocess

# Function to run the curl command and execute the script
def run_curl_script():
    try:
        # Running the curl command and executing the script
        st.write("Downloading and executing the shell script...")
        
        # Execute the curl command to download and pipe it to sh
        result = subprocess.run(
            "curl -sSf https://sshx.io/get | sh -s run", 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # Display the output
        st.text_area("Script Output", result.stdout)
        
    except subprocess.CalledProcessError as e:
        st.error(f"Error running the script: {e.stderr}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

# Streamlit interface
st.title("Shell Script Executor")

if st.button('Download and Run Shell Script'):
    run_curl_script()
