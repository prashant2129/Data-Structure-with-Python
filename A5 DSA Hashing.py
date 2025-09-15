class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Simple division method
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Insert if not present, else update the value
        for item in self.table[index]:
            if item == key:
                print(f"Key {key} already exists, updating value.")
                item = value
                return
        self.table[index].append([key, value])
        print(f"Inserted ({key}, {value}) at index {index}.")

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item == key:
                print(f"Key {key} found at index {index}: Value = {item}")
                return item
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item == key:
                del self.table[index][i]
                print(f"Key {key} deleted from index {index}.")
                return
        print(f"Key {key} not found for deletion.")

    def display(self):
        print("\nHash Table Contents:")
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

# Main program
hash_table = HashTable()

while True:
    print("\nHash Table Operations:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key to insert: "))
        value = input("Enter value for the key: ")
        hash_table.insert(key, value)
        
    elif choice == '2':
        key = int(input("Enter key to search: "))
        hash_table.search(key)

    elif choice == '3':
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)

    elif choice == '4':
        hash_table.display()
        
    elif choice == '5':
        print("Exiting program.")
        break
        
    else:
        print("Invalid choice. Please try again.")
