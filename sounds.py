import pygame as pg

class Sound:
    def __init__(self):
        pg.mixer.init()
        self.sugar_drop_sound = pg.mixer.Sound("./Sounds/sugardrop.mp3")
        self.explosion_sound = pg.mixer.Sound("./Sounds/bucketexplosion.mp3")
        self.level_complete_sound = pg.mixer.Sound("./Sounds/levelcomplete.mp3")
        
        # Initialize channels
        self.sugar_drop_channel = pg.mixer.Channel(0)
        self.explosion_channel = pg.mixer.Channel(1)
        self.level_complete = pg.mixer.Channel(2)  # For other sounds

    def volume(self, volume):
        """Set the volume for all sounds."""
        self.volume = volume
        pg.mixer.music.set_volume(self.volume)
        self.sugar_drop_sound.set_volume(self.volume)
        self.explosion_sound.set_volume(self.volume)
        # Set volume for other sounds here

    def play_sugardrop(self):
    #     if not self.sugar_drop_channel.get_busy():
        self.sugar_drop_channel.play(self.sugar_drop_sound)

    def play_explosion(self):
    #     if not self.explosion_channel.get_busy():
        self.explosion_channel.play(self.explosion_sound)

    def play_sound_level(self):
    #     if not self.level_complete.get_busy():
        self.level_complete.play(self.level_complete_sound)
    
    def adjust_volume(self, delta):
        """Adjust volume by delta amount."""
        new_volume = max(0.0, min(1.0, self.volume + delta))
        self.volume(new_volume)