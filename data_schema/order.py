from pydantic import BaseModel

# Data for enable functionality
class enable_data(BaseModel):
    query_about_order:bool


# order of data
orders_db = {
    "id_123": {"status": "Shipped", "delivery_date": "2025-09-12"},
    "id_456": {"status": "Processing", "delivery_date": "2025-09-15"},
    "id_789": {"status": "Delivered", "delivery_date": "2025-09-05"},
}
