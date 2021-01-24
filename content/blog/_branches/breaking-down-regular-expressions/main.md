---
title: Breaking down Regular Expressions - 1
published: 2019-02-29T20:18:13Z
published_verbose: July 20, 2019
tags: python,regex,programming,regular-expressions
keywords: python
        regex
        programming
        regular-expressions
header_image: https://cdn-images-1.medium.com/max/800/1*etsG-pvhozsmeWDyVrXXkA.jpeg
canonical_url: https://medium.com/@vidbagadia/https-medium-com-vidbagadia-breaking-down-regular-expressions-0-a6675d7f102c
description: A Quick and Step by Ste Guide to Regular Expression using Python
---

![regular expression](https://cdn-images-1.medium.com/max/800/1*etsG-pvhozsmeWDyVrXXkA.jpeg)

For this article, I will be building this all out right from the ground up. You might be an experienced developer reading this article, a college student with some idea of what the name means, or someone who’s not a programmer but want to know what the term **Regular Expression** is. Anyone and everyone is welcome.

Before proceeding, I’d like to put something to light and that is that I cannot write regular expressions for a pattern at the top of my head. At times, I forget the most basic syntax of writing a particular element in a **regex** (the shorter form of regular expression). Which is why, this is more of a documentation for myself than for the public. I learn better when I read something that is written by me than looking up for distributed resources for a topic. And if I am going to write a detailed piece on regular expressions, why not write it like an article.

Feel free to add suggestions or provide feedback (constructive, please).


### The Restaurant Scenario

Let us begin with a scenario first. You travel to a new city and you enter a very popular restaurant for lunch. So popular that they have 50 pages of menu. You take the menu in your hand and you just freeze. You have not visited the place before, you don’t know what the place serves, and you’re hungry. _Very hungry._

Lucky for you, the staff at the restaurant is super helpful. That is how they became popular in the first place, you think. Instead of going through every item from the menu, which would practically be impossible, you just ask for some basic ingredients you want in your food.

You call for the waiter and ask them to bring you something that has both cheese and peas in it. Now because (a) the staff is super friendly — they accept your request which is not exactly an order (b) the staff is super talented and know their menu really well — so they return to you with a list of dishes that has both cheese and peas in it.

Great! This list is relatively smaller and you can now go through the menu and decide what you want and place the order.

If you understand the above scenario, you now have a basic idea of what regular expressions are. Let me draw the analogy.


### The Parallel

When you first asked (_queried_) the waiter to bring you items that had cheese and peas, you gave them a _combination_ of ingredients or a _pattern_ you wanted (you could’ve asked for food that was barbecued or roasted, and they’d still come up with a list for you). The waiter now had **two** inputs. They had the very large menu they have been dealing with for years, and a combination you wanted.

The waiter _matched_ your combination to find the menu you wanted.

In the world of software, this isn’t so different. Here, you give a **sequence** or a **pattern** of characters to a system and ask them to return all the **matching ** results.

Let’s connect this to the example above. Suppose you are being served by a new waiter. Let’s call her Lucy. Lucy doesn’t have the entire menu memorized yet and is struggling to get you the complete list. She has other tables to attend and also cannot sit and match it for you physically. Her colleagues are busy attending tables too.

But she’s smart with computers.

Because she works for a rich restaurant, they have their menu digitally on a computer. She writes a quick regular expression to match all the dishes that contain both cheese and peas in their name, and voila, she now has the list ready for you!

And this is a real life use case of regular expressions. You take the _combination/ pattern/ sequence of characters_ **(“cheese”, “peas”)**, and you match it with the entire menu **(“peas dipped in cheese”, “cheese honey & peas special”, etc)**.

Now we’ll extend the above example for another real life use case, just so we can be sure that we understand what’s going on. Lucy is going through the menu and being new to the crew, she suddenly notices something. While noting down **“shredded cheese and peas with creem”** , she notices that _cream_ has been spelled wrong. Because she now has the power of regular expression, she enters a search for _“cream”_ — the actual spelling, and finds no result. But she does remember learning a few dishes with cream in them. Where are they?

She then does a search for the dishes which have “_creem”_ in them and there they are. All the dishes have _cream_ spelled out the wrong way! Again, she’s good with computers. After completing her orders, she finds all the dishes with the misspelled word _“creem”_ and replaces those with the correct _“cream”_. She later notifies the management about it and there’s a happy ending with bonuses which she later uses to buy herself a whipped cream machine.


### The Definition

I love the resources of [**MDN**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions), so let’s take a look on how they define regular expressions and see if we can understand the technical definition now that we know what it is and how it can be used.

> Regular expressions are patterns used to match character combinations in strings.

And, that’s it. You now know what regular expressions are used for.

Wait a minute, stop scrolling, and lift your finger off the screen or mouse. Now take a moment to think of some real life incidents where you could’ve used regular expressions. Make it as absurd as possible — finding all the blue-colored jackets in a mall, getting carpets with either a black or blue border with flowers in the center.

### The Where & Why Part of It

Now that you’ve given it a thought, we’ll end this part by taking a look at some very concrete scenarios where regular expressions are used extensively. This will help us get a more technical perspective towards this.

1. While filling out online forms have you ever come across constraints that go: “_please input digits only_”, I mean that’s a bummer, right? Well no, they are important and are achieved using regular expressions. The system checks if the value entered matches with a predefined string that goes from zero to nine [0–9]. We will check examples like these later in the series.

2. Did you forget where you have placed a file on your computer and the file was important? But you don’t usually panic, do you? You simply click the search option and type the few letters you are confident the file name contains. The system takes the input (_the cheese and peas_) and tries to find the relating items in your file storage system (_the menu_).

3. It is also useful in web scraping — when you want to get some information from a web page using code. You can enter what pattern you are looking for — for instance, a heading which contains the word “NEWS” in it. A very very basic use of regular expression in web scraping can be found [here](https://github.com/vidhibagadia/Packt-Tracer) for a small and personal project.

This article starts everything from the very beginning and will probably be not useful to people with some experience. The next article in the sequence will be dropping soon, and it will focus on turning your patterns and text to actual code we can use. So, stick around for that if you’d like to.

To the ones starting out, just a note of caution, I’ve witnessed senior developers struggling with regular expressions as well. And it is _completely_ fine to not grasp it in your first, second, third or even the seventieth attempt. The more and more you (we) use it in projects, the friendlier the concept becomes and honestly that should be the end goal. Not to master it, but to befriend it.

I forget the regex syntax almost for every other project that I use, but I know what to do and just have to verify and modify if the syntax works properly. I’ve a long way to go too, but it has been okay for any project that I’ve wanted to include regular expressions in.

You’ll be fine too.