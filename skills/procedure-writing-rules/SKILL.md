---
name: procedure-writing-rules
description: "Write procedural text so a reader who was not there can execute it cold. Applies ASD-STE-100 (Simplified Technical English) to any numbered steps, runbook, deploy guide, access checklist, or the procedural sections of a SKILL.md. Use when authoring or editing instructions someone else will follow. Do NOT use for chat replies, analysis, outreach, marketing copy, commit messages, or PR descriptions."
---

# Procedure writing rules

Procedural text has one job: a reader who was not in the room executes it correctly on the first try. That reader is tired, is skimming, and does not share your context.

These rules come from **ASD-STE-100** (Simplified Technical English), maintained by the ASD Simplified Technical English Maintenance Group. It was built in 1986 for aircraft maintenance manuals, so that a mechanic could not misread a step. It is the right standard for a runbook and the wrong standard for anything you argue rather than execute.

## Scope

**Applies to:** numbered steps, runbooks, deploy guides, access checklists, migration instructions, incident procedures, agent-scaffolding templates, acceptance criteria phrased as actions, and the procedural sections of a SKILL.md.

**Does not apply to:** chat replies, analysis, strategy memos, customer-facing copy, outreach, commit messages, PR descriptions, or the reasoning sections of a planning doc. Those stay on your usual house style (and [`stop-slop`](https://github.com/hardikpandya/stop-slop), if you use it).

**Precedence.** Inside procedural text these rules **override** any terse house style. Articles are required and fragments are not permitted here, whatever the surrounding document does. A dropped article is a saved keystroke and a lost reader. Plain-prose rules still apply: no adverbs, no passive, no vague declaratives.

## The rules

1. **One instruction per sentence.** One step does one thing. If a step contains "and then," it is two steps.
2. **Start with the verb, in the imperative.** "Run the migration." Not "The migration should be run." Not "You will want to run the migration."
3. **20 words maximum per step.** 25 for a descriptive sentence. A longer sentence is a step you have not finished splitting.
4. **Use articles. Write complete sentences.** "Set the profile" beats "set profile."
5. **One word, one meaning. Never vary the term.** If the thing is `the pod`, it is `the pod` in every step. Elegant variation ("the container," "the instance," "the workload") makes the reader wonder whether you mean a fourth thing.
6. **No `-ing` forms** except inside a technical name. "Before you deploy," not "before deploying."
7. **No metaphor, no idiom, no analogy.** "Spin up," "kick off," "wire it to," "under the hood" all fail. Say what happens.
8. **Put the condition before the action.** "If the check fails, revert the tag." Not "Revert the tag if the check fails." The reader must know whether the step applies before they read the step.
9. **Put the warning before the step it guards**, never after. A caution below the command arrives too late to be a caution.
10. **Name the object every time. No pronouns across step boundaries.** "It" in step 4 refers to something the reader chose in step 2, and they no longer remember which.
11. **State the expected result.** Every step a reader can get wrong silently ends with what they should see. Without it there is no way to verify a step short of running the next one.
12. **Never leave a prohibition as a trailing fragment.** "Not on a schedule" reads as an aside. "Do not put it on a schedule" reads as a rule.

**We take the rules, not the dictionary.** Full STE also constrains vocabulary to about 900 approved words, enforced by a checker (HyperSTE, Congree, the TechScribe checker). We run no checker, so a vocabulary rule nothing verifies would just be decoration. Domain terms stay as they are: HMAC, dbt, Kubernetes, and every identifier are technical names, which full STE permits anyway.

## Before and after

**A build instruction** (from the [`product-thinking`](https://github.com/robertmnyborg/product-thinking) Self-Serve Build Route):

> Give Claude the Build Sheet and ask for a skill that executes the workflow once, for today's data — not on a schedule, not as a service.

becomes:

> Give the Build Sheet to Claude. Ask Claude for a skill that does the workflow one time, on the data of today. Do not put the skill on a schedule. Do not build the skill as a service.

The two prohibitions were trailing fragments after an em dash. A reader skims past those. As sentences they are rules.

**A publish step** (from a spec-writing skill):

> Publish to the wiki (on "publish"): `create_page` tool, `html` body. Space: ENG for handoffs, PRODUCT for product-led specs.

becomes:

> To publish, use the tool `create_page`. Set the body format to `html`. For an engineering handoff, use the space `ENG`. For a product-led spec, use the space `PRODUCT`.

The original compresses two independent choices into one comma. The reader must work out that the space depends on the spec type. The rewrite makes it a branch they cannot miss.

**A checklist step** (from `product-thinking`, step 3):

> From the steps, enumerate every system the workflow touches and build the access checklist — one row per system: what credential it needs · who grants it · verified yes/no.

becomes:

> List every system that the workflow touches. Write one row for each system. In each row, record the credential, the person who grants it, and whether you verified it.

The middle-dot list was formatting standing in for a sentence. It survives fine as a table. It does not survive as prose.

## What this costs

STE trades memorability for precision. A figurative line is usually the one a reader repeats back to you, and rule 7 deletes it. Accept that inside a procedure and refuse it everywhere else. A runbook nobody quotes is working correctly. A strategy memo nobody quotes is not.

Expect procedural text to get roughly 30 to 50 percent longer in word count and meaningfully faster to execute. Length is not the metric. First-try success is.

## Kill condition

Drop this skill if a sample of rewritten runbooks shows no reduction in clarifying questions or failed first runs after two months of use. Measure it with [`skill-eval`](https://github.com/robertmnyborg/skill-eval) against a procedure someone else has to execute.
