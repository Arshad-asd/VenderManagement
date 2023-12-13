<div align="center">
  <h1><a href="#" style="color: #3498db; text-decoration: none;">Vendor Management System with Performance Metrics</a></h1>
</div>


This repository contains the source code for a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, purchase order tracking, and calculates vendor performance metrics.

## Table of Contents

- [Core Features](#core-features)
- [API Endpoints](#api-endpoints)
- [API Documentation](#api-documentation)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)
- [License](#license)

## Core Features

### API Endpoints

1. Vendor Profile Management:

**Description:**

The Vendor Profile Management feature enables the system to store detailed information about vendors. Each vendor is uniquely identified by a vendor code. The information includes the vendor's name, contact details, physical address, and other relevant details. Through dedicated API endpoints, users can create, retrieve, update, and delete vendor profiles, providing a comprehensive solution for managing vendor information.

- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

2. Purchase Order Tracking:

**Description:**

The Purchase Order Tracking feature facilitates the monitoring and management of purchase orders. The system tracks essential details such as PO number, vendor reference, order date, items, quantity, and status. Through API endpoints, users can create, retrieve, update, and delete purchase orders. The system also allows listing all purchase orders with an option to filter by vendor, providing a comprehensive overview of procurement activities.

- `POST /api/purchase_orders/`: Create a new purchase order.
- `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

3. Vendor Performance Evaluation:

**Description:**

The Vendor Performance Evaluation feature focuses on assessing and analyzing the performance of vendors based on specific metrics. These metrics include On-Time Delivery Rate, Quality Rating, Response Time, and Fulfillment Rate. Additional fields are added to the vendor model to store these performance metrics. Through a dedicated API endpoint, users can retrieve a vendor's performance metrics, allowing for a thorough evaluation of vendor performance over time.

- `GET /api/vendors/{vendor_id}/performance/`: Retrieve a vendor's performance metrics.

## API Documentation

### `POST /api/vendors/`

**Description:**

Create a new vendor.

**Request:**

- **Method:** `POST`
- **Endpoint:** `/api/vendors/`
- **Body:**
  - `name` (string, required): Vendor's name.
  - `contact_details` (string, required): Contact information of the vendor.
  - `address` (string, required): Physical address of the vendor.
  - `vendor_code` (string, required): A unique identifier for the vendor.

**Response:**

- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "Vendor ABC",
      "contact_details": "contact@vendor.com",
      "address": "123 Main Street",
      "vendor_code": "VEN001",
      "on_time_delivery_rate": 0.0,
      "quality_rating_avg": 0.0,
      "average_response_time": 0.0,
      "fulfillment_rate": 0.0
    }
    ```

- **Error Response:**
  - **Status Code:** 400 Bad Request
  - **Body:**
    ```json
    {
      "error": "Invalid data. Please provide valid information."
    }
    ```

**Example:**

```bash
curl -X POST http://localhost:8000/api/vendors/ -d '{"name": "Vendor ABC", "contact_details": "contact@vendor.com", "address": "123 Main Street", "vendor_code": "VENDOR-001"}' -H 'Content-Type: application/json'
```

### `GET /api/vendors/`

**Description:**

List all vendors.

**Request:**

- **Method:** `GET`
- **Endpoint:** `/api/vendors/`

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    [
      {
        "id": 1,
        "name": "Vendor ABC",
        "contact_details": "contact@vendor.com",
        "address": "123 Main Street",
        "vendor_code": "VEN001",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 0.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.0
      },
      {
        "id": 2,
        "name": "Vendor XYZ",
        "contact_details": "info@vendorxyz.com",
        "address": "456 Oak Avenue",
        "vendor_code": "VEN002",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 0.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.0
      }
    
    ]
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "No vendors found."
    }
    ```

**Example:**

```bash
curl -X GET http://localhost:8000/api/vendors/
```

### `GET /api/vendors/{vendor_id}/`

**Description:**

Retrieve a specific vendor's details.

**Request:**

- **Method:** `GET`
- **Endpoint:** `/api/vendors/{vendor_id}/`

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "Vendor ABC",
      "contact_details": "contact@vendor.com",
      "address": "123 Main Street",
      "vendor_code": "VEN001",
      "on_time_delivery_rate": 95.5,
      "quality_rating_avg": 4.2,
      "average_response_time": 12.5,
      "fulfillment_rate": 98.8
    }
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Vendor not found."
    }
    ```

**Example:**

```bash
curl -X GET http://localhost:8000/api/vendors/1/
```

### `PUT /api/vendors/{vendor_id}/`

**Description:**

Update a vendor's details.

**Request:**

- **Method:** `PUT`
- **Endpoint:** `/api/vendors/{vendor_id}/`
- **Body:**
  - `name` (string): Vendor's name.
  - `contact_details` (string): Contact information of the vendor.
  - `address` (string): Physical address of the vendor.

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "id": 1,
      "name": "Updated Vendor Name",
      "contact_details": "updated_contact@vendor.com",
      "address": "456 Updated Street",
      "vendor_code": "VEN001",
      "on_time_delivery_rate": 95.5,
      "quality_rating_avg": 4.2,
      "average_response_time": 12.5,
      "fulfillment_rate": 98.8
    }
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Vendor not found."
    }
    ```

**Example:**

```bash
curl -X PUT http://localhost:8000/api/vendors/1/ -d '{"name": "Updated Vendor Name", "contact_details": "updated_contact@vendor.com", "address": "456 Updated Street"}' -H 'Content-Type: application/json'
```

### `DELETE /api/vendors/{vendor_id}/`

**Description:**

Delete a vendor.

**Request:**

- **Method:** `DELETE`
- **Endpoint:** `/api/vendors/{vendor_id}/`

**Response:**

- **Success Response:**
  - **Status Code:** 204 No Content

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Vendor not found."
    }
    ```

**Example:**

```bash
curl -X DELETE http://localhost:8000/api/vendors/1/
```

### `POST /api/purchase_orders/`

**Description:**

Create a new purchase order.

**Request:**

- **Method:** `POST`
- **Endpoint:** `/api/purchase_orders/`
- **Body:**
  - `vendor` (integer, required): ID of the vendor for the purchase order.
  - `order_date` (string, required): Date when the order was placed (format: "YYYY-MM-DD").
  - `delivery_date` (string, required): Expected or actual delivery date of the order (format: "YYYY-MM-DD").
  - `items` (object, required): Details of items ordered.
  - `quantity` (integer, required): Total quantity of items in the purchase order.
  - `status` (string, required): Current status of the purchase order (e.g., "pending", "completed", "canceled").
  - `quality_rating` (float): Rating given to the vendor for this purchase order (nullable).

**Response:**

- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "po_number": "PO123",
      "vendor": 1,
      "order_date": "2023-01-15",
      "delivery_date": "2023-01-30",
      "items": {"item1": "description1", "item2": "description2"},
      "quantity": 100,
      "status": "pending",
      "quality_rating": null,
      "issue_date": "2023-01-01",
      "acknowledgment_date": null
    }
    ```

- **Error Response:**
  - **Status Code:** 400 Bad Request
  - **Body:**
    ```json
    {
      "error": "Invalid data. Please provide valid information."
    }
    ```

**Example:**

```bash
curl -X POST http://localhost:8000/api/purchase_orders/ -d '{"vendor": 1, "order_date": "2023-01-15", "delivery_date": "2023-01-30", "items": {"item1": "description1", "item2": "description2"}, "quantity": 100, "status": "pending", "quality_rating": null}' -H 'Content-Type: application/json'
```

### `GET /api/purchase_orders/`

**Description:**

List all purchase orders with an option to filter by vendor.

**Request:**

- **Method:** `GET`
- **Endpoint:** `/api/purchase_orders/`
- **Query Parameters:**
  - `vendor` (integer, optional): Filter purchase orders by vendor ID.

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    [
      {
        "po_number": "PO123",
        "vendor": 1,
        "order_date": "2023-01-15",
        "delivery_date": "2023-01-30",
        "items": {"item1": "description1", "item2": "description2"},
        "quantity": 100,
        "status": "pending",
        "quality_rating": null,
        "issue_date": "2023-01-01",
        "acknowledgment_date": null
      },
      {
        "po_number": "PO456",
        "vendor": 2,
        "order_date": "2023-02-01",
        "delivery_date": "2023-02-15",
        "items": {"item3": "description3", "item4": "description4"},
        "quantity": 150,
        "status": "completed",
        "quality_rating": 4.5,
        "issue_date": "2023-01-10",
        "acknowledgment_date": "2023-01-12"
      }
    ]
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "No purchase orders found."
    }
    ```

**Example:**

```bash
# Get all purchase orders
curl -X GET http://localhost:8000/api/purchase_orders/

# Get purchase orders for a specific vendor (e.g., vendor ID 1)
curl -X GET http://localhost:8000/api/purchase_orders/?vendor=1
```

### `GET /api/purchase_orders/{po_id}/`

**Description:**

Retrieve details of a specific purchase order.

**Request:**

- **Method:** `GET`
- **Endpoint:** `/api/purchase_orders/{po_id}/`

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "po_number": "PO123",
      "vendor": 1,
      "order_date": "2023-01-15",
      "delivery_date": "2023-01-30",
      "items": {"item1": "description1", "item2": "description2"},
      "quantity": 100,
      "status": "pending",
      "quality_rating": null,
      "issue_date": "2023-01-01",
      "acknowledgment_date": null
    }
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Purchase order not found."
    }
    ```

**Example:**

```bash
curl -X GET http://localhost:8000/api/purchase_orders/1/
```

### `PUT /api/purchase_orders/{po_id}/`

**Description:**

Update a purchase order.

**Request:**

- **Method:** `PUT`
- **Endpoint:** `/api/purchase_orders/{po_id}/`
- **Body:**
  - `order_date` (string): Date when the order was placed (format: "YYYY-MM-DD").
  - `delivery_date` (string): Expected or actual delivery date of the order (format: "YYYY-MM-DD").
  - `items` (object): Details of items ordered.
  - `quantity` (integer): Total quantity of items in the purchase order.
  - `status` (string): Current status of the purchase order (e.g., "pending", "completed", "canceled").
  - `quality_rating` (float): Rating given to the vendor for this purchase order.

**Response:**

- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "po_number": "PO123",
      "vendor": 1,
      "order_date": "2023-01-15",
      "delivery_date": "2023-01-30",
      "items": {"item1": "updated_description1", "item2": "updated_description2"},
      "quantity": 150,
      "status": "completed",
      "quality_rating": 4.2,
      "issue_date": "2023-01-01",
      "acknowledgment_date": null
    }
    ```

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Purchase order not found."
    }
    ```

**Example:**

```bash
curl -X PUT http://localhost:8000/api/purchase_orders/1/ -d '{"order_date": "2023-01-15", "delivery_date": "2023-01-30", "items": {"item1": "updated_description1", "item2": "updated_description2"}, "quantity": 150, "status": "completed", "quality_rating": 4.2}' -H 'Content-Type: application/json'
```

### `DELETE /api/purchase_orders/{po_id}/`

**Description:**

Delete a purchase order.

**Request:**

- **Method:** `DELETE`
- **Endpoint:** `/api/purchase_orders/{po_id}/`

**Response:**

- **Success Response:**
  - **Status Code:** 204 No Content

- **Error Response:**
  - **Status Code:** 404 Not Found
  - **Body:**
    ```json
    {
      "error": "Purchase order not found."
    }
    ```

**Example:**

```bash
curl -X DELETE http://localhost:8000/api/purchase_orders/1/
```

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Arshad-asd/VendorManagementSystemwithPerformanceMetrics.git
```

2. Create and activate a virtual environment
   
```bash
python -m venv venv
```
```bash
# On Windows: .\venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```
```bash
cd VendorManagementSystemwithPerformanceMetrics
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser for administrative access:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)

## Testing

To run the test suite, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the [MIT License](LICENSE).
