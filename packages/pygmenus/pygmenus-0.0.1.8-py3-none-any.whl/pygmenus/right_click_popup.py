import pygame

class RightClickPopup:
    def __init__(self, screen, x, y, options, height, width, font=None, font_color=(0, 0, 0),
                 background_color=(200, 200, 200), border_color=(0, 0, 0), button=None, window_size=None):  # Pass window_size as a parameter
        self.screen = screen
        self.x = x
        self.y = y
        self.options = options
        self.height = height
        self.width = width
        self.font = font or pygame.font.Font(None, 24)
        self.font_color = font_color
        self.background_color = background_color
        self.border_color = border_color
        self.is_visible = False
        self.buttons = []  # Store the buttons for each option
        self.selected_option = None  # Initialize to None
        self.popup_rect = pygame.Rect(x, y, width, height * len(options))
        self.prev_mouse_inside_popup = False
        self.button_class = button  # Store the button class to create buttons later
        self.window_size = window_size

    def show_popup(self, x, y):
        self.x = x
        self.y = y
        self.is_visible = True
        self.popup_rect.topleft = (x, y)

        # Creating buttons with default styling
        if self.button_class:
            self.buttons.clear()
            for i, option in enumerate(self.options):
                button_obj = self.button_class(self.screen, 0, i * (self.height + 2), self.window_size, text=option, right_click_popup=self)
                print(f"Debug: Button created for option '{option}' at x: {button_obj.x}, y: {button_obj.y}") 
                self.buttons.append(button_obj)
                print(f"Debug: Button added to buttons list") 
                
        print(f"Debug: Number of buttons created: {len(self.buttons)}") 

        # Set the default selected_option only if it's not already set
        if self.selected_option is None and self.buttons:
            self.selected_option = self.buttons[0].text
            print(f"Debug: Default selected_option set to '{self.selected_option}'")

        
        # Set the default selected_option to button[0]
        if self.buttons:
            self.selected_option = self.buttons[0].text
            print(f"Debug: Default selected_option set to '{self.selected_option}'")





    def hide_popup(self):
        self.is_visible = False


    def is_mouse_inside_popup(self):
        return self.is_visible and self.popup_rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if self.is_visible:
            mouse_inside_popup = self.is_mouse_inside_popup()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos):
                            # If a button inside the popup is clicked, return True to indicate the event was handled
                            print("Button inside popup was clicked")
                            return True

                    if not mouse_inside_popup:
                        self.hide_popup()
                        return True

            elif event.type == pygame.MOUSEMOTION:
                if not mouse_inside_popup:
                    if self.prev_mouse_inside_popup:
                        self.hide_popup()

            self.prev_mouse_inside_popup = mouse_inside_popup

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.hide_popup()

        return False

    def draw(self):
        if not self.is_visible:
            return

        total_height = len(self.options) * (self.height + 2) + 2

        popup_surface = pygame.Surface((self.width, total_height))
        popup_surface.fill(self.background_color)

        pygame.draw.rect(popup_surface, self.border_color, popup_surface.get_rect(), 2)

        for i, button in enumerate(self.buttons):
            button_y = i * (self.height + 2)
            button.update_pos(0, button_y)  # Updating button's position
            button.draw_on_surface(popup_surface)

            # Draw a green checkmark next to the option set (button 0)
            if i == 0:
                checkmark_font = pygame.font.Font(None, 36)
                checkmark_text = checkmark_font.render("X", True, (0, 255, 0))
                popup_surface.blit(checkmark_text, (self.width - 30, button_y + 5))

        self.screen.blit(popup_surface, (self.x, self.y))




