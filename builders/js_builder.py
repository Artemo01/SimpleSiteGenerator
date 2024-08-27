import os

JS_CONTENT = '''let counter = 0;

document.getElementById('incrementBtn').addEventListener('click', () => {
    counter++;
    document.getElementById('counter').textContent = counter;
});

document.getElementById('decrementBtn').addEventListener('click', () => {
    counter--;
    document.getElementById('counter').textContent = counter;
});
'''


class JsBuilder:
    def __init__(self, path):
        self.path = path

    def create_js_file(self):
        js_path = os.path.join(self.path, 'script.js')
        with open(js_path, 'w') as js_file:
            js_file.write(JS_CONTENT)
        print(f"JavaScript file created: {js_path}")