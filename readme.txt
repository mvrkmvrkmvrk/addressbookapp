Steps to run the addressbook application.

1. Either download the app folder from github https://github.com/mvrkmvrkmvrk/addressbookapp
or from the attached email.

2. Install necessary modules to run the fast api app, after you have already installed python 3.

	- pip install fastapi
	- pip install uvicorn

3. Now go to the command line and navigate to the folder mentioned in point 1 above. Navigate futher where "addressbook_app"
is located.

4. Now, enter the command:
	python3 -m uvicorn addressbook_app.main:app --reload
	or
	uvicorn addressbook_app.main:app --reload

5. Now you would have have the local server up and running at the url: http://127.0.0.1:8000

6. In order to test the api go to interactive docs: http://127.0.0.1:8000/docs

7. Here you can see all the app's endpoints which you can test in the following order:
	- POST /addresses/ add some dummy latitude and longitude to create an address.
	- GET /addresses/{address_id} here you can enter the id-1(generally) which will retrieve the above address
	- GET /addresses/ here you will retrieve all addresses added in the database
	- PUT /addresses/{address_id} here enter id and new coordinates to update the address
	- DELETE /addresses/{address_id} this will delete the given address mentioned by its id
	- GET /search_addresses/ here given the coordinates and a distance, it will retrive all addresses within the given distance
