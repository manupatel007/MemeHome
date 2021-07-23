# MemeHome

Internship Task

This project is hosted on heroku at --> https://memehome.herokuapp.com/

task1 and task2 is tha name given to apps corresponding to these tasks.

## How to run this project locally?

1. Clone this repository.
2. Run ```pip install pipenv``` in CLI
3. Run ```pipenv shell``` in the root directory to install the dependencies.
4. Run ```python MemeHome/manage.py runserver``` in the same directory to start server.
5. Go to http://127.0.0.1:8000/ on your browser.
6. Choose the task to navigate(Task 1 and Task 2)


## To dos(Task 1)

- [x] Overriding Default user model using AUTH_USER_MODEL
- [x] Username should start with a/A and end with 1/0(Using Regex in models)
- [x] Manually applied SHA 256 algo on password field
- [x] Basic validation on password(in forms.py)
- [x] Task title validation of minimum characters.(in forms.py)
- [x] Textarea for Task description in forms.
- [x] Applying Pagination on queryset.
- [x] Generating Fake data using Faker.
- [x] Added Default image if no image in a post.
- [x] Deploy on Heroku.

## To dos(Task 2)

- [x] Algorithm to display hierarchical data.

