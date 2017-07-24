---
layout: post
title: "Maintaining an open-source project"
description: "My experience maintaining an open-source project with over 200.000 downloads each month"
date: 2017-07-24
tags: []
comments: true
share: true
---

## Background
During my time at university I did some web-development work on the side. There was this one project where we were using Angular, this was in 2014 so the version were probably around 1.2. I had this dropdown directive which had a bug so severe I could not use the directive. _Hmmm.._ I thought to myself, _what do I do?_ I went online and I found the Github repository where it was hosted, I created a Github account and posted an issue for the bug. I sat there for a moment and thought about how long it would take before the bug was fixed. Then it struck me - _I can fix it by myself!_

What an epiphany! I'll just do it by myself. Soon enough I found the bug and added an option as a configurable flag for the directive. I read the documentation about how to create a pull request and I did it. It felt so good, I was instantly addicted (this PR is still not merged, this was 2.5 years ago). From that moment on I started looking for projects to contribute to on Github, and it was not long before I created my own Angular directive. I spent a lot of time on it and it's actually used in production on some sites today.

As time went by I did some PRs here and there, nothing fancy. I continued doing this for a year on and off, but I never let go of the idea of having my own project where people posted issues, pull requests and asked questions. That was my goal. When I started working for Spotify the team I joined were using React which I had never used before. We needed a datepicker so I went online and found one and we started using it. I looked at the README page and the code of the component and I remember thinking that there's room to improve it. So I added a linter and did some general clean up of the code and documentation. I noticed that it was the creator of the project that reviewed and merged my my PRs, so I knew he was somewhat active.

## Joining the team
After having contributing to the project for a month or so I had worked up the courage to e-mail the creator to ask if I could help him in maintaining the component. It felt like I was asking someone to let me be a part of a secret society, even though he was the only one regularly working on it. I was so happy when I got a reply saying "Yes, please join! I've noticed your help over the last weeks and I could really need your help". I started working on it immediately. I resolved issue after issue, fixing bug after bug and I felt awesome. I was in charge of where this project was going and I was helping people to solve their problems. At this point it had 35k downloads per month from npm so it was a big deal (to me) at the moment. The creator and I had some e-mail contact but I did all the work on Github. This continued for months and I even made a roadmap for the next major version which would resolve all big bugs and add more features.

As time progressed I slowly began feeling a sense of hopelessness, because no matter how much effort I put in to fixing bugs and reviewing pull requests the issues kept on coming in. And new bugs were found all the time. This was all I ever wanted but yet it began feeling like a burden. I spent less and less time working on the component until one day I realised I had not touched it for a month, and the amount if issues coming in were increasing as the popularity increased. At first I was so happy that the downloads/month just kept on going up. I felt like I was doing something good for the world, but now I wanted the downloads to decrease. I watched it go to 50k, 100k, 150k, 170k, 190k, 210k all the way up to 226.000 downloads per month. That's when I decided to remove the npm badge in the README showing how many downloads/month the project had. Since then it has decreased significantly (star driven development* ftw, right?).

_* When you decide on the usage of open-source software based on the amount of stars/downloads/forks the project has, instead of looking at the source code and your needs_ 

## Learnings
I've now been the maintainer for this project for a year, and I have learned a lot. What exactly have I learned? 
- Open-sourcing development is a lot of fun, but it can be exhausting if you lose your motivation. I keep motivation up by working with other people, and I don't mean random people doing a single PR but rather having a team of people where you can bounce ideas off of each other and ask for help.
- People are bad at reading documentation. I can't tell you how many duplicate questions I've had to answer just because people are too lazy to go through the documentation.
- People are lazy at reading anything. I spent a lot of time writing contribution guidelines and also a template to use for submitting issues and PRs. Most of the time people would just erase the entire template and just write down their issue sometimes making me ask questions I had in the template. Annoying.
- People do not think like me when it comes to code. I have a clear vision about what is good code and what is not, which I apparently do not share with everyone contributing to this project. There are some PRs where it's obvious that the author have spent time making the code as nice as possible, those PRs are really appreciated.
- People are terrible at writing sensible commit messages. This was probably what surprised me the most. In an open-source world on Github using Git we have a limited space to communicate with our future selfs. We should use that space wisely and by best effort try to be as clear as we can when writing these messages. A commit subject like "_Fixed render bug_" without any commit body is a poor use of the space you have to work with. This does not concern a lot of people, apparently. This sometimes results in me taking their code, pushing my own commit with a clear and descriptive message and closing their PR (Yes, I think it's _that_ important).
- It's a very nice feeling to merge someone's pull request. I myself know how it feels to have your piece of code merged into the master branch of a repository and released out in the open, and doing this for other people is just great. It's a win-win-win situation where the author of the PR gets to have this warm and fuzzy feeling (and hopefully learned something along the way), I as the maintainer have an issue fixed/a feature added and the world gets to take part of this new and improved version of the component. I love it.
- Don't always trust your tests. One evening I was fixing an issue and at the same time updating the `package.json` file. I updated the path of a script from being relative to being absolute. I ran all the tests and everything was green, so I deployed the version and went to bed. The following morning I come into work, I see that our build pipeline is broken and I realize it's _my change_ the following evening that caused it. At the same time issues for the component are being created from people all over the world saying their builds are failing. _I panic._ It took a while for me to realise it was the small configuration change that caused it to fail. Luckily I could fix and verify it from work. Phew.

All in all I learned that people are awesome. Despite you not reading the documentation I spent hours on writing, I still love the fact that you take time out of your life to contribute to free software that will be used by people you do not know. Thanks for that, if you're not doing it you should! And if you are doing it please continue.

## What's next?
We're currently looking for a new member to join the team. This will hopefully spark a light in my motivation so we can finish the next major version, that is my preliminary next goal with this project.

If you get the chance to maintain a project of any size I strongly recommend you to do it. It will take up as much time as you will let it, but it will be worth it, I promise.

Thanks for reading,

Simon
