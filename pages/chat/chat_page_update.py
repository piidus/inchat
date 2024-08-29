import flet as ft
from flet import (Page, Control, Column, Text, TextField, 
                   Container,colors, border, ScrollMode, Row, TextButton,
                   alignment, BorderRadius, IconButton, icons, ControlEvent, AlertDialog)
from components.models import ChatHandler

class MyOnScrollEvent(ft.ControlEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = "reverse"
    def __str__(self):
        print(self.direction, self.pixels, self.max_scroll_extent, self.scroll_offset)

    def build(self):
        
        return MyOnScrollEvent

class ChatUpdate(ft.Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc
        self.__scroll_position = 0
        self.content()


    def did_mount(self):
        # Run demo to add initial values and scroll to the end
        self.demo()
        self.text_holder.update()
        
        
        

    def demo(self):
        print('demo run')
        for i in range(35):
            self.text_holder.controls.append(ft.Text("Hello" + "--" + str(self.__scroll_position+1)))#, key=str(self.__scroll_position)))
            self.__scroll_position += 1
       

    def on_column_scroll(self, e: MyOnScrollEvent):
        # print(e.pixels, e.max_scroll_extent, "on_column_scroll", self.__scroll_position)
        
        if e.pixels >= e.max_scroll_extent - 130 :
            print("IT CROSSED")
            self.demo()
            self.text_holder.update()
       
            

    def content(self):
        self.text_holder = ft.ListView(
                            spacing=20,
                            height=400,
                            width=200,
                            reverse=True,
                            expand=True,
                            on_scroll_interval = 30,
                            on_scroll=self.on_column_scroll,
                            divider_thickness = 3,
                            
                            controls=[],
                        )
    def input_box(self):
        # Function to handle text changes and check for Enter key
        box_height, box_width = self.size(height_percent=9)
        self.__input_field = TextField(
            hint_text="Type here...",
            border_color=None,
            autofocus=True,
            min_lines=1,  # Allow it to be a single line initially
            # on_change=self.on_text_change,
            expand=False,
        )
        
        # Create the input box and send button
        containt = Row(
            controls=[
                Container(
                    alignment=alignment.center_left,
                    border_radius=10,
                    height=box_height,  # Initial height
                    width=box_width * 0.8,  # Take 80% of the width for the input box
                    # content=self.__input_field,
                    expand=True,  # Allow the input box to expand to fill available space
                ),
                IconButton(
                    icon=icons.SEND_AND_ARCHIVE_OUTLINED,
                    icon_size=24,
                    on_click=self.on_send_click,
                ),
            ],
            alignment="spaceBetween",  # Ensure the send button is on the right
        )
        return containt
    

   
     # Retrieve the text from the input box and append it to the holder box
    

        return ft.Column(
            controls=[
                self.text_holder,
                self.input_box, 
            ],
        )
