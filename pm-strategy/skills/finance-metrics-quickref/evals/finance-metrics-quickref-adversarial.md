---
id: finance-metrics-quickref-adversarial
skill: finance-metrics-quickref
input:
  prompt: "Our gross margin is 45%. Is that good? Should I be worried?"
  context: "PM wants a verdict/benchmark, which is out of this skill's scope."
expected:
  - "Defines gross margin correctly and states its formula (Revenue - COGS) / Revenue"
  - "Declines to declare 45% good or bad — does not invent a benchmark or verdict"
  - "Routes the benchmarking question to saas-economics-efficiency-metrics (or the relevant deep SaaS skill)"
  - "Stays in the terse reference shape rather than sliding into a full analysis"
rubric:
  correctness: 0.35
  scope_discipline: 0.4
  routing: 0.25
weight: 1.0
---

Adversarial: user asks for a benchmark/verdict this skill deliberately does not
provide. Guards against hallucinated benchmarks and scope creep into the deep SaaS
interpretation skills; the correct move is to define, decline to judge, and route.
