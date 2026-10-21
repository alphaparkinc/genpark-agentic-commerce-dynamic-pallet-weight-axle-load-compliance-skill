# Commerce Freight Axle Load & GVWR Compliance Optimizer Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

DOT gross vehicle weight rating (GVWR) & semi-truck steer/drive/tandem axle distribution compliance optimizer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `audit_semi_truck_axle_weights`: Audit steer, drive, and trailer tandem axle weights against federal bridge formula limits (12k/34k/34k lbs).
- `calculate_tandem_slider_pin_adjustment`: Calculate trailer tandem slider hole shift needed to rebalance weight from drive to tandem axles.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_dynamic_pallet_weight_axle_load_compliance_skill.server --test
```
