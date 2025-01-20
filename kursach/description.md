# Instruments in Music
The Instruments in Music project is a web application that allows users to search for information about instruments used in songs.

## Team
- Maria Bulytova — Frontend Developer.
- Vitriak Bohdan — Backend Developer.

## Описание
The web application provides the following features:
- Search for songs by title or genre.
- Display a list of songs with available instruments.
- View information about instruments on click.

## Requirements
To ensure the correct operation of the project, the following is required:
- Installed **Python 3.x** for the backend.
- Installed **XAMPP** with MySQL port configured to **8000**.
- Configured databases in **phpMyAdmin**. 

## Installation
1. Set up a local server with port **8000**:
   - Install **XAMPP** on your computer.
   - Open the **XAMPP** Control Panel.
   - Go to **MySQL** settings and change the port to **8000**:
     1. Find the line `port=3306` and change it to `port=8000`.
     2. Restart the MySQL server from the XAMPP Control Panel.

2. Clone the repository:
    ```cmd
    git clone https://github.com/Bvitriak1/Instruments-in-Music
    cd instruments-in-music
    ```
3. Create the database:
	- Find the music_db.sql file in the project folder after cloning.
	- Open phpMyAdmin (usually accessible at http://localhost:8000/phpmyadmin).
	- Go to the SQL tab.
	- Copy the content of the music_db.sql file.
	- Paste it into the text field and click Execute.
This will create the music_db database and populate it with initial data.

4. Install all required dependencies:
    For installing Python dependencies (if using Flask):
    ```cmd
    pip3 install flask pymysql
    ```
## Running
To run the application, follow these steps:

1. Start the server:
    **Python**:
    ```cmd
    python app.py
    ```

2. Open a browser and go to the address provided in the terminal.

## Project Structure
```
├── /static
│   ├── /css
│   │   └── style.css         # CSS styles
│   └── /js
│       └── script.js         # JavaScript scripts
│
├── /templates
│   └── index.html            # Main HTML page
│
├── app.py                    # Main server script
│
├── music_db.sql              # SQL file to create the database
│
├── requirements.txt          # List of Python dependencies
│
└── README.md                 # Project documentation
```
## Technologies

- **HTML5** — for page structure.
- **CSS3** — for styling and animations.
- **JavaScript** — for dynamic interactions.
- **Python (Flask)** — for the backend.
- **SQL** — for working with the database.