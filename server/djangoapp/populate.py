from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    c_m_i = [] # c_m_i is car_make_instances
    for data in car_make_data:
        c_m_i.append(CarMake.objects.create(name=data.name, description=data.description))

    # Create CarModel instances including the required dealer_id field
    car_model_data = [
        {"name": "Pthfder", "type": "SUV", "year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "Qashqai", "type": "SUV", "year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "A-Class", "type": "SUV", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "C-Class", "type": "SUV", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "E-Class", "type": "SUV", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "A4", "type": "SUV", "year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A5", "type": "SUV", "year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A6", "type": "SUV", "year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "Sorrento", "type": "SUV", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Carnival", "type": "SUV", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Cerato", "type": "Sedan", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Corolla", "type": "Sedan", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Camry", "type": "Sedan", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Kluger", "type": "SUV", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
