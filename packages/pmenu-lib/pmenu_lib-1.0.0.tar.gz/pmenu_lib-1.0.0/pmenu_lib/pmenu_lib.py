"""
@file     pmenu_lib.py
@brief    Sleek dmenu alternative written in Python and powered by curses.
@date     26/07/2023
@author   Julio Cabria
"""


import curses
from contextlib import suppress


def pmenu(lines):
    """
    Display a menu with the given lines and return the selected option.

    Args:
        lines: The lines to display in the menu.

    Returns:
        The selected option or None if the user quits the menu.
    """
    try:
        return curses.wrapper(_display_menu, lines)
    except KeyboardInterrupt:
        return None


def _display_menu(stdscr, lines):
    """
    Display a menu with the given lines and return the selected option.

    Args:
        stdscr: The curses screen.
        lines: The lines to display in the menu.

    Returns:
        The selected option or None if the user quits the menu.
    """
    current_row = 0
    curses.curs_set(0)
    curses.use_default_colors()

    while True:
        stdscr.clear()

        max_rows, _ = stdscr.getmaxyx()
        max_display_rows = min(max_rows, len(lines))

        start_row = max(0, current_row - max_rows + 1)
        end_row = start_row + max_display_rows

        # Populate the screen with the lines
        for i, line in enumerate(lines[start_row:end_row], start=start_row):
            with suppress(curses.error):
                if i == current_row:
                    stdscr.addstr(i - start_row, 0, line, curses.A_REVERSE)
                    continue
                stdscr.addstr(i - start_row, 0, line)

        stdscr.refresh()

        # Read a key from the keyboard
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if current_row > 0:
                current_row -= 1
            elif start_row > 0:
                start_row -= 1
        elif key == curses.KEY_DOWN:
            if current_row < len(lines) - 1:
                current_row += 1
            elif end_row < len(lines):
                start_row += 1
        elif key == ord('q'):
            return None
        elif key == ord('\n'):
            return lines[current_row]
