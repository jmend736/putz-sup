import json

with open("vote/putzen.json") as f:
    putzen = json.load(f)["putzen"]
    putzen_kerbs = set([i for i in putzen.values()])


class Putzen(object):
    def __init__(self, input):
        self.name = input

    def __unicode__(self):
        return self._name

    def __repr__(self):
        pre = "Kerberos: "
        post = ""
        return pre + self._name + post

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, (str, unicode)):
            t = type(name)
            raise TypeError("Input name must be string, not " + str(t))
        elif str(name) in putzen_kerbs:
            self._name = name
        else:
            try:
                self._name = putzen[str(name)]
            except KeyError:
                raise KeyError("Not a putzen?")

    @name.deleter
    def name(self):
        raise Exception("Can't delete putzen!")
