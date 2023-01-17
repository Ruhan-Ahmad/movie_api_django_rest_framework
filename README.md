# movie_api_django_rest_framework
This project includes,
  * Users Model
  * Movies Info Model
  * Rating Model
  
  **User model** is a custom user model in django rest framework and stores firstname, lastname, phone, email, and passwords and other boolean such as is_active, is_superuser etc.
  **Movies Info** consist of movie_name, movie_short_description, movie_long_description, thumbnail_url, movie_url and movie_genre.
  **Rating model** consist of starts and comment and some extra fields.
  
  # Setup
  1. Clone this repo
  ```Git
  git clone https://github.com/Ruhan-Ahmad/movie_api_django_rest_framework.git
  ```
  2. Create Database and include credentails in the .env file or directly into setting.py in movies/movies/settings.py.
  3. Run
  ```Python
  python manage.py makemigrations
  ```
  ```Python
  python manage.py migrate
  ```
  4. Download required libraries
  ```Python
  python -r requirements.txt
  ```
  5. Navigate to movies folder and run
  ```Python
  python manage.py runserver
  ```
  
