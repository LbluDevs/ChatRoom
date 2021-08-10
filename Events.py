class events:
    def on_hover(obj, **kwargs):
        """Takes two parameters text and text before
            when hovers the text placed will be applied
            when leaves the normal text will be applied
        """
        text = kwargs.get('text')
        text_before = kwargs.get('text_bf')

        obj.bind('<Enter>', lambda x: obj.config(text=text))
        obj.bind('<Leave>', lambda x: obj.config(text=text_before))

    def on_enter_pressed(obj, next_obj):
        """Takes two parameters the object that is focused
            and the object that will be focused next
            """
        obj.bind('<Return>', lambda x: next_obj.focus())

    def on_enter_pressed_send(obj, next_obj):
        """Takes two parameters the object that is focused
            and the function that will be called
            """
        obj.bind('<Return>', lambda x: next_obj())