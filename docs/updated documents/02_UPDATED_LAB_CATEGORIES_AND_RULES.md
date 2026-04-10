# Updated Lab Categories And Rules

## Current Lab Categories

- Electrocardiogram (ECG)
- Ultrasound Scan
- Urine Examination (Input Condition: Bladder needs to be full)
- Blood Test (Includes all Pathology, Biochemistry, Hematology, Immunology, and Genetics)
- Ophthalmology Examination
- Pure Tone Audiometry

## Current Core Rules

- emergency is highest priority
- arrival wait increases over time
- age does not increase priority
- age `>= 50` and `< 2` increase floor-movement protection
- explicit test-code support is primary
- normalized category fallback is secondary
- only ACTIVE labs are eligible
- selected lab must fit within lab time and specialist shift time
- female-only patient or specialist conditions are enforced where required
- only the failed test is marked unschedulable

## Current Dependency Rules

- ECG before TMT if both exist
- Ultrasound before urine-related tests

## Current Ordering Hints

- `FULL_BLADDER` moves earlier
- `Strict Fasting Blood` moves earlier
- `PREFERRED_LAST` moves later where feasible

## Current Specialist Logic

Specialist logic uses only:

- name
- gender
- shift start
- shift end
