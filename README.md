

# UE-AD-A1-MIXTE

# Cinema Management System

This project is a cinema management application designed to manage movies, showtimes, bookings, and user profiles.

## Features

- **Movie Management**: Add, update, and delete movies.
- **Showtime Management**: Schedule and assign theaters for movie showtimes.
- **Booking Management**: Reserve seats for a showtime.
- **User Management**: Handle user-related operations.

## Project Architecture

This project utilizes a Microservices Architecture, composed of four main services:

- **User**: Manages user-related operations.
- **Movie**: Handles movie information.
- **Booking**: Manages movie reservations.
- **Showtime**: Provides showtime information for movies.

The image below illustrates how these microservices communicate using different types of APIs:

![Project Architecture](image.png)

## Prerequisites

Ensure you have the following installed before starting the project:

- Python
- Pip

## Installation and Local Setup

Follow these steps to set up and run the project locally.

1. **Clone the Repository**

   ```bash
   git clone "the repo"
   ```

2. **Install Dependencies**

   Ensure Python and Pip are installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Servers**

   Open separate terminal windows for each service and start them with the following commands:

   - **Movie Service** (Port 3200)
     ```bash
     cd movie
     python movie.py 
     ```

   - **Booking Service** (Port 3201)
     ```bash
     cd booking
     python booking.py 
     ```

   - **Showtime Service** (Port 3202)
     ```bash
     cd showtime
     python showtime.py 
     ```

   - **User Service** (Port 3203)
     ```bash
     cd user
     python user.py 
     ```

4. **Testing with Postman**

   Here are some sample endpoints to test:

   - **GET Requests**:
     ```
     http://127.0.0.1:3004/movies/<id>  # Displays user details for "display movies of this id"
     http://127.0.0.1:3004/movie//bookings/<userid>  # Sget booking by userid
     ```

         ```
