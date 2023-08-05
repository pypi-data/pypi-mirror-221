import pygame
import sys
import pygame.locals


class console:
    @staticmethod
    def log(*values, sep=" "):
        print("\033[0m", *values, "\033[0m", sep=sep, file=sys.stdout)

    @staticmethod
    def warn(*values, sep=" "):
        print("\033[33m", *values, "\033[0m", sep=sep, file=sys.stdout)

    @staticmethod
    def error(*values, sep=" "):
        print("\033[31m", *values, "\033[0m", sep=sep, file=sys.stdout)


class Sprite:
    def __init__(self, position=(0, 0), image=None, size=(0, 0), custom_locals={}, alignment=("_lt/", "_tp/"), show=True, screen=None):
        self.var = custom_locals
        self.position = (position[0], position[1])
        self.size = size
        self.image = image
        self.alignment = alignment
        self.show = show
        self.screen = screen

    def instance(self, screen):
        self.screen = screen
        if self.image is not None:
            sprite_width, sprite_height = self.size
            x, y = self.position
            align_horizontal, align_vertical = self.alignment

            if align_horizontal == "_lt/":
                x += 0
            elif align_horizontal == "_ct/":
                x -= sprite_width / 2
            elif align_horizontal == "_rg/":
                x -= sprite_width

            if align_vertical == "_tp/":
                y += 0
            elif align_vertical == "_md/":
                y -= sprite_height / 2
            elif align_vertical == "_bt/":
                y -= sprite_height

            adjusted_position = (x, y)

            screen.screen.blit(pygame.image.load(
                self.image), adjusted_position)

    def update(self, screen):
        self.instance(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.running = False

    def is_clicked(self, button):
        mouse_pos = self.screen.get_mouse_position()
        if self.image is not None:
            x, y = self.position
            width, height = self.size
            align_horizontal, align_vertical = self.alignment

            if align_horizontal == "_lt/":
                x += 0
            elif align_horizontal == "_ct/":
                x -= width / 2
            elif align_horizontal == "_rg/":
                x -= width

            if align_vertical == "_tp/":
                y += 0
            elif align_vertical == "_md/":
                y -= height / 2
            elif align_vertical == "_bt/":
                y -= height

            if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height and self.screen.is_mouse_clicked(button):
                return True

        return False

    def is_hovered(self):
        mouse_pos = self.screen.get_mouse_position()
        if self.image is not None:
            x, y = self.position
            width, height = self.size
            align_horizontal, align_vertical = self.alignment

            if align_horizontal == "_lt/":
                x += 0
            elif align_horizontal == "_ct/":
                x -= width / 2
            elif align_horizontal == "_rg/":
                x -= width

            if align_vertical == "_tp/":
                y += 0
            elif align_vertical == "_md/":
                y -= height / 2
            elif align_vertical == "_bt/":
                y -= height
            if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                return True

        return False


class Window:

    def __init__(self, size=(100, 100), caption="unnamed", color=(255, 255, 255)):
        self.width = size[0]
        self.height = size[1]
        self.caption = caption
        self.backgroundColor = color
        self.running = True
        self.screen = pygame.display.set_mode((self.width, self.height))
        self._lastbutton = self.mouse_state()["button"]
        self.update()

    def mouse_state(self):
        button = None
        position = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:
            button = "_lt/"
        elif pygame.mouse.get_pressed()[1] == 1:
            button = "_md/"
        elif pygame.mouse.get_pressed()[2] == 1:
            button = "_rg/"
        else:
            button = None

        clicked = pygame.mouse.get_pressed() == 1

        return {"position": position, "button": button, "clicked": clicked, "last_button": self._lastbutton}

    def update(self):
        self._lastbutton = self.mouse_state()["button"]
        if not self.running:
            pygame.quit()
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.backgroundColor)


class Time:
    @staticmethod
    def wait(ms=0, objetive=None):
        if objetive is None:
            objetiveTime = Time.get() + int(ms)
        else:
            objetiveTime = objetive

        if not Time.get() >= objetiveTime:
            pygame.time.wait(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            Time.wait(objetive=objetiveTime)

    @staticmethod
    def get():
        return pygame.time.get_ticks() / 1000.0

    class timer:

        clock = pygame.time.Clock()
        start_time = None
        elapsed_time = 0
        running = False

        @staticmethod
        def start():
            if not Time.timer.running:
                Time.timer.start_time = Time.get()
                Time.timer.running = True

        @staticmethod
        def get():
            if Time.timer.running:
                return Time.get() - Time.timer.start_time + Time.timer.elapsed_time
            else:
                return Time.timer.elapsed_time

        @staticmethod
        def stop():
            if Time.timer.running:
                Time.timer.elapsed_time += Time.get() - Time.timer.start_time
                Time.timer.running = False

        @staticmethod
        def end():
            Time.timer.stop()
            Time.timer.elapsed_time = 0


class Text:
    @staticmethod
    def display(screen=None, text="", position=(0, 0), color=(0, 0, 0), font=None, size=50, alignment=("_lt/", "_tp/")):
        if screen is None:
            raise ValueError(
                "No se ha especificado la pantalla para mostrar el texto.")

        font = pygame.font.Font(font, size)

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()

        if alignment[0] == "_ct/":
            text_rect.centerx = position[0]
        elif alignment[0] == "_rg/":
            text_rect.right = position[0]
        elif alignment[0] == "_lt/":
            text_rect.left = position[0]

        if alignment[1] == "_md/":
            text_rect.centery = position[1]
        elif alignment[1] == "_bt/":
            text_rect.bottom = position[1]
        elif alignment[1] == "_tp/":
            text_rect.top = position[1]

        screen.screen.blit(text_surface, text_rect)

        return text_rect

    @staticmethod
    def delete(screen, text_rect):
        if text_rect is not None:
            pygame.draw.rect(screen.screen, (0, 0, 0), text_rect)
            pygame.display.update(text_rect)


class Image:
    @staticmethod
    def displayImage(screen, image, position, size, opacity=255, brightness=255):
        if isinstance(image, str):
            image_surface = pygame.image.load(image).convert_alpha()
        elif isinstance(image, pygame.Surface):
            image_surface = image
        else:
            raise ValueError(
                "El argumento 'image' debe ser una cadena de ruta de archivo o un objeto pygame.Surface.")

        if size != image_surface.get_size():
            image_surface = pygame.transform.scale(image_surface, size)

        if opacity < 255:
            image_surface.set_alpha(opacity)

        if brightness < 255:
            image_surface = pygame.Surface.convert(image_surface)
            image_surface.fill(
                (brightness, brightness, brightness), None, pygame.BLEND_RGB_MULT)

        screen.screen.blit(image_surface, position)

    @staticmethod
    def newImage(bitMap, size=(16, 16)):
        image_surface = pygame.Surface(size, pygame.SRCALPHA)

        for y in range(size[1]):
            for x in range(size[0]):
                pixel_color = bitMap[y * size[0] + x]
                image_surface.set_at((x, y), pixel_color)

        return image_surface

    @staticmethod
    def createBitMap(color, size):
        bitmap = []
        count = 0
        w, h = size
        for i in range(w):
            for j in range(h):
                bitmap.append(color)
        return bitmap
