# Secure Agent Service

**Open-source, self-hosted secure AI agent runtime** built with FastAPI, LangGraph, and Arcade.dev.

This service allows developers to run multi-user AI agents that can safely interact with external tools (Gmail, Slack, Notion, and more) on behalf of end-users — with proper authentication and Human-in-the-Loop (HITL) safety controls.

> **Status**: Early stage / Work in progress  
> Designed for self-hosting. No hosted SaaS version is provided.

---

## What is this?

Secure Agent Service is a backend API that solves one of the hardest problems in building production AI agents:

> How do you let an AI agent act on real user accounts (email, Slack, Notion, etc.) **securely**, for **many users**, without building complex OAuth flows and safety systems yourself?

This project gives you a ready-to-run foundation that handles:

- Multi-user isolation
- Secure tool authentication via [Arcade.dev](https://arcade.dev)
- Agent orchestration with [LangGraph](https://langchain-ai.github.io/langgraph/)
- Human-in-the-Loop approval for sensitive actions (send email, post to Slack, create Notion pages, etc.)

You run the service yourself. Your application talks to it via HTTP APIs.

---

## Key Features

- **Self-hosted** — full control over data and infrastructure
- **Multi-user support** — each end-user has isolated tool access
- **Secure tool calling** powered by Arcade.dev (Gmail, Slack, Notion, and more)
- **Human-in-the-Loop (HITL)** — agents must request approval before executing risky actions
- **Conversation memory** using LangGraph threads + persistent checkpointer
- **Clean FastAPI architecture** with SQLAlchemy, Alembic, and proper project structure
- Designed to be extended with more tools and providers

---

## Problem It Solves

Building agents that can *actually do things* for real users is difficult because of:

- Complex OAuth flows for every tool
- Token management and security risks
- Lack of user isolation
- No built-in safety for irreversible actions

This project provides a clean, reusable backend so you don’t have to solve these problems from scratch.

---

## Tech Stack

| Layer              | Technology                      |
|--------------------|---------------------------------|
| API Framework      | FastAPI                         |
| Agent Orchestration| LangGraph + langchain-arcade    |
| Tool Authentication| Arcade.dev                      |
| Database           | PostgreSQL + SQLAlchemy 2.0     |
| Migrations         | Alembic                         |
| Configuration      | pydantic-settings               |
| Testing            | pytest                          |
| Packaging          | pyproject.toml                  |

---

## Project Structure

```text
secure-agent-service/
├── app/
│   ├── api/           # FastAPI routers
│   ├── agents/        # LangGraph agent logic
│   ├── arcade/        # Arcade client & tool management
│   ├── core/          # Config, security, exceptions
│   ├── db/            # Database session
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   └── main.py
├── alembic/           # Database migrations
├── tests/
├── .env.example
├── docker-compose.yml
├── pyproject.toml
└── README.md