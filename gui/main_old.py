import time

import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C"),
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ]))


    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    t = ft.Text("Hello, Flet :) !", color="green")
    # page.add(ft.SafeArea(t))
    page.controls.append(t)
    page.update()

    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1)

    def remove_task(e : ft.ControlEvent):
        # e.page.controls.remove(e.target)
        print(e.name)
        pass

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value, on_change=remove_task(e)))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))


ft.app(main)
