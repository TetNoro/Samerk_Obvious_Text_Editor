import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class TextViewWindow(Gtk.Window):
    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.SAVE
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File Saved: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def imprimir_info(self, *arg):
        print(arg[2])

    def onFocusIn(self, tv, event):
        textbuf = tv.get_buffer()
        if (textbuf.get_text(textbuf.get_start_iter(), textbuf.get_end_iter(), True) == self.text_place_holder):
            textbuf.set_text("")
        return False


    def onFocusOut(self, tv, event):
        textbuf = tv.get_buffer()
        if (textbuf.get_text(textbuf.get_start_iter(), textbuf.get_end_iter(), True) == ""):
            textbuf.set_text(self.text_place_holder)
        return False


    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_border_width(20)
        self.set_default_size(-1, 350)
        self.grid = Gtk.Grid()
        
        self.box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box_text_editor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        self.text_place_holder = """Inserta texto aqui
        """
        self.show_place_holder = True

        self.add(self.box_outer)

        # Scroll izquierdo
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        
        # Textview
        textview_one = Gtk.TextView()
        textbuffer_one = textview_one.get_buffer()
        textbuffer_one.set_text(self.text_place_holder)
        textview_one.connect("focus-in-event", self.onFocusIn)
        textview_one.connect("focus-out-event", self.onFocusOut)
        #textview_one.connect("focus-out-event", self.erase_place_holder)
        #textview_one.connect("focus-in-event", self.set_place_holder)

        # Scrol derecho
        scrolledwindow_two = Gtk.ScrolledWindow()
        scrolledwindow_two.set_hexpand(True)
        scrolledwindow_two.set_vexpand(True)

        # Textview dwerecho
        textview_two = Gtk.TextView()
        textbuffer_two = textview_two.get_buffer()
        textbuffer_two.set_text("""Aca puedes ver la salida de tu codigo
:)
        """
        )

        # Unir cosas
        scrolledwindow.add(textview_one)
        self.box_text_editor.pack_start(scrolledwindow, True, True, 0)
        textview_one.get_buffer().connect("insert-text", self.imprimir_info)

        scrolledwindow_two.add(textview_two)
        self.box_text_editor.pack_start(scrolledwindow_two, True, True, 0)

    
        # Crate toolbar
        toolbar = Gtk.Toolbar()

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

        button_open = Gtk.ToolButton()
        button_open.set_icon_name("document-open-symbolic")
        button_open.connect("clicked", self.on_file_clicked)
        toolbar.insert(button_open, 12)

        button_save = Gtk.ToolButton()
        button_save.set_icon_name("document-save-symbolic")
        button_save.connect("clicked", self.on_save_clicked)
        toolbar.insert(button_save, 13)

        button_delete = Gtk.ToolButton()
        button_delete.set_icon_name("user-trash-symbolic")
        toolbar.insert(button_delete, 14)

        button_cut = Gtk.ToolButton()
        button_cut.set_icon_name("edit-cut-symbolic")
        toolbar.insert(button_cut, 12)

        button_copy = Gtk.ToolButton()
        button_copy.set_icon_name("edit-copy-symbolic")
        toolbar.insert(button_copy, 13)

        button_paste = Gtk.ToolButton()
        button_paste.set_icon_name("edit-paste-symbolic")
        toolbar.insert(button_paste, 14)

        button_refresh = Gtk.ToolButton()
        button_refresh.set_icon_name("view-refresh-symbolic")
        toolbar.insert(button_refresh, 15)

        # Crear los botones
        grid_botones = Gtk.Grid()


        check_editable = Gtk.CheckButton(label="Editable")
        check_editable.set_active(True)
        grid_botones.attach(check_editable, 0, 0, 1, 1)

        check_cursor = Gtk.CheckButton(label="Cursor Visible")
        check_cursor.set_active(True)
        grid_botones.attach_next_to(
            check_cursor, check_editable, Gtk.PositionType.RIGHT, 1, 1
        )

        radio_wrapnone = Gtk.RadioButton.new_with_label_from_widget(None, "No Wrapping")
        grid_botones.attach(radio_wrapnone, 0, 1, 1, 1)

        radio_wrapchar = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Character Wrapping"
        )
        grid_botones.attach_next_to(
            radio_wrapchar, radio_wrapnone, Gtk.PositionType.RIGHT, 1, 1
        )

        radio_wrapword = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Word Wrapping"
        )
        grid_botones.attach_next_to(
            radio_wrapword, radio_wrapchar, Gtk.PositionType.RIGHT, 1, 1
        )

        # pack
        self.box_outer.pack_start(toolbar, False, False, 0)
        self.box_outer.pack_start(self.box_text_editor, True, True, 0)
        self.box_outer.pack_start(grid_botones, False, False, 0)

win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
