# power_terminal

## Things Python should have out of the box.

This package was created when I realised that github copilot was writing most of the code for a terminal controller I was writing by itself. I realised that developers were writing this things by hand.

## Usage

![Usage](https://i.imgur.com/m6UenjP.png)

## Reference

### terminal.introduction(name, version, author)

A short introduction for whatever program you're making.

_name_: The name of the program. <br>

_version_: The version of the program. <br>

_author_: The author of the program, though, when left empty, will use the name of the creator of the package.

### terminal.clear()

Clears the terminal, it's the equivalent of 'cls' on Windows' PowerShell or 'clear' in Bash.

![terminal.clear() example](https://i.imgur.com/bAfEO68.png)

### terminal.statement(string)

Prints a string in green letters.

### terminal.debug(string)

Prints a string in bright yellow, preceded by the "DEBUG: " prefix.

### terminal.error(string)

Prints a string in bright red, preceded by the "ERROR: " prefix.

### terminal.restart()

Restart's the program. It may be quite useful to avoid the use of **while** loops in CLI programs.

### terminal.progress(done, total, length, string, fill, empty)

Prints a progress bar to the terminal.

_done_: The number (int) of actions that have been done up to this point. <br>

_total_: The total number of actions to be done during the execution of the progress bar. <br>

_length_: The width (in characters, assuming your terminal uses a monospace font) of the progress bar. It's not obligatory. <br>

_string_: A string to be displayed right below the bar. It's not obligatory. <br>

_fill_: The character the will fill up the progress bar. By default, it's the "█" character.<br>

_empty_: The character that will represent the "empty space" yet to be filled in the progress bar. By default, it's an empty string with a space. (" ")

### terminal.countdown(string, millisecons)

Counts down in milliseconds.

### terminal.confirm(string, error_string)

Asks the user to confirm or deny an action (Y/n).

## Credits

Created by Matheus Goulart.
