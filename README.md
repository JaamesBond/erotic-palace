Girls Management System

Wellcome to my revolutionary solution of managing the infamous Red Light District's girls.

Before you can use these apps, make sure you have the requirements installed:
Windows: py -m pip install -r requirements.txt
Linux: python3 -m pip install -r requirements.txt

Also, you have to run "girlsdb.py" once before running any of the apps. This will create the database and populate it with some example data.

So, assuming this is already unzipped, proceed as follows:
1. Go to this directory (API) with: cd <path-to-directory>
2. Install a Python Environment:
    Windows: py -m venv .venv
    Linux: python3 -m venv .venv
3. Activate the VEnv:
    Windows: .\.venv\Scripts\activate
    Linux: sudo ./venv/Scripts/activate
4. Install requirements in the VEnv:
    Windows: py -m pip install -r requirements.txt
    Linux: python3 -m pip install -r requirements.txt
5. Run the girlsdb script:
    Windows: py .\girlsdb.py
    Linux: python3 ./girlsdb.py

After completing all these steps, in the same terminal you should start the API server as follows:
    Windows: py .\girls_api.py
    Linux: python3 ./girls_api.py

Now, with this terminal opened, open another one, repeat steps 1 and 3 from above and start the frontend website with:
    Windows: py .\girls_frontend.py
    Linux: python3 ./girls_frontend.py