import flet as ft
from flet import (Page, Control, Column, Text, TextField, ElevatedButton,
                   Container,colors, border, border_radius, Row, 
                   alignment, TextAlign, border)
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

    def on_send_click(self, e):
        print("Send button clicked")
    def input_box(self):
    # This container will be used as an input box with specific dimensions
        box_height, box_width = self.size(height_percent=9)
        # Create the input box and send button
        containt = Row(
            controls=[
                Container(
                    alignment=alignment.center_left,
                    # bgcolor=colors.AMBER_100,
                    border_radius=10,
                    height=box_height,
                    width=box_width * 0.8,  # Take 80% of the width for the input box
                    content=TextField(hint_text="Type here...", border_color=None,),
                    
                    expand=True  # Allow the input box to expand to fill available space
                ),
                ElevatedButton(
                    text="Send",
                    on_click=self.on_send_click,  # Replace with your send function
                    expand=False  # Do not expand the button; it should have a fixed size
                )
            ],
            alignment="spaceBetween"  # Ensure the send button is on the right
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