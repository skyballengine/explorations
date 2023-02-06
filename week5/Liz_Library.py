# Author: Elizabeth Riutta
# Github Username: ERR97056
# Description: A script that acts as a Library simultation and behaves as any normal library would.
# 1/22/2023
class LibraryItem():
    """This class sets up all needed items that will be apart of the main library"""

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_location(self):
        return self._location

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_checked_out_by(self, x):
        self._checked_out_by = x

    def get_requested_by(self):
        return self._requested_by

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_date_checked_out(self, date_checked_out):
        self._date_checked_out = date_checked_out

    def set_requested_by(self, requested_by):
        self._requested_by = requested_by

    def get_library_item_id(self):
        return self._library_item_id

    def set_location(self, item_location):
        self._location = item_location


class Book(LibraryItem):
    """This class handles all of the book items in the library"""

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        return self._author

    def get_checkout_length(self):
        return 21


class Movie(LibraryItem):
    """This class handles all of the movie items in the library"""

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        return self._director

    def get_checkout_length(self):
        return 7


class Album(LibraryItem):
    """This class handles all of the album items in the library"""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        return self._artist

    def get_checkout_length(self):
        return 14


class Patron():
    """This class handles all of the patrons that are apart of the library"""

    def __init__(self, patron_ID, name):
        self._patron_ID = patron_ID
        self._name = name
        self._checked_out_items = []
        self._fine = 0
        self._current_day = 0

    def get_fine_amount(self):
        return self._fine

    def get_name(self):
        return self._name

    def get_patron_ID(self):
        return self._patron_ID

    def add_library_items(self, library_id):
        self._checked_out_items.append(library_id)

    def remove_library_items(self, library_id):
        self._checked_out_items.remove(library_id)

    def amend_fine(self, fine_amount):
        self._fine = fine_amount + self._fine

    def get_checked_out_items(self):
        return self._checked_out_items


class Library():
    """A class that represents the simulated library"""

    def __init__(self):
        self._members = {}
        self._holdings = {}
        self._current_day = 0

    def get_holdings(self):
        return self._holdings

    def get_library_item(self, library_item_id):
        return self._holdings[library_item_id]

    def get_patron(self, patron_id):
        return self._members[patron_id]

    def add_library_item(self, library_item):
        self._holdings[library_item.get_library_item_id()] = library_item

    def add_patron(self, patron):
        self._members[patron.get_patron_ID()] = patron

    def lookup_library_item_from_id(self, library_item_id):
        if library_item_id not in self._holdings:
            return "None"
        else:
            return self._holdings[library_item_id]

    def lookup_patron_from_id(self, patron_id):
        if patron_id not in self._members:
            return "None"
        else:
            return self._members[patron_id]

    def check_out_library_item(self, patron_ID, library_item_id):
        library_item = self._holdings[library_item_id]
        patron = self._members[patron_ID]
        requested_by = library_item.get_requested_by()
        if patron_ID not in self._members:
            return "patron not found"
        if library_item_id not in self._holdings:
            return "item not found"
        if library_item.get_location() == "CHECKED OUT":
            return "item already checked out"
        if library_item.get_location() == "ON HOLD":
            if patron_ID != requested_by:
                return "item on hold by other patron"
            else:
                library_item.set_requested_by(None)
        library_item.set_checked_out_by(patron)
        library_item.set_date_checked_out(self._current_day)
        library_item.set_location("CHECKED OUT")
        patron.add_library_items(library_item_id)
        return "check out successful"

    def return_library_item(self, library_item_id):
        library_item = self._holdings[library_item_id]
        patron = library_item.get_checked_out_by()
        if library_item_id not in self._holdings:
            return "item not found"
        if library_item.get_location() == "ON SHELF":
            return "item already in library"
        else:
            if library_item.get_requested_by() == "ON HOLD":
                library_item.set_location("ON HOLD")
            else:
                library_item.set_location("ON SHELF")
            library_item.set_checked_out_by(None)
            patron.remove_library_items(library_item_id)
            library_item.set_date_checked_out(0)
        return "return successful"

    def request_library_item(self, patron_ID, library_item_id):
        """

        :param patron_ID:
        :param library_item_id:
        :return:
        """
        library_item = self._holdings[library_item_id]
        print(library_item)
        if patron_ID not in self._members:
            return "patron not found"
        if library_item_id not in self._holdings:
            return "item not found"
        if library_item.get_location() == "ON HOLD":
            return "item already on hold"
        else:
            library_item.set_requested_by(patron_ID)
            return "request successful"

    def pay_fine(self, patron_ID, fine_amount):
        patron = self._members[patron_ID]
        if patron_ID not in self._members:
            return "patron not found"
        patron.amend_fine(-fine_amount)

    def increment_current_date(self):
        self._current_day += 1
        for patron_id in self._members:
            patron = self._members[patron_id]
            for item_id in self._holdings:
                library_item = self._holdings[item_id]
                if library_item.get_location() == "CHECKED OUT":
                    if (self._current_day - library_item.get_date_checked_out()) > library_item.get_checkout_length():
                        patron.amend_fine(0.10)


b1 = Book("345", "Phantom Tollbooth", "Juster")
b2 = Book("297", "Little Women", "Abbott")

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
lib.add_patron(p1)
lib.add_patron(p2)
print(lib.lookup_library_item_from_id("345"))
item_id = b1.get_library_item_id()
patron_id = p1.get_patron_ID()
lib.check_out_library_item(patron_id, item_id)
print(p1.get_checked_out_items())

print(f"Patron 1 Fine Amount: {p1.get_fine_amount()}")
p1.amend_fine(10)
lib.pay_fine(patron_id, 30)
print(f"Patron 1 Fine Amount: {p1.get_fine_amount()}")
print(lib.request_library_item(patron_id, item_id))
print(lib._members)


