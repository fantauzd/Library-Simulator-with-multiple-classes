# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/16/2023
# Description: This file emulates a library simulator with LibraryItem, Patron, and Library classes.
# LibraryItem has three subclasses: Book, Album, and Movie.

class LibraryItem:
    """
    A class for LibraryItem objects that patrons may check out from the library.

    We have six data members:
    * library_item_id, unique identifier (unenforced)
    * title, may not be unique
    * location, can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
    * checked_out_by, refers to relevant patron object, if applicable
    * requested_by, refers to the Patron that has requested it
    * date_checked_out, will be set to current_date of Library when checked out
    """

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """
        A method to return the LibraryItem object's unique item id
        :return: the library item id, unique identifier
        """
        return self._library_item_id

    def get_title(self):
        """
        A method to return the LibraryItem object's title
          :return: a string, title
        """
        return self._title

    def get_location(self):
        """
        A method to return the LibraryItem object's current location
        :return: A string, can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        """
        return self._location

    def set_location(self, location):
        """
        A method to change the LibraryItem object's current location, can be "ON_SHELF", "ON_HOLD_SHELF",
        or "CHECKED_OUT"
        :return: None
        """
        self._location = location

    def get_checked_out_by(self):
        """
        A method to return the patron that has checked out the LibraryItem object
        :return: None or the patron object that has checked out the object
        """
        return self._checked_out_by

    def set_checked_out_by(self, checked_out_by):
        """
        A method to change the data member representing the patron that has checked out
        the LibraryItem object by passing parameter
        :return: None
        """
        self._checked_out_by = checked_out_by

    def get_requested_by(self):
        """
        A method to return the patron that has requested the LibraryItem object
        :return: None or the patron object that has requested the object
        """
        return self._requested_by

    def set_requested_by(self, requested_by):
        """
        A method to change the data member representing the patron that has requested the LibraryItem object
        by passing parameter
        :return: None
        """
        self._requested_by = requested_by

    def get_date_checked_out(self):
        """
        A method to return the date of the library that the object was last checked out
        :return: None or the date the LibraryItem object was last checked out
        """
        return self._date_checked_out

    def set_date_checked_out(self, date_checked_out):
        """
        A method to change the data member representing the last date the object was checked out on by passing parameter
        :return: None
        """
        self._date_checked_out = date_checked_out


class Book(LibraryItem):
    """
    A class representing a book type of LibraryItem that patrons may check out, inherits from LibraryItem.
    Books have authors and a check-out length of 21 days.
    """

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """
        returns the author for the book object
        :return: a string, the author
        """
        return self._author

    def get_check_out_length(self):
        """
        returns the check-out length for the Book object
        :return: an integer, 21
        """
        return 21


class Album(LibraryItem):
    """
    A class representing an album type of LibraryItem that patrons may check out, inherits from LibraryItem.
    Albums have artists and a check-out length of 14 days.
    """

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """
        returns the artist for the album object
        :return: a string, the artist
        """
        return self._artist

    def get_check_out_length(self):
        """
        returns the check-out length for the Album object
        :return: an integer, 14
        """
        return 14


class Movie(LibraryItem):
    """
    A class representing a movie type of LibraryItem that patrons may check out, inherits from LibraryItem.
    Movies have directors and a check-out length of 7 days.
    """

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """
        returns the director for the Movie object
        :return: a string, the director
        """
        return self._director

    def get_check_out_length(self):
        """
        returns the check-out length for the Movie object
        :return: an integer, 7
        """
        return 7


class Patron:
    """
    A class representing a patron of the library. The patron may check out items from the library and
    accrue fees for keeping items past the return date.

    We have 4 data members:
    * patron_id, a unique identifier (assumed unique)
    * name, (of patron) cannot be assumed unique
    * check_out_items, collection of LibraryItems that a Patron currently has checked out
    * fine_amount, how much patron owes in fines, may be negative
    """

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def amend_fine(self, amount):
        """
        receives as an argument a negative or positive value and changes the fine_amount data member by that amount
        :return: None
        """
        new_amount = self._fine_amount + amount
        self._fine_amount = new_amount

    def get_fine_amount(self):
        """
        returns the current fine amount owed by the patron to the library
        :return: fine amount
        """
        return self._fine_amount

    def get_patron_id(self):
        """
        returns the unique patron_id for the patron
        :return: patron_id
        """
        return self._patron_id

    def get_name(self):
        """
        returns the name of the library patron
        :return: a string, patron's name
        """
        return self._name

    def set_name(self, new_name):
        """
        changes the name of a current library patron
        :return: None
        """
        self._name = new_name

    def get_checked_out_items(self):
        """
        returns the collection of checked_out_items in the form of a list
        :return: a list of checked out items
        """
        return self._checked_out_items

    def add_library_item(self, library_item_being_checked_out):
        """
        adds the specified item (passed as parameter) to the list of checked_out_items
        :param library_item_being_checked_out: a LibraryItem object or a subclass object (Book, Album, Movie objects)
        :return: None
        """
        self._checked_out_items.append(library_item_being_checked_out)

    def remove_library_item(self, library_item_being_returned):
        """
        removes the specified item (passed as parameter) from the list of checked out items
        :param library_item_being_returned: a LibraryItem object or a subclass object (Book, Album, Movie objects)
        :return: none
        """
        self._checked_out_items.remove(library_item_being_returned)


class Library:
    """
    A class representing a library with a holding of LibraryItem objects that Patrons may check out and return to the
    Library. Fines will be issued when checked out items go beyond their return date, which is assigned at check out.

    We have three data members:
    * holdings, a list of LibraryItem objects
    * members, a list of Patron objects
    * current_date, an integer representing days since Library object was created
    """

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, new_library_item):
        """
        passes a new library object as a parameter and then adds it to the holdings data member collection
        :param new_library_item: LibraryItem object
        :return: None
        """
        self._holdings.append(new_library_item)

    def add_patron(self, new_patron):
        """
        passes a new patron object as a parameter and then adds it to the 'member' data member collection
        :param new_patron: Patron object
        :return: None
        """
        self._members.append(new_patron)

    def lookup_library_item_from_id(self, id_request):
        """
        looks through the library's holdings to find and return the LibraryItem object with a library_item_id matching
        the id_request. Library._holdings looks like: [LibraryItem1, LibraryItem2]
        :param id_request: the id that the desired Library item object has
        :return: the Library item object with matching id
        """
        for library_item in self._holdings:
            if library_item.get_library_item_id() == id_request:
                return library_item

        return None

    def lookup_patron_from_id(self, id_request):
        """
        looks through the library's members to find and return the Patron object with a patron_id matching
        the id_request. Library._members looks like: [Patron1, Patron2]
        :param id_request: the id that the desired Patron has
        :return: the Patron object with matching id
        """
        for patron in self._members:
            if patron.get_patron_id() == id_request:
                return patron

        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        takes two parameters for the id of the patron checking out the library item, and for the id of the library item
        being checked out. Checks if the patron is a member and if the library item is in holdings. Then checks to see
        if the library item is already checked out or on hold for another patron. If none of the above conditions
        prevent the book from being checked out, then the library item's checked_out_by, date_checked_out, and location,
        are updated. If the library_item was on hold for this patron, then this hold is updated. Also updates the
        patron's checked out items.
        :param patron_id: id of patron checking out
        :param library_item_id: id of item being checked out
        :return: A string about the result of the check-out attempt, either the problem encountered or a success message
        """
        patron = self.lookup_patron_from_id(patron_id)  # patron is the patron object
        library_item = self.lookup_library_item_from_id(library_item_id)  # library_item is the LibraryItem object
        if patron == None:
            return "patron not found"
        elif library_item == None:
            return "item not found"
        else:
            item_location = library_item.get_location()
            holding_patron = library_item.get_requested_by()
            if item_location == "CHECKED_OUT":
                return "item already checked out"
            # True if requested by another patron
            elif item_location == "ON_HOLD_SHELF" and holding_patron.get_patron_id() != patron_id:
                return "item on hold by other patron"
            # True if requested by same patron
            elif item_location == "ON_HOLD_SHELF" and holding_patron.get_patron_id() == patron_id:
                library_item.set_requested_by(None)
                library_item.set_checked_out_by(patron)
                library_item.set_date_checked_out(self._current_date)
                library_item.set_location("CHECKED_OUT")
                patron.add_library_item(library_item)
                return "check out successful"
            else:  # Runs whenever book is available (not checked out or requested)
                library_item.set_checked_out_by(patron)
                library_item.set_date_checked_out(self._current_date)
                library_item.set_location("CHECKED_OUT")
                patron.add_library_item(library_item)
                return "check out successful"

    def return_library_item(self, library_item_id):
        """
        Takes a parameter for the id of the library item being returned. Checks to see if the item belongs to the
        library. Ensures that the item was checked out. If all is in order, returns the book and updates the patron's
        checked out items, the library item's location, and the library item's checked_out_by data member.
        :param library_item_id: id of the library item being returned
        :return: A string about the result of the return attempt
        """
        library_item = self.lookup_library_item_from_id(library_item_id)  # library_item refers to LibraryItem object
        if library_item == None:
            return "item not found"
        elif library_item.get_location() != "CHECKED_OUT":  # True if library item on hold or on shelf already
            return "item already in library"
        else:
            patron = library_item.get_checked_out_by()  # patron refers to Patron object
            patron.remove_library_item(library_item)
            library_item.set_checked_out_by(None)
            if library_item.get_requested_by() == None:  # Runs when item does not have a request
                library_item.set_location("ON_SHELF")
                return "return successful"
            else:  # Runs when item has a request
                library_item.set_location("ON_HOLD_SHELF")
                return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        Takes the id of the patron and id of the library item as parameters. Checks if the patron is a member of the
        library and if the library item is in the library's holdings. Checks if the library item is already on hold.
        Otherwise, updates the item's requested_by data member and moves it to "ON_HOLD_SHELF".
        :param patron_id: id of patron requesting item
        :param library_item_id: id of library item being requested
        :return: a string about the result of request
        """
        patron = self.lookup_patron_from_id(patron_id)  # patron is the patron object
        library_item = self.lookup_library_item_from_id(library_item_id)  # library_item is the LibraryItem object
        if patron == None:
            return "patron not found"
        elif library_item == None:
            return "item not found"
        # Runs if library item is already requested, either is on hold or will be placed on hold when returned
        elif library_item.get_requested_by() != None:
            return "item already on hold"
        else:  # Runs when item and patron are valid and item is not already requested
            library_item.set_requested_by(patron)
            if library_item.get_location == "ON_SHELF":
                library_item.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, payment_amount):
        """
        Takes the patron id and the amount they are paying as parameters. Checks if the patron is a member of the
        library. If they are a member, the amend_fine() function is used to lower the patron's fine by the amount paid.
        :param patron_id: id of patron paying
        :param payment_amount: the amount being paid, in dollars (float or int)
        :return: A string about the result of payment
        """
        patron = self.lookup_patron_from_id(patron_id)  # patron is the patron object
        if patron == None:
            return "patron not found"
        else:
            patron.amend_fine(-payment_amount)  # Passes a negative value for payment amount so fine is decreased
            return "payment successful"

    def increment_current_date(self):
        """
        Increments the current day by one and charges 0.1 dollars to each patron for each library item they have overdue
        :return: None
        """
        self._current_date += 1
        for member in self._members:
            for item in member.get_checked_out_items():
                if item.get_date_checked_out() + item.get_check_out_length() < self._current_date:
                    member.amend_fine(.1) # adds 10 cents to fine for each book a patron has overdue

