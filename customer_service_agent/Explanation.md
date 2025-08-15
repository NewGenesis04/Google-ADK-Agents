
# Explanation of the Customer Service Agent

This document breaks down the structure and functionality of the `customer_service_agent`, a multi-agent system built using the Google Agent Development Kit.

## High-Level Overview

The `customer_service_agent` is designed to act as a primary point of contact for a customer. It's a "root agent" that intelligently routes user queries to a set of specialized "sub-agents." Each sub-agent is an expert in a specific domain (e.g., sales, support, policies). This architecture allows for a modular and scalable customer service solution.

## File Breakdown

-   **`main.py`**: This is the entry point for the application. It sets up the environment, initializes the session, and runs the main conversation loop. It's responsible for handling user input and orchestrating the interaction with the agent system.

-   **`agent.py`**: This file defines the primary `customer_service_agent`. This agent doesn't have many tools of its own. Its main purpose is to understand the user's intent and delegate the task to the appropriate sub-agent. It holds the definitions for all the sub-agents.

-   **`utils.py`**: A collection of helper functions used throughout the application. These include functions for managing the `interaction_histo ry` within the session state, displaying the current state for debugging purposes, and formatting the terminal output for better readability.

-   **`sub_agents/`**: This directory houses the specialized agents. Each sub-agent is defined in its own file and has a specific role.

## The Agent Hierarchy

The system uses a hierarchical agent structure.

### `customer_service_agent` (The Root Agent)

-   **Role**: To a  ct as a receptionist and dispatcher.
-   **Functionality**: It analyzes the user's query and determines which specialized sub-agent is best equipped to handle it. It maintains the shared state of the conversation, including user information, purchase history, and a log of all interactions.

### Sub-Agents (The Specialists)

1.  **`policy_agent`**:
    -   **Purpose**: To answer questions about the community guidelines, course policies, refund policies, and privacy policies.
    -   **Tools**: None. It's a knowledge-based agent.

2.  **`sales_agent`**:
    -   **Purpose**: To handle all inquiries related to purchasing courses.
    -   **Tools**:
        -   `purchase_course`: A tool that simulates the purchase of a course and updates the session state to reflect the new purchase.

3.  **`course_support_agent`**:
    -   **Purpose**: To provide assistance with the content of courses that the user has already purchased.
    -   **Tools**: None. It references the `purchased_courses` in the state to verify ownership before providing support.

4.  **`order_agent`**:
    -   **Purpose**: To manage a user's purchase history and handle refund requests.
    -   **Tools**:
        -   `refund_course`: A tool that processes a course refund and updates the session state by removing the course from the `purchased_courses` list.
        -   `get_current_time`: A simple tool to fetch the current time, which can be used for timestamping transactions.

## State Management

The session state is a critical component of this system. It's a Python dictionary that is passed to every agent in the hierarchy. This allows the agents to have context about the user and the conversation.

-   **`initial_state`**: Defined in `main.py`, it sets up the default state for a new user session.
-   **Key State Variables**:
    -   `user_name`: The name of the user.
    -   `purchased_courses`: A list of courses the user has purchased. This is modified by the `sales_agent` and `order_agent`.
    -   `interaction_history`: A log of all interactions between the user and the agents.

## How It Works: The Conversation Flow

1.  A user starts the application by running `main.py`.
2.  A new session is created with an initial state.
3.  The user types a query (e.g., "How do I buy the course?").
4.  The `customer_service_agent` receives this query.
5.  The root agent's underlying model determines that this is a sales-related question and delegates the task to the `sales_agent`.
6.  The `sales_agent` engages with the user. If the user decides to purchase, the `purchase_course` tool is triggered.
7.  The `purchase_course` tool updates the `purchased_courses` list in the session state.
8.  The `sales_agent` provides a confirmation message to the user.
9.  The `interaction_history` is updated with the details of this transaction.
10. The conversation continues, with the root agent always ready to route the next query to the appropriate specialist.
