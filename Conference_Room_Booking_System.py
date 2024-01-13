'''
Create a conference room booking system with classes for rooms, reservations,
and users. Include methods for checking room availability, booking time slots, and
sending notifications.
'''
import datetime  # Import for handling dates and times

class Room:
    """Represents a conference room with its capacity and reservations."""

    def __init__(self, room_number, capacity):
        """Initializes a Room with its number and capacity."""
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = []  # Stores room reservations as a list of dictionaries

    def is_available(self, start_time, end_time):
        """Checks if the room is available during the specified time range."""
        for reservation in self.reservations:
            if not (end_time <= reservation["start_time"] or start_time >= reservation["end_time"]):
                return False  # Overlaps with an existing reservation
        return True  # No conflicts found

    def book_room(self, user, start_time, end_time):
        """Books the room for the given user and time range."""
        if self.is_available(start_time, end_time):
            self.reservations.append({"user": user, "start_time": start_time, "end_time": end_time})
            print(f"Room {self.room_number} booked successfully for {user} from {start_time} to {end_time}.")
        else:
            print(f"Room {self.room_number} is not available during the specified time.")

    def __str__(self):
        """Returns a string representation of the room for printing."""
        return f"Room {self.room_number} - Capacity: {self.capacity}"

class User:
    """Represents a user of the booking system."""

    def __init__(self, user_id, name):
        """Initializes a User with their ID and name."""
        self.user_id = user_id
        self.name = name

class ConferenceRoomBookingSystem:
    """Manages conference rooms and booking operations."""

    def __init__(self):
        """Initializes the booking system with an empty list of rooms."""
        self.rooms = []

    def add_room(self, room):
        """Adds a room to the booking system."""
        self.rooms.append(room)

    def find_room(self, room_number):
        """Finds a room by its number."""
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None  # Room not found

    def display_available_rooms(self, start_time, end_time):
        """Displays rooms that are available during the specified time."""
        available_rooms = [room for room in self.rooms if room.is_available(start_time, end_time)]
        if not available_rooms:
            print("No rooms are available during the specified time.")
        else:
            print("Available Rooms:")
            for room in available_rooms:
                print(room)

# ... (Menu-related functions and main loop with comments)
