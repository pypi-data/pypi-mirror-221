import pygame
from .textbox import TextBox

class Slider:
    def __init__(self, screen, x, y, window_size, width=200, height=20, border_color=(0, 0, 0), textbox_height=40, textbox_width=40, align=None, button=None, callback=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.window_size = window_size
        self.width = width
        self.height = height
        self.border_color = border_color
        self.align = align
        self.slider_rect = pygame.Rect(self.x, self.y + self.height // 2 - 2, self.width, 4)
        self.circle_radius = self.height // 2
        self.circle_x = self.x
        self.circle_y = self.y + self.height // 2
        self.circle_color = border_color
        self.value = 0  # Slider value between 0 and 100
        self.max_value = 100  # Default max value
        self.min_value = 0  # Default min value
        self.dragging = False  # Is the slider being dragged?
        self.button = button  # Reference to the attached button
        self.callback = callback  # Callback function to be called on slider release
        self.textbox_height = textbox_height
        self.textbox_width = textbox_width

        # If the slider is attached to a button, update the position to be above the button
        if self.button:
            self.update_position_according_to_button()

        # Create TextBox after potential button position update
        self.create_textbox()

    def create_textbox(self):
        textbox_x = self.x + (self.width - self.textbox_width) // 2  # Adjust for width of TextBox for center alignment
        textbox_y = self.y - self.textbox_height - 10  # Position the TextBox slightly above the Slider
        self.textbox = TextBox(self.screen, textbox_x, textbox_y, self.window_size, width=self.textbox_width, height=self.textbox_height, border_color=self.border_color, border_size=1, font_size=15)
        print(f"[Debug] Slider TextBox: Created at x: {textbox_x}, y: {textbox_y}.")  # Debugging print statement

    def update_position_according_to_button(self):
        if self.button:
            self.x = self.button.rect.centerx - self.width // 2
            self.y = self.button.rect.y - self.height - 10  # Position it 10 units above the button
            self.update_positions()
            print(f"[Debug] Slider: Repositioned to x: {self.x}, y: {self.y}.")  # Debugging print statement

            # Re-create the TextBox with the updated position
            self.create_textbox()

    def update_positions(self):
        # Update the shapes associated with the slider
        self.slider_rect = pygame.Rect(self.x, self.y + self.height // 2 - 2, self.width, 4)
        self.circle_x = self.x
        self.circle_y = self.y + self.height // 2
        self.update_textbox_position()
        print(f"[Debug] Slider: Positions updated - circle_x: {self.circle_x}, circle_y: {self.circle_y}.")  # Debugging print statement

    def update_textbox_position(self):
        # Update the position
        self.textbox.x = self.x + (self.width - self.textbox_width) // 2  # Adjust for width of TextBox for center alignment
        self.textbox.y = self.y - self.textbox_height - 10  # Position the TextBox slightly above the Slider
        print(f"[Debug] Slider TextBox: Intended reposition to x: {self.textbox.x}, y: {self.textbox.y}.")  # Debugging print statement

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.slider_rect.collidepoint(event.pos) or ((self.circle_x - self.circle_radius <= event.pos[0] <= self.circle_x + self.circle_radius) and (self.circle_y - self.circle_radius <= event.pos[1] <= self.circle_y + self.circle_radius)):
                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging:
                self.dragging = False
                if self.callback is not None:
                    self.callback(self.value)  # Call the callback function with the slider value as an argument

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            if self.x <= event.pos[0] <= self.x + self.width:  # Check if the mouse motion is within slider's width
                self.circle_x = event.pos[0]

        # Handle events for the textbox
        self.textbox.handle_events(event)

        # Update the Slider value if the TextBox text is changed
        if self.textbox.is_active and self.textbox_previous_text != self.textbox.text:
            self.update_from_textbox()

        # Update the previous TextBox text for the next event handling
        self.textbox_previous_text = self.textbox.text

        # Check for backspace key press in the textbox
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            if self.textbox.text == "":
                print("[Debug] Backspace pressed, setting slider value to 0.")  # Debugging print statement
                self.textbox.text = "0"
                self.update_from_textbox()

        self.update()

    def draw(self):
        pygame.draw.ellipse(self.screen, self.border_color, self.slider_rect, 1)
        pygame.draw.circle(self.screen, self.circle_color, (self.circle_x, self.circle_y), self.circle_radius)
        self.textbox.draw()

    def update(self):
        self.value = ((self.circle_x - self.x) / self.width) * (self.max_value - self.min_value)
        self.textbox.text = str(round(self.value))

    def update_from_textbox(self):
        try:
            # If textbox text is empty, set the value to 0
            if not self.textbox.text:
                print("[Debug] Textbox is empty, setting slider value to 0.")  # Debugging print statement
                self.value = 0
                self.circle_x = self.x
            else:
                value = float(self.textbox.text)
                if self.min_value <= value <= self.max_value:
                    self.value = value
                    self.circle_x = ((self.value / (self.max_value - self.min_value)) * self.width) + self.x
        except ValueError:
            print("[Debug] ValueError occurred in update_from_textbox")  # Debugging print statement
            pass
