class RakObat:
    def _init_(self):
        self.size = 10  # Ukuran hash table
        self.map = [None] * self.size

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def tambahObat(self, jenisObat, namaObat):
        index = self.hash_function(jenisObat)
        if self.map[index] is None or self.map[index][0] == "deleted":
            self.map[index] = (jenisObat, namaObat)
            return True
        else:
            # Collision occurred, perform linear probing
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is None or self.map[next_index][0] == "deleted":
                    self.map[next_index] = (jenisObat, namaObat)
                    return True
                next_index = (next_index + 1) % self.size
            return False

    def lihatObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        if self.map[index] is not None and self.map[index][0] == jenisObat:
            return self.map[index][1]
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is not None and self.map[next_index][0] == jenisObat:
                    return self.map[next_index][1]
                next_index = (next_index + 1) % self.size
            return "None"

    def ambilObat(self, jenisObat):
        index = self.hash_function(jenisObat)
        if self.map[index] is not None and self.map[index][0] == jenisObat:
            self.map[index] = ("deleted", None)
            return True
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.map[next_index] is not None and self.map[next_index][0] == jenisObat:
                    self.map[next_index] = ("deleted", None)
                    return True
                next_index = (next_index + 1) % self.size
            return False

    def printAll(self):
        if all(item is None or item[0] == "deleted" for item in self.map):
            print("Rak obat sudah penuh")
        else:
            for item in self.map:
                if item is not None and item[0] != "deleted":
                    print(f"{item[0]}: {item[1]}")

if _name_ == "_main_":
    rak1 = RakObat()
    print
    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    rak1.tambahObat("Vitamin", "Vitacimin")

    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))

    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()