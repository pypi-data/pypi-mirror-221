import pygame

class Button:
    def __init__(self, screen, x, y, window_size, width=50, height=30, background_color=(65, 105, 225), border_color=(0, 0, 0),
                 shadow_intensity=0.5, text="", font=None, font_color=(255, 255, 255), align="right", slider=None, callback=None, right_click_popup=None):

        self.screen = screen
        self.window_size = window_size
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background_color = background_color
        self.pressed_color = [int(bc * 0.8) for bc in background_color]  # The pressed color is 20% darker than the background color
        self.border_color = border_color
        self.shadow_intensity = shadow_intensity
        self.text = text
        self.font = font or pygame.font.Font(None, 24)
        self.font_color = font_color
        self.align = align
        self.callback = callback
        self.is_pressed = False
        self.flash_timer = 0  # Timer for flash effect (measured in milliseconds)
        self.flash_duration = 200  # Duration of the flash effect (200ms)


        # Slider initialization
        self.slider = slider
        if self.slider is not None:
            self.slider.button = self  # Inform the slider about the button it's attached to
            print("[Debug] Button: Slider attached.")  # Debugging print statement
        else:
            print("[Debug] Button: No slider attached.")  # Debugging print statement

        # Right-click popup initialization
        self.right_click_popup = right_click_popup

        # Calculate the minimum required width based on the length of the text
        text_width = self.font.size(self.text)[0] + 20  # Add some padding to the text width
        if self.rect.width is None or self.rect.width < text_width:
            self.rect.width = text_width

        # Adjust the x position based on the align attribute
        if align == "right":
            self.rect.x = window_size[0] - width - x
        elif align == "center":
            self.rect.x = (window_size[0] - width) // 2
        elif align == "left":
            self.rect.x = x

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):

                    # Set the button as pressed and start the flash timer
                    self.is_pressed = True
                    self.flash_timer = pygame.time.get_ticks()

                    if self.slider is not None:
                        slider_value = self.slider.value
                        self.call_desired_function(slider_value)
                    else:
                        self.call_desired_function()

            elif event.button == 3:  # Right-click event
                if self.right_click_popup is not None and self.rect.collidepoint(event.pos):
                    self.right_click_popup.show_popup(*event.pos)


    def draw(self):

        # Update the flash effect
        current_time = pygame.time.get_ticks()
        if self.is_pressed and current_time - self.flash_timer <= self.flash_duration:
            current_color = self.pressed_color
        else:
            self.is_pressed = False  # Reset the pressed state after the flash effect is over
            current_color = self.background_color

        # Draw the button background
        current_color = self.pressed_color if self.is_pressed else self.background_color
        pygame.draw.rect(self.screen, current_color, self.rect)

        # Draw the button border
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)

        # Draw the button text
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_on_surface(self, surface):
        # Draw the button background
        current_color = self.pressed_color if self.is_pressed else self.background_color
        pygame.draw.rect(surface, current_color, self.rect)

        # Draw the button border
        pygame.draw.rect(surface, self.border_color, self.rect, 2)

        # Draw the button text
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def call_desired_function(self, slider_value=None):
        # This is a placeholder for the actual function you want to call when the button is pressed
        # The function should be able to handle situations when no slider_value is provided
        pass

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)