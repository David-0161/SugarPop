import pygame as pg

class Sound:
    def _init_(self):
        pg.mixer.init()
        self.sugar_drop_sound = pg.mixer.Sound("path/to/sugar_drop_sound.wav")
        self.explosion_sound = pg.mixer.Sound("path/to/explosion_sound.wav")
        # self.
        # Initialize volume
        self.volume = 1.0  # 1.0 is max volume, 0.0 is mute
        self.volume(self.volume)
        
        # Initialize channels
        self.sugar_drop_channel = pg.mixer.Channel(0)
        self.explosion_channel = pg.mixer.Channel(1)
        self.other_channel = pg.mixer.Channel(2)  # For other sounds

    def volume(self, volume):
        """Set the volume for all sounds."""
        self.volume = volume
        pg.mixer.music.set_volume(self.volume)
        self.sugar_drop_sound.set_volume(self.volume)
        self.explosion_sound.set_volume(self.volume)
        # Set volume for other sounds here

    def play_sugardrop(self):
        if not self.sugar_drop_channel.get_busy():
            self.sugar_drop_channel.play(self.sugar_drop_sound)

    def play_explosion(self):
        if not self.explosion_channel.get_busy():
            self.explosion_channel.play(self.explosion_sound)

    def play_sound_level(self, sound):
        if not self.other_channel.get_busy():
            self.other_channel.play(sound)

    def adjust_volume(self, delta):
        """Adjust volume by delta amount."""
        new_volume = max(0.0, min(1.0, self.volume + delta))
        self.volume(new_volume)