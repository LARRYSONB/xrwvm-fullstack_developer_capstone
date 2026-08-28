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
        {"name": "Pthfder", "yr": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "Qashqai", ""yr": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "XTRAIL", "yr": 23, "dealer_id": 1, "car_make": c_m_i[0]},
        {"name": "A-Class", "yr": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "C-Class", "yr": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "E-Class", "yr": 23, "dealer_id": 2, "car_make": c_m_i[1]},
        {"name": "A4", "yr": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A5", "yr": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "A6","yr": 23, "dealer_id": 3, "car_make": c_m_i[2]},
        {"name": "Sorrento", "yr": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Carnival", "yr": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Cerato", "yr": 23, "dealer_id": 4, "car_make": c_m_i[3]},
        {"name": "Corolla", "yr": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Camry", "yr": 23, "dealer_id": 5, "car_make": c_m_i[4]},
        {"name": "Kluger", "yr": 23, "dealer_id": 5, "car_make": c_m_i[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            year=data['yr'],
            dealer_id=data['dealer_id']
        )
