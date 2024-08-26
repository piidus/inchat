import flet as ft
from flet import (Page, Control, Column, Text, TextField, ElevatedButton,
                   Container,colors, border, border_radius, Row, 
                   alignment, TextAlign, border)
class Chat(Control):
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc
        self.text_display = Text("")
        self.content = self.main_content  

    def size(self, height_percent = 100, width_percent = 100):
        height = self.page.height * height_percent / 100
        width = self.page.width * width_percent / 100
        return height, width

    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        self.page.update()

    def on_send_click(self, e):
        # Retrieve the text from the input box and update the text holder
        input_text = "Sample text"  # This should be retrieved from the actual input control
        self.text_display.value = input_text
        self.page.update()  # Refresh the page to reflect changes
        print("Send button clicked")
        
    def text_holder(self):
        # Container that will hold the text display
        return Container(
            alignment=alignment.center,
            bgcolor=colors.BLUE_100,
            border_radius=10,
               # Set the width as needed
            content=Row(
                controls=[
                    Text("Text Holder"),
                    self.text_display],
            ),  # Display the text
            border=border.all(1, colors.BLACK),
        )
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
    #Holder Container
    def holder_box(self):

        box_height, box_width = self.size(height_percent=60)
        holder = Container(
                alignment=alignment.center,
                bgcolor=colors.GREEN_100,
                border_radius=10,
                height=box_height,  # Half the height of the parent container
                # width=container_w * 0.8,   # 80% of the parent container's width
                content=Column(
                    controls=[Text("Input Holder"),
                                self.text_holder(),
                            ],
                        ),
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
            Text("This is Page 2"),
            ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
            Text(f"Last Page: {last_page}", selectable=False),
        ]
    )