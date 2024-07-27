class FriendNetwork:
    def _init_(self):
        # Initializes an empty dictionary to store the network of friends.
        self.network = {}
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def add_friend(self, person, friend):
        # Adds a friendship between two people.
        if person not in self.network:
            self.network[person] = []
        if friend not in self.network:
            self.network[friend] = []
        self.network[person].append(friend)
        self.network[friend].append(person)
        # Time Complexity: O(1) for each dictionary operation.
        # Space Complexity: O(1) for each call, O(n + m) overall where n is the number of people and m is the number of friendships.

    def get_friends(self, person):
        # Returns a list of friends of the specified person.
        return self.network.get(person, [])
        # Time Complexity: O(1) for dictionary lookup.
        # Space Complexity: O(1)

    def common_friends(self, person1, person2):
        # Returns a list of common friends between two people.
        friends1 = set(self.get_friends(person1))
        friends2 = set(self.get_friends(person2))
        return list(friends1 & friends2)
        # Time Complexity: O(F1 + F2) where F1 and F2 are the number of friends of person1 and person2 respectively.
        # Space Complexity: O(F1 + F2) for the sets created.

    def nth_connection(self, start, end):
        # Returns the nth connection (degrees of separation) between two people.
        if start == end:
            return 0
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            current, depth = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            for friend in self.get_friends(current):
                if friend == end:
                    return depth + 1
                if friend not in visited:
                    queue.append((friend, depth + 1))
        return -1
        # Time Complexity: O(n + m) for BFS where n is the number of vertices (people) and m is the number of edges (friendships).
        # Space Complexity: O(n) for the visited set and the queue.

    def print_network(self):
        # Prints the entire network of friends.
        for person in self.network:
            print(f'{person}: {self.network[person]}')
        # Time Complexity: O(n + m) to print the entire network where n is the number of vertices and m is the number of edges.
        # Space Complexity: O(1) per call.

def main():
    fn = FriendNetwork()
    
    # Adding default friends Alice and Bob
    fn.add_friend('Alice', 'Bob')
    
    # Take custom input
    while True:
        choice = input("\nChoose an option:\n1. Add friend\n2. Get friends\n3. Find common friends\n4. Find nth connection\n5. Print network\n6. Exit\n")
        
        if choice == '1':
            person = input("Enter the name of the first person: ")
            friend = input("Enter the name of the friend: ")
            fn.add_friend(person, friend)
            print(f"Added friendship between {person} and {friend}.")
        
        elif choice == '2':
            person = input("Enter the name of the person: ")
            friends = fn.get_friends(person)
            print(f"Friends of {person}: {friends}")
        
        elif choice == '3':
            person1 = input("Enter the name of the first person: ")
            person2 = input("Enter the name of the second person: ")
            common = fn.common_friends(person1, person2)
            print(f"Common friends of {person1} and {person2}: {common}")
        
        elif choice == '4':
            start = input("Enter the starting person's name: ")
            end = input("Enter the ending person's name: ")
            connection = fn.nth_connection(start, end)
            print(f"Connection between {start} and {end}: {connection}")
        
        elif choice == '5':
            fn.print_network()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
