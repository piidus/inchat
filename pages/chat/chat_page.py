import flet as ft
from flet import Page, Control, Column, Text, ElevatedButton, Container
class Chat(Control):
    def __init__(self, page: Page, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.pc = pc

  
    def did_mount(self):
        self.page.session.set("last_page", "Page2")
        print('did mount page 2')
        self.page.update()

    def content(self):
        last_page = self.page.session.get("last_page")
        return Column(            
            controls=[
                Container(bgcolor="blue", height=200, width=200,
                    
                ),
                Text("This is Page 2"),
                ElevatedButton("Go to Page 1", on_click=lambda _: self.pc.load_page("Login")),
                Text(f"Last Page: {last_page}", selectable=False),

            
            ]
        )
