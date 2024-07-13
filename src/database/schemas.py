def individual_record(todo):
    return {
        "id": str(todo["_id"]),
        "record_identifier": todo["record_identifier"],
        "description": todo["description"],  
        "timestamp": todo["timestamp"],      
        "category": todo["category"]         
    }

def all_records(todos):
    return [individual_record(todo) for todo in todos]
