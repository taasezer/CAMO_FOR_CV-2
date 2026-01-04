from fastapi import APIRouter
import random
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/summary")
def get_summary():
    """
    Returns high-level stats for the dashboard cards.
    """
    # In a real app, this would query the DB. 
    # For the demo, we simulate dynamic activity.
    now = datetime.now()
    base_count = 120 + (now.minute % 10)
    
    return {
        "today_packages": base_count,
        "throughput": f"{40 + random.randint(-5, 5)}/h",
        "pending": random.randint(2, 12),
        "efficiency": "98.2%"
    }

@router.get("/activity-graph")
def get_activity_graph():
    """
    Returns hourly package counts for the chart.
    """
    data = []
    start_hour = 8 # 8 AM
    current_hour = datetime.now().hour
    
    for h in range(start_hour, 19): # Up to 6 PM
        if h > current_hour:
            break
            
        count = random.randint(15, 60)
        # Simulate lunch break drop
        if h == 12: count = random.randint(5, 15)
        
        data.append({
            "time": f"{h}:00",
            "packages": count,
            "errors": random.randint(0, 3)
        })
        
    return data
