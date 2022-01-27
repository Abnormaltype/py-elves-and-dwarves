from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, musical_instrument, nickname):
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname}" \
               f" has bow of the {self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level