<!-- EMAIL-MIGRATION-NOTE -->
## ⚠️ Verify & clean up email migration (2026-07-08)

Commit history on `main` was rewritten to reattribute all commits to the GitHub
noreply email `30530199+alexsmedile@users.noreply.github.com` (was: personal /
machine-hostname emails). Author + committer dates and file content are preserved.

**Before continuing work, verify:**
- [ ] GitHub shows commits linked to your profile, original dates intact
- [ ] Local `main` matches `origin/main` (`git fetch && git log origin/main -1`)
- [ ] Your in-progress working-tree changes are still present and correct

**Backup:** original pre-rewrite history is on the local branch
`backup/pre-email-rewrite`. Once you've confirmed everything is fine:
`git branch -D backup/pre-email-rewrite`

**Note:** `main` was force-pushed — existing clones/forks have diverged.
Unmerged side branches (if any) still carry the old email; rewrite them only if resurrected.

---

