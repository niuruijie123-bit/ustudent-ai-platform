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

```mermaid
flowchart TD
    U[User / Browser] --> ALB[Application Load Balancer]

    ALB --> FE[Frontend<br/>React]
    ALB --> BE[Backend<br/>Spring Boot]
    ALB --> AI[AI Service<br/>FastAPI]

    BE --> DB[(PostgreSQL / Amazon RDS)]

    AI --> RAG[RAG / Handbook Retrieval]
    AI --> AGENT[Agent / Tool Calling]
    AGENT --> BE

    ECR[Amazon ECR] --> FE
    ECR --> BE
    ECR --> AI

    TF[Terraform] --> AWS[AWS Infrastructure]
