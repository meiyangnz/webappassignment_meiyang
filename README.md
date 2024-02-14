# webappassignment_meiyang

Selwyn Panel Beaters Web Application Report
Project Overview
This report outlines the development of a web application for Selwyn Panel Beaters to manage customers, jobs, services, parts, and billing. The application is developed using Python Flask for the backend, MySQL for the database, and HTML/CSS (Bootstrap) for the frontend.

Solution Structure
Routes & Functions
/admin: Renders the admin dashboard with links to manage customers, jobs, parts, and services.
/currentjobs: Displays current jobs for technicians, including customer names and job dates.
/job/<int:job_id>: Shows details for a specific job, allowing technicians to add services/parts and mark jobs as complete.
/add_customer: Form for administrators to add new customers.
/add_part: Form for administrators to add new parts.
/add_service: Form for administrators to add new services.
/schedule_job: Allows administrators to schedule a new job by selecting a customer and date.
/unpaid_bills: Displays unpaid bills for administrators, with functionality to mark them as paid.
/overdue_bills: Lists all bills, highlighting overdue ones.
Assumptions & Design Decisions
Assumptions:

The application is intended for internal use, hence basic security measures without advanced authentication.
Administrators are responsible for managing entities (customers, services, parts) and billing.
Technicians focus on job management, including adding services/parts to jobs.
Design Decisions:

Flask: Chosen for its simplicity and flexibility in developing web applications.
MySQL: Provides robust data storage for customers, jobs, services, and parts.
Bootstrap: Ensures a responsive design for the application's front end, improving usability across devices.
Modular Templates: Used template inheritance in Flask to maintain a consistent layout across different pages.
Client-side Validation: Assumed for simplicity, although server-side validation is implemented for robustness.


Project Report – Part 2
Database Questions Answered
Job Table Creation: The SQL statement for creating the job table includes references to the customer table to maintain relational integrity. It stores job details, including cost, completion, and payment status.

Relationships: The foreign key constraints in the job, job_part, and job_service tables ensure referential integrity, linking jobs to customers and services/parts to jobs.

Insert Statements: Initial data for customers, parts, and services are provided to populate the database, facilitating immediate functionality testing upon deployment.

Audit Trail and Logins: Suggestions for extending the database schema to include audit trails (timestamped records of additions) and a hypothetical implementation of login functionality were discussed, highlighting the importance of security and data integrity.

Conclusion
This web application offers a streamlined interface for Selwyn Panel Beaters to manage their operations more efficiently. By leveraging Flask, MySQL, and Bootstrap, the application achieves a balance between functionality and usability, catering to the needs of both technicians and administrators.