import flet as ft
from todo import TodoApp

def main(page: ft.Page):
    # create application instance
    app1 = TodoApp()
    app2 = TodoApp()

# add application's root control to the page
    page.add(app1, app2)

ft.app(target=main)