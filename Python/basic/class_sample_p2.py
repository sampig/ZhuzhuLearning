#!/usr/bin/env python2.7


class Player(object):
    __name = None
    position = None
    numbers = []

    def __init__(self, name=None):
        if name is not None:
            self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def play(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def passes(self):
        print self.position, self.__name, "is passing."


class Goalkeeper(Player):
    def __init__(self, name=None):
        self.position = "Goalkeeper"
        self.hand = self.Hand(self)
        if name is not None:
            super(Goalkeeper, self).__init__(name)

    def play(self):
        print self.position, self.getName(), "is playing."

    def save(self):
        print self.position, self.getName(), "saved."

    def __superman(self):
        print "This is a bug."

    class Hand:
        def __init__(self, outer):
            self.outer = outer

        def keep_ball(self):
            print self.outer.getName(), "keeps the ball."


class Defender(Player):
    def __init__(self, name=None):
        self.position = "Defender"
        if name is not None:
            super(Defender, self).__init__(name)

    def play(self):
        print self.position, self.getName(), "is playing."


def start_play():
    g = Goalkeeper("Buffon")
    g.numbers.append(1)
    d = Defender()
    d.setName("Chiellini")
    d.numbers.append(3)
    g.play()
    g.save()
    g.hand.keep_ball()
    g.passes()
    try:
        g.__superman()
    except:
        print "Error invoking method."
    g._Goalkeeper__superman()
    d.play()
    d.passes()
    print "g Numbers:", g.numbers
    print "d NUmbers:", d.numbers
    g.numbers = []
    d.numbers.append(3)
    print "g Numbers:", g.numbers
    print "d NUmbers:", d.numbers
    g.numbers.append(10)
    print "g Numbers:", g.numbers
    print "d NUmbers:", d.numbers

    # Inheritance
    print "g is Player?", isinstance(g, Player)
    print "g is Goalkeeper?", isinstance(g, Goalkeeper)
    print "g is Defender?", isinstance(g, Defender)
    print "Goalkeeper is Player?", issubclass(Goalkeeper, Player)
    print "Defender is Player?", issubclass(Defender, Player)
    print "Goalkeeper is Defender?", issubclass(Goalkeeper, Defender)
    print "Defender is Goalkeeper?", issubclass(Defender, Goalkeeper)


if __name__ == "__main__":
    start_play()
