---
id: gtm-motions-edge
skill: gtm-motions
input:
  prompt: "Design GTM motions for a developer-focused API platform with a hybrid market."
  context: "ACV: $500–$5k (SMB self-serve tier at $500/mo; enterprise tier at $5k+/mo). Sales cycle: 2 weeks (SMB), 8 weeks (enterprise). Product: low onboarding friction for SMBs, complex integration for enterprise. Addressable: 50k SMBs + 500 enterprise targets. Team: 2 engineers, 1 growth lead. Existing traction: 100 free trial signups, 20 paying SMBs, 2 enterprise pilots. Strong developer community presence (GitHub)."
expected:
  - "Product profile is captured with nuanced ACV/cycle split (SMB vs enterprise)"
  - "Motion stack acknowledges the hybrid market (not one-size-fits-all); e.g., PLG for SMB tier + ABM/Outbound for enterprise"
  - "Scoring reflects SMB and enterprise trade-offs (e.g., PLG high for SMB, lower for enterprise)"
  - "Secondary motion (community, partner ecosystem) is evaluated for developer audience and network effects"
  - "Playbooks are differentiated per segment/motion (SMB free-trial flow vs enterprise ABM sprint)"
  - "Buyer journey mapping recognizes different paths for SMB (self-serve) and enterprise (sales-led decision)"
  - "Assumptions acknowledge the challenge of dual-segment execution (team/budget constraints)"
rubric:
  correctness: 0.3
  completeness: 0.25
  hybrid_motion_reasoning: 0.25
  segment_differentiation: 0.2
weight: 1.0
---

Edge case: hybrid motion scenario (SMB/enterprise split, developer audience) requiring careful segmentation and trade-off reasoning. Guards against assuming a single motion fits all segments and ensures the skill can handle conflicting constraints (low ACV + high ACV, self-serve + complex).

