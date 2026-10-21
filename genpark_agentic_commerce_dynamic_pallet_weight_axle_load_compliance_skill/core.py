# -*- coding: utf-8 -*-
"""Commerce Freight Axle Load Compliance Optimizer for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class FreightAxleLoadComplianceOptimizer:
    @staticmethod
    def audit_semi_truck_axle_weights(steer_axle_lbs: float, drive_axle_lbs: float, tandem_trailer_axle_lbs: float) -> Dict[str, Any]:
        gross = steer_axle_lbs + drive_axle_lbs + tandem_trailer_axle_lbs
        violations = []
        if steer_axle_lbs > 12000: violations.append("OVERWEIGHT_STEER_AXLE (>12,000 lbs)")
        if drive_axle_lbs > 34000: violations.append("OVERWEIGHT_DRIVE_AXLE (>34,000 lbs)")
        if tandem_trailer_axle_lbs > 34000: violations.append("OVERWEIGHT_TANDEM_AXLE (>34,000 lbs)")
        if gross > 80000: violations.append("OVERWEIGHT_GROSS_GVWR (>80,000 lbs)")
        is_legal = len(violations) == 0
        return {"gross_weight_lbs": gross, "is_dot_compliant": is_legal, "violations": violations, "scale_verdict": "SCALE_PASS" if is_legal else "SCALE_FAIL_FINE_RISK"}

    @staticmethod
    def calculate_tandem_slider_pin_adjustment(overweight_axle: str, excess_weight_lbs: float) -> Dict[str, Any]:
        # Rule of thumb: 1 pin hole shift rebalances ~250-400 lbs
        holes = max(1, int(excess_weight_lbs // 350))
        direction = "SLIDE_TANDEMS_FORWARD" if overweight_axle == "TANDEM" else "SLIDE_TANDEMS_BACKWARD"
        return {"overweight_axle": overweight_axle, "excess_lbs": excess_weight_lbs, "pin_holes_to_slide": holes, "slide_direction": direction}
