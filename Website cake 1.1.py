from jinja2 import Template

def generate_html(title, content):
    # HTML template
    template_str = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
    </head>
    <body>
        <div>
            <h1>{{ title }}</h1>
            <p>{{ content }}</p>
        </div>
    </body>
    </html>
    '''

    # Create a Jinja2 Template object
    template = Template(template_str)

    # Render the template with provided variables
    return template.render(title=title, content=content)

def save_to_file(html_content, filename='index.html'):
    # Save the generated HTML content to a file
    with open(filename, 'w') as file:
        file.write(html_content)

def main():
    # Main function
    website_title = input("Enter website title: ")
    website_content = input("Enter website content: ")

    # Generate HTML content
    html_content = generate_html(website_title, website_content)

    # Save to file
    save_to_file(html_content)
    print(f"Website '{website_title}' generated successfully in 'index.html'.")

if __name__ == "__main__":
    main()
