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
        # time.sleep(1)
        # self.text_holder.auto_scroll = False
        # self.text_holder.on_scroll = self.on_column_scroll
        # self.text_holder.update()
        
        

        # Scroll to the end after page update
        # self.text_holder.scroll_to(key=f"{self.__scroll_position}", duration=500)
        # self.text_holder.on_scroll = self.on_column_scroll
        # # self.text_holder.update()
        # # Activate on_scroll and deactivate auto_scroll after the initial setup
        # # self.text_holder.auto_scroll = False
        # self.text_holder.on_scroll = None
        # self.page.update()
        # time.sleep(1)
        # self.text_holder.on_scroll = self.on_column_scroll
        # self.text_holder.scroll_to(delta=0)
        # self.text_holder.update()
        
        

    def demo(self):
        print('demo run')
        for i in range(12):
            self.text_holder.controls.append(ft.Text("Hello" + "--" + str(self.__scroll_position), key=str(self.__scroll_position)))
            self.__scroll_position += 1
        print('demo done', len(self.text_holder.controls))
        # self.text_holder.scroll_to(len(self.text_holder.controls) - 1)

    def on_column_scroll(self, e: ft.OnScrollEvent):
        print(e.pixels, "on_column_scroll", self.__scroll_position)

        if e.pixels >= e.max_scroll_extent -2:
            self.demo()
            # self.text_holder.update()
        self.text_holder.update()
            

    def content(self):
        self.text_holder = TextHolderColumn(
                            spacing=10,
                            height=200,
                            width=200,
                            # scroll="auto",
                            # auto_scroll=True,
                            expand=True,
                            # item_extent=50,
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
