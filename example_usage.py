from client import AgenticSupplyChainBullwhipDampener

def main():
    dampener = AgenticSupplyChainBullwhipDampener()
    orders = [45, 50, 48, 52, 49, 120]
    res = dampener.compute_dampened_reorder_quantity("SKU-9901-PREMIUM", current_inventory=110, recent_order_history=orders, lead_time_days=7)
    print("--- Supply Chain Bullwhip Dampener ---")
    print(f"SKU: {res['sku_id']} | Surge Ratio: {res['surge_ratio_detected']}x")
    print(f"Damping Factor Applied: {res['bullwhip_damping_factor']}")
    print(f"Recommended Replenishment: {res['recommended_order_units']} units")

if __name__ == "__main__":
    main()
