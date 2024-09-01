from flet import (Page, Control, Column, Text, TextField, KeyboardEvent,
                   Container,colors, border,  Row, TextButton,
                   alignment, BorderRadius, IconButton, icons, ListView, AlertDialog)
from components.models import ChatHandler
import time

class Chat(Control):   
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

   
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc
        self.__message_id = 0
        self.content = self.main_content
        
        # self.page.window_maximizable = True
        # self.page.window_resizable = True
        # self.page.on_keyboard_event = self.keyboard_event

    # def keyboard_event(self, e: KeyboardEvent):
    #     if e.key :
    #         self.page.window_minimizable = True
    #         # Adjust layout or TextField height
    #         print("keyboard_show")
    #         self.page.update()
    #     elif e.key == "":
    #         self.page.window_maximizable = True
    #         # self.page.window_maximized = True
    #         # Revert layout or TextField height
    #         self.page.update()
    #     else:
    #         print(e.__dict__)

        

    

    def size(self, height_percent = 100, width_percent = 100):
        '''return height, weight'''
        height = self.page.height * height_percent / 100
        width = self.page.window.width * width_percent / 100
        return height, width
    def did_mount(self):
          
        try:
            start_time = time.time()
            chat_handler = ChatHandler()
            messages = chat_handler.all_chats()
            # messages = messages[::-1]       
            if messages:
                print('messages not none')
                # print(messages)
                for message in messages:
                    message_id = message[0]
                    new_chat = message[2]  + str(message_id)
                    holder = self.message_designer(new_chat = new_chat)
                    self.text_holder.controls.append(holder)
                    self.__message_id += 1
                self.text_holder.update()
            end_time = time.time()
            print(f"Execution time: {end_time - start_time} seconds, {self.__message_id} messages")
                    # print(new_chat)
        except Exception as e:
            print(e)
       
        
        
        
    def chat_flow_controller(self, no_of_messages:int)->int:
        '''it takes how many no of chat need then 
            it set self.__message_id - no and
            it returns the last message id'''
        try:
            if self.__message_id == 0:
                return -1
            elif self.__message_id  < no_of_messages:
                '''messase are less than no of messages, so set message id to 0 
                and return no of messages as last message id'''
                self.__message_id = 0
                return no_of_messages
            elif self.__message_id >= no_of_messages:
                '''message are more than no of messages, so set message id to message id - no of messages
                and return message id as last message id'''
                last_index = self.__message_id
                self.__message_id -= no_of_messages # set message id
                return last_index

            else:
                print('ERROR IN CHAT FLOW CONTROLLER')
        except Exception as e:
            print('CHAT FLOW ERROR',e)
       
   
       
    def holder_box_controller(self, message, type):
        # print('holder box controller started')
        if type == "incoming":
            holder = self.message_designer(new_chat = message, type = type)
            self.text_holder.controls.insert(0, holder)
            self.text_holder.update()
            
        elif type == "outgoing":
            holder = self.message_designer(new_chat = message, type = type)
            self.text_holder.controls.insert(0, holder)
            self.text_holder.update()
            # Initialize 
        
        else:
            # print("Update Need in holder box controller")
            #show popup as error
            alert = AlertDialog(
                title=Text("Error"),
                content=Text("Update Need in holder box controller"),
                actions=[TextButton("OK")], open=True
            )

            self.page.add(alert)  # Add the alert to the page

            
            alert.update()    # Update the alert (optional)

            # print("Update Need in holder box controller")
    
   #insert the message in the database
    #Will be used to send the message
    def input_box_send(self, e):
       
        msg = (self.__input_field.value)
        if msg:
            #save the message in the database
            chat_handler = ChatHandler()
            chat_handler.insert_data(message=msg)
            # print("Send button clicked, text:", msg)
        
            # add the message to the holder box
            self.holder_box_controller(message=msg, type="outgoing")
            self.__input_field.value = ""
            self.__input_field.update()
            
    
    # Design and style the text holder
    def message_designer(self, new_chat = "", type = "incoming"):
        '''It Holds the Input as output'''
        # Create a Container to hold the Column
        text_container = Container(
            bgcolor=colors.GREY_300,
            # width=150,
            # width=self.page.width - 30,
            content= Column(
                    controls=[                
                            Text(new_chat, text_align='right', size=25, 
                                 color=colors.BLUE_700),
                        ],),
            border=border.all(1, colors.BLACK),
            padding=5,
            margin=0,
            # alignment=alignment.center_right,
            alignment=alignment.center_right,
            
            border_radius= BorderRadius(top_left=10, bottom_right=10, bottom_left=0, top_right=0),
        )
        return text_container
   
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
                    on_click=self.input_box_send,
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
        self.text_holder = ListView(
                            spacing=20,
                            # height=400,
                            # width=200,
                            reverse=True,
                            expand=True,
                            on_scroll_interval = 50,
                            # on_scroll=self.on_column_scroll,
                            divider_thickness = 1,
                            
                            controls=[],
                    )

        return self.text_holder

     # Retrieve the text from the input box and append it to the holder box
    def main_content(self):
        height, width = self.size()
        # print(height, width, "height, width")
        return Container(
            height=height-100,
            content=Column(
                controls=[
                    self.output_box(),
                    self.input_box(), 
                ],
            )
        )