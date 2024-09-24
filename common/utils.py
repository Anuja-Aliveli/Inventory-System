# Generate 13 length id based on previous id
def generate_id(type, latest_id):
    if latest_id is not None:
        sequential_number = int(latest_id[3:]) + 1
    else:
        sequential_number = 1
    sequential_number = f'{sequential_number:010d}'  # 10 digits
    new_user_id = f'{type}{sequential_number}'
    return new_user_id

# Gives the Latest ID of that particular table
def get_latest_id(model_name,field_name):
    latest_id = model_name.objects.order_by(f'-{field_name}').first()
    if latest_id:
        latest_id = getattr(latest_id, field_name)
    else:
        latest_id = None
    return latest_id
