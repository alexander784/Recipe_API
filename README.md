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
1. Ensure you have Python and pip installed. If not, refer to the prerequisites in the documentation.
2. Clone this repository to your local machine:

  git clone `https://github.com/alexander784/Recipe_API.git`
3. Create and activate a virtual environment:
  `python -m venv env`
`# On Windows:`
`. env/Scripts/activate`
`# On macOS/Linux:`
`source env/bin/activate`
4. Install the required dependencies:
   `pip install -r requirements.txt`

5. Confirm SQlite database configurations:
`DATABASES = {`
    `'default': {`
        `'ENGINE': 'django.db.backends.``sqlite3',`
        `'NAME': BASE_DIR / 'db.``sqlite3',`
    `}`
`}`

1. Apply database migrations:
`python3 manage.py makemigrations`
`python3 manage.py migrate`

2. Run the development server:
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

`{`
    `"id": 1,`
    `"name": "recipe title",`
    `"description": "Description of the recipe."`
`}`

## API Usage:
1. Get list of all recipes: <br>
`GET http://127.0.0.1:8000/recipe_app/`

2. Create new recipe <br>

`POST http://127.0.0.1:8000/recipe_app/`
`{`
    `"title": "Pilau",`
    `"description": "Boil water for about ten minutes."`
`}`

3. Get details of a specific recipe by ID:
`GET http://127.0.0.1:8000/recipe_app/1/` 

4. Update an existing recipe by ID:
`PUT http://127.0.0.1:8000/recipe_app/1/`
`{`
    `"name": "Pilau masala",`
    `"description": "Pilau spices"`
`}`

5. Delete a recipe by ID:
`DELETE http://127.0.0.1:8000/recipe_app/1/`

## <p> Author: Alexander Nyaga.</p>

## License 
This project is licensed under MIT License.
























