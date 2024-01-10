"# AI-PDF-Chat" 
1. Make venv ("python -m venv venv" in powershell)
2. Activate venv ("venv\Scripts\activate" in powershell)
    If not working make sure that the powershell policy is set to RemoteSigned and not Restricted.
    (Commands: "Get-ExecutionPolicy"- To check Policy, "Set-ExecutionPolicy RemoteSigned" - To set Policy, then run in powershell where the env located the comand to activate it, then you can return the policy to Restricted (for security reasons) but you dont have to , "Set-ExecutionPolicy Restricted" To set the policy).
3. Install packages ("pip install streamlit" and so on in powershell)
4. Run the file ("streamlit run app.py" in powershell or "streamlit run app.py --server.address 127.0.0.1 --server.port 8000")


Feel free to clone this repository.