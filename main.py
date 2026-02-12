from pyscript import display, document



def create_account(e):
    document.getElementById('output').innerHTML = ''
    
    username = document.getElementById('input1').value
    password = document.getElementById('input2').value

    if len(username) < 7:
        display(f'Username must be at least 7 characters long.', target='output')
    if len(password) < 10:
        display(f'Password must be at least 10 characters long.', target='output')

    if password.isalpha():
            display(f'Password must contain numbers', target='output')

    elif password.isdigit():
            display(f'Password must contain letters', target='output')
    
    if len(username) >= 7 and len(password) >= 10 and not password.isalpha() and not password.isdigit():
        display(f'Account created successfully!', target='output')