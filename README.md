## hotel-project

A backend API for a hotel booking platform, built with Django and Django REST Framework (DRF).

## What's this about?
This is my portfolio project, basically an "Amazon for hotels" idea. It's a platform where:
- Hotel owners can have pages and upload posts (like Instagram-style pages and posts), and send notifications to followers.
- Users (clients) can search and find hotels tailored to their needs, book rooms, rate hotels with stars, leave comments on hotel pages or individual posts.
- There's a wallet system for payments and bookings.
- Planning an achievement/badges system to reward active users with temporary discounts or offers.

It is purely a backend, means no HTML templates or frontend. Everything is DRF endpoints returning JSON.

## Current Status: Work in progress!
No features are fully implemented yet. Core stuff like user/auth, hotel listings, and some social features (posts, comments, ratings) are there or partially done. Payments, wallet, and achievements are under development.

This is just for my GitHub portfolio to show my Django/DRF skills and API design, authentication, models, serializers, etc...

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (for dev, but easy to switch to Postgres)
- Will dockerize it later

## How to Run (Quick Setup)
1. Clone the repo: `git clone https://github.com/17Nad/hotel-project`
2. Create a virtual environment: `python -m venv venv` and then activate it with `venv/Script/activate` (on windows) or `source venv/bin/activate` (on linux). 
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py makemigrations` then `python manage.py migrate` 
5. Create superuser if needed: `python manage.py createsuperuser`
6. Start server: `python manage.py runserver`


Thanks for checking it out!
