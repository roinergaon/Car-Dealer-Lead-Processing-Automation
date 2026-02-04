# Car Dealer Lead Processing Automation

This project simulates an end-to-end **car dealer lead processing pipeline** built with **FastAPI**, **Docker**, and **asynchronous background processing**.

The system receives leads, validates them, enriches them via a mock external API, scores and prioritizes them, routes them to the correct owner, and logs every processing stage in a structured way.

---

## Architecture Overview

- **FastAPI** – main REST API for receiving leads  
- **Mock API service** – simulates external lead enrichment  
- **Async background tasks** – non-blocking lead processing  
- **Structured logging** – JSON logs for each pipeline stage  
- **Docker Compose** – orchestrates all services  
- **File-based storage** – processed leads are persisted as JSON  

---

## Requirements

- **Docker Desktop** (includes Docker & Docker Compose)  
  Install from: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- No local Python installation is required

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/roinergaon/Car-Dealer-Lead-Processing-Automation.git
cd Car-Dealer-Lead-Processing-Automation
```
Build and start the services:
```bash
docker-compose up --build
```
This starts:

main-api – FastAPI service (port 8000)
mock-api – mock enrichment service (port 8001)

Sample leads are provided in:

data/sample_leads.json

To send them from inside the Docker container:

Open a shell inside the main API container:

```bash
docker-compose exec main-api bash
```
Run the posting script: python post_leads.py
processed_leads.json will be saved inside data folder.

You should see a response confirming that the leads were successfully received.

POST /api/leads - Receives a list of leads and processes them asynchronously.

Request Body Example:
```bash
[
  {
    "BranchID": "400",
    "WorkerCode": "W123",
    "AskedCar": "M100",
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john@example.com",
    "Phone": "0541234567",
    "FromWebSite": "DealerSite",
    "Area": "Center"
  }
]
```
Response Example:
```bash

{
  "message": "1 lead(s) received"
}
```

Actual processing continues asynchronously in the background.

Each lead goes through the following stages (logged as structured JSON):

received – lead accepted by the API

rejected – validation failure

enrichment_failed – external enrichment error

processed – lead scored and routed

waiting – final state after persistence

Logs are written to: logs/leads.log


## Purpose

- Created as part of a backend / automation engineering assignment to demonstrate:

- API design

- Asynchronous processing

- Docker-based environments

- Clean project structure and logging



https://github.com/user-attachments/assets/5dabd1fb-3110-4a72-883f-de88c3add418

