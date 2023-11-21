# Recipe Recommendation System (RRS)

## Introduction
The Recipe Recommendation System is an innovative platform for food enthusiasts who want to discover new recipes based on their dietary preferences, such as vegetarian, non-vegetarian, or vegan options, and filter out recipes based on allergens. It's designed to be intuitive, allowing users to search for recipes by various criteria and manage their culinary preferences easily.

## Features
- **User Registration**: Sign up with a username, password, dietary preference (veg/non-veg/egg), and a list of allergens.
- **User Login**: Secure login with a username and password.
- **Home Page**: Browse through a list of top recipes. Utilize the 'Exclude Allergens' feature to customize recipe suggestions.
- **Recommender Page**: Extensive search functionality by name, ingredients, cuisine, allergens, excluded ingredients, and dietary preference.
- **Recipe Details**: Click on any recipe to view comprehensive details including cook time, ingredients, and step-by-step cooking instructions.
- **Bookmarking**: A dedicated page for all your bookmarked recipes, easily accessible for future reference.
- **User Profile Management**: View and edit your username, password, allergen list, and dietary preferences.

## Getting Started
To get started with the Recipe Recommendation System, follow the steps below:

### Prerequisites
- Ensure you have a modern web browser installed (Chrome, Firefox, Safari, etc.)
- Access to an active internet connection.

### Installation
No installation required. Access the Recipe Recommendation System through your web browser.

### Registration and Login
1. Navigate to the registration page via the homepage.
2. Fill in the required fields and submit your registration.
3. Once registered, log in using your credentials to access the full suite of features.

## Usage
- Use the home page to view and filter top recipes.
- On the recommender page, search for recipes by various criteria tailored to your dietary needs.
- Bookmark your favorite recipes for quick access later.
- Visit your profile page to update your user information and preferences.

- Sure, here's an additional section for your README that covers the technology stack and basic instructions on how to run the application locally:

---

## Technology Stack
This project is built with Flask, a micro web framework written in Python. It utilizes the MySQL Connector/Python to communicate with the MySQL database, ensuring a seamless data flow for the application.

### Requirements
- Python 3.x
- Flask
- MySQL
- MySQL Connector/Python

## Local Development

### Setting Up the Development Environment
Before running the application, ensure you have Python installed on your system. You'll also need to set up a MySQL database that the application will interface with. 

1. Clone the repository to your local machine:
   

2. Navigate to the cloned directory:

 
3. Install the required Python packages using pip:


### Configuring the Database
Ensure your MySQL service is running and you have created a database for the application. Use the provided schema.sql file to set up the required tables:

```
mysql -u username -p database_name < schema.sql
```

Update the `helper.py` file or a separate config file with your database connection details(your PC):

```python
con = m.connect(host = "localhost", user = "root", password = "password",
                 database = "rrs")
```

### Running the Application
After setting up the database and configuration, start the Flask application by running:

```
python app.py
```

The application will start and run on a default port (usually 8000) unless specified otherwise. You can access it by visiting `http://localhost:8000` in your web browser.

---

These instructions assume a basic familiarity with Python environments and MySQL setup. Users may need to adjust database connection settings or install additional software depending on their system configuration.

## Acknowledgements
- This project was created by Shriansh Mohanty, Shyam Krishna Sateesh, Shubha Masti and Shreya Sridhar for their Software Engineering Project - 2023.

