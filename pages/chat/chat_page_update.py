import flet as ft
from flet import (Page, Control, Column, Text, TextField, 
                   Container,colors, border, ScrollMode, Row, TextButton,
                   alignment, BorderRadius, IconButton, icons, ControlEvent, AlertDialog)
'''
    __init__ : pc for page controller | self.content returns the main content of the page
    self.size() : it returns the height and width of the container
    self.did_mount() : sets the last page in the session and updates the page with previous messages
    self.on_text_change() : a helper function that increases the height of the TextField and ensures the Container holding the TextField also adjusts its height
    self.input_box() : takes input 
    self.output_box() : contain all messages
    self.message_designer : returns the designing message container       
    self.holder_box_controller() : check incoming or outgoing messages and save data to database, 
                        and add them to the holder box
'''
class MyOnScrollEvent(ft.ControlEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = "reverse"
    def __str__(self):
        print(self.direction, self.pixels, self.max_scroll_extent, self.scroll_offset)

    def build(self):
        
        return MyOnScrollEvent

class ChatUpdate(Control):
    def __init__(self, page: ft.Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc
        self.__scroll_position = 0
        self.content = self.main_content

    def size(self, height_percent = 100, width_percent = 100):
        '''return height, weight'''
        height = self.page.window.height * height_percent / 100
        width = self.page.window.width * width_percent / 100
        return height, width
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
       
            

   
    def input_box(self):
        # Function to handle text changes and check for Enter key
        box_height, box_width = self.size()
        # print(box_height, box_width, "box_height, box_width")
        self.__input_field = TextField(
            hint_text="Type here...",
            border_color=None,
            autofocus=True,
            width=box_width * 0.75,  # Allow it to be a single line initially
            # height=ft.AUTO,
            multiline=True,
            max_lines=5,
            # on_change=self.on_text_change,
            expand=False,
        )
        icon_button = Container(
            content=IconButton(
                    icon=icons.SEND_AND_ARCHIVE_OUTLINED,
                    icon_size=24,
                    # on_click=self.on_send_click,
                ),
        )
        # Create the input box and send button
        total_containt = Row(
            controls=[
                self.__input_field,
                icon_button,
                ],
                alignment="spaceBetween",  # Ensure the send button is on the right
            )
        return total_containt
    
    def output_box(self):
        '''This is the container that holds all output as text_holder'''
        self.text_holder = ft.ListView(
                            spacing=20,
                            # height=400,
                            # width=200,
                            reverse=True,
                            expand=True,
                            on_scroll_interval = 30,
                            on_scroll=self.on_column_scroll,
                            divider_thickness = 3,
                            
                            controls=[],
                    )

        return self.text_holder

     # Retrieve the text from the input box and append it to the holder box
    def main_content(self):
        height, width = self.size()
        return Container(
            height=height,
            content=Column(
                controls=[
                    self.output_box(),
                    self.input_box(), 
                ],
            )
        )
