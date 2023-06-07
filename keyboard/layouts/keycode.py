from .style import Style

class KeyCode(object):
    
    def __init__(self, kc, js) -> None:
        self.text = js["text"]
        self.alt_text = js["alt_text"]
        self.caps = js["caps"]
        self.shift = js["shift"]
        self.alt_keycodes = js["alt_keycodes"]
        self.key_type = js["key_type"]
        self.keycode = kc

class Color(object):
    def __init__(self, js=None, r=0, g=0, b=0) -> None:
        self.red = int(js["r"]) if js is not None else r
        self.green = int(js["g"]) if js is not None else g
        self.blue = int(js["b"]) if js is not None else b

    def to_hex(self):
        return "#{:02x}{:02x}{:02x}".format(self.red, self.green, self.blue)


class KeyStyle(object):

    def __init__(self, style:Style, kc) -> None:

        stl = style.get_style_by_type(kc.key_type) if kc is not None else None 
        stl = style.get_style_by_keycode(kc.keycode) if kc is not None else None
        
        self.width = 0 if stl is None else stl["width"]
        self.background = Color(r=0,g=0,b=0) if stl is None else Color(js=stl["background"])
        self.color = Color(r=0,g=0,b=0) if stl is None else Color(js=stl["background"])
        self.pos_x = 0
        self.pos_y = 0

        

class Key(object):
    def __init__(self, stl, kc, js) -> None:
        
        self.keycode = KeyCode(kc, js)
        self.key_style = KeyStyle(stl, self.keycode)
        self.pressed = False
        self.hold = False

