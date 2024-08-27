import os

CSS_CONTENT = '''body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.header {
    background-color: #007BFF;
    color: white;
    width: 100%;
    padding: 20px 0;
    text-align: center;
    flex-shrink: 0;
}

.header__title {
    margin: 0;
    font-size: 24px;
}

.main-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: white;
    width: 300px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: auto;
}

.main-content__title {
    margin-bottom: 20px;
    color: #333;
}

.counter {
    font-size: 48px;
    margin-bottom: 20px;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
}

.button {
    padding: 10px 20px;
    font-size: 24px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background-color: #007BFF;
    color: white;
    transition: background-color 0.3s;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.button:hover {
    background-color: #0056b3;
}

.button:active {
    background-color: #00408d;
}
'''


class CssBuilder:
    def __init__(self, path):
        self.path = path

    def create_css_file(self):
        css_path = os.path.join(self.path, 'index.css')
        with open(css_path, 'w') as css_file:
            css_file.write(CSS_CONTENT)
        print(f"CSS file created: {css_path}")