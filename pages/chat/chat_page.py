import flet as ft
from flet import (Page, Control, Column, Text, ElevatedButton,
                   Container,colors, border, border_radius, Row, alignment)
class Chat(Control):
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

    def size(self, height_percent = 100, width_percent = 100):
        height = self.page.height * height_percent / 100
        width = self.page.width * width_percent / 100
        return height, width

    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        self.page.update()


    def input_box(self):
    # This container will be used as an input box with specific dimensions
        containt = Row(
            controls=[
                Container(
                    alignment=alignment.bottom_center,
                    bgcolor=colors.AMBER_100, 
                    border_radius=10, 
                    height=self.size(height_percent=9)[0],  # Very small height as specified
                    content=Text("Type here..."),
                    border=border.all(1, colors.BLACK),
                    expand=True
            )
            ]
        )
        return containt

    def content(self):
        last_page = self.page.session.get("last_page")
        container_h, container_w = self.size(70)  # Getting the container size

        return Column(     
            controls=[       
                Container(
                    alignment=alignment.bottom_center,
                    bgcolor=colors.WHITE38, 
                    border_radius=10,
                    border=border.all(1, colors.BLACK), 
                    height=container_h, 
                    width=container_w,
                    content=self.input_box()  # Adding the small input box inside the container
                ),
                Text("This is Page 2"),
                ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
                Text(f"Last Page: {last_page}", selectable=False),
            ]
        )