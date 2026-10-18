# genpark-agentic-supply-chain-bullwhip-dampener-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

AI Supply Chain & Commerce Bullwhip Effect Dampener. Applies safety stock PID dampening, order surge smoothing, and lead-time demand volatility filtering to eliminate inventory whipsawing across multi-tier supplier networks.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
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

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
