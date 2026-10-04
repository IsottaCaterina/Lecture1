
import flet as ft

from UI.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c)
    v.carica_interfaccia()


ft.app(target = main)

"""import flet as ft


def main(page: ft.Page):
    mytxt = ft.Text(value = "Ciao da TdP 2026",
                    size = 24,
                    color = "red")
    page.controls.append(mytxt)
    page.update()

    mytxt2 = ft.Text("Un sottotitolo per il mio programma")
    page.add(mytxt2)

    row1 = ft.Row([ft.Text("Colonna 1"),
                   ft.Text("Colonna 2"),
                   ft.Text("Colonna 3")],
                  alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

ft.app(target = main)"""
