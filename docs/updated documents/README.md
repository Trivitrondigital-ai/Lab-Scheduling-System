# Updated Documents

This folder contains the latest recovered documentation set for the current system.

## Files

- `01_UPDATED_SOURCE_BASIS.md`
- `02_UPDATED_LAB_CATEGORIES_AND_RULES.md`
- `03_UPDATED_SCHEDULING_LOGIC.md`
- `04_UPDATED_FLOWS_AND_DIAGRAMS.md`
- `05_UPDATED_SYSTEM_ARCHITECTURE_DIAGRAMS.md`
- `06_UPDATED_DATA_FLOW_DIAGRAMS.md`
- `07_UPDATED_ALL_DIAGRAMS.md`

## Current Run Commands

Updated backend:

```cmd
cd /d "d:\LAB_Sheduling\updated backend"
C:\Users\praju\miniconda3\Scripts\activate.bat
conda activate labqs
python -m uvicorn app.main:app --host 127.0.0.1 --port 8010 --reload
```

Frontend:

```cmd
cd /d "d:\LAB_Sheduling\Lab Scheduling System Design - Frontend"
npm run dev
```
