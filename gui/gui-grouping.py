import flet as ft

groups = [
    ["psiholog iasi",
    ["psiholog iasi", "psiholog iasi pacurari", "psiholog iasi tg cucu", "psiholog iasi tarif", "psiholog iasi pret"]],
    ["psiholog online", ["psiholog online", "psiholog online pret", "psiholog online sedinta"]],
    ["cabinet psihoterapie", ["cabinet psihoterapie", "cabinet psihoterapie online", "cabinet psihoterapie iasi"]],
    ["psihoterapeut iasi", ["psihoterapeut iasi", "psihoterapeut iasi online", "psihoterapeut iasi pacuarari"]],
]


def main(page: ft.Page):
    page.title = "Simple List management"
    page.spacing = 0
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    for group in groups:
        tiles = []
        for keyword in group[1]:
            container = ft.Container(
                content=ft.Row(controls=[
                    ft.Text(keyword),
                ])
            )
            container.padding = ft.padding.only(left=40)

            tiles.append(ft.ListTile(
                title=container
            ))

        page.add(
            ft.ExpansionTile(
                affinity=ft.TileAffinity.LEADING,
                title=ft.Row(
                    controls=[
                        ft.Text(group[0], style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.Text(f'({len(group[1])})', style=ft.TextStyle(weight=ft.FontWeight.NORMAL, size=15)),
                    ]
                ),
                controls=tiles
            )
        )


ft.app(main)
