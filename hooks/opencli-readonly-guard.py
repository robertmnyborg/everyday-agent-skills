#!/usr/bin/env python3
"""opencli-readonly-guard: Claude Code PreToolUse hook for the Bash tool.

WHY
OpenCLI drives your logged-in Chrome. Its reddit and twitter adapters include
writes (post, reply, comment, upvote, like, follow, delete, DM) next to the
reads used for research. A write posts publicly as you and cannot be taken
back, so the guard is code, not a line in a skill.

PREDICATE (an allowlist, not a denylist)
Every `opencli` invocation in the command must be one of:
  - a meta command: doctor, list, --version, --help, profile list|use|rename
  - reddit  <READ verb>  (see REDDIT_READ)
  - twitter <READ verb>  (see TWITTER_READ)
Anything else is denied: other sites, `opencli browser` (generic clicking),
plugin or adapter installs, and every write verb. New upstream verbs stay
blocked until you add them here by hand.

`opencli` only counts in command position (start of the command, or after
; && || | or a leading `env`/`sudo`/`command`), so `grep opencli file` passes.

A false block costs one edit to this file; a missed write is a public post.
Run tests/opencli-readonly-guard.test.sh after any change.
"""
import json
import re
import shlex
import sys

REDDIT_READ = {"hot", "frontpage", "popular", "search", "subreddit", "read",
               "user", "user-posts", "user-comments"}
TWITTER_READ = {"trending", "search", "timeline", "tweets", "lists",
                "list-tweets", "profile", "article", "thread", "followers",
                "following"}
META = {"doctor", "list", "--version", "-V", "--help", "-h"}
VALUE_FLAGS = {"--profile", "--window", "--site-session", "-f", "--format"}
SEPARATORS = {";", "&&", "||", "|", "&"}
PREFIXES = {"env", "sudo", "command", "exec", "time", "nohup"}


def verdict(args):
    """Return None if allowed, else the blocked command."""
    i = 0
    while i < len(args) and args[i].startswith("-") and args[i] not in META:
        i += 2 if args[i] in VALUE_FLAGS else 1
    rest = args[i:]
    if not rest:
        return None
    head = rest[0]
    if head in META:
        return None
    if head == "profile" and len(rest) > 1 and rest[1] in {"list", "use", "rename"}:
        return None
    verb = rest[1] if len(rest) > 1 else ""
    if head == "reddit" and verb in REDDIT_READ:
        return None
    if head == "twitter" and verb in TWITTER_READ:
        return None
    return f"`opencli {head} {verb}`".replace(" `", "`").strip()


def split_tokens(cmd):
    # Pad separators so shlex sees them as their own tokens.
    padded = re.sub(r"(\|\||&&|[;|&])", r" \1 ", cmd)
    try:
        return shlex.split(padded, posix=True)
    except ValueError:
        return padded.split()


def blocked_calls(cmd):
    tokens = split_tokens(cmd)
    blocked = []
    at_start = True
    for idx, tok in enumerate(tokens):
        if tok in SEPARATORS:
            at_start = True
            continue
        if at_start and (tok in PREFIXES or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", tok)):
            continue  # still in command position
        if at_start and re.fullmatch(r"(.*/)?opencli", tok):
            seg = []
            for t in tokens[idx + 1:]:
                if t in SEPARATORS:
                    break
                seg.append(t)
            reason = verdict(seg)
            if reason:
                blocked.append(reason)
        at_start = False
    return blocked


def main():
    cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    if "opencli" not in cmd:
        return 0
    blocked = blocked_calls(cmd)
    if not blocked:
        return 0
    print(f"""BLOCKED by opencli-readonly-guard: {', '.join(blocked)} is not on the read-only allowlist.

OpenCLI runs inside your logged-in Chrome, so any write posts publicly as you.
Research use is limited to:
  reddit:  {' '.join(sorted(REDDIT_READ))}
  twitter: {' '.join(sorted(TWITTER_READ))}
Other sites and `opencli browser` are blocked. If you want a write, run it
yourself (in Claude Code: `! opencli ...`).""", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
