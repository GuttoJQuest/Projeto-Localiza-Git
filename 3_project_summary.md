AWARI Course
Programming Logic
Professor Emanuel Viana

UML PROJECT: LOCALIZA

Student: André Gustavo Coelho Pereira

![diagrama_uml_localiza](https://github.com/user-attachments/assets/651ed0c5-85b0-4811-856d-26cc4d0cf230)


Challenge proposed by Professor Emanuel Viana at the conclusion of the Programming Logic Course on the AWARI platform:

With the setup completed for maintaining code versioning and using an IDE that facilitates agile development, let’s move on to our challenge!

Localiza, a well-known Brazilian network specializing in car rentals, has requested your services as a software developer to implement a new management system for car rentals and returns, as well as for registering cars, customers, and employees. After completing the requirements gathering meeting, you identified the following needs:

a. Each car must have the following records: license plate, year, color, model, mileage, daily rate, and observations.

b. Localiza has two car categories: sports cars, which have attributes for time to reach 100 km/h and a list of upgrades (you can add some generic examples), and utility vehicles, which include attributes for the number of passengers, trunk size, and kilometers per liter of gasoline.

c. A car is linked to a reservation that has an associated customer, a code, a status flag, a start date, and an end date.

d. A reservation is always associated with only one customer, and a customer can only have one active reservation.

e. Each employee must have the following records: name, CPF, age, address, hire date, salary, number of rentals processed, status (active or inactive), and a contact phone number.

f. A customer must have the following attributes: name, CPF, age, birth date, driver’s license number, driver’s license photo, license expiration year, address, contact phone number, and email.

g. Additionally, Localiza wants to send promotions to the email addresses of registered customers. These promotions must include a title, a description, and an expiration date.

Your task is to analyze all the above requirements, create a UML diagram if necessary, and develop the software according to the client's described needs.

At the end of the project, you must deliver the GitHub repository link containing the project implementation as well as any related documentation.



**AWARI**  
**Course: Programming Logic**  
**Professor: Emanuel Viana**  
**Student: André Gustavo Coelho Pereira**  

**Localiza Project**  
**1 – Class Identification**  

**Detailed Explanation of Each Field**  

**General Functionality**  

The challenge consisted of implementing a program to manage a vehicle rental system, including the registration of customers, employees, cars (sports and utility), reservations, and promotions, using Python.  

The code features classes structured as the foundation of the system, allowing for future customizations and expansions, such as data persistence and user interfaces.  

To meet the client's requirements, it was recommended to create an initial UML diagram, representing the relationships between entities, ensuring the client's needs are addressed in an organized and scalable manner.  

---

**1. Client Class**  
- Represents a system customer.  
**Attributes:**  
- **Client identification:**  
  `name`, `cpf`, `age`, `birth_date`  
- **Driver’s license information:**  
  `license_number`, `license_photo`, `expiration_year`  
- **Contact and location:**  
  `address`, `phone`, `email`  
- **Association with a reservation** (initially set to `None`):  
  `reservation`  
**Methods:**  
- Returns the reservation associated with the client:  
  `get_reservations()`  

---

**2. Employee Class**  
- Represents a system employee.  
**Attributes:**  
- **Employee identification:**  
  `name`, `cpf`, `age`  
- **Contact information:**  
  `address`, `phone`  
- **Employment details:**  
  `hire_date`, `salary`, `rentals_processed`  
- **Employee status (active/inactive):**  
  `status`  

---

**3. Car Class**  
- Represents a generic car available for rental.  
**Attributes:**  
- **Car identification and characteristics:**  
  `plate`, `year`, `color`, `model`  
- **Usage and cost information:**  
  `mileage`, `daily_rate`  
- **Additional notes:**  
  `observation`  

---

**4. Car Subclasses**  

**SportsCar Class**  
- Represents a sports car.  
**Additional Attributes:**  
- **Performance data:**  
  `time_to_100kmh`  
- **Specific upgrade list:**  
  `upgrade_list`  

**UtilityCar Class**  
- Represents a utility car.  
**Additional Attributes:**  
- **Passenger capacity:**  
  `passengers`  
- **Trunk size:**  
  `trunk_size`  
- **Fuel efficiency:**  
  `km_per_liter`  

---

**5. Reservation Class**  
- Represents a car rental reservation.  
**Attributes:**  
- **Reservation identification and status:**  
  `code`, `status`  
- **Reservation period:**  
  `start_date`, `end_date`  
- **Association with a car and a client:**  
  `car`, `client`  
**Methods:**  
- Calculates the total cost of the reservation based on the number of days and the car's daily rate:  
  `calculate_cost()`  

---

**6. Promotion Class**  
- Represents a promotion that can be sent to clients.  
**Attributes:**  
- **Promotion details:**  
  `title`, `description`  
- **Promotion validity date:**  
  `expiration_date`  