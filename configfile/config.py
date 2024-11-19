from pymongo import MongoClient

MONGO_URI = "mongodb://127.0.0.1:27017/"
DATABASE_NAME = "sampleupload"  # Use your actual database name
USER_COLLECTION = "users"  # Corrected variable name


def get_db():
    """Connect to MongoDB and return the database instance."""
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    return db  # Return only the database instance

def get_users_collection():
    """Get the users collection from the database."""
    db = get_db()  # Get the database
    user_collection = db[USER_COLLECTION]  # Use a single bracket for collection
    return user_collection  # Return only the collection

