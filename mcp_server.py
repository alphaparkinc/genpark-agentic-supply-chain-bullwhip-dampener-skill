#!/usr/bin/env python3
import json
import sys
from client import AgenticSupplyChainBullwhipDampener

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        dampener = AgenticSupplyChainBullwhipDampener()
        history = [20, 22, 19, 21, 25, 23, 60]  # surge spike on day 7
        res = dampener.compute_dampened_reorder_quantity("SKU-LOGIX-88", 40, history, lead_time_days=5)
        assert res["surge_ratio_detected"] > 1.5
        assert res["bullwhip_damping_factor"] == 0.65
        assert res["recommended_order_units"] > 0
        print(f"[TEST PASS] Bullwhip Dampener Units: {res['recommended_order_units']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-bullwhip-dampener", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "compute_dampened_reorder_quantity", "description": "Dampen supply chain bullwhip spikes for optimal procurement"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                dampener = AgenticSupplyChainBullwhipDampener()
                out = dampener.compute_dampened_reorder_quantity(
                    args.get("sku_id", "SKU-UNKNOWN"),
                    int(args.get("current_inventory", 0)),
                    args.get("recent_order_history", []),
                    int(args.get("lead_time_days", 7)),
                    float(args.get("target_service_level_z", 1.65))
                )
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
