# Updated Source Basis

## Current Source Of Truth

The latest updated-document set is based on the recovered backend in:

- `D:\LAB_Sheduling\updated backend`

Main source files used:

- `app/constants.py`
- `app/models.py`
- `app/store.py`
- `app/services/scheduling.py`
- `app/services/queue.py`
- `app/main.py`

## Current System Basis

- PHR remains the source of patient visit data and required tests
- frontend consumes overall visit state only
- backend stores per-test scheduling state
- updated backend is the active target backend
- scheduling uses emergency, arrival wait, dependency, movement protection, lab eligibility, and queue pressure

## Current Seed Shape

Recovered backend currently seeds:

- 6 specialists
- 6 labs
- 8 patient visits

## Current Queue Model

Each lab queue stores:

- `current`
- `next`
- `pending`
- `consecutive_pending_accepts`
