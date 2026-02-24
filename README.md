LogisticHub Exam Project
---
📌 **Overview**

LogisticHub is a web-based logistics management platform built with Django.
It connects drivers and companies through transport offers and driver availability postings.

The system allows:

Companies to register and post transport offers

Drivers to register and publish their availability

Mutual interaction through comments (connections)

---

🚀 **Features**


🏢 Companies Section

View all companies (paginated, 6 per page, 2 columns layout)

Register a new company

View company details

View all company offers

Add new company offers

Connect with available drivers through comments



🚚 **Drivers Section**

View all drivers (paginated, 6 per page, 2 columns layout)

Register a new driver

View available drivers

Add driver availability

Connect with company offers through comments

---

🧪 How to Experience Full Functionality

To fully explore the platform:

Register multiple companies

Create several company offers

Register multiple drivers

Add driver availability posts

Interact through clickable cards (comment sections)

Each comment creates a real-time connection between drivers and companies.

---

🏠 Home Page & Navigation

All Company Offers and Driver Availabilities are displayed on the Home Page as clickable cards

Clicking a card redirects directly to the detail or comment/connection section

Also by clicking on the connected drivers/companies you can display extra details

From the navigation menu, you can access:

All Companies → view companies and their offers

All Drivers → view drivers and availability

Edit and delete options are available for all entries to manage data easily


---

🔄 **Interaction System**

Companies can comment on driver availability (creates connection)

Drivers can comment on company offers (creates connection)

Automatic ManyToMany linking after comment submission

Collapsible connection sections

---

🔍 **Search & Pagination**

Search by keywords indicated in the placeholders of the searchbars

Independent pagination for:

Offers

Drivers

Companies

Availability

Comment sections

---

🎨 UI / UX Design

Responsive design using Bootstrap 5

Frosted glass (jelly) navbar and footer

Dynamic background images per section:

Home

Companies

Drivers

Smooth background transitions

Card-based clickable layout with hover effects

---

🛠 **Tech Stack**

Backend:

Python

Django 

Postgres SQL Database

Frontend:

HTML5

CSS3

Bootstrap 5

Bootstrap Icons

---

⚙️ Installation

⚠️ Before starting: Make sure to create a PostgresSQL database
and replace the database credentials and SECRET_KEY in your .env file
with your own values (if you don`t have .env just create one).

--
- in your .env file

DB_NAME=your_db_name

DB_USER=your_db_user

DB_PASS=your_db_password

DB_HOST=your_db_host

DB_PORT=your_db_port

SECRET_KEY=your_secret_key_here

--

Create virtual environment:

python -m venv .venv

Activate environment:

- Windows:

.venv\Scripts\activate

- macOS/Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start server:

python manage.py runserver

Open:

http://127.0.0.1:8000/ or  http://localhost:8000/

---

📝 Notes:

No authentication system is implemented (exam requirement).

Class-Based Views are used throughout the project.

Pagination is implemented for all major lists.

Forms are implemented using Django ModelForms.