# pmenu
*Sleek dmenu alternative written in Python and powered by curses.*
<br>

## Usage
The ```pmenu(options)``` function will return the selected option as a ```str```, or ```None``` if the menu is closed without selecting an option.
```python
from pmenu_lib import pmenu

selected_option = pmenu(["Option1", "Option2", "Option3"])
```

```
> Option1
Option2
Option3

(Enter)
```

```python
print(selected_option)
>> "Option1"
```

```
> Option1
Option2
Option3

(Esc)
```

```python
print(selected_option)
>> None
```
<br>

## Menu bindings

- **Up arrow**: Highlight the previous menu entry.
- **Down arrow**: Highlight the next menu entry.
- **Enter**: Select the highlighted entry.
- **Esc**: Close the menu.
