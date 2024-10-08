Recipe API
Introduction
<p> This is a RESTful API developed on Django, a strong Python web framework, with SQlite as the database backend. The API allows users to manage recipes by executing CRUD (Create, Read, Update, and Delete) activities on them. Each recipe contains a title and a description.</p>

## Features

Create a new recipe  with title and description. <br>
Retrieve a list of all recipes.<br>
Retrieve details of a specific recipe by its ID.<br>
Update an existing recipe  title and/or description.<br>
Delete recipe by its ID.<br>

## Technologies Used:

** Django: A high-level web framework written in Python<br>
** Django REST framework: A powerful and flexible toolkit for building Web APIs in Django.<br>
Python: The programming language used for backend development.<br>
Git: Version control system for tracking changes in source code.<br>

## Setup and Installation 
<p>To run the recipe API locally on your machine, follow these steps:</p>
1. Ensure you have Python and pip installed. If not, refer to the prerequisites in the documentation.<br>
2. Clone this repository to your local machine:<br>

 git clone `https://github.com/alexander784/Recipe_API.git`<br>
3. <p>Create and activate a virtual environment:</p>
  `python -m venv env`<br>
`# On Windows:`<br>
`. env/Scripts/activate`<br>
`# On macOS/Linux:`<br>
`source env/bin/activate`<br>

4. Install the required dependencies:<br>
   `pip install -r requirements.txt`<br>

5. Confirm SQlite database configurations:<br>
`DATABASES = {`<br>
    `'default': {`<br>
        `'ENGINE': 'django.db.backends.``sqlite3',`<br>
        `'NAME': BASE_DIR / 'db.``sqlite3',`<br>
    `}`<br>
`}`<br>

1. Apply database migrations:<br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`

2. Run the development server:<br>
`python3 manage.py runserver`

<p>The API should be accessible at: http://127.0.0.1:8000/recipe_app/</p>

# API End points
<p> The following are the Recipe API Endpoints:</p>


## Request and Response Format
<p>The API accepts and returns data in JSON format.</p> <br>

`{`<br>
    `"title": "recipe title",`<br>
    `"description": "Describe the recipe."`<br>
`}`

<p>Response format (GET and POST):</p> <br>

`{`<br>
    `"id": 1,`<br>
    `"name": "recipe title",`<br>
    `"description": "Description of the recipe."`<br>
`}`<br>

## API Usage:
1. Get list of all recipes: <br>
`GET http://127.0.0.1:8000/recipe_app/`

2. Create new recipe <br>

`POST http://127.0.0.1:8000/recipe_app/`<br>
`{`<br>
    `"title": "Pilau",`<br>
    `"description": "Boil water for about ten minutes."`<br>
`}`

3. Get details of a specific recipe by ID:<br>
`GET http://127.0.0.1:8000/recipe_app/1/` 

4. Update an existing recipe by ID:<br>

`PUT http://127.0.0.1:8000/recipe_app/1/`<br>
`{`<br>
    `"name": "Pilau masala",`<br>
    `"description": "Pilau spices"`<br>
`}`<br>

5. Delete a recipe by ID:<br>
`DELETE http://127.0.0.1:8000/recipe_app/1/`

## <p> Author: Alexander Nyaga.</p>

## License 
This project is licensed under MIT License.
























