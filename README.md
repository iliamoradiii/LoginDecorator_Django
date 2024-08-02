# Django Project with User and Admin Panels

## Introduction
This is a Django project that includes two types of panels: one for users and one for administrators. The project features a modular architecture with user authentication and cookie validation implemented using decorators. The models are organized in a separate app called `models` for better readability.

## Features
- User and Admin panels
- Modular authentication system
- Custom cookie generation algorithm
- Organized models for better code readability


## Installation
1. Clone the repository:
```sh
git clone https://github.com/iliamoradiii/LoginDecorator_Django.git
cd LoginDecorator_Django
python -m venv env
```
  
2. Activate the virtual environment:
  On Windows:
  ```sh
  .\env\Scripts\activate
  ```
  On macOS and Linux:
  ```sh
  source env/bin/activate
  ```
3. Install the dependencies:
```
python -m pip install Django==4.2.14
```

## Usage

1. Create a superuser:
```sh
python manage.py createsuperuser
```
2. Run the development server:
```sh
python manage.py runserver
```










