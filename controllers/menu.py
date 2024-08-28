import flet as ft

def menu(pc):
    return ft.AppBar(
        title=ft.Text("In-Chat"),
        actions=[
            ft.IconButton(
                icon=ft.icons.HOME,
                on_click=lambda _: pc.navigate_to("Login")
            ),
            ft.IconButton(
                icon=ft.icons.INFO,
                on_click=lambda _: pc.navigate_to("Chat")
            ),
            ft.IconButton(
                icon=ft.icons.EDIT_ATTRIBUTES_ROUNDED,
                on_click=lambda _: pc.navigate_to("ChatUpdate")
            ),
        ]
    )
