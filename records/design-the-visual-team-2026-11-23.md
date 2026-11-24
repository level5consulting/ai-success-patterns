# Design the Visual, Program the Number - team review (Mon Nov 23, 2026, night run)

Assemble the Team, run from the assemble-the-team skill. Team confirmed by Greg in chat Sun Nov 22, 7:10 PM (no 4 PM needed). Reviewed: the draft in records/design-the-visual-interview-2026-11-23.md (Greg's Nov 23 reset - not the old "Draw the Number" idea). Each voice speaks to the draft only, not to each other. No recommendations - Greg decides each item on the Morning Review form (item 2026-11-23-visual).

## The team
1. **Ray Delgado (adversarial)** - controller at a 200-person distributor who builds every chart in Excel himself. Here to question whether the premise holds at all.
2. **Renee Calloway (who carries this? - standing seat)** - senior program coordinator who assembles the monthly deck everyone edits. Here to say what lands on her plate and what comes off it.
3. **Dr. Anita Shah** - CFO at a mid-size manufacturer who has sent a team away over numbers that didn't match. Here to say what a decision-maker needs to trust the scorecard.
4. **Jamal Wright** - operations analyst who has never written code. Here to say whether he could actually do this on his own.

## The voices

**Ray Delgado (adversarial):**
"I'll be blunt - the story is the strongest part, and it undercuts the advice. The AI gave you a different grade on the same data. That's not a design problem, that's the AI doing arithmetic it shouldn't be doing. So why is step 1 'design the look in the AI'? The fix is step 2 - put the math in a program. The design part reads like a bonus that got promoted to the headline. If I already have the look in Excel, does this pattern have anything for me, or is it 'Models Are Not Good at Everything' with a chart on top?
Second: you checked the numbers by hand once. That proves one run. Your problem was that the grade moved between runs. The test that matches the failure is run it twice on the same data and see if you get the same grade - the draft never says that.
Third: 'a small program that reads the live data.' Who changes it when the data source changes - a new field, a renamed column? Programs break quietly too. The draft makes it sound like you build it once and you're done.
And the '90s programming theory' line - I'd guess half your readers hear 'this is old and I'm being lectured.' If it's spec-first, say what that means in plain words."

**Renee Calloway (who carries this?):**
"I'm the one who puts the monthly deck together, so I read this asking: when this goes in, who runs the program every month? The draft says 'have the AI build a small program' and then stops. Somebody has to run it, notice when it fails, and fix it. If that's me, that's new work on my plate - and I'd want someone to tell me that up front.
What comes off my plate is real, though: re-totaling the numbers every month, chasing the three people who each have a different version, re-pasting charts. If the page said that, I'd be on board.
The new Start-here pages have a 'Who owns the work / What you stop doing' box. This draft doesn't have one, and it needs it more than most - a program with no owner is exactly how we ended up with that macro nobody understands.
One more: the design step. In my world the leader approves the look. Is the design something I build and they sign off on, or something they do themselves? The draft doesn't say who designs."

**Dr. Anita Shah (CFO):**
"The grade moving from A to F on unchanged data is the single fastest way to lose a finance leader. I'd want the draft to say what that cost - did a wrong grade reach anyone? Did a decision get made on it? Right now it's a technical annoyance; to me it's a credibility event.
To trust a scorecard I need three things on it: what data it used and as of when, how the grade is calculated (the weights), and that it was produced the same way as last month. The draft says design the visual first - I'd want the design to include those things, not just the look.
You say this is a leadership pattern. Then talk to the leader. The draft is written to the person building it. What does the leader ask for? Something like 'Was this number programmed or generated?' - that's the question I'd want my team to expect from me.
And 'you get the speed for free' - fine, but I'd lead with accuracy and consistency. Speed is not why I'd care."

**Jamal Wright (never written code):**
"I like that it's honest - 'this will be your first time using The Compressed Apprenticeship.' But then I'm on my own. What is the 'small program'? A Python file? An Excel macro? Something the AI runs for me? Where does it run? I'd need one sentence on that or I'll stall at step 2.
The mentor line is good. What do I ask them for in that 'small amount of time'? If the page said 'ask them to read the program and run it once with you,' I could do that.
'Learn testing theory' scares me a little. The draft says it isn't hard - then give me the one test to start with. 'Work out one row by hand, check it matches' I can do.
The 'AI chataholics' line - that might be me. It reads a bit like a jab at the people the pattern is for. I'd still read on, but some won't.
Step 1, feeding it a picture of something drawn on paper - that's the line that would get me to try it. It's buried in step 1. I'd want it closer to the top."

## Changes proposed (one per line, persona in brackets, no recommendations)
1. Say why designing in the AI comes first, or make "put the math in a program" the headline instead - as written the fix is step 2 and the design reads like a bonus (Ray Delgado)
2. Say what this adds for someone who already has the look built in Excel, and how it differs from Models Are Not Good at Everything (Ray Delgado)
3. Add the test that matches the failure: run it twice on the same data and check you get the same grade (Ray Delgado)
4. Say who updates the program when the data source changes - it isn't build once and done (Ray Delgado)
5. Replace or explain "90s programming theory" in plain words (spec first) - some readers will hear a lecture (Ray Delgado)
6. Add a "Who owns the work / What you stop doing" box: who runs the program each month and fixes it when it fails; what comes off the plate (re-totaling, chasing versions, re-pasting charts) (Renee Calloway)
7. Say who designs the visual - the builder with the leader signing off, or the leader (Renee Calloway)
8. Say what the moving grade cost - did a wrong grade reach anyone or a decision (Dr. Anita Shah)
9. The design should include the data source and as-of date, how the grade is calculated (weights), and that it was produced the same way as last time - not just the look (Dr. Anita Shah)
10. Write to the leader too: the question a leader asks, e.g. "Was this number programmed or generated?" (Dr. Anita Shah)
11. Lead with accuracy and consistency; keep speed as the by-product (Dr. Anita Shah)
12. One sentence on what the "small program" is and where it runs (Jamal Wright)
13. Say what to ask the mentor for (e.g. read the program and run it once with you) (Jamal Wright)
14. Name the first test for a beginner: work out one row by hand and check it matches (Jamal Wright)
15. Soften or drop "AI chataholics" - it may read as a jab at the readers the pattern is for (Jamal Wright)
16. Move "feed it a picture of something you drew on paper" closer to the top (Jamal Wright)

Also on the form (not team items): confirm the two [Synthesized] lines (lead, When to use it) and the level (Leadership - one of the site's three levels: Foundation, Practice, Leadership).
