import os

from builders.html_builder import HtmlBuilder
from builders.css_builder import CssBuilder
from builders.js_builder import JsBuilder


class ProjectBuilder:
    def __init__(self, project_name, parent_dir):
        self.project_name = project_name
        self.parent_dir = parent_dir
        self.path = os.path.join(parent_dir, project_name)

    def create_project_directory(self):
        try:
            os.makedirs(self.path)
            print(f"Created directory: {self.path}")
        except OSError as e:
            print(f"Failed to create directory. Error: {e}")
            exit(1)

    def build_project(self):
        HtmlBuilder(self.path).create_html_file()
        CssBuilder(self.path).create_css_file()
        JsBuilder(self.path).create_js_file()


def main():
    parent_dir = input("Enter path for your project: ")
    project_name = input("Enter project name: ")

    project = ProjectBuilder(project_name, parent_dir)
    project.create_project_directory()
    project.build_project()


if __name__ == "__main__":
    main()