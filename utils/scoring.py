def calculate_score(workflow, roi):

    score = 50

    if "manual" in workflow.lower():
        score += 15

    if "excel" in workflow.lower():
        score += 10

    if "error" in workflow.lower():
        score += 10

    if "automation" in roi.lower():
        score += 10


    return min(score,100)