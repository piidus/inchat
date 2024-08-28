from flet import (Page, Control, Column, Text, TextField, ListView,
                   Container,colors, border, ScrollMode, Row, OnScrollEvent,
                   alignment, BorderRadius, IconButton, icons, ControlEvent)
from components.models import insert_message_thread, ChatHandler
import flet as ft
class MyOnScrollEvent(OnScrollEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_delta =None
        self.direction= None
        self.overscroll= None
        self.velocity= None


class ChatUpdate(Control):   
    '''
        __init__ : pc for page controller | self.content returns the main content of the page
        self.size() : it returns the height and width of the container
        self.did_mount() : sets the last page in the session and updates the page with previous messages
        self.on_text_change() : a helper function that increases the height of the TextField and ensures the Container holding the TextField also adjusts its height
        self.input_box() : takes input 
        self.holder_box() : contain previous messages
        self.message_designer : returns the message container
        
        self.holder_box_controller() : returns the holder box with previous messages
    '''

    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc 
        self.content()
        
        # self.content = self.main_content
    # hold one listview and one row horizoltally
    def demo(self):
        for i in range(25):
            self.text_holder.controls.append(ft.Text("Hello"+"--"+str(i)))
            self.page.update()
    def on_column_scroll(self,e: OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )
        if e.pixels == e.max_scroll_extent:
            self.demo()

    def content(self):
        self.text_holder = ft.Column(
            spacing=10,
            height=200,
            width=200,
            scroll="always",            
            on_scroll=self.on_column_scroll,
            # auto_scroll=True,
            
        )
        self.demo()
        return ft.Column(
            controls=[
                self.text_holder,
                ft.Row(
                    controls=[
                        ft.Text("Row"),
                    ],
                ),
            ],
        )