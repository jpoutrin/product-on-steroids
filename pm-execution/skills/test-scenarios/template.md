# Test Scenarios: <User Story Title>

## Overview

**User Story:** As a <role>, I want <goal>, so that <benefit>.

**Acceptance Criteria:**
1. <criterion 1>
2. <criterion 2>
3. <criterion 3>

**Scenarios generated:** <N> (including <M> edge/error cases)

---

## Test Scenarios

### Scenario 1: <Scenario Name>

**Test Objective:** <What this scenario validates — one sentence tied to a specific acceptance criterion.>

**Starting Conditions:**
- <System state or configuration required>
- <Data or records that must exist>
- <User account, permissions, or session state>

**User Role:** <Registered User | Admin | Guest | …>

**Test Steps:**
1. <Action> → <Expected result>
2. <Action> → <Expected result>
3. <Action> → <Expected result>
4. <Action> → <Final expected result>

**Expected Outcomes:**
- <Observable result 1 — binary pass/fail>
- <Observable result 2>
- <Observable result 3>

---

### Scenario 2: <Scenario Name>

**Test Objective:** <What this scenario validates.>

**Starting Conditions:**
- <System state>
- <Data setup>
- <Permissions>

**User Role:** <Role>

**Test Steps:**
1. <Action> → <Expected result>
2. <Action> → <Expected result>
3. <Action> → <Expected result>

**Expected Outcomes:**
- <Observable result 1>
- <Observable result 2>

---

### Scenario 3 (Edge Case): <Scenario Name>

**Test Objective:** <What edge or error condition is exercised.>

**Starting Conditions:**
- <Edge-case state — e.g., empty data set, invalid input, boundary value>
- <Any special configuration>

**User Role:** <Role>

**Test Steps:**
1. <Action> → <Expected result>
2. <Action> → <Expected result>

**Expected Outcomes:**
- <System behaviour under the edge condition>
- <Error message or fallback displayed, if applicable>

---

## Coverage Summary

| Acceptance Criterion | Scenario(s) | Gap |
|----------------------|-------------|-----|
| <Criterion 1> | Scenario 1 | — |
| <Criterion 2> | Scenario 2 | — |
| <Criterion 3> | Scenario 3 (edge) | <gap note if any> |
