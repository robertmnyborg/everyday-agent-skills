#!/usr/bin/env bash
# Usage: bash tests/opencli-readonly-guard.test.sh
set -u
HOOK="$(cd "$(dirname "$0")/.." && pwd)/hooks/opencli-readonly-guard.py"
pass=0; fail=0

check() { # expected_exit command
  local want="$1" cmd="$2" got
  printf '%s' "$cmd" | python3 -c 'import json,sys; print(json.dumps({"tool_input":{"command":sys.stdin.read()}}))' \
    | python3 "$HOOK" 2>/dev/null
  got=$?
  if [ "$got" = "$want" ]; then pass=$((pass+1)); else fail=$((fail+1)); echo "FAIL (want $want, got $got): $cmd"; fi
}

check 0 'opencli reddit search "tool reviews" --limit 10'
check 0 'opencli --profile personal twitter search "ai agents" --limit 20'
check 0 'opencli doctor'
check 0 'opencli profile list'
check 0 'grep -n opencli ~/.claude/settings.json'
check 0 'echo "opencli twitter post hi"'
check 0 'ls && opencli reddit read abc123 --depth 2'
check 2 'opencli twitter post "hi"'
check 2 'opencli reddit comment t3_abc "x"'
check 2 'opencli linkedin search foo'
check 2 'opencli browser s1 click 3'
check 2 'ls; opencli twitter like 123'
check 2 'env FOO=1 opencli twitter reply 123 "x"'
check 2 '/usr/local/bin/opencli reddit upvote abc'

echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
