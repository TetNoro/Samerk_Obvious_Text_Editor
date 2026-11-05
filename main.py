import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class TextViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_border_width(20)
        self.set_default_size(-1, 350)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textview()

    def create_textview(self):
        box_outer1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(box_outer1, 0, 1, 1, 1)
        textview_one = Gtk.TextView()
        textbuffer_one = textview_one.get_buffer()
        textbuffer_one.set_text(
            "This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly."
        )
        scrolledwindow.add(textview_one)
        box_outer1.add(scrolledwindow)

        box_outer2 = Gtk.Box(spacing=6)
        scrolledwindow_two = Gtk.ScrolledWindow()
        scrolledwindow_two.set_hexpand(True)
        scrolledwindow_two.set_vexpand(True)
        self.grid.attach(box_outer2, 3, 1, 1, 1)
        textview_two = Gtk.TextView()
        textbuffer_two = textview_two.get_buffer()
        textbuffer_two.set_text(
            "Other text "
        )
        
        scrolledwindow_two.add(textview_two)
        box_outer2.add(scrolledwindow_two)
    
        


win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
