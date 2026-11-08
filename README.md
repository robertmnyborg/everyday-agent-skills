# everyday-agent-skills

Four small Claude Code skills for daily work: writing steps someone else can follow, judging a tool before you adopt it, decoding a confusing Slack message, and reading Reddit and X without risk of posting.

## Install

```bash
git clone https://github.com/robertmnyborg/everyday-agent-skills
cp -R everyday-agent-skills/skills/* ~/.claude/skills/
```

For `social-research`, also install the guard hook:

```bash
cp everyday-agent-skills/hooks/opencli-readonly-guard.py ~/.claude/hooks/
```

Then register it in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "python3 ~/.claude/hooks/opencli-readonly-guard.py" }]
      }
    ]
  }
}
```

Run `bash tests/opencli-readonly-guard.test.sh` to check the hook.

## procedure-writing-rules

**Failure it prevents:** a runbook or set of steps that only works for the person who wrote it.

**How:** applies 12 rules from ASD-STE-100 (Simplified Technical English, written for aircraft maintenance manuals) to procedural text only: one instruction per sentence, verb first, condition before action, warning before the step, no pronouns across steps, and an expected result for every step that can fail silently. It includes before-and-after rewrites and says where the rules do not apply (chat, analysis, marketing copy).

## tool-fit

**Failure it prevents:** a link to a new repo or product answered with a README summary instead of a decision.

**How:** reads the README, license, last release, and requirements; searches your existing skills, hooks, and MCP servers for overlap; checks what leaves the machine. The answer opens with yes, no, or "only if one condition", and nothing gets installed until you say so.

## explain-message

**Failure it prevents:** a Slack message in someone else's shorthand that you reply to without understanding.

**How:** reads the full thread and up to 3 linked items, then answers in a fixed shape: what they are asking you, what it says in plain words, one concrete example, your call, and a draft reply. A final check rewrites any sentence that still holds a term you did not use.

## social-research

**Failure it prevents:** research on Reddit and X that accidentally posts, likes, or replies as you, or that quotes a snippet without the thread behind it.

**How:** uses [OpenCLI](https://github.com/jackwener/opencli) against your logged-in Chrome, read-only. The bundled hook allows only read verbs on reddit and twitter and blocks everything else, including other sites and generic browser clicks. The skill runs several phrasings, opens the top threads, and quotes verbatim with permalink, author, and date.

Requirements: Claude Code; Python 3 for the hook; OpenCLI and a logged-in Chrome for `social-research`; a Slack MCP or connector for `explain-message` (it also works from a pasted message).

## License

MIT
