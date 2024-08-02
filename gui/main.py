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

    statsA = ft.Text(value="No keyword: 0");
    statsB = ft.Text(value="No keyword: 0");
    statsR = ft.Text(value="No keyword: 0");

    def str_2_keys(str):
        chunks = str.strip().split(sep="\n")
        clean_chunks = filter(lambda x : x != '', chunks)
        return clean_chunks

    def update_no_keywords_a(e, update=True):
        a_values = set(str_2_keys(tfA.value))
        statsA.value = f'No keyword: {len(a_values)}'
        if update:
            page.update()

    def update_no_keywords_b(e, update=True):
        b_values = set(str_2_keys(tfB.value))
        statsB.value = f'No keyword: {len(b_values)}'
        if update:
            page.update()

    def update_no_keywords_r(e, update=True):
        r_values = set(str_2_keys(tfR.value))
        statsR.value = f'No keyword: {len(r_values)}'
        if update:
            page.update()

    def update_stats(e, update):
        update_no_keywords_a(e, False)
        update_no_keywords_r(e, False)
        update_no_keywords_b(e, False)
        page.update()

    tfA = ft.TextField(multiline=True, min_lines=15, max_lines=15, on_change=update_no_keywords_a)
    tfR = ft.TextField(multiline=True, min_lines=20, max_lines=20, on_change=update_no_keywords_r)
    tfB = ft.TextField(multiline=True, min_lines=15, max_lines=15, on_change=update_no_keywords_b)



    def a_minus_b(e):
        a_values = set(tfA.value.strip().split(sep="\n"))
        b_values = set(tfB.value.strip().split(sep="\n"))
        r_values = a_values.difference(b_values)
        tfR.value = "\n".join(r_values)
        update_stats(e, False)
        page.update()

    def b_minus_a(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.difference(a_values)
        tfR.value = "\n".join(r_values)
        update_stats(e, False)
        page.update()

    def a_union_b(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.union(a_values)
        tfR.value = "\n".join(r_values)
        update_stats(e, False)
        page.update()

    def a_intersection_b(e):
        a_values = set(tfA.value.split(sep="\n"))
        b_values = set(tfB.value.split(sep="\n"))
        r_values = b_values.intersection(a_values)
        tfR.value = "\n".join(r_values)
        update_stats(e, False)
        page.update()

    def copy_r_to_b(e):
        tfB.value = tfR.value
        update_stats(e, False)
        page.update()

    def copy_r_to_a(e):
        tfA.value = tfR.value
        update_stats(e, False)
        page.update()

    def switch_a_b(e):
        tmp = tfA.value
        tfA.value = tfB.value
        tfB.value = tmp
        update_stats(e, False)
        page.update()




    a = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(content=ft.Text(value="List A")),
                ft.Container(content=tfA),
                statsA
            ],
        ),
        # bgcolor=ft.colors.AMBER_50,
        expand=1
    )

    r = ft.Container(
        content=ft.Column(controls=[
                ft.Row(controls=[
                    ft.ElevatedButton(text="A\\B", on_click=a_minus_b, tooltip='Keywords present in A but not in B'),
                    ft.ElevatedButton(text="B\\A", on_click=b_minus_a, tooltip='Keywords present in B but not in A'),
                    ft.ElevatedButton(text="B∪A", on_click=a_union_b, tooltip='Keywords present either in A or in B'),
                    ft.ElevatedButton(text="B∩A", on_click=a_intersection_b, tooltip='Keywords present both in A and in B'),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[ft.Text(value="Result list")], alignment=ft.MainAxisAlignment.START),
                tfR,
                statsR,
                ft.Row(
                    controls=[ft.ElevatedButton(text="A<->B", on_click=switch_a_b, tooltip='Switch keywords between A and B')],
                    alignment=ft.MainAxisAlignment.CENTER
                       ),
            ],
            # alignment=ft.alignment.center
        ),
        expand=1
    )

    b = ft.Container(
        content=ft.Column(controls=[
            ft.Text(value="List B"),
            tfB,
            statsB
        ]),
        expand=1
    )

    row = ft.Row(
        controls=[
            a,
            ft.Column(
                controls=[ft.ElevatedButton(text="<--", on_click=copy_r_to_a, tooltip='Copy resulted keywords to A')],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            r,
            ft.Column(
                controls=[ft.ElevatedButton(text="-->", on_click=copy_r_to_b,  tooltip='Copy resulted keywords to B')],
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
