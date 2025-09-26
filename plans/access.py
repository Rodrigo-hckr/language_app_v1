from config import PLANS

def get_plan_features(plan_name):
    return PLANS.get(plan_name, PLANS["Gratis"])