#!/usr/bin/env python2.7


class Player(object):
    def factory(type):
        if type == "Goalkeeper":
            return Goalkeeper()
        if type == "Defender":
            return Defender()
        # assert 0, "Unknown player creation: " + type
        raise AssertionError("Unknown player creation: " + type)

    creator = staticmethod(factory)


class Goalkeeper(Player):
    def play(self): print("Goalkeeper is playing.")


class Defender(Player):
    def play(self): print("Defender is playing.")


def start_play():
    players = ["Defender", "Goalkeeper", "Defender", "Forward"]
    for p in players:
        try:
            Player.creator(p).play()
        except Exception, e:
            print e


if __name__ == "__main__":
    start_play()
