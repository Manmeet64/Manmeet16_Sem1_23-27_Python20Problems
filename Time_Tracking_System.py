'''
Develop a time tracking system for employees with classes for employees,
projects, and time entries. Implement methods for logging hours, generating
timesheets, and calculating overtime.
'''
class Employee:
    """Represents an employee in the time tracking system."""

    def __init__(self, name):
        """Initializes an Employee with their name."""
        self.name = name

    def get_name(self):
        """Returns the employee's name."""
        return self.name


class Project:
    """Represents a project that employees can work on."""

    def __init__(self, project_name):
        """Initializes a Project with its name."""
        self.project_name = project_name

    def get_project_name(self):
        """Returns the project's name."""
        return self.project_name


class TimeEntry:
    """Represents a single time entry for an employee and project."""

    def __init__(self, employee, project, hours):
        """Initializes a TimeEntry with the employee, project, and hours worked."""
        self.employee = employee
        self.project = project
        self.hours = hours

    def get_employee(self):
        """Returns the employee associated with the time entry."""
        return self.employee

    def get_project(self):
        """Returns the project associated with the time entry."""
        return self.project

    def get_hours(self):
        """Returns the number of hours worked in the time entry."""
        return self.hours


class TimeTrackingSystem:
    """Manages time entries and provides reporting for employees."""

    def __init__(self):
        """Initializes the TimeTrackingSystem with an empty list of time entries."""
        self.time_entries = []

    def log_hours(self, employee, project, hours):
        """Logs a new time entry for the given employee, project, and hours."""
        time_entry = TimeEntry(employee, project, hours)
        self.time_entries.append(time_entry)

    def generate_timesheet(self):
        """Prints a formatted timesheet of all logged time entries."""
        print("Timesheet:")
        for entry in self.time_entries:
            print(f"Employee: {entry.get_employee().get_name()}, "
                  f"Project: {entry.get_project().get_project_name()}, "
                  f"Hours: {entry.get_hours()}")

    def calculate_overtime(self):
        """Calculates the total overtime hours worked based on standard hours per week."""
        standard_hours_per_week = 40
        total_hours = sum(entry.get_hours() for entry in self.time_entries)
        return max(0, total_hours - standard_hours_per_week)
