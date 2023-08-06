import pygame

class ImageInterface:
    def __init__(self, screen):
        self.screen = screen
        self.image = None
        self.original_image = None
        self.image_rect = None
        self.is_dragging = False
        self.drag_offset = (0, 0)
        self.error_message = None
        self.font = pygame.font.Font(None, 24)
        self.zoom_level = 1

    def load_image(self, image_path):
        try:
            self.original_image = pygame.image.load(image_path)
            self.image = self.original_image.copy()
            self.image_rect = self.image.get_rect()
            self.error_message = None
        except FileNotFoundError as e:
            self.image = None
            self.original_image = None
            self.image_rect = None
            self.error_message = "Error loading image: No file found"

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.image_rect and self.image_rect.collidepoint(event.pos):
                self.is_dragging = True
                self.drag_offset = (event.pos[0] - self.image_rect.x, event.pos[1] - self.image_rect.y)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            if self.image_rect:
                self.image_rect.x = event.pos[0] - self.drag_offset[0]
                self.image_rect.y = event.pos[1] - self.drag_offset[1]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            self.zoom_level *= 1.1
            self.update_image()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            self.zoom_level /= 1.1
            self.update_image()

    def update_image(self):
        width = int(self.image.get_width() * self.zoom_level)
        height = int(self.image.get_height() * self.zoom_level)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image_rect.size = self.image.get_size()

    def draw(self):
        if self.image:
            self.screen.blit(self.image, self.image_rect)
        elif self.error_message:
            text_surface = self.font.render(self.error_message, True, (255, 0, 0))
            text_rect = text_surface.get_rect()  
            text_rect.topleft = (0, self.screen.get_height() // 2)
            self.screen.blit(text_surface, text_rect)
