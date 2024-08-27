import os

HTML_CONTENT = '''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter Example</title>
    <link href="./index.css" type="text/css" rel="stylesheet">
</head>
<body>
    <header class="header">
        <h1 class="header__title">HTML/CSS/JS Project</h1>
    </header>
    <main class="main-content">
        <h2 class="main-content__title">Counter</h2>
        <div id="counter" class="counter">0</div>
        <div class="buttons">
            <button id="decrementBtn" class="button">-</button>
            <button id="incrementBtn" class="button">+</button>
        </div>
    </main>
    <script src="./script.js"></script>
</body>
</html>
'''


class HtmlBuilder:
    def __init__(self, path):
        self.path = path

    def create_html_file(self):
        html_path = os.path.join(self.path, 'index.html')
        with open(html_path, 'w') as html_file:
            html_file.write(HTML_CONTENT)
        print(f"HTML file created: {html_path}")