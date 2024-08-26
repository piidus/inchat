import flet as ft
from flet import (Page, Control, Column, Text, TextField, ElevatedButton,
                   Container,colors, border, ScrollMode, Row, 
                   alignment, Icon, border)
class Chat(Control):
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc
        self.holder_column = self.text_holder('new_chat')
        self.content = self.main_content  


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
        box_height, box_width = self.size(height_percent=9)
        self.__input_field=TextField(hint_text="Type here...", border_color=None,)
        # Create the input box and send button
        containt = Row(
            controls=[
                Container(
                    alignment=alignment.center_left,
                    # bgcolor=colors.AMBER_100,
                    border_radius=10,
                    height=box_height,
                    width=box_width * 0.8,  # Take 80% of the width for the input box
                    
                    content=self.__input_field,
                    expand=True  # Allow the input box to expand to fill available space
                ),
                ElevatedButton(
                    # text="Send",
                    icon=Icon(name=ft.icons.SEND_AND_ARCHIVE_SHARP, color=colors.TEAL_300, size=24),
                    on_click=self.on_send_click,  # Replace with your send function
                    # expand=False  # Do not expand the button; it should have a fixed size
                    bgcolor=colors.AMBER_100
                )
            ],
            alignment="spaceBetween"  # Ensure the send button is on the right
        )
        
        return containt
    #Holder Container
    def on_send_click(self, e):
        # Retrieve the text from the input box and append it to the holder box
        tes = str(self.__input_field.value)
        # print(tes)
        if tes:
        # self.holder_column.controls.append(new_text)
            self.holder_column.controls.append(self.text_holder(new_chat=tes))

            self.page.update()  # Refresh the page to reflect changes
            print("Send button clicked")

    def text_holder(self, new_chat=None):
        '''It Holds the Input as output'''
        # Container that will hold the text display
        text_column = Column(
            controls=[
                Text(new_chat),
            ],
            
        )
        return text_column

    def holder_box(self):
        '''This is the container, holds all output as text_holder'''
        box_height, box_width = self.size(height_percent=60)

        holder = Container(

            alignment=alignment.bottom_center,
            bgcolor=colors.GREEN_100,
            border_radius=10,
            height=box_height,  # Set the height as needed
            content=Column(
    
                controls=[self.holder_column,],
                spacing=5,
                scroll=ScrollMode.AUTO,
                auto_scroll=True,
                width=box_width - 30,
                # expand=True,
                ),  # Use the holder_column to append texts
            border=border.all(1, colors.BLACK),
            
        )

        return holder
    def main_content(self):
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
                content=Column(
                    controls=[
                         # Adding the input box inside the inner container
                        self.holder_box(),
                        self.input_box(), 
                    ]
                )
            ),
            # Text("This is Page 2"),
            # ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
            # Text(f"Last Page: {last_page}", selectable=False),
        ]
    )