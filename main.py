import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_border_width(20)
        self.set_default_size(-1, 350)
        self.grid = Gtk.Grid()
        
        self.box_outer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(self.box_outer)

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
        self.box_outer.pack_start(scrolledwindow, True, True, 0)

        scrolledwindow_two.add(textview_two)
        self.box_outer.pack_start(scrolledwindow_two, True, True, 0)
    
        


win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
