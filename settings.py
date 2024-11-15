class Settings():
    """A class to store all the settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        #controls how quickly the fleet drops down the screen each time an alien reaches either edge
        self.fleet_drop_speed = 15
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.alien_points = 50
        #how quickly the alien point values increase
        self.score_scale = 1.5
        #initializing the values for attributes that need to change throughout the course of a game
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 represents right; -1 for left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        

'''
The settings file contains the settings class. This class only has an initializer method which initializes attributes controlling the game's appearance and the ship's speed
'''