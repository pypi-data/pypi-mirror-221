# PygameLab

PygameLab is a versatile Python library for game development using Pygame.


## Features

- Simplified game development with Pygame
- Easy sprite handling and manipulation
- Efficient event handling and input management
- Flexible text rendering with alignment options
- Image loading, display, and manipulation
- Polygon drawing and shape rendering
- Timer and time-related utilities
- Random number generation and utilities
- JSON and text file handling
- Unicode character retrieval
- Console logging and debugging utilities


## Installation

You can install PygameLab using pip:

`pip install PyGameLab`


## Usage

Here's a simple example of how to use PygameLab to create a game window:

```python
from PyGameLab.common import Window

# Create a game window
window = Window((800, 600), "My Game")

# Main game loop
while window.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False

    window.update()

pygame.quit()
```

For more information, documentation, and examples, visit the [PyGameLab website](https://pygamelab.feippe.com).


## License
This project is licensed under the MIT License - see the [LICENCE](LICENSE) file for details.

