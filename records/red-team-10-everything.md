# Red team - Models Are Not Good at Everything (November 9-10, 2026)

Findings only - nothing applied. Greg decides each item in the Morning Review form. Reviewed: patterns/10-models-are-not-good-at-everything.md (draft 1, overnight November 9-10). Web address stays patterns/10-models-are-not-good-at-math.html.

**Team (proposed with the AI Reads, Tools Copy draft, November 4; approved by Greg for this combined pattern, November 5, 2026). All four are fictional reviewers:**
- **Nina Sorensen (adversarial)** - data engineer: "this is a model limit that will go away, and people won't write queries."
- **Marcus Hale** - finance manager who moves data between systems every month-end.
- **Joy Adeyemi** - paralegal who quotes contracts and checks citations.
- **Pete Lindgren** - small-business owner who only has Excel.

---

## Round 1 - Problem, Value and Context

**Nina (adversarial):** You've written a list of things models are bad at, dated today, on a page that will live for years. Half the tools I use already run code for arithmetic. "Not good at math" is less true every quarter, and a reader who just watched their assistant run a Python cell will decide the whole page is out of date. The Notes say "some now run code on their own" - that's buried. Say it in the math step: if the AI ran code, ask to see the code and the inputs, and that counts as the fix. And the long-documents research is from 2023, published 2024. Models built for long context have moved since. Present it as a research finding with its date, and lean on the practice argument - "ask where in the document the answer is, and go read it" holds no matter what. Put a "list checked" date on the weak spots so a stale list looks maintained, not ignorant.

**Marcus:** The analyst story is my month. That's the opener I'd forward to my team. Two things. First, "prove the copy" should say totals tie out to the source - that's the word my people use, and it's the check the analyst in the story skipped. Second, I do this every month. The page says the formula is reusable in Value but never tells me to save it. Save the formula, the query, the steps - next month you rerun them instead of asking the AI again and getting a slightly different one. Value line is fine: "part of a financial analyst's job" is honest. Don't let anyone edit it into "replaces an analyst."

**Joy:** The citations section is the one I'd use, and it's close. The Stanford CIS number needs care. "About 90% came from solo or small firms" says where the filings came from, not that small firms are worse with AI - big firms have more people checking. Keep the sentence exactly as the source states it and don't add a reason. On regulatory: "a qualified person" is right, but readers will ask "qualified how?" The draft lists compliance officer, attorney, accountant, licensed professional - good - but "check the official source for the right place and the current date" should say "the version in force on the date that matters," because for us the date of the contract can matter more than today. And Step 5's last line - "Asking the AI whether its own source is real is not a check" - is the most useful sentence on the page. Move it up.

**Pete:** It's long. Five weak spots, seven steps, a table, a prompt. I'd read the lead and the table and stop. Put the table right under the lead, before the analyst story, so I get the whole thing in ten seconds. "Script," "query" and "export" - I know a filter and copy and paste. The draft says "if you don't know how, have the AI tell you the steps," which saves it, but say it in the table too. And the $103,570 analyst means nothing to me. I'd never hire one. I'd hire a bookkeeper, and my accountant is my "qualified person." If the Value line is going to be about roles, give me one I'd actually pay for.

**Round 1 proposed changes:**
1. Solution: move the weak-spot table up to sit right under the lead (before the Problem's story), and add "AI can tell you the steps" to the copying row. (Pete)
   - Proposed table row text: "Copying exact data | Rows changed, swapped or missing | AI reads, your tools copy (filter, copy and paste - the AI can tell you the steps); check the totals"
2. Step 2 (math): add "If your AI tool runs code itself, ask to see the code and the inputs. That counts - it's the pattern working." And put a "Weak spots list checked: November 2026" line under the table. (Nina, adversarial)
3. Problem, long documents: frame as a dated research finding and lead with the fix that holds regardless. Proposed text: "In 2024, researchers found that models did best when the key information was at the start or end of a long input, and much worse when it was in the middle (Liu et al., \"Lost in the Middle\"). Models have improved since; the habit still holds - ask where the answer is, and go read that page." (Nina, adversarial)
4. Step 3 (copying) and Measure it: say the totals "tie out" to the source, and add "Save the formula, query or steps. Next month, rerun them - don't ask the AI again." (Marcus)

## Round 2 - Solution and Use this pattern

**Nina (adversarial):** The prompt says "Never present a number you predicted as a number you calculated." Fine. But you're asking the same model to police itself on exactly the weak spots it can't see. The botwatch in Phase 4 lists what to check - good - but it should say the checker is a person or a fresh model, not this chat. Your own Judge the Outcome pattern says that. Use it.

**Marcus:** Step 7, "Do the botwatch, then ship," is the step I'd tape to my monitor. But "ideally someone who didn't produce it" - at month-end it's me and one other person. Say what to do when there is no one else: a fresh chat or a different model, pointed at the saved work, asked what's wrong with it. Then a person still signs.

**Joy:** Step 4 should not stop at "a qualified person signs off." Before that person sees it, the team should already have been challenged. That's Assemble the Team - this week's theme - and it's only a connection in Notes. In regulatory work it's the obvious move: run the draft past a compliance voice, an auditor voice and the person who has to live with the rule, then take the questions to your real expert. It saves the expert's time and it's where the botwatch starts. Also, Step 5: the quote check and the citation check are separate. A real case can be quoted wrong. Say "open it, find the passage, and compare the quote word for word."

**Pete:** The prompt is good - I'd paste that. But "regulatory" scared me off at first; for me it's sales tax and payroll. One example in Step 4 in plain words and I'd see myself in it.

**Round 2 proposed changes:**
5. Step 4 (regulatory): add Assemble the Team before the real sign-off, and a plain example. Proposed text: "Before it goes to your expert, run Assemble the Team on it - a compliance voice, an auditor, and the person who has to live with the rule - and take their questions with you. Your expert's time goes further. Whether it's a privacy rule, an industry standard or your sales tax, the version in force on the date that matters is the one that counts." (Joy, Pete; theme)
6. Step 7 (botwatch) and prompt Phase 4: when no second person is available, use a fresh chat or a different model pointed at the saved work and asked what's wrong with it - and a person still signs. Proposed Phase 4 line: "Name the independent check: a person who didn't produce the work, or a fresh chat or different model pointed at the saved work and asked what's wrong with it. This chat is not the check." (Nina, adversarial; Marcus)
7. Step 5 (citations): move "Asking the AI whether its own source is real is not a check" to the first sentence of the step, and add "A real source can still be quoted wrong - compare the quote word for word." Keep the Stanford CIS sentence exactly as the source states it, with no added reason. (Joy)

## Round 3 - Fit with Greg's priorities and housekeeping

**Strings, not singles (flag):** The string is stated in the Solution and Notes ("calculate with code, copy with tools, review independently"), but not in the lead. A reader who stops at the lead - Pete - sees a list, not a string. And with AI Reads, Tools Copy folded in, readers will ask whether it's still a separate pattern: the draft treats it as a named step inside this one, which is consistent with the string but should be said plainly once.

**This week's theme, Assemble the Team (flag):** Before change 5, the draft only mentions Assemble the Team in Connections. Change 5 makes it a step; without it the pattern misses the week's theme.

**Value realized (flag):** The draft says "value realized from pattern usage," uses "a role that pays a median of about $103,570," and says the sign-off stays with people. No "hires" wording. Pete's bookkeeper role has no verified figure on file - it needs a 4 PM BLS check before any page uses it.

**Housekeeping:** Seven pattern pages, the AI Reads, Tools Copy draft, index.html, README.md and BACKLOG.md still name "Models Are Not Good at Math" (Judge the Outcome, Not the Craft; Right Tool, Right Job; Research Partner, Not All-Knowing Oracle; Avoid the Naughty List; Ghost in the Workflow; Dashboards That Answer a Question; The Productivity-to-Headcount Trap). The published page shows Foundation; the decision says Practice.

**Round 3 proposed changes:**
8. Lead: end with the string. Proposed text: "Calculate with code, copy with tools, review independently." And in Solution: "AI Reads, Tools Copy is now a step in this pattern; its name stays, because a team can say it out loud." (Strings flag)
9. Value: add a second role for small businesses - bookkeeping - only after a 4 PM BLS check of the median pay; until then, leave it out. (Pete; Value realized flag)
10. On publish: rename every link and mention of "Models Are Not Good at Math" across the site to "Models Are Not Good at Everything" (same web address), take AI Reads, Tools Copy off Coming Soon, and change the level tag to Practice if Greg confirms. (Housekeeping)

---

## Not in the list - questions for Greg
- Level: Practice (as decided for the copying part) or keep Foundation?
- The two proposed weak spots (citations and quotes; long documents): accept or reject each.
- Jen Vodenlich's "I just have to check prices" fits Step 7. Her recorded consent is for the Results page; ask her before using it here.
- Greg's own example for Notes.
