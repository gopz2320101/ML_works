1. first update the requirements.txt file with names of the required packages.
2. run the code in the terminal :
   pip download -r requirements.txt -d "put the location to store here"
3. To take the wheel package inside the server and unpack it, run the below code:
   pip install -r requirements.txt --no-index --find-link "path of wheel file inside server"
