import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
page.bgcolor = "#0C905A"

ft.app(main)
