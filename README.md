# UStudent AI Platform

A full-stack AI student assistant that integrates course information, handbook retrieval, academic planning, and tool-using AI workflows.

This repository consolidates a guided AI engineering course project into a portfolio-oriented monorepo, covering the frontend, backend, AI service, containerisation, and AWS infrastructure.

> **Project context:** The core application architecture and several backend, RAG, and agent components were instructor-scaffolded. My work focused on integration, configuration, testing, deployment, debugging, and understanding the end-to-end system.

---

## Overview

UStudent is designed as a multi-service student support platform.

The system includes:

- a React frontend for student interaction
- a Spring Boot backend for course and student data
- a FastAPI AI service for RAG and agent workflows
- PostgreSQL for application data
- Docker for containerisation
- AWS ECS Fargate for cloud execution
- Amazon ECR for Docker image storage
- Amazon RDS for PostgreSQL
- an Application Load Balancer for request routing
- Terraform for infrastructure provisioning

---

## Architecture

The platform uses a multi-service cloud architecture:

- **User / Browser**
  → Application Load Balancer

- **Frontend**
  → React + Nginx
  → Runs as an ECS Fargate service

- **Backend**
  → Spring Boot
  → Runs as an ECS Fargate service
  → Connects to PostgreSQL on Amazon RDS

- **AI Service**
  → FastAPI
  → RAG / handbook retrieval
  → Agent / tool calling
  → Communicates with backend APIs

- **Amazon ECR**
  → Stores Docker images for frontend, backend, and AI services

- **Terraform**
  → Provisions AWS infrastructure including VPC, ECS, ALB, ECR, and RDS

---

## Key Features

### AI and RAG

- Handbook question answering using retrieval-augmented generation
- Semantic retrieval over handbook content
- Course-related question answering
- Graduation eligibility workflows
- Agent-based tool calling
- Multi-turn AI chat support

### Backend

- Course information APIs
- Student and enrolment workflows
- PostgreSQL persistence
- REST API integration with the AI service

### Frontend

- Student login interface
- Course-related user workflows
- AI chat interface
- Integration with backend and AI APIs

### Cloud Deployment

- Dockerised frontend, backend, and AI services
- Docker images stored in Amazon ECR
- Services deployed on Amazon ECS Fargate
- PostgreSQL hosted on Amazon RDS
- Application Load Balancer for request routing
- Infrastructure provisioned with Terraform

---

## My Contributions

This was a guided, instructor-scaffolded AI engineering project. Several core application, backend, RAG, and agent components were provided as starter implementations.

My hands-on work focused on:

- Configuring and testing FastAPI endpoints
- Validating graduation eligibility behaviour with automated tests
- Configuring and testing the handbook RAG workflow
- Configuring LLM integration
- Running and analysing agent and tool-calling workflows
- Testing AI-to-backend API integration
- Running the multi-service application with Docker
- Configuring Terraform variables and provisioning AWS infrastructure
- Building and pushing frontend, backend, and AI Docker images to Amazon ECR
- Deploying the three services to Amazon ECS Fargate
- Verifying ALB routing, backend APIs, RDS connectivity, and AI chat end to end
- Debugging deployment failures using ECS service events and CloudWatch logs

---

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | React, JavaScript, Nginx |
| Backend | Spring Boot, Java / Kotlin, Gradle |
| AI Service | Python, FastAPI |
| AI | RAG, vector search, agent / tool calling |
| Database | PostgreSQL |
| Containers | Docker |
| Cloud | AWS ECR, ECS Fargate, ALB, RDS, VPC, CloudWatch |
| Infrastructure | Terraform |
| CI/CD | Bitbucket Pipelines |
| Testing | Pytest, backend tests |


---

## Repository Structure

- `frontend/` — React frontend
- `backend/` — Spring Boot backend
- `ai-service/` — FastAPI, RAG, and agent service
- `infrastructure/` — Terraform AWS infrastructure
- `docs/screenshots/` — Demo and deployment screenshots
- `README.md` — Portfolio documentation
- `.gitignore` — Local and sensitive-file exclusions

---

## AWS Deployment

The application was successfully deployed to AWS using a container-based architecture.

Source Code → Docker Build → Amazon ECR → Amazon ECS Fargate → Application Load Balancer → Public Application

Terraform was used to provision:

- VPC and subnets
- Security groups
- NAT gateways
- Amazon ECR repositories
- Amazon ECS cluster and services
- Application Load Balancer
- Amazon RDS PostgreSQL

The AWS environment is created on demand and destroyed after demonstrations to avoid unnecessary cloud costs.

---

## Deployment Verification

The deployed system was verified end to end.

### Frontend

The public application endpoint returned **HTTP 200**.

### Backend and Database

The course API successfully returned course data through:

`GET /api/courses`

This confirmed the path:

`ALB → Backend ECS Service → PostgreSQL / RDS`

### AI Service

The AI endpoint was tested with:

> How many credits do I need to graduate?

and successfully returned:

> You need 120 credits to graduate.

This validated the end-to-end AI path:

`Client → ALB → Frontend / API routing → AI Service → Agent / Tool → Handbook retrieval → Response`

---

## Deployment Troubleshooting

During deployment, I diagnosed several production-style issues.

### ECS image pull failure

**Error:** `CannotPullContainerError`

ECS attempted to start tasks before the required Docker images were available in ECR.

I built, tagged, and pushed the frontend, backend, and AI images to ECR, then forced new ECS deployments.

### HTTP 503 from the frontend

The Application Load Balancer was reachable, but there was no healthy frontend task.

I inspected ECS desired, pending, and running task counts, along with ECS service events.

### Nginx startup failure

CloudWatch logs showed:

`host not found in upstream "ustudent-backend"`

The frontend was rebuilt using the intended production Docker configuration and redeployed.

### AI Chat returned HTTP 502

After rebuilding the production images and redeploying the ECS services, the `/ai/agent-chat` endpoint passed end-to-end verification.

---

## Security

This portfolio repository intentionally excludes:

- `.env` files
- AWS credentials
- LLM API keys
- Terraform variable files containing secrets
- Terraform state files
- Private keys
- Virtual environments
- Dependency directories

Example configuration files are used instead of real credentials.

---

## Demo

Deployment screenshots and a short demo will be added later.

The AWS environment is not kept running continuously to avoid unnecessary cloud costs.

**Live demo available on request.**

---

## Project Attribution

This project was completed as part of a guided AI engineering learning program.

Several core application components and starter implementations were instructor-provided. This repository is intended to demonstrate my hands-on experience with:

- System integration
- API testing
- RAG and agent workflows
- Docker
- AWS deployment
- Terraform
- Cloud troubleshooting
- End-to-end validation

It should not be interpreted as claiming independent authorship of all underlying application code.
