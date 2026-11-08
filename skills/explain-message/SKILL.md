---
name: explain-message
description: Explain a Slack message, thread, or DM that the user does not understand, and say what it asks of them. Use when the prompt is a Slack link plus "help me understand this", "I don't understand this message", "what is X asking", "what does this mean", "is <name> right?", "help me with this:", "how should I respond", or a pasted message from a colleague or their AI agent.
---

# explain-message

The user reads many messages written in someone else's shorthand (a salesperson's pipeline terms, an engineer's code terms, a colleague's AI agent output). The answer must land on the first read.

## Procedure

1. Read the full thread with your Slack tool (for example `slack_read_thread`), not only the linked message. Read the 10 messages before it in the channel or DM if the thread starts mid-topic. If the user pasted the message and you have no Slack tool, work from the paste and say so.
2. Open every link, file, PR, or doc in the message that the meaning depends on. Read at most 3.
3. If the message names a project the user works on, find its folder or repo and read its README or notes file.
4. Write the answer in the shape below. Do not add other sections.
5. Check the answer against the gate below before you send it.

## Answer shape

- **What they're asking you:** one line. Say "nothing, FYI only" when that is the case.
- **What the message says, in plain words:** 2-4 sentences. Use no code identifiers, acronyms, or internal names that the user did not use. Define a term you must keep in the same sentence.
- **One concrete example:** one real entity (a customer, a lead, a page) that shows what the message means.
- **Your call:** the decision or reply it needs, with a recommendation.
- **Draft reply:** ready to paste. If it asks someone for something, open with their name and the action, then the deadline. Use only facts and dates the user gave.

## Gate

Could the user act on the answer without asking "what does that mean"? If a sentence holds a term they did not use, rewrite the sentence.
