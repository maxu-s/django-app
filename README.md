# Soldank++ Website
[WIP] Open-source Django web application for 2D (side-view) multiplayer arcade game [Soldank++](https://github.com/nedik/soldank-plus-plus). The project is available at [soldankpp.com](soldankpp.com)

[![Discord](https://img.shields.io/discord/1224452056245600417.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/gvhsk8NZHD)

## Screenshot
<img src="https://github.com/user-attachments/assets/ada52f35-e2b2-4b11-9a73-9bbaa492af13" alt="website1" width="550"/>
<img src="https://github.com/user-attachments/assets/30e3540a-a8b9-4b9a-9ca3-52c2abe1753c" alt="website2" width="550"/>
<img src="https://github.com/user-attachments/assets/05f484cb-943e-4ea9-934f-f5a9bb1f23eb" alt="website3" width="550"/>

## Building

1. Make sure you have [python3.8](https://www.python.org) (or higher) and clone this repository:
```
> git clone https://github.com/maxu-s/spp-website
> cd spp-website
```
2. Create a virtual environment then install the required packages:
```
> python -m venv venv
> pip install -r requirements.txt
```
3. Activate virtual enviroment from your terminal system:
```
> cd path/to/your/repository
> source venv/bin/activate   # on Linux/macOS
> venv\Scripts\activate      # on Windows
```
4. To keep sensitive information out of the code, environment variables are stored in a .env file. You will need to create this file manually. Create a file named ```.env``` in the root of your project (where manage.py is located) and add the following content to it:
```
DJANGO_SECRET_KEY='print-your-web-key-here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,
```
5. Replace ```print-your-web-key``` with your actual Django ```SECRET_KEY```. Generate that key using:
```
> python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
6. Run the following commands to apply the migrations and start the server:
```
> python manage.py collectstatic
> python manage.py migrate
> python manage.py runserver
```
