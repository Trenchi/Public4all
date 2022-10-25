from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################

class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    e_mail = Column(String)

    # Foreignkeys
    addresses_id = Column(Integer, ForeignKey("addresses.id"))
    street_and_number_id = Column(Integer, ForeignKey("street_and_number.id"))
    zip_code_id = Column(Integer, ForeignKey("zip_code.id"))
    city_id = Column(Integer, ForeignKey("city.id"))


class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Street_and_Number(Base):
    __tablename__ = "street_and_number"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Zip_Code(Base):
    __tablename__ = "zip_code"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String)


def initialize_database():
    """
    Initializes the database and creates all tables.

    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    """
    session.add(friend)


def database_get_all_friends():
    """
    Database command to get all friends.
    """
    all_friends = session.query(Friend).all()
    print(all_friends)


# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

    # Example to add a new friend
    new_friend = Friend(e_mail="jack@example.com", first_name="Jack")
    database_add_friend(new_friend)

    # Example to list all friends
    database_get_all_friends()