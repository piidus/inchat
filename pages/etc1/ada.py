import flet as ft

class Ada(ft.Control): 
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc  
        page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def content(self):
        # Chat messages
        chat = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
        )
        chat_container = ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        )
        # A new message entry form
        new_message = ft.TextField(
            hint_text="Write a message...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            # on_submit=send_message_click,
        )
        
        send_row = ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    # on_click=send_message_click,
                ),
            ]
        )

        # self.page.add(text_field)

        # self.page.update()
        return ft.Column(
            controls=[
                chat_container, 
                send_row
            ],
            expand=True
        )
