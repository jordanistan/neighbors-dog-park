from square.client import Client
import os
import csv
import datetime
import json

client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='sandbox')

def load_customers():
    # Usually, you would load this from a file or a database
    data = """
    {
        "customers": [
            {
                "id": "JDKYHBWT1D4F8MFH63DBMEN8Y4",
                "created_at": "2016-03-23T20:21:54.859Z",
                "updated_at": "2016-03-23T20:21:55Z",
                "given_name": "Amelia",
                "family_name": "Earhart",
                "email_address": "Amelia.Earhart@example.com",
                "address": {
                    "address_line_1": "500 Electric Ave",
                    "address_line_2": "Suite 600",
                    "locality": "New York",
                    "administrative_district_level_1": "NY",
                    "postal_code": "10003",
                    "country": "US"
                },
                "phone_number": "+1-212-555-4240",
                "reference_id": "YOUR_REFERENCE_ID",
                "note": "a customer",
                "preferences": {
                    "email_unsubscribed": false
                },
                "creation_source": "THIRD_PARTY",
                "group_ids": [
                    "545AXB44B4XXWMVQ4W8SBT3HHF"
                ],
                "segment_ids": [
                    "1KB9JE5EGJXCW.REACHABLE"
                ],
                "version": 1
            }
        ]
    }
    """
    return json.loads(data)

def customers_to_renew(customers, years=1):
    now = datetime.datetime.utcnow()
    renewal_list = []
    for customer in customers["customers"]:
        created_at = datetime.datetime.strptime(customer["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if (now - created_at).days >= years * 365:  # 365 days/year
            renewal_list.append((created_at, customer))

    # Sort the list based on the created_at field to get the top 20 oldest customers
    renewal_list.sort(key=lambda x: x[0])

    for _, customer in renewal_list[:20]:
        yield customer

data = load_customers()
renewal_list = list(customers_to_renew(data))

# Now, we write the results to a CSV file
with open('renewal_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Given Name", "Family Name", "Email", "Phone Number"])  # header
    for customer in renewal_list:
        writer.writerow([customer['given_name'], customer['family_name'], customer['email_address'], customer['phone_number']])