# Lyric Viewer Code

from lyricsgenius import Genius
import dearpygui.dearpygui as dpg

genius = Genius("rYNuzhwwnCZK1PdTKeXZJs_sZrLa4y6HyPlcbGmaH5mdycgALoysNSMdHWNQ-xWV")


def find_song():  # Main function, searches genius api from user input.
    try:
        song_name = dpg.get_value("input_song")
        artist_name = dpg.get_value("input_artist")
        artist = genius.search_artist(artist_name, max_songs=1, sort="title")
        song = artist.song(song_name)
        lyrics = song.lyrics
        # Generates unique tag for every new tab.
        unique_id = dpg.generate_uuid()
        #  Creates new tab using previously generated info.
        dpg.add_tab(label=song_name, tag=unique_id, parent="Song Tab", closable=True)
        dpg.add_text(default_value=lyrics, parent=unique_id)

    except AttributeError:  # Catches error from lack of input.
        print("No input.")


dpg.create_context()
dpg.set_global_font_scale(1.25)

with dpg.window(tag="Primary Window"):  # Main window ui
    dpg.add_spacer(height=5)
    dpg.add_input_text(tag="input_song", hint="Enter Song Name")
    dpg.add_input_text(tag="input_artist", hint="Enter Artist")
    dpg.add_button(label="Search", tag="Call Function", callback=find_song)  # Calls main function.
    dpg.add_tab_bar(label="Songs", tag="Song Tab", reorderable=True)

# DearPyGUI
dpg.create_viewport(title="Lyric Viewer", width=600, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
