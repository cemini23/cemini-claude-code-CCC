---
title: Latent Space — AIEWF Daily Dispatch: The great loops debate and the state of AI engineering
type: source
tags: []
keywords: []
related: []
maturity: draft
created: 2026-07-05
updated: 2026-07-05
cross-wiki-source: @osint-wiki/sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md
---

# Latent Space — AIEWF Daily Dispatch: The great loops debate and the state of AI engineering

## Relations

- @osint-wiki/sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

One of the highlights of the final day of the AI Engineer World’s Fair was a debate about loops. It nicely captured an argument running through the whole conference: are autonomous software factories viable now, or is the engineering discipline lagging behind the ambition?

 Allie Howe from Keycard was the moderator and she opened by asking, “is there or is there not a delta between the hype behind loops and what actually works in practice?”

 The pro-loop case was presented by Geoffrey Huntley, creator of the  Ralph Loop , and Keycard CEO Ian Livingstone. Huntley opened by saying loops are already here. “It’s inevitable, it’s here to stay,” adding that “I don’t see myself going back to writing code by hand.”

 Livingstone said that verifiability is ultimately what it’s about — and you can achieve that with any code, regardless of how it was produced. He also pointed out that loops have always been a core aspect of software development:

 “A loop is at the core of ‘I try something, I learn something, I apply something.’ And all we’re really talking about is how quickly we can expedite that process.”

 On the skeptical side were Dex Horthy from HumanLayer and Greg Pstrucha from Subroutine. Horthy began by noting that he wasn’t anti-loops. “The basic take here is not whether loops are good or bad,” he said, noting that “Kubernetes is actually built on loops — built on control loops. But they’re deterministic loops.” Horthy’s issue is that “the hype is outrunning the discipline.”

 “I haven’t seen proof that we are at a point where we can just step up an abstraction level,” Horthy said, referring to agents controlling the coding. “I actually think we need to step down an abstraction level, if anything.”

 Pstrucha was mainly concerned about the economic viability of agentic loops, which he said wasn’t sustainable. You can’t “orchestrate your problems away by buying more tokens,” he said.

  “[We’re] kind of like locomotive engineers now. That’s our job: to keep the locomotive on the rails.”
- Geoffrey Huntley, loops advocate

  Huntley then offered this wonderful analogy for loopmaxxing: “[We’re] kind of like locomotive engineers now. That’s our job: to keep the locomotive on the rails.”

 The discussion turned to  software factories , the metaphor that has really taken hold of the industry. Horthy worries that when everything is automated in a factory-like agent environment, “you never touch the problem.” So instead, he advises to start small and iterate with agent loops — to “build up intuition” and not try to automate end to end from the start.

 Even Huntley recognized some of the dangers in loops. He said that software factories represent where we are headed in the future, but cautioned that it’s not yet solved in the market. “This is frontier thinking,” he said.

 At the end of the hour-long debate, Howe polled the audience to ask which side ‘won’. Ironically, this resulted in a human failure: the stage lights were too bright for Howe or any of the debate participants to see how many hands were raised. If only an agent was in charge of dimming the lights.

 Anthropic’s next big thing: Claude Tag

 Perhaps one example of a company moving to a software factory model is Anthropic. Mike Krieger, one of the co-founders of Instagram back in Web 2.0 and now Head of Labs at Anthropic, was interviewed by swyx in one of the morning sessions.

 Krieger talked about  Claude Tag , Anthropic’s internal model which the company announced to the world last week. He described Tag as more delegated, asynchronous and proactive than Claude. It perhaps suggests what an early software factory looks like in practice — not agents replacing a team, but multiple people delegating responsibilities to a system like Claude Tag.

                                     Mike Krieger talking with swyx at AIEWF today.    “Most usage is actually much more delegated,” he said regarding his team’s usage of Tag. He gave an example of how they instruct the agents: “Don’t just fix this bug. Now you are responsible for this part of the codebase, and I want you to monitor this feedback channel and proactively take on tasks.”

 “That’s really changed how we operate currently,” he continued. “It’s much more this multiplayer, async, proactive way.”

 However, he also indicated there are some negative consequences to becoming more automated. He noted that his team is “bottlenecked on reviews” and on the “human ability to fully conceptualize what we’re doing.”

 2026 AI Engineer Survey

 Back to the current reality for most AI engineers. This morning, Barr Yaron from Amplify presented her annual survey of the industry.

 According to Amplify’s data, 95% of respondents now use agents — roughly double last year’s share. Among teams using agents, 89% said those agents could write data, up from 52% the previous year.

 “Agents are no longer reading, summarizing, drafting,” Yaron said. “They’re taking actions inside the systems.”

                                     Barr Yaron presenting her AI engineering survey.    The controls, however, remain comparatively primitive. Human approvals and permissions were the two leading safeguards, followed by a scattered collection of task decomposition, retrieval, memory and sandboxing techniques.

 “Nobody has settled the control layer for agents,” Yaron said.

 Cost is also a concern. Forty percent of respondents said that AI costs regularly limit how ambitiously they use AI, while another 36% said it sometimes does. Token usage is now the second-most monitored production metric, behind quality.

 The survey captured the conference’s central contradiction. AI has made experimentation cheaper and enabled teams to produce more software, but 59% of respondents to the Amplify survey fear that today’s AI-generated code is creating long-term liabilities.

 Closing keynotes

 The final sessions of the conference appropriately took us back to thinking optimistically about AI technology — about building with it. After all, that’s why the AI Engineer World’s Fair exists, and it’s where the fun is!

 Theo Browne showcased several software projects he had built, or was still building, with AI. His point was that the scale of what an individual developer can realistically attempt has shifted. “What used to be a startup is now a side project,” he said, while projects he would once have dismissed as “too big” are moving within reach.

 Garry Tan, president and CEO of Y Combinator, followed by giving that optimism an organizational form. The fastest-growing founders YC sees, he said, are “not treating AI as autocomplete, they’re treating it as a workforce.”

                                     Garry Tan at AIEWF.    Tan’s closing prescription was: “Build an AI-native company, not a company that just uses AI.”

 The debates during the week showed how much engineering remains before the AI-native vision is viable for all. But the closing keynotes offered a reminder of why the engineers who attended this conference are pursuing it: they just want to ride those locomotives!
