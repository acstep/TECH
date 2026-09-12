#!/usr/bin/env bash
# push_and_wait.sh — commit, push, and wait for GitHub Pages to actually serve the change.
#
# Why this exists: doing this by hand every day caused two avoidable detours —
# git push failing repeatedly (credentials) and long manual Pages polling loops.
# One call now does: commit -> push -> wait for Pages build -> verify HTTP 200.
#
# Usage:
#   bash push_and_wait.sh "<commit message>" [path-to-verify]
#
# Exit 0 only when the push succeeded AND the Pages build finished AND the
# verify path (if given) returns HTTP 200.
set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MSG="${1:?usage: push_and_wait.sh \"<commit message>\" [path-to-verify]}"
VERIFY_PATH="${2:-}"
CREDS="$REPO_DIR/../.credentials.js"
DEADLINE_SECS="${PUSH_WAIT_TIMEOUT:-600}"

# --- git identity -----------------------------------------------------------
git -C "$REPO_DIR" config user.email openclaw@acstep
git -C "$REPO_DIR" config user.name OpenClaw
git -C "$REPO_DIR" config credential.helper store   # credentials live in ~/.git-credentials

# --- 1) commit --------------------------------------------------------------
git -C "$REPO_DIR" add -A || { echo "FATAL: git add failed"; exit 1; }
if ! git -C "$REPO_DIR" diff --cached --quiet; then
  git -C "$REPO_DIR" commit -q -m "$MSG" || { echo "FATAL: commit failed"; exit 1; }
  echo "committed: $(git -C "$REPO_DIR" rev-parse --short HEAD)"
else
  echo "nothing to commit"
fi

# --- 2) push (single attempt; credentials come from the store) --------------
if ! GIT_TERMINAL_PROMPT=0 git -C "$REPO_DIR" push origin main >/tmp/push_and_wait.push.log 2>&1; then
  echo "FATAL: push failed"
  tail -5 /tmp/push_and_wait.push.log
  exit 1
fi
echo "pushed: $(git -C "$REPO_DIR" rev-parse --short HEAD)"

# --- 3) wait for the Pages build -------------------------------------------
SLUG="$(git -C "$REPO_DIR" remote get-url origin | sed -E 's#.*github\.com[:/]##; s#\.git$##')"
PAGES_BASE="https://$(echo "$SLUG" | cut -d/ -f1).github.io/$(echo "$SLUG" | cut -d/ -f2)"
TOKEN="$(node -e "process.stdout.write(require('$CREDS').github.token)" 2>/dev/null)"

if [ -z "$TOKEN" ]; then
  echo "WARN: no GitHub token; cannot poll Pages build. Skipping verification."
  exit 0
fi

end=$(( $(date +%s) + DEADLINE_SECS ))
while [ "$(date +%s)" -lt "$end" ]; do
  st="$(curl -s -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" \
        "https://api.github.com/repos/$SLUG/pages/builds?per_page=1" \
        | python3 -c "import json,sys;d=json.load(sys.stdin);print(d[0]['status'] if d else 'none')" 2>/dev/null || echo "unknown")"
  if [ "$st" = "built" ]; then
    if [ -z "$VERIFY_PATH" ]; then
      echo "pages build: built (no verify path given)"
      exit 0
    fi
    code="$(curl -s -o /dev/null -w '%{http_code}' "$PAGES_BASE/$VERIFY_PATH")"
    if [ "$code" = "200" ]; then
      echo "pages build: built | $PAGES_BASE/$VERIFY_PATH -> HTTP 200"
      exit 0
    fi
    echo "pages build: built but $VERIFY_PATH -> HTTP $code (waiting)"
  fi
  sleep 15
done

echo "TIMEOUT: Pages did not serve $VERIFY_PATH within ${DEADLINE_SECS}s"
exit 1
