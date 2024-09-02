import flet as ft
class Ada(ft.Control): 
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc  
        # page.title = "Adaptive Height Text Field"
    def content(self):
        chat_container = ft.Container(
            # content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        send_row = ft.Row(
                    [
                        # new_message,
                        ft.IconButton(
                            icon=ft.icons.SEND_ROUNDED,
                            tooltip="Send message",
                            # on_click=send_message_click,
                        ),
                    ]
                ),

        # self.page.add(text_field)

        self.page.update()
        return ft.Column(
            controls=[
                chat_container, 
                send_row],
            )