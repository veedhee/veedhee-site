---
title: HSTS (HTTP Strict Transport Security) - A buddy to HTTPS 🛡️
published: 2021-02-26
published_verbose: February 26, 2021
tags: security,https,hsts,http strict transport security,web security
keywords: security
        web
        https
        hsts
        http strict transport security
header_image: https://cdn-images-1.medium.com/max/800/1*etsG-pvhozsmeWDyVrXXkA.jpeg
description: A learning guide to what HSTS is with its buddy HTTPS
---

The first time I came upon HSTS or whatever it was supposed to mean was when I was trying to be a developer like everyone else - improving our product's Lighthouse score. We then later concluded that Lighthouse only gives us the basic few requirements and we needed something more muscled up to check for other vulnerabilities along with basic performance. This is also how we ended up updating our third-party CSS and JS libraries but that is not the point we are discussing today. 

We had a little warning that we did not have a specific HSTS header set. Well I hadn't heard of it before (a point to note here would be that it is because of my lack of exposure to security headers in general). And then I did, again, wha any other developer would - Google the hell out of it!

This was quite some time back, but I'm revisiting this to oil the information on it. I tend to forget stuff if I don't write it down. And also, who knows, it might help someone understand something! That's always a good thing to have.

#### 🛡️ It all starts with HTTPS

Alright alright, I know the protagonist of this blog is HSTS, and not HTTPS. But it is impossible to talk about HSTS wihout tagging its buddy HTTPS along in the conversation. We will not go into the detais of _how_ it works, but instead of _why_ it matters and its importance in the way the web works. If you're familiar with https, the next section  might be your starting point.

There's **http** and there's **https**. Both are the same protocols with the difference of an **'s'** between them. Literally, and also conceptually. It is a _what-you-see-is-what-you-get_ kinda thing if you want to be funny about it. The "s" is for **_security_**. HTTPS is a secure version of HTTP. Secure in what sense, you ask?

While on the internet, we transfer A LOT of data. We keep on sending requests, receiving responses for every information, for every page. And it would be much easier if the only data we were trading were cat pictures (which ultimately we'd want to share with as many people as possible), but it's not. We trade details like login details, bank informaion, and so much more. These are sensitive, something we don't want to share with people, but something that still has to flow through the wires and be communicaed between you and the server. HTTPS is what helps us send this over securely.

With https, the communicaion between the client (browser) and the server is encrypted such that the information being sent over the wire cannot be intercepted by someone other than the server for which the information is intended to. If anyone tries to look at the encrypted data, it will seem like a string of random characters. But because of the way encryption works, the server has some additional knowledge which lets it decrupt the information and consume the actual information. This _additional knowledge_ that the server has needs to be kept secret and private.

ecause of what we discussed before, the use of https becomes especially important when dealing with wesites that log you in your account. Since HTTP is stateless (ie, everytime you request a page, it knows nothing about you other than what you send in the current request), the server has to somehow recognize you and determine your identitt from the information you send with every request. Which also means that with every request, you're sending some sensitive data over to the server which you do not want anyone else to get hold of. (if someone gets hold of what you send with each request to authenticate/identify yourself, the attacker could also easily use that in their request to pose as you).

#### 🛡️ Present Day: HSTS

Let's continue HTTPS' story. We now know how important it is for websites to serve and receive content over https. But what if users access the site over http? 

One way to get around it and enforce that communications take place over https would be to redirect any request on http to https. We can permanently redirect all http requests to https and it would work for us most times. But what could be the problems?

1. Redirection affects performance. We first request http which redirects us to https, after which our request is processed. Let's say we care more about security than performance, and we don't mind the redirection. Any problems then?

2. Yes, there still can be problems - security problems. Even if we set up a redirection, the initial request goes over http. And if you're logged in or you're trying to submit a form with sensitive data, it is still available for someone in the middle to intercept or attack it.

There is another way to enforce HTTPS, and that is (_finally!_) with HSTS. 

HSTS (HTTP Strict Transport Security) is a security-enhancement achieved with the use of a response header (headers that are sent by the server in response to a client's request). 

Suppose you're trying to access a website example.com, you can do it either via http or https. Let's assume it does it over http, so this initial request is not secure. Now, the server redirects to the https endpoint like we discussed previously. 

At this stage, HSTS comes into picture as the response includes the HSTS header. This header instructs the browser to use HTTPS for every connection to the site and its subdomains (if _includeSubDomains_ specified in the header) from now on. This rule is valid for a period of time which is specified n the response header as well.

What this means is that after receiving this header, the browser will absolutely not load any resource over http for the particular domain. If the browser is asked to load a resurce over HTTP, it will try using HTTPS instead. In case HTTPS fails, the connection must be terminated.

There only needs to be one request to the domain, and with the help of redirection + HSTS, we can ensure that any more connections to the domain for that browser happen via https.

Note from the MDN Docs:

>The Strict-Transport-Security header is ignored by the browser when your site is accessed using HTTP; this is because an attacker may intercept HTTP connections and inject the header or remove it. When your site is accessed over HTTPS with no certificate errors, the browser knows your site is HTTPS capable and will honor the Strict-Transport-Security header.

Is there a caveat here as well? Hmm, we'll see. ut first let's have the last piece of HSTS together, - how to set it up, and its componenets.

#### 🛡️ HSTS! Dis-assemble!

The HSTS hader can be set in a response like you'd set u any other header. For more technical how-to, visit your preferred backend tech documentation. Te syntax for the header is:

```s
Stric-Transport-Security: max-age=<expiry_time>; [includeSubDomains] [preload]
```

In the above syntax, the directives enclosed in square brackets [] are optional. 

1. max-age: This is what tells the browser the duration for which it has to remember to exclusvely access a domain over https. This is specified in seconds and the maximum value is 2 years.
We usually specify the HSTS header for every response delivered over https. Thus, whenever the header is sent in the response, the rwser will update the expiration time for that ste, and this duration is refreshed which prevents it from timing out and expiring.
When the specified time elapses, the next attemt to request resource over http will proceed normally without automatically using https. 

2. includeSubDomains: This is optional. If this parameter is included in the header value, the security enforcement will be applied to all the subdomains of the site.

3. preload: This is optonal as well. _[continued...]_