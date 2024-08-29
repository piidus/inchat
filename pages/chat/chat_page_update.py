import flet as ft
import time
class TextHolderColumn(ft.ListView):
    def __init__(self, *args, **kwargs):
        super().__init__(
            spacing=kwargs.get('spacing', 10),
            height=kwargs.get('height', 200),
            width=kwargs.get('width', 200),
            # scroll=kwargs.get('scroll', "always"),
            on_scroll=kwargs.get('on_scroll', None),
            # auto_scroll=kwargs.get('auto_scroll', True),
            reverse=kwargs.get('reverse', True),
            expand=kwargs.get('expand', True),
            controls=kwargs.get('controls', []),
            # item_extent=kwargs.get('item_extent', 50),
        )
class MyOnScrollEvent(ft.ControlEvent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = "reverse"
        # self.event_type = "update"
        # self.scroll_to = (delta =-5)
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
                            spacing=10,
                            height=400,
                            width=200,
                            reverse=True,
                            expand=True,
                            on_scroll_interval = 30,
                            on_scroll=self.on_column_scroll,
                            controls=[],
                        )

        return ft.Column(
            controls=[
                self.text_holder,
                ft.Row(
                    controls=[
                        ft.Text("Row", size=20),
                        ft.ElevatedButton("Chat"),
                    ],
                ),
            ],
        )
