class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start_index = index  

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == key:
                print(f"Key {key} already exists!")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table is full! Cannot insert.")
                return

        self.table[index] = key
        print(f"Inserted key {key} at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print(f"Key {key} not found in table.")

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = "DELETED"
                print(f"Key {key} deleted from index {index}")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print(f"Key {key} not found, cannot delete.")

    def display(self):
        print("\nCurrent Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

if __name__ == "__main__":
    ht = HashTable()

    while True:
        print("\n--- Hash Table Menu ---")
        print("1. Insert Key")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Table")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key (integer): "))
            ht.insert(key)

        elif choice == 2:
            key = int(input("Enter key to search: "))
            ht.search(key)

        elif choice == 3:
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == 4:
            ht.display()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
