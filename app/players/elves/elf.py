from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):

    def __init__(self, musical_instrument, nickname):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing"
              f" a song on the {self._musical_instrument}")