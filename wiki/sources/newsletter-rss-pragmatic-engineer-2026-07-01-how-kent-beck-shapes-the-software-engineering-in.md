---
title: The Pragmatic Engineer — How Kent Beck shapes the software engineering industry
type: source
tags: []
keywords: []
related: []
maturity: draft
created: 2026-07-05
updated: 2026-07-05
cross-wiki-source: @osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md
---

# The Pragmatic Engineer — How Kent Beck shapes the software engineering industry

## Relations

- @osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Stream the latest episode

  Listen and watch now on  YouTube ,  Spotify  ,  and  Apple .  See the episode transcript at the top of this page, and timestamps for the episode at the bottom.

  Brought to You by

                 •    Antithesis   .    If you’re using agents to code, the problem isn’t writing the code but making sure that nothing broke. Antithesis runs your whole system in a hostile environment and identifies hard-to-find bugs before users hit them in production. Teams like Jane Street, Fly.io, and the etcd community use agents safely and ship better code, faster, with Antithesis.    Learn more.

    •    WorkOS     – make your app and agents Enterprise Ready, with SSO, SCIM, RBAC, and more.    Get started.

   •    turbopuffer   .    A vector and full-text search engine built on object storage. It’s fast, cheap, and extremely scalable. It’s never been better to try it out: last week, they dropped their base price from $64 per month to $16 per month.    Give it a spin now   .

  In this episode

  Few have made as big an impact on software engineering as this week’s guest on the Pragmatic Engineer podcast, Kent Beck. He created Extreme Programming, pioneered test-driven development (TDD), co-created JUnit, and is one of the authors of the famous ‘Agile Manifesto’. But these days, he’s re-examining many ideas for the age of AI, and says we’re failing to accumulate trust during this new era at the same high rate as new code is being accumulated.

  Longtime readers will remember how Kent and I bonded over our co-authored article in our   response to McKinsey on measuring engineering productivity  , and Kent was on the podcast a year ago, talking   about TDD and AI.

                                      With Kent Beck, in the studio       Today’s episode is the previously untold story of Kent’s remarkable career and how he became the industry legend he is today.    We start with Kent’s journey from discovering Smalltalk in the early days of personal computing, to helping define modern software engineering practices. We explore the origins of TDD, design patterns, Extreme Programming, and Agile – along with some lessons learned at Apple and Facebook.

  Kent explains why he believes software engineering is about    far more    than writing code, why no one yet knows exactly how engineers should work alongside AI agents, and how his “explore, expand, extract” framework can help engineers navigate major technology shifts.

 Key observations from Kent

        Here are 12 rarely-told stories and observations from Kent:

   1. Coding is only a small part of software engineering – the rest can’t be automated.    Kent rebuts the claim that coding – and eventually the whole software engineering craft – will vanish. He believes coding is only part of what we do, and a small part of it, too. Through your work, you also build confidence, make connections with other people, and develop your personal understanding of the domain. This will remain important, even if we develop our skills in other areas than coding.

   2. Lesser-known story: fired by Apple.    Kent joined the tech giant in 1987, drawn in by Smalltalk, whose language was taking off at the time. Xerox had handed the language to a few companies to see who could run with it, and Apple was one. But Apple’s customers wanted C and Pascal compilers instead, so the Smalltalk project went nowhere. Kent joined a team building a programming language for kids, but says he was eventually fired because he was in “punk mode” and wanted to do things his own way, instead of being a team player.

   3. Kent used to keep a thesaurus close at hand.    When working at Tektronix in the late 1980s with    Ward Cunningham    (the creator of the first wiki, and a pioneer in design patterns), they built HotDraw, a graphical editor with a boxes-and-arrows model. For naming core abstractions, Beck chose “drawing object,” “drawing handle,” etc. But Ward cared intensely about nomenclature and hunted for better vocabulary, so they kept a physical thesaurus which was well thumbed. Beck recalls they became pretty obsessed about the names of things.

   4. TDD wasn’t ‘invented’ so much as ‘rediscovered’ by Kent.    As a kid, Kent read one of his father’s programming books from the tape-to-tape era, when an input tape like time cards was fed through a payroll program to produce an output tape, such as one with checks. The book’s advice was to take a real input tape and manually type the expected output tape before writing the program. He read this, didn’t understand it, and forgot about it.

  Years later, Kent built SUnit, a small testing framework, and randomly remembered the input-tape trick, so mapped it onto SUnit. If he followed the pattern, he’d write the test before the code. He laughed out loud at this because it seemed like such a stupid idea: why write a test that’s guaranteed to fail, when the classes and methods aren’t even defined yet? But when he did, he found his anxiety about programming vanished. This is when he became a TDD convert.

   5. Kent invented Extreme Programming (XP) while on the Chrysler payroll project.    Kent threw away a codebase that didn’t work and restarted the project with a new methodology. He paired with others, and used his own ideas for testing. Later, he coined the new  methodology’s name by deliberately picking one that he knew would be unpopular with the tech establishment of the day: “extreme programming” was born.

   6. The Agile Manifesto came together in a messy way.    In 2001, a loose group of folks who rejected waterfall development gathered at Snowbird, Utah, to rethink programming. Kent recalls this summit proceeded badly as everyone pushed contradictory ideas. During a break, Martin Fowler and Jim Highsmith stayed behind, and when the others returned, they found the values written on the whiteboard. Kent’s contribution was the word “daily”: “Business people and developers must work together daily throughout the project.”

   7. Calling it “agile” was an error.    Kent objected to the word “agile” at the time, and still does today, since nobody claims they prefer “rigid” development, and everyone says they’re “agile”, even when they’re not. He would’ve preferred a less spacious term, like with “extreme programming”: after all, it’s hard to call yourself an “extreme programmer” without actually following that methodology.

   8. The Dotcom Bust hit very hard.    The day before the 9/11 terror attack in 2001, Kent had eight months of consulting work booked at top rates and was finishing work on a house in rural Oregon. The next day, everything was canceled, just as big bills fell due. He burned out into depression and was left unable to program for years, in what was a “lost decade.”

   9. At 50, Kent joined Facebook and realized nobody cared about testing or TDD.    At Facebook, Kent found a company that barely did any form of unit testing, while running a massive, stable, and fast-growing site. He signed up to teach a TDD class at a hackathon — he wrote the book, after all! The classes either side of his in the schedule both filled up, but the TDD class got zero signups, not even a pity one. He made the decision to forget everything he knew and to relearn software engineering as it was at Facebook. In the end, he stayed seven years.

   10. Building software products has three phases: explore, expand, extract   . This is Kent’s “3X” model. ‘Explore’ means trying many cheap uncorrelated experiments, ‘expand’ involves focusing on the one thing that’s working and overcoming obstacle after obstacle, while ‘extract’ is a repeatable playbook and economies of scale. How you code, hire, and organize differs across each phase.

   11. Kent has always been an anxious programmer.    He describes himself as chronically anxious because the more complex the code is, the more he knows it could break. This was the fuel behind testing and TDD, which are approaches designed to soothe an anxious mind.

   12. Kent sees himself as a “tree shaker, not a jelly maker.”    He starts things like patterns, SUnit, JUnit, TDD, XP, 3X, then pushes them until they take off, before moving on to the next thing. It’s his defining trait, and may explain his enormous output, and also why he abandoned TDD just as it peaked.

   +1:       The human part is the most important one in software engineering.    As Kent explained:

   “This is the biggest cosmic, practical joke ever. As young people, we were promised: “Okay, here’s this computer and once you’ve completely understand this computer, you’ll be fine. That’s all you need to do.”

So I set out the first part of my career just to become the best programmer that I could be because that’s what it would take to be successful. And then you realize: sorry, there’s this whole human side. Your ability to affect change in the world is gated by your ability to communicate with, to soothe, to understand other human beings. And those are exactly the skills that I thought I didn’t need to learn!

So I was promised: just understand the computer and you’ll be successful. And then someone went “just kidding, understand people!” And now I was in a position of being ten years behind.”

   The Pragmatic Engineer deepdives relevant for this episode

     Measuring developer productivity? A response to McKinsey    – co-written with Kent Beck

     TDD, AI agents and coding with Kent Beck

     Paying down tech debt

     The past and future of modern backend practices

    Timestamps

  00:00  Intro

  03:47  Human engineers aren’t going away

  08:00  Kent’s path into tech

  13:50  Undergraduate and graduate studies

  17:21  Kent’s first programming job

  18:54  The rise and fall of Smalltalk

  27:04  Working with Ward Cunningham

  37:36  Design patterns

  44:05  Working at Apple

  51:08  CRC Cards

  59:29  Testing tools in the language

  1:04:22  The C3 project with Martin Fowler

  1:09:54  Extreme Programming

  1:16:25  Developing TDD

  1:25:07  Writing the Agile Manifesto

  1:30:00  Agile’s impact

  1:32:40  Agile’s downside

  1:37:32  The Dotcom Bust

  1:44:30  Lessons from working at Facebook

  1:59:44  Kent’s ‘Good to Great’ program at Facebook

  2:06:07  Soft skills engineers need to learn

  2:09:30  AI and the challenges of acceleration

  2:15:53  Explore, expand, extract

  2:22:33  What Kent is excited about

  References

   Where to find Kent Beck:

  • X:    https://x.com/kentbeck

  • LinkedIn:    https://www.linkedin.com/in/kentbeck

  • Website:   https://kentbeck.com

  • GitHub:    https://github.com/kentbeck

  •  Newsletter:

    Software Design: Tidy First?  Software design is an exercise in human relationships. So are all the other techniques we use to develop software. How can we geeks get better at technique as one way of getting better at relationships?  By Kent Beck            Mentions during the episode:

  • TDD, AI agents and coding with Kent Beck:    https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent

  • Anthropic CEO Predicts AI Will End Coding and Software Engineering:

    •    Extreme Programming Explained: Embrace Change   :    https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658

  •    Tidy First?: A Personal Exercise in Empirical Software Design   :    https://www.amazon.com/Tidy-First-Personal-Exercise-Empirical/dp/1098151240

  •    Test Driven Development: By Example   :    https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530

  • Tektronics:   https://www.tek.com/

  • Ward Cunningham on LinkedIn:    https://www.linkedin.com/in/wardcunningham

  • Design Principles Behind Smalltalk:    https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html

  • Kotlin:   https://kotlinlang.org

  • Swift:   https://www.swift.org

  • Prolog:    https://en.wikipedia.org/wiki/Prolog

  • The Timeless Way of Building:    https://www.amazon.com/Timeless-Way-Buil
