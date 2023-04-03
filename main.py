from flet import Page, flet
from todo import TodoApp


def main(page: Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app)


flet.app(target=main)
