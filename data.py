from faker import Faker

fake = Faker()

def get_fake_data():
    """
    Get fake data
    """
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }