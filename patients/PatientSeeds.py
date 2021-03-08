from models import Patient

def create_patients():

    patents = [
        {
            "first_name": "Ben",
            "last_name": "Garlock",
            "ssn": "555-555-5555",
            "email": "ben.garlock@gmail.com"
        },
        {
            "first_name": "Alyson",
            "last_name": "dysuza",
            "ssn": "777-777-7777",
            "email": "adysuza@benco.bengarlock.com"
        },
        {
            "first_name": "Matt",
            "last_name": "Touron",
            "ssn": "555-555-5555",
            "email": "mtouron@benco.bengarlock.com"
        },
    ]

    for patient in patents:
        Patient.objects.create(
            first_name=patient["first_name"],
            last_name=patient["last_name"],
            ssn=patient["ssn"],
            email=patient["email"]
        )




