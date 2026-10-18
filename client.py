"""
AI Supply Chain Bullwhip Effect Dampener (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import math
from typing import Dict, Any, List, Optional

class AgenticSupplyChainBullwhipDampener:
    def __init__(self, dampener_name: str = "GenPark-Bullwhip-Dampener"):
        self.dampener_name = dampener_name

    def compute_dampened_reorder_quantity(
        self,
        sku_id: str,
        current_inventory: int,
        recent_order_history: List[int],
        lead_time_days: int = 7,
        target_service_level_z: float = 1.65
    ) -> Dict[str, Any]:
        if not recent_order_history:
            return {"sku_id": sku_id, "recommended_order_units": 0, "verdict": "EMPTY_HISTORY"}
            
        n = len(recent_order_history)
        avg_daily_demand = sum(recent_order_history) / n
        
        # Standard deviation of demand
        variance = sum((x - avg_daily_demand) ** 2 for x in recent_order_history) / max(1, n - 1)
        std_daily_demand = math.sqrt(variance)
        
        # Lead time demand & Safety Stock
        lead_time_demand = avg_daily_demand * lead_time_days
        safety_stock = target_service_level_z * std_daily_demand * math.sqrt(lead_time_days)
        target_stock_level = lead_time_demand + safety_stock
        
        raw_order_deficit = target_stock_level - current_inventory
        
        # Bullwhip dampening: exponential smoothing filter (alpha=0.6) on surge spikes
        latest_demand = recent_order_history[-1]
        surge_ratio = latest_demand / max(1.0, avg_daily_demand)
        
        damping_factor = 1.0
        if surge_ratio > 1.8:
            # Dampen spike by 35% to prevent upstream over-ordering panic
            damping_factor = 0.65
        elif surge_ratio < 0.5:
            damping_factor = 1.15
            
        final_dampened_order = max(0, int(math.ceil(raw_order_deficit * damping_factor)))
        
        return {
            "dampener": self.dampener_name,
            "sku_id": sku_id,
            "current_inventory": current_inventory,
            "average_daily_demand": round(avg_daily_demand, 2),
            "safety_stock_units": int(math.ceil(safety_stock)),
            "target_stock_level": int(math.ceil(target_stock_level)),
            "surge_ratio_detected": round(surge_ratio, 2),
            "bullwhip_damping_factor": damping_factor,
            "recommended_order_units": final_dampened_order,
            "verdict": "DAMPENED_REORDER_CALCULATED"
        }
