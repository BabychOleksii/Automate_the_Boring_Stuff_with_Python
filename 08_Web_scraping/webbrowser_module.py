import sys, webbrowser, pyperclip


sys.argv = ['mapit.py', '870', 'Valencia', 'St.', 'San', 'Francisco', 'CA', '94110']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.', 'San', 'Francisco', 'CA', '94110'] -> 870 Valencia St.
    # San Francisco CA 94110
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com.ua/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com.ua/maps/place/' + address)
