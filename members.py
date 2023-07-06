import datetime
import squareconnect
from squareconnect.rest import ApiException

# Configure Square API credentials
squareconnect.configuration.access_token = 'YOUR_ACCESS_TOKEN'

def get_list_of_members():
    try:
        # Create an instance of the Square API MembersApi
        members_api = squareconnect.MembersApi()

        # List members
        response = members_api.list_members()

        # Return the list of members
        return response.members

    except ApiException as e:
        print("Exception when calling MembersApi->list_members: %s\n" % e)
        return []

def get_top_paying_customers(members, count):
    # Sort members by lifetime value (highest paying first)
    sorted_members = sorted(members, key=lambda x: x.lifetime_value, reverse=True)

    # Return the top paying customers
    return sorted_members[:count]

def get_memberships_about_to_expire(members, count):
    # Get the current date
    current_date = datetime.date.today()

    # Filter memberships that are about to expire
    expiring_memberships = [
        member for member in members if member.memberships and member.memberships[0].expires_at.date() <= current_date
    ]

    # Sort expiring memberships by expiration date (closest first)
    sorted_memberships = sorted(expiring_memberships, key=lambda x: x.memberships[0].expires_at)

    # Return the top memberships about to expire
    return sorted_memberships[:count]

# Get the list of members
members_list = get_list_of_members()

# Get the top 20 paying customers
top_paying_customers = get_top_paying_customers(members_list, 20)

# Display the top 20 paying customers
print("Top 20 Paying Customers (VIP):")
for customer in top_paying_customers:
    print(customer.given_name, customer.family_name)

# Get the top 10 memberships about to expire
expiring_memberships = get_memberships_about_to_expire(members_list, 10)

# Display the top 10 memberships about to expire
print("\nMemberships About to Expire:")
for member in expiring_memberships:
    expiration_date = member.memberships[0].expires_at.date()
    print(member.given_name, member.family_name, "- Expiration Date:", expiration_date)
