from flet import (Page, Control, Column, Text, TextField, 
                   Container,colors, border, ScrollMode, Row, 
                   alignment, BorderRadius, IconButton, icons, ControlEvent)
from components.models import insert_message_thread, ChatHandler


class Chat(Control):    
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc 
        #supply the main content to page controller
        self.content = self.main_content
        
        



    # This function is used to calculate the height and width of the container
    def size(self, height_percent = 100, width_percent = 100):
        height = self.page.height * height_percent / 100
        width = self.page.width * width_percent / 100
        return height, width
    
    
    # This function is used to set the last page in the session
    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        # first update with previous messages
        self.holder_box_controller()
        self.page.update()
    def on_text_change(self, e: ControlEvent):
            if "\n" in e.control.value:
                # Increase the height of the TextField
                self.__input_field.height += 20  # Increment height
                # Ensure the Container holding the TextField also adjusts its height
                e.control.parent.height = self.__input_field.height
                self.page.update()

    def input_box(self):
        # Function to handle text changes and check for Enter key
        box_height, box_width = self.size(height_percent=9)
        self.__input_field = TextField(
            hint_text="Type here...",
            border_color=None,
            autofocus=True,
            min_lines=1,  # Allow it to be a single line initially
            on_change=self.on_text_change,
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
                    content=self.__input_field,
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
    

    #insert the message in the database
    #Will be used to send the message
    def on_send_click(self, e):
       
        tes = (self.__input_field.value)
        if tes:
            insert_message_thread(tes)
            print("Send button clicked, text:", tes)
            t = self.holder_box_controller()
        
            
        
        
        # print("Send button clicked, text:", tes)
    def holder_box_controller(self):
        print('holder box controller started')
            # Initialize 
        try:
            chat_handler = ChatHandler()
            messages = chat_handler.last_10_messages()
            messages = messages[::-1]       
            if messages:
                print('messages not none')
                # print(messages)
                for message in messages:
                    new_chat = message[2]
                    holder = self.text_holder(new_chat = new_chat)
                    self.holder_column.controls.append(holder)
                    self.holder_column.update()
                    # print(new_chat)
        except Exception as e:
            print(e)
        else:
            self.__input_field.value = ""
            self.page.update()

    # Design and style the text holder
    def text_holder(self, new_chat = ""):
        '''It Holds the Input as output'''
        # Create a Container to hold the Column
        text_container = Container(
            bgcolor=colors.GREY_300,
            # width=150,
            width=self.page.width - 30,
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

    # It holds the output Box container
    def holder_box(self):
        '''This is the container that holds all output as text_holder'''
        box_height, box_width = self.size(height_percent=80)
        
        # Initialize holder_column as a Column
        self.holder_column = Column(
            controls=[],  # Start with an empty list of controls
            spacing=15,
            scroll=ScrollMode.AUTO,
            auto_scroll=True,
            width=box_width - 30,
        )

        holder = Container(
            alignment=alignment.bottom_center,
            bgcolor=colors.GREEN_100,
            border_radius=10,
            height=box_height,  # Set the height as needed
            content=self.holder_column,  # Set holder_column as the content of the holder
            border=border.all(1, colors.BLACK),
        )

        return holder

    # Main content of the page
    def main_content(self):
        """
        Returns the main content of the page, including a container with a column of controls.
        
        The container has a white background, a black border, and a bottom-center alignment.
        
        The column of controls includes a holder box and an input box.
        
        :return: A Column control containing the main content of the page.
        """

        last_page = self.page.session.get("last_page")
        container_h, container_w = self.size(height_percent=85)  # Getting the container size

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
                    ],
                    scroll=ScrollMode.AUTO,  # Enable auto-scrolling
                )
            ),
            # Text("This is Page 2"),
            # ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
            # Text(f"Last Page: {last_page}", selectable=False),
        ]
    )