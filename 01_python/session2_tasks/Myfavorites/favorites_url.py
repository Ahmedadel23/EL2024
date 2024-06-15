import webbrowser

# Dictionary of favorite websites
favorite_websites = {
    'Google': 'https://www.google.com',
    'GitHub': 'https://www.github.com',
    'Stack Overflow': 'https://stackoverflow.com',
}

def firefox(url):
 
    # Open the URL in Firefox
    webbrowser.get('firefox').open(url)

# Example usage
if __name__ == '__main__':
    # Open GitHub in Firefox
    firefox(favorite_websites['GitHub'])
