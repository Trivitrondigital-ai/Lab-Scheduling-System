# Updated All Diagrams

## 1. High-Level Architecture

```mermaid
flowchart LR
    PHR[PHR System] --> API[Updated Backend API]
    FE[Frontend UI] --> API
    API --> SCH[Scheduling Service]
    API --> QUE[Queue Service]
    API --> STORE[(State Store)]
    SCH --> STORE
    QUE --> STORE
    API --> FE
```

## 2. End-To-End Logic

```mermaid
flowchart TD
    A[PHR visit received] --> B[Read tests]
    B --> C[Apply priority, ordering, and movement logic]
    C --> D[Apply dependency logic]
    D --> E[Evaluate candidate labs]
    E --> F[Check active status, slot fit, and gender eligibility]
    F --> G[Rank by movement and queue pressure]
    G --> H[Assign lab or mark only failed test unschedulable]
    H --> I[Dispatch dependency-ready tests to queues]
    I --> J[Lab specialist queue actions]
    J --> K[Refresh scheduling state]
```

## 3. Queue Logic

```mermaid
flowchart TD
    A[Lab queue stack] --> B[current]
    A --> C[next]
    A --> D[pending]
    C --> E[accept-current]
    B --> F[complete-current]
    B --> G[move-current-to-pending]
    D --> H[accept-from-pending]
    H --> I[max 2 continuous pending accepts]
```

## 4. Data Flow

```mermaid
flowchart TD
    A[Visit Intake] --> B[Scheduling State]
    C[Lab and Specialist Setup] --> B
    B --> D[Queue State]
    D --> E[Lab Specialist Actions]
    E --> B
    B --> F[Frontend Bootstrap Output]
```

## 5. Current Notes

- backend keeps per-test state internally
- frontend consumes overall visit status only
- updated backend is the active backend target
- recovered seed data currently includes 8 patients
