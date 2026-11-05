import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_border_width(20)
        self.set_default_size(-1, 350)
        self.grid = Gtk.Grid()
        
        self.box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box_text_editor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        self.add(self.box_outer)
        self.box_outer.pack_end(self.box_text_editor, True, True, 0)

        # Scroll izquierdo
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        
        # Textview
        textview_one = Gtk.TextView()
        textbuffer_one = textview_one.get_buffer()
        textbuffer_one.set_text(
            "This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly."
        )

        # Scrol derecho
        scrolledwindow_two = Gtk.ScrolledWindow()
        scrolledwindow_two.set_hexpand(True)
        scrolledwindow_two.set_vexpand(True)

        # Textview dwerecho
        textview_two = Gtk.TextView()
        textbuffer_two = textview_two.get_buffer()
        textbuffer_two.set_text(
            "This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly."
        )

        # Unir cosas
        scrolledwindow.add(textview_one)
        self.box_text_editor.pack_start(scrolledwindow, True, True, 0)

        scrolledwindow_two.add(textview_two)
        self.box_text_editor.pack_start(scrolledwindow_two, True, True, 0)
    
        # Crate toolbar
        toolbar = Gtk.Toolbar()
        self.box_outer.pack_start(toolbar, True, True, 0)

        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        toolbar.insert(button_bold, 0)

        button_italic = Gtk.ToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        toolbar.insert(button_italic, 1)

        button_underline = Gtk.ToolButton()
        button_underline.set_icon_name("format-text-underline-symbolic")
        toolbar.insert(button_underline, 2)

        radio_justifyleft = Gtk.RadioToolButton()
        radio_justifyleft.set_icon_name("format-justify-left-symbolic")
        toolbar.insert(radio_justifyleft, 4)

        radio_justifycenter = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifycenter.set_icon_name("format-justify-center-symbolic")
        toolbar.insert(radio_justifycenter, 5)

        radio_justifyright = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyright.set_icon_name("format-justify-right-symbolic")
        toolbar.insert(radio_justifyright, 6)

        radio_justifyfill = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyfill.set_icon_name("format-justify-fill-symbolic")
        toolbar.insert(radio_justifyfill, 7)

        button_clear = Gtk.ToolButton()
        button_clear.set_icon_name("edit-clear-symbolic")
        toolbar.insert(button_clear, 9)

        button_search = Gtk.ToolButton()
        button_search.set_icon_name("system-search-symbolic")
        toolbar.insert(button_search, 11)

win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
