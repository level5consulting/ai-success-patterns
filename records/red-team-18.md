# Red team - Pattern 18, Avoid the Naughty List (overnight, October 22-23, 2026)

Findings only - nothing applied. Greg makes the calls Friday (Morning Review form). Reviewed: patterns/18-avoid-the-naughty-list.md (with Greg's October 22 answers: Foundation; data in general; the Planview action-item-log example).

**Team (approved by Greg, October 22, 2026):**
- **Frank Kowalski (adversarial)** - data governance lead who has watched "AI will fix our data" projects corrupt records and won't let AI near production.
- **Joyce Lin** - analyst who sends the naughty list every month.
- **Raj Mehta** - data engineer who would write and run the scripts.
- **Diane Foster** - manager who receives the naughty list and resents it.

---

## Round 1 - Problem and Value

**Frank (adversarial):** The first two paragraphs are fair. Then you write "AI could change most of that." Most? You've sold me a magic fix in the fourth paragraph and only walk it back later. And "the audit takes hours, not weeks" in Value is a promise you can't keep - it depends on data volume and how many systems. Say what changes, not how fast.

**Joyce:** Your Planview example is the strongest thing on the page - audit reports turned into assigned actions with fix instructions, tracked in an action item log. Move it up. It's not a detour before "The truth is in between." It IS the answer, and AI makes it cheap.

**Diane:** "Owners get help, not a list" is the line I'd forward to my boss. But the Value section doesn't say the fix requests are short. The reason I ignore the naughty list is that it's 400 rows. Say: each owner sees only their records, a handful at a time.

**Raj:** "Problems stop coming back" is the real value, and it's buried fourth. Put it first or second - a cleanup that doesn't fix the cause is just next quarter's naughty list.

**Round 1 proposed changes:**
1. Replace "AI could change most of that" with something narrower: AI can take over the audit, the instructions, and the chasing - people still own the fix. (Frank)
2. Drop "hours, not weeks" from Value; describe what changes, not a speed claim. (Frank)
3. Move the Planview example up so it leads the "better way" paragraph. (Joyce)
4. In Value, say owners see only their own records, a few at a time - not a 400-row list. (Diane)
5. Move "Problems stop coming back" to the top two of Value. (Raj)

## Round 2 - Context and Solution (including "Use this pattern")

**Frank (adversarial):** Step 2, "audit a copy, not the live data" - good, but a copy of customer or HR data is still sensitive data, now sitting in an AI tool. Add: use an approved tool, and remove or mask personal data the audit doesn't need. Otherwise I'll block this whole pattern, and I should.

**Raj:** Step 3's scripts need a dry run that reports what would change before anything changes - a count and a sample. And a way to undo it. If I can't roll it back, I'm not running it.

**Joyce:** Step 4 turned the naughty list into an action item log - good. Give it an owner and a due date per action, and a way to see what's overdue. That's what made it work at Planview: nobody had to chase, because the log did.

**Diane:** The "Use this pattern" prompt drafts notes to owners. Tell it to keep them short and polite, and to say why the fix matters. I fix things faster when I know who's waiting on them.

**Frank (adversarial), on Step 1:** "Write down what good looks like" - and agree it with the owners first. If the rules come from the data team alone, every finding becomes an argument.

**Round 2 proposed changes:**
6. Step 2: use an approved tool, and remove or mask personal data the audit doesn't need. (Frank)
7. Step 3: every script does a dry run first (what would change - a count and a sample) and has a way to undo. (Raj)
8. Step 4: each action has an owner and a due date, and the log shows what's overdue - the log does the chasing. (Joyce)
9. Use this pattern: owner notes stay short and polite, and say why the fix matters. (Diane)
10. Step 1: agree the rules with the data owners before the audit, not after. (Frank)
