# Student Club Member Checker
from pyscript import display, document # type: ignore

def student_club(e):
    document.getElementById('result').innerHTML = ' '
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    # Combines the first and last names 
    studentname = firstname + ' ' + lastname

    # List of members 
    cosmic_names = ['Elianna Co','Georgina Sarmiento','Mallorie Micu', '']

    # Checks if student's name inputted matches a current member 
    member_checker = studentname in cosmic_names

    # Displays acceptance or rejection 
    display_message = (f'Sorry, you are not a part of the Cosmic Writers Guild.', f'Congratulations {studentname}, you are now part of the OBMC Cosmic Writers Guild Club!')

    document.getElementById('result').innerHTML = (display_message[member_checker])