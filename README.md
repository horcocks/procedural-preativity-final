# Forward
Dropping all pretense–there are many people enrolled in this event that are entirely underqualified. I am one of these people.

That said, I would propose that engineering one’s way into an event far above their level of expertise for the purpose of actually completing the assignment is very on-brand for something called a “Hackathon”.

With that in mind, I give you the results of my efforts: a good-faith attempt at a system of rapidly producing first drafts of full novels.

# Introduction
For myself and many other writers, the first draft is the most difficult and time-consuming piece of any long-form writing project.  Before the first draft, stories and characters exist in a haze of possibilities, and while you don’t know the exact words that will go onto each page, you know how it should feel.  

The problem arises when your first draft doesn’t make you feel what you know you should be feeling.  This is normal and expected, because this isn’t your story yet–this is just your draft.

The most meaningful writing advice I’ve ever received is that the purpose of a first draft is merely to exist. It doesn’t matter how good it is.  It doesn’t matter that nothing is punctuated correctly.  It doesn’t matter that you switch from first person past to third person progressive tense.  It’s a draft–all it has to do is exist, so that you can improve it later. 

From this draft you can craft narrative, work on characterization, and navigate a complicated plot, which simply isn’t possible beforehand.  I don’t care how organized you are, or how much backstory you write, or how much you research, you don’t know how your story is going to go until you actually draft it.

The best way to write a good book is to write a bad draft, as quickly as possible.

Because the first draft is often the gatekeeper of any finished work, my goal in this event was to design and demonstrate a system of rapid drafting.  I have a 50,000 word first draft of a novel, and Claude helped me write it in 3 days.  


It’s awful, it’s filled with that flowery language that AI loves, and all of the characters speak like they’re from The Canterbury Tales… but it doesn’t matter.  My awful first draft will work exactly the same as any other, because the purpose of a first draft is merely to exist. I can do what I always do–put the draft in one window, and rewrite it into another.  This system has already saved me about 4 months.

My story has the right characters, the right plot, the right story beats, the right tone.  All it lacks is the right words.
# Overview

## Preliminary setup:
Generate a core of Characters and World Concepts
Use these concepts to create a single Seed Chapter
Convert this Seed Chapter to an outline.
Use the first outline to create your next outline.

## Core Drafting Loop:
Use the outline to quickly draft a new chapter
Update the outline with the specifics of your chapter.
Create the outline of your next chapter.
Repeat

# The Tools
All of the currently available AI-assisted writing tools (that I’ve seen, at least) are based upon the goal of producing finished prose.  This is fantastic, and is incredibly useful for small sections of text, but all of their systems tend to fall apart when they are applied to longer pieces.  Writing a novel is different from writing an email.

As an alternative, I propose a more layered system of content generation, with the AI acting as a writing assistant along the way. This system must allow for the following:

-Rapid creation of new content, with the ability to overcome “writer’s block”

-The ability to generate tens of thousands of words without entering a hallucinatory spiral.

-Complete customizability, since the needs of each writer will be unique

-Adjustable “autopilot”, to retain the feeling of actually writing a novel

I believe that I have succeeded at a prototype of such a system, using a few novel techniques.
# Compact Character Notation, or “ComCards”

Compact Character Notation is an attempt to facilitate the creation of fully realized, complex characters for use in AI-Assisted Fiction. To do this, several goals must be balanced:

The characterization must be robust enough for a sufficiently-advanced AI to produce smooth and enjoyable prose.
The notation must be easily parsed and edited by humans without AI assistance.
Information should be as compact as possible, to ensure consistency over time through efficient token usage.
Characters should be self-contained, for easy use across multiple projects.
The same system should allow for creation of large “main characters” with complex personalities and goals, as well as more focused “side characters” with smaller token counts.

With these goals in mind, I give you a Compact Card:

Character Name[
(Gender) (In-universe descriptor 1) (In-universe descriptor 2 if needed)

2-3 Physical Description tags

4-8 Personality tags, with at least one “negative” trait.

2-4 Secondary appearance tags, such as clothing or body language

In-universe special characteristics.

(Optional Tags can be added as needed)

(Organize additional tags with newlines)

]

Individual tags are separated by commas, and categories by newlines.

This ComCard can be utilized anywhere that the character’s personality will influence the prose, in most cases without any special instructions–the AI can figure it out!

As a concrete example, here is a short ComCard for a minor character that might be found in a fantasy novel.

T'Sha[

Moon Elf Sage

Short Black Hair, Grey Eyes, Long pointy ears

Logical, Smart, Dry sense of humor, stern, loyal, lonely

Dark Grey robes with inlaid star maps, graceful movements

Only shows tiny hints of emotion

]

This format can be expanded with traditional “prose” characterization by adding additional newlines. Here is the same character, if she were the protagonist of a story.

T'Sha[

Moon Elf Sage

Short Black Hair, Grey Eyes, Long pointy ears

Logical, Smart, Dry sense of humor, stern, loyal, lonely

Dark Grey robes with inlaid star maps, graceful movements

Only shows tiny hints of emotion, doesn't feel she's earned her station.

On a quest to destroy the Cursed Sword of Syr Conrad

T’Sha is the daughter of an Elven Ambassador. Though she is unaccustomed to rough travel, she is dedicated and steadfast when it comes to adversity. She is a bit too focused on decorum at times, and can sometimes cause problems due to her inflexibility. She wishes that she were able to express her wants and feelings better, but is deeply afraid of opening up too much and being found unworthy of love.
]


Note that the additions are focused on nuance and in-universe details, rather than overall characterization–the addition of prose should enhance the character, rather than change the character, so that the shorter “side character” version can still produce consistent characterization.

ComCards can also be used for items, organizations, or abstract in-universe concepts. These have looser standards, as the content will be more varied, though they still follow the same outline.  Here are another example that might be found in a fantasy novel:

The Sword of Syr Conrad[

Cursed Longsword

Twisted iron hilt, inlaid diamonds, cruel spikes

Looking at it directly causes mild nausea, the wielder hears whispers in combat.

Currently possessed by the Spirit of Syr Conrad, a fallen paladin.

To destroy it, the Spirit of Syr Conrad must forgive himself for his failure.

]
## What? Why Chats?
There are two primary reasons why I’ve built this prototype around a chat client.

-Framing a discussion as a roleplay implies the existence of an author separate from Claude.  This gives us inherent control over tone and flow that would otherwise require separate systems, which produces better prose as a result.

-Writing a draft is as personal as it is complex, with writers using wildly different organizational systems and software.  Using chats and framing each “tool” as a separate character is a more flexible system than any single app, offering multiple simultaneous conversations and easy organization.

Long-term, a dedicated app makes sense, but for the purposes of this event I felt that the added functionality of a third-party chat client solved too many problems to ignore.
The Benefit
After all is said and done, the questions must be asked… why?  Why go through all of this trouble to set up what the AI could probably do right out of the box?

I was able to use this process to produce 25,000 words of a novel in a single continuous chat conversation without the AI repeating or hallucinating, including multiple chapter rewrites and edits.

Anyone who has tried to use AI to write long-form knows that this is fairly unusual.


# The Setup
## World Axioms

Before we can begin designing characters and concepts, there are some broad-stroke decisions we need to make about the world.  These World Axioms will be the predefined rules for tone and background that we’ll use to create our first characters.  As an example, a World Axiom for my sample novel styled after a Young Adult fantasy novel:

The world is magical high-fantasy. 
## Character Creation

With these Axioms in mind, we’ll create our first character.  This is the first introduction to our first layer of content creation–the topic editors.  Meet Harmony, the Character Creator.

Harmony is the first of our “Critique” style creators.  These are fantastic for the following reason: Critique of unclear details is biased towards questions. This means that you can give Harmony a very rough character idea, and she won’t make up details–rather, she will ask you follow up questions to better define your character.  The idea at this point is not to write, it is to facilitate writing.

Here is a general workflow for the Character Creator:

Load your World Axioms into Harmony’s Description.
Give Harmony either a ComCard or a Character Prompt.
Harmony will convert your ComCard to a prose description, or your prose to a ComCard.
Harmony will ask you questions about the character. Answer any or all you’d like.
Review the content.  If it’s acceptable, add it to the Lore.  Otherwise, ask for another round of critique.

## World Creation

Flint is our World Creator.  Like Harmony, he is biased towards questions.  His overall workflow is similar to Harmony–the major difference between the two is how they prefer their ComCards. Use flint to create magic systems, organizations, political conflicts, or any major “abstracts” of your story.

Here is a general workflow for the World Creator:

Load your World Axioms into Flint’s Description.
Give Flint either a ComCard or a facet of your world.
Flint will convert your ComCard to a prose description, or your prose to a ComCard.
Flint will ask you questions about the idea. Answer any or all you’d like.
Review the content.  If it’s acceptable, add it to the Lore.  Otherwise, ask for another round of critique.


## Seed Chapter
Before we can automate the outlining and drafting process, we need to produce a sample of what your writing will look like.  It doesn’t need to be polished–this is merely a rough template for the Outliner to work with. To create our first chapter, we’ll work with Eithne, our Scribe.

Eithne, unlike our previous tools, is not biased towards questions.  Rather, Eithne is biased towards content production.  Writing this chapter is going to be the most “hands-on” portion of this exercise, though Eithne’s proclivity towards word count should push us forwards regardless.

Prompt Eithne to tell your story however you’d prefer, though my style is usually 2-3 sentence prompts.  Feel free to make editing suggestions now, since we’ll want to avoid them until the end otherwise.

## The Initial Outline

Once we have a seed chapter generated, we’ll begin our story outline.  Work with T’Sha, our Outline Creator, to write a series of prompts that could have generated the story that you wrote. 

The purpose of this step is to create an outlining style tailored to:

-Your writing style.
-Your story.
-The capabilities of your language model.

## The Loop

Once we have a single template outline, let T’Sha know how you’d like your next chapter to go.  She will convert your idea into a series of 5-6 prompts that you’ll then give to Eithne. Depending on your writing style and model capabilities, in my experience this might produce anywhere from 500-1500 words per prompt.

Once you’ve completed your series of prompts with Eithne, take a look through the draft and make sure nothing has changed drastically–sometimes Claude likes to be a bit too creative, and other times you’ll want to change specific things here and there.  If the outline in your records doesn’t match the content of your story, give the text of your chapter back to T’Sha to convert into a new outline.

From there, you’ll repeat until done.  Generate your next outline, expand the outline into full text for your draft, update the outline, and so on.

It sounds simple… but it just works.


# Conclusion
And… there it is.  My contribution to the future of AI storytelling.  It’s not much, but I believe that two specific pieces are worth at least a passing glance:

-Token-efficient summaries to keep characters consistent over time.
-The outline-draft-outline loop.

If that is sufficient to count as an actual submission to this event, then I’ll continue to use my API access to improve the system and publish my findings.  If not, then it’s been quite a ride.

-H


