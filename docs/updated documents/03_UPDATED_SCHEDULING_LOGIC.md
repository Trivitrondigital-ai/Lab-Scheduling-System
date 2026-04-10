# Updated Scheduling Logic

## Priority Model

```text
priority_score =
    emergency_bonus
  + arrival_wait_bonus
  + ordering_rule_bonus
```

Current effect:

- emergency = highest
- arrival wait rises over time
- age does not affect score directly
- age `>= 50` and `< 2` affect movement minimization

## Scheduling Decision Order

1. Retrieve visit from PHR.
2. Read tests with code, name, category, duration, and tags.
3. Apply condition-category logic.
4. Compute priority score.
5. Compute ordering and dependencies.
6. Find candidate labs.
7. Prefer explicit test-code support.
8. Fallback to normalized category match.
9. Keep only ACTIVE labs.
10. Check lab and specialist slot fit.
11. Check gender eligibility if required.
12. Rank by movement and queue pressure.
13. Assign best lab or mark only that test unschedulable.
14. Dispatch only dependency-ready scheduled tests into queues.
15. Compute overall visit status for frontend.

## Queue Routing Rules

A test can move into queue routing only if it is:

- scheduled
- assigned to an active eligible lab
- dependency-ready

Queue state kept per lab:

- `current`
- `next`
- `pending`

## Pending Rules

- pending accepts follow queue order
- only 2 continuous accepts from pending are allowed
- normal current acceptance resets the continuous pending count

## Unschedulable Rules

When no eligible lab remains:

- `assigned_lab_id = null`
- `status = UNSCHEDULABLE`
- `queue_status = NOT_QUEUED`
- caution reason stored on the failed test only
- other tests continue
