import pygame
import pygame.locals as pl
import pygame.cursors


# Constants
CURSOR_BLINK_TIME = 500  # Cursor visibility time in milliseconds (0.5 seconds)
BACKSPACE_HOLD_TIME = 150  # Time (in milliseconds) to allow holding backspace for continuous deletion
TRUNCATE_MARKER = "..."  # Ellipsis to indicate text truncation
CURSOR_COLOR = (200, 200, 200)  # Color of the cursor

class TextBox:
    def __init__(self, screen, x, y, window_size, width=200, height=30, border_color=(0, 0, 0), text="Enter a msg", font=None, align=None, button=None, font_size=24, border_size=2):
        self.screen = screen
        self.x = x
        self.rect = pygame.Rect(x, y, width, height)
        self.border_color = border_color
        self.text = text
        self.font = font or pygame.font.Font(None, font_size)
        self.is_active = False
        self.align = align
        self.cursor_visible = False
        self.cursor_timer = 0
        self.button = button  # The attached button (if any)
        self.border_size = border_size

        # Adjust the x position based on the align attribute
        if align == "right":
            self.rect.x = window_size[0] - width - x
        elif align == "center":
            self.rect.x = (window_size[0] - width) // 2
        elif align == "left":
            self.rect.x = x

        self.backspace_timer = 0
        self.backspace_held = False

        # If a button is provided, attach it to the TextBox
        if self.button is not None:
            self.attach_button(self.button)

    def attach_button(self, button):
        self.button = button
        button_height = self.rect.height - 4  # Adjust button height to fit within the TextBox
        button.rect.height = button_height
        button.rect.y = self.rect.y + 2  # Vertically center the button inside the TextBox

        # Attach the button to the right side of the TextBox
        button.rect.x = self.rect.right - button.rect.width

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.is_active = self.rect.collidepoint(event.pos)
            if self.is_active:
                self.cursor_timer = 0
        elif event.type == pygame.locals.DROPFILE:
            if self.rect.collidepoint(pygame.mouse.get_pos()):  # check if file was dropped on TextBox
                self.text = event.file  # get the file path
                self.is_active = False

    def handle_key_event(self, event):
        if self.is_active and event.type == pygame.KEYDOWN:
            if self.text == "Enter a msg":
                self.text = ""

            if event.key == pygame.K_RETURN:
                self.is_active = False
                if self.button is not None:
                    new_event = pygame.event.Event(
                        pygame.MOUSEBUTTONDOWN, 
                        {'pos': self.button.rect.center, 'button': 1}
                    )
                    pygame.event.post(new_event)
            elif event.key == pygame.K_BACKSPACE:
                self.backspace_timer = 0
                if self.backspace_held:
                    if pygame.time.get_ticks() - self.backspace_timer > BACKSPACE_HOLD_TIME:
                        self.text = self.text[:-1]
                        self.backspace_timer = pygame.time.get_ticks()
                else:
                    self.text = self.text[:-1]

                self.backspace_held = True
                self.backspace_timer = pygame.time.get_ticks()

            else:
                text_surface = self.font.render(self.text + event.unicode, True, self.border_color)
                if text_surface.get_rect().width <= self.rect.width - 20:
                    self.text += event.unicode

        elif event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            self.backspace_held = False

        # Track when backspace key is released
        elif event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            self.backspace_held = False

    def update(self, dt):
        # Handle backspace timer to allow holding backspace to delete characters
        if self.backspace_held and pygame.time.get_ticks() - self.backspace_timer > BACKSPACE_HOLD_TIME:
            self.text = self.text[:-1]
            self.backspace_timer = pygame.time.get_ticks()

        # Set the cursor visibility to True when the TextBox is active
        self.cursor_visible = self.is_active

        # Toggle the cursor visibility based on the CURSOR_BLINK_TIME constant
        self.cursor_timer += dt
        if self.cursor_timer >= CURSOR_BLINK_TIME:
            self.cursor_visible = not self.cursor_visible

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  # Set the mouse cursor to the IBeam cursor
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Change it back to the default cursor when not over the textbox


        # Calculate the minimum required width for the TextBox based on the length of the text
        text_surface = self.font.render(self.text, True, self.border_color)
        min_width = text_surface.get_rect().width + 20

        # Set the TextBox width to the minimum required width
        self.rect.width = max(min_width, self.rect.width)


    def draw(self):
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_size)

        # Calculate the available width for the text within the TextBox, considering the button
        available_width = self.rect.width - 20
        if self.button is not None:
            available_width -= (self.rect.right - self.button.rect.left)

        # Create a temporary string for the visible text
        visible_text = self.text
        text_surface = self.font.render(visible_text, True, self.border_color)

        # Truncate the visible text with ellipsis (...) at the beginning if it overflows into the button area
        if text_surface.get_rect().width > available_width:
            ellipsis_width = self.font.render(TRUNCATE_MARKER, True, self.border_color).get_rect().width
            while text_surface.get_rect().width > available_width - ellipsis_width and len(visible_text) > 1:
                visible_text = visible_text[1:]
                text_surface = self.font.render(TRUNCATE_MARKER + visible_text, True, self.border_color)

        text_rect = text_surface.get_rect(left=self.rect.x + 10, centery=self.rect.centery)
        self.screen.blit(text_surface, text_rect)

        # Draw the cursor if the TextBox is active and the cursor is visible
        if self.is_active and self.cursor_visible:
            cursor_pos = text_rect.right + 2
            cursor_top = text_rect.top + 2
            cursor_bottom = text_rect.bottom - 2
            cursor_width = 2

            # Calculate the alpha value for the cursor based on the cursor timer
            alpha = int(abs((pygame.time.get_ticks() % (2 * CURSOR_BLINK_TIME)) - CURSOR_BLINK_TIME) / CURSOR_BLINK_TIME * 255)

            # Create a cursor surface with a transparent rectangle
            cursor_surface = pygame.Surface((cursor_width, cursor_bottom - cursor_top), pygame.SRCALPHA)  # Use SRCALPHA flag for transparency
            cursor_surface.fill((CURSOR_COLOR[0], CURSOR_COLOR[1], CURSOR_COLOR[2], alpha))

            # Draw the cursor surface onto the screen at the appropriate position
            self.screen.blit(cursor_surface, (cursor_pos, cursor_top))
