# E-Commerce delivery project


Welcome to the E-Commerce delivery project! This Django project provides a robust set of APIs for managing orders and users in an e-commerce setting. It includes features such as placing orders, retrieving order details, checking order status, creating users, and listing users. Additionally, the project incorporates Celery for asynchronous task scheduling to update order status and send email notifications

## Installation

Clone the repository:

   ```
git clone https://github.com/MitanshuBaranwal/ecommerce-delivery-updater.git
   ```

Install dependencies:
   ```
pip install -r requirements.txt
   ```
## Configure Django settings:

### Create a .env file and configure the necessary environment variables:
   ```
DJANGO_SECRET_KEY=your_secret_key

DEBUG=True
   ```
### Migrate the database:

   ```
python manage.py makemigrations 
   ```

   ```
python manage.py migrate
   ```
### Run the development server:

   ```
python manage.py runserver
   ```

The API should be accessible at http://localhost:8000/.

### API Endpoints

Check Connection

   ```
Endpoint: /hi

Method: GET
   ```

### Description: API for checking connection returns "Hello!".

Place Order

   ```

Endpoint: /place-order

Method: POST
   ```


### Description: API for placing orders. Accepts order details in the request payload.

Order Details

   ```
Endpoint: /order-details/{order_id}

Method: GET
   ```


### Description: API for retrieving details of a specific order.

Order Status Details

   ```
Endpoint: /order-status/{order_id}

Method: GET
   ```

### Description: API for retrieving status details of a specific order.

Create User

   ```
Endpoint: /create-user

Method: POST
   ```

### Description: API for creating new users. Accepts user details in the request payload.

List Users

   ```
Endpoint: /user-list

Method: GET
   ```

### Description: API for listing all users.

Asynchronous Order Status Update

The project leverages Celery for asynchronous task scheduling to update order status over time. The order_status_update task handles the transition of order status and sends email notifications.

## Usage:

Access the provided API endpoints using your preferred HTTP client.

Ensure Celery is running to handle asynchronous tasks:

   ```
celery -A ecommerce_project  worker --pool=solo -l info
   ```

Customize the project according to your specific e-commerce requirements.

## Notes:

Ensure a production-ready Django configuration for deployment.

Update the Celery configuration and message broker settings based on your deployment environment.



### Use with Docker
1. Build docker container using the below command:
      ```
      docker-compose up --build
      ```
2.  Start Docker Compose services in detached mode:
      ```   
      docker-compose up -d
      ```



## Contact
For any enquiries please contact me at :
      
      mitanshubaranwal70232@gmail.com
      



