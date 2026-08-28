from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "desc": "Great Japanese technology"},
        {"name": "Mercedes", "desc": "Great German technology"},
        {"name": "Audi", "desc": "Great German technology"},
        {"name": "Kia", "desc": "Great Korean technology"},
        {"name": "Toyota", "desc": "Great Japanese technology"},
    ]

    c_m_i = [] # c_m_i is car_make_instances
    for data in car_make_data:
        c_m_i.append(CarMake.objects.create(name=data.name, desc=data.desc))

    # Create CarModel instances including the required dealer_id field
    car_model_data = [
        {"name": "Pthfder", "year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "Qashqai", ""year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "XTRAIL", "year": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "A-Class", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "C-Class", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "E-Class", "year": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "A4", "year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A5", "year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A6","year": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "Sorrento", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Carnival", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Cerato", "year": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Corolla", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Camry", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Kluger", "year": 23, "dealer_id": 5, "car_make": c_m_i[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
