import time

import flet as ft


def main(page: ft.Page):
    page.title = "Simple List management"
    page.vertical_alignment = ft.MainAxisAlignment.START

    #page.horizontal_alignment = ft.CrossAxisAlignment.START

    # lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    # count = 1
    # for i in range(0, 60):
    #     lv.controls.append(ft.Text(f"Line {count}"))
    #     count += 1

    tfA = ft.TextField(multiline=True, min_lines=15, max_lines=15)
    tfR = ft.TextField(multiline=True, min_lines=20, max_lines=20)
    tfB = ft.TextField(multiline=True, min_lines=15, max_lines=15)

    def a_minus_b(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = a_values.difference(b_values)
        tfR.value = "\n".join(r_values)
        page.update()

    def b_minus_a(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.difference(a_values)
        tfR.value = "\n".join(r_values)
        page.update()

    def a_union_b(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.union(a_values)
        tfR.value = "\n".join(r_values)
        page.update()

    def a_intersection_b(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.intersection(a_values)
        tfR.value = "\n".join(r_values)
        page.update()

    def copy_r_to_b(e):
        tfB.value = tfR.value
        page.update()

    def copy_r_to_a(e):
        tfA.value = tfR.value
        page.update()

    def switch_a_b(e):
        tmp = tfA.value
        tfA.value = tfB.value
        tfB.value = tmp
        page.update()


    a = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(content=ft.Text(value="List A")),
                ft.Container(content=tfA)
            ],
        ),
        # bgcolor=ft.colors.AMBER_50,
        expand=1
    )

    r = ft.Container(
        content=ft.Column(controls=[
                ft.Row(controls=[
                    ft.ElevatedButton(text="A\\B", on_click=a_minus_b),
                    ft.ElevatedButton(text="B\\A", on_click=b_minus_a),
                    ft.ElevatedButton(text="B∪A", on_click=a_union_b),
                    ft.ElevatedButton(text="B∩A", on_click=a_intersection_b),
                ], alignment=ft.MainAxisAlignment.CENTER),
                tfR,
                ft.Row(controls=[ft.Text(value="Result list")], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[ft.ElevatedButton(text="A<->B", on_click=switch_a_b)], alignment=ft.MainAxisAlignment.CENTER),
            ],
            # alignment=ft.alignment.center
        ),
        expand=1
    )

    b = ft.Container(
        content=ft.Column(controls=[
            ft.Text(value="List B"),
            tfB
        ]),
        expand=1
    )

    row = ft.Row(
        controls=[
            a,
            ft.Column(
                controls=[ft.ElevatedButton(text="<--", on_click=copy_r_to_a)],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            r,
            ft.Column(
                controls=[ft.ElevatedButton(text="-->", on_click=copy_r_to_b)],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            b
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.controls.append(row)
    page.update()


ft.app(main)
