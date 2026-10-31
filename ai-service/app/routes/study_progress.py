from fastapi import APIRouter,Query


router = APIRouter()

@router.get("/study-progress")
def study_progress(earned_credits: int = Query(..., ge = 0)) -> dict:
    remaining = max(0, 120 - earned_credits)

    return {"earned_credits": earned_credits,
    "remaining_credits": remaining
    }