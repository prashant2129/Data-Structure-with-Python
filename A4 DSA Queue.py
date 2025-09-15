event_queue = []

def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added to the queue.")

def process_next_event():
    if event_queue:
        event = event_queue.pop(0)
        print(f"Processed event: '{event}'")
    else:
        print("No events to process.")

def display_pending_events():
    if event_queue:
        print("Pending Events:")
        for idx, event in enumerate(event_queue, 1):
            print(f"{idx}. {event}")
    else:
        print("No pending events.")

def Cancel_event(event_name):
    if event_name in event_queue:
        event_queue.remove(event_name)
        print(f"Event '{event_name}' has been cancel.")
    else:
        print(f"Event '{event_name}' not found or already processed.")

while True:
    print("\n---EVENT MENU---")
    print("1. Add event")
    print("2. Process next event")
    print("3. Display pending events")
    print("4. Cancel an event")
    print("5. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        event = input("Enter event name:")
        add_event(event)
    elif choice == 2:
        process_next_event()
    elif choice == 3:
        display_pending_events()
    elif choice == 4:
        event_name = input("Enter event name to Cancel:")
        Cancel_event(event_name)
    elif choice == 5:
        print("Exiting Event processing system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
