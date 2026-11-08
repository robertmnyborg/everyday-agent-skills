---
name: tool-fit
description: Judge whether an external tool, repo, app, or service is worth using for the user. Use when the prompt is a GitHub or product URL plus "can I use this?", "what can this do for me?", "what can I do with this", "is this useful / valuable to my workflow", or "will it add value to my output".
---

# tool-fit

The user sends a link and asks whether it is worth their time. The answer is a verdict they can act on in one read, not a summary of the README.

## Procedure

1. Read the README, the license, the latest release or commit date, and the install requirements. Check that the requirements match this machine (`uname -a`, plus `sw_vers` on macOS) when it is a local install.
2. Find what it overlaps in the existing setup. Search the descriptions in `~/.claude/skills/*/SKILL.md`, the hooks in `~/.claude/settings.json`, the user's scripts directory if they keep one, and the MCP server list for the same job. Name the overlap, or say "no overlap" and what you searched.
3. If it runs code locally or calls the network, look at what it sends and where. Grep the source for endpoints when the repo is small enough to read.
4. Write the answer in the shape below.

## Answer shape

- **Verdict:** yes, no, or "only if <one condition>", in the first line. In the whole answer, name at most one thing that would make it worth trying, or one cheap test. Never a list of conditions.
- **What it is:** one or two sentences in plain words, with one concrete example of its use for the user's work.
- **Overlap:** what it duplicates or beats in the current setup, by name.
- **Checks:** license (personal use, and commercial use at the user's employer if it is for work), maturity (version, last commit, one maintainer or many), privacy (what leaves the machine).
- **Next step:** the install command or the one-line trial, only if the verdict is yes.

Do not install, sign up, or run the tool until the user says so.
