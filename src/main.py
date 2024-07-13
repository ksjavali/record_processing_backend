from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_records
from database.models import Records, DeleteIDsModel
from bson.objectid import ObjectId
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError
from datetime import datetime

# Initialize FastAPI application
app = FastAPI()

# Initialize APIRouter for defining routes
router = APIRouter()

# Create MongoDB index on 'record_identifier' for uniqueness
collection.create_index([("record_identifier", ASCENDING)], unique=True)


# Default route returning a simple message
@router.get("/")
async def home():
    return {
        "message" : "Records app is running"
    }

# Route to fetch all records from MongoDB collection
@router.get("/all/records")
async def  get_all_records():
    data = collection.find( )
    return all_records(data)

# Route to fetch records by category ID
@router.get("/category/{category_id}")
async def get_records_by_category(category_id: int):
    try:
        # Retrieve records matching the category and non-deleted criteria
        data = collection.find({"category": category_id})
        
        # Convert cursor to list to check if any documents exist
        records = list(data)
        if not records:
            return HTTPException(status_code=404, detail=f"No records found for category {category_id}")
        
        # Return formatted records
        return all_records(records)
    
    except HTTPException:
        # Propagate HTTPExceptions 
        return HTTPException(status_code=404, detail=f"No records found for category {category_id}")
    
    except Exception as e:
        # Catch any unexpected errors and return HTTP 500
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


# Route to fetch records by record indentifier
@router.get("/record_identifier/{record_id}")
async def get_records_by_record_id(record_id: str):
    try:
        # Retrieve records matching the record_id and non-deleted criteria
        data = collection.find({"record_identifier": record_id})
        
        # Convert cursor to list to check if any documents exist
        records = list(data)
        if not records:
            return HTTPException(status_code=404, detail=f"No records found for record {record_id}")
        
        # Return formatted records
        return all_records(records)
    
    except HTTPException:
        # Propagate HTTPExceptions 
        return HTTPException(status_code=404, detail=f"No records found for record {record_id}")
    
    except Exception as e:
        # Catch any unexpected errors and return HTTP 500
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

# Route to fetch records by description
@router.get("/description/{description}")
async def get_records_by_description(description: str):
    try:
        # Retrieve records matching the description and non-deleted criteria
        data = collection.find({"description": description})
        
        # Convert cursor to list to check if any documents exist
        records = list(data)
        if not records:
            return HTTPException(status_code=404, detail=f"No records found for record {description}")
        
        # Return formatted records
        return all_records(records)
    
    except HTTPException:
        # Propagate HTTPExceptions 
        return HTTPException(status_code=404, detail=f"No records found for record {description}")
    
    except Exception as e:
        # Catch any unexpected errors and return HTTP 500
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

# Route to fetch records by timestamp
@router.get("/timestamp/{timestamp}")
async def get_records_by_timestamp(timestamp: datetime):
    try:
        # Retrieve records matching the timestamp and non-deleted criteria
        data = collection.find({"timestamp": timestamp})
        
        # Convert cursor to list to check if any documents exist
        records = list(data)
        if not records:
            return HTTPException(status_code=404, detail=f"No records found for timestamp {timestamp}")
        
        # Return formatted records
        return all_records(records)
    
    except HTTPException:
        # Propagate HTTPExceptions 
        return HTTPException(status_code=404, detail=f"No records found for timetsamp {timestamp}")
    
    except Exception as e:
        # Catch any unexpected errors and return HTTP 500
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


# Route to create a record
@router.post("/")
async def create_record(record: Records):
    try:
        # Insert document with unique 'record_identifier'
        collection.insert_one(dict(record))
        return {"status_code": 200, "message": "Record created successfully"}
     # Handle case where record_identifier is not unique

    except DuplicateKeyError:
        return HTTPException(status_code=400, detail="Record identifier must be unique")
    
    # Handle any other unexpected errors
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error creating record: {e}")
  
    
# Route to update a record
@router.put("/{record_id}")
def update_record(record_id:str, updated_record: Records):
    try:
        # id = ObjectId(record_id)
        existing_doc = collection.find_one({"record_identifier":record_id})
        if not existing_doc:
            return HTTPException(status_code = 404, detail = "ID does not exist")
        resp = collection.update_one({"record_identifier":record_id}, {"$set":dict(updated_record)})
        return {"status_code":200, "message": "Task updated successfully"}

    except Exception as e:
        return HTTPException(status_code = 500, detail = f"Some error occured {e}")

# Route to delete a record
@router.delete("/delete/{record_id}")
async def delete_record(record_id: str):
    try:
        existing_doc = collection.find_one({"record_identifier":record_id})
        if not existing_doc:
            return HTTPException(status_code = 404, detail = "ID does not exist")
        resp = collection.delete_one({"record_identifier":record_id})
        return {"status_code":200, "message": "Task deleted successfully"}

    except Exception as e:
        return HTTPException(status_code = 500, detail = f"Error {e}")
    

# Route to many records based on record_ids
@router.delete("/delete")
async def delete_many_records(delete_ids_model: DeleteIDsModel):
    try:
        # Validate and convert list of record_ids
        record_identifiers = delete_ids_model.ids
        
        # Delete documents based on record_identifiers
        result = collection.delete_many({"record_identifier": {"$in": record_identifiers}})
        
        # Check deletion result
        if result.deleted_count > 0:
            return {"status_code": 200, "message": f"{result.deleted_count} records deleted successfully"}
        else:
            return HTTPException(status_code=404, detail="No records found for the provided record identifiers")
    
    except HTTPException as e:
        return e
    
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


app.include_router(router)