# utils/score_calc.py
def calculate_influence_score(cred, longevity, engagement):
    score = (cred * 0.4) + (longevity * 0.3) + (engagement * 0.3)
    return round(score, 2)
