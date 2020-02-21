from random import randint


class Dna(str):
    def __init__(self, sequence):
        self.seq = sequence
        self.gc = 0
        self.length = len(self.seq)
        self.i = 0
        self.number = randint(1, 100000)
        self.complement_copy = ''
        self.transcribed_copy = ''
        super(str, self).__init__()

    def gc_content(self):
        g = self.seq.count('G')
        c = self.seq.count('C')
        self.gc = (g + c)/len(self.seq)

    def reverse_complement(self):
        for el in self.seq:
            if el == 'A':
                self.complement_copy += 'T'
            if el == 'T':
                self.complement_copy += 'A'
            if el == 'G':
                self.complement_copy += 'C'
            if el == 'C':
                self.complement_copy += 'G'
        self.complement_copy = self.complement_copy[::-1]  # Записываем в направлении 5' - 3'

    def transcribe(self):
        for el in self.seq:
            if el == 'A':
                self.transcribed_copy += 'U'
            if el == 'T':
                self.transcribed_copy += 'A'
            if el == 'G':
                self.transcribed_copy += 'C'
            if el == 'C':
                self.transcribed_copy += 'G'
        self.transcribed_copy = self.transcribed_copy[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.length:
            self.i += 1
            return self.seq[self.i - 1]
        else:
            raise StopIteration

    def __eq__(self, other):
        return isinstance(other, Dna) and self.seq is other.seq

    def __hash__(self):
        return self.number

    def __str__(self):
        return self.seq

    def __repr__(self):
        return self.seq


class Rna(str):
    def __init__(self, sequence):
        self.seq = sequence
        self.gc = 0
        self.length = len(self.seq)
        self.i = 0
        self.number = randint(1, 100000)
        self.reverse_copy = ''
        super(str, self).__init__()

    def gc_content(self):
        g = self.seq.count('G')
        c = self.seq.count('C')
        self.gc = (g + c)/len(self.seq)

    def reverse_complement(self):
        for el in self.seq:
            if el == 'A':
                self.reverse_copy += 'U'
            if el == 'U':
                self.reverse_copy += 'A'
            if el == 'G':
                self.reverse_copy += 'C'
            if el == 'C':
                self.reverse_copy += 'G'
        self.reverse_copy = self.reverse_copy[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.length:
            self.i += 1
            return self.seq[self.i - 1]
        else:
            raise StopIteration

    def __eq__(self, other):
        return isinstance(other, Rna) and self.seq is other.seq

    def __hash__(self):
        return self.number

    def __str__(self):
        return self.seq

    def __repr__(self):
        return self.seq


x = Dna('AAGTTCGG')
x.gc_content()
print(x.gc)
x.reverse_complement()
print(x.complement_copy)
x.transcribe()
print(x.transcribed_copy)

for element in x:
    print(element)

y = Dna('AAGTTCGG')
is_eq = (x == y)
print(is_eq)

some_set = set()
some_set.add(x)
print(some_set)
