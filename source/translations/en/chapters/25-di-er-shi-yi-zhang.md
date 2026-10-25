---
id: di-er-shi-yi-zhang
num: 21
part: chao-yue-pian
nav: Chapter 21: A Deeper Look at Mobile Networks and Information Security
toc: default
kind: chapter
---

### Chapter 21: In-depth Exploration of Mobile Networks and Information Security

{class="chapter-intro mb-4"}
Using a VPN

#### : Your phone → VPN encrypted tunnel → VPN server → target website. The data is encrypted and encapsulated, so "peeping toms" can only see a bunch of garbled text. Additionally, the target website sees the IP address of the VPN server, not your real IP.

So what can a VPN actually do? Simply put: first,

- <strong>protect your privacy on public Wi-Fi</strong>; second,
- <strong>bypass geographical restrictions</strong>(such as watching content only available in certain countries); third,

prevent your Internet Service Provider (ISP) from logging your browsing habits <strong>. But I must remind you:</strong> don't use free VPNs!<strong>Free often means your data is their "commodity." I have a friend who used a free VPN, and his phone started popping up ads for no reason. Later we found out that the VPN had packaged and sold his browsing data to advertisers. So when choosing a VPN, either choose a paid big brand (like NordVPN, ExpressVPN), or simply don't use one.</strong> Also, VPN is not omnipotent. It can only protect data "in transit." If the target website itself is insecure, or your phone already has malware, a VPN can't help you.<strong>2. The "Sweet Trap" of Public Wi-Fi—More Dangerous Than You Think</strong> You might think, it's just connecting to free Wi-Fi, how much risk can there be? Let me tell you a true story: security researchers once did an experiment where they set up a Wi-Fi hotspot called "Starbucks_Free" at an airport, and within an hour, over a hundred people connected. In reality, this hotspot was set up by the researchers themselves, and all <strong>unencrypted traffic</strong> passing through this hotspot—such as the content of HTTP web pages you visit and App communications without TLS enabled—they could indeed intercept and view.

But note a key premise: today, the WeChat, online banking, and Alipay you use daily have mostly already adopted HTTPS encryption. In other words, even if attackers intercept the data packets, what they see is just a bunch of garbled text, and they

#### cannot directly read your chat content or payment password

. However, they can still know which websites you visited (domains). If certain old Apps or web pages are still using HTTP plaintext transmission, the content will be completely exposed. This type of attack is called a "Man-in-the-Middle" attack, and the principle is that the attacker "inserts themselves" between you and the real Wi-Fi router. What's more frightening is that many people's phones are set to "automatically connect to known Wi-Fi." Attackers only need to set their hotspot name to one you've connected to before (such as "ChinaNet" or "CMCC"), and your phone will automatically connect to it.<strong>So how to defend against this? Here are a few practical suggestions:</strong> Look for HTTPS

: The address bar starts with https://, and the extra "s" stands for Secure. When accessing any website that requires a password, if you see http:// (without the s), stop immediately and don't enter anything! Now mainstream browsers will display an "insecure" warning before non-HTTPS websites, so be alert when you see this mark.<strong>Turn off "auto-connect"</strong>: Whether iPhone or Android, turn off "auto-join" or "auto-connect" in Wi-Fi settings. Rather than letting your phone judge for itself, manually tap each time.

Use mobile data for sensitive operations

- <strong>: Transfers, logging into online banking, entering ID numbers... honestly use your own 4G/5G data for these operations, don't save that little bit of data.</strong> Forget infrequently used Wi-Fi
- <strong>: After returning from a business trip or travel, "forget" all the hotel Wi-Fi and airport Wi-Fi you temporarily connected to before. This way, next time your phone won't automatically connect to a fake hotspot with the same name.</strong>3. How Does HTTPS Protect You?—SSL/TLS Handshake
- <strong>I just mentioned HTTPS, so how does it actually work? Every time you visit an HTTPS website, an "SSL/TLS handshake" occurs between the browser and the server. The whole process goes something like this:</strong> Your browser says: "Hey, server, I want to communicate securely with you, here's my list of encryption capabilities (supported encryption algorithms, etc.)."
- <strong>The server replies: "Okay, I've selected this set of encryption schemes from your list, here's my digital certificate, which contains my public key, signed and certified by a certain CA organization."</strong> The browser verifies the certificate's authenticity: Was it issued by a trusted CA? Has it expired? Does the domain name match?

#### After verification passes, both parties use public key encryption to negotiate a "session key," and all subsequent communication is encrypted with this key.

This is like going to a bank to do business: you first hand over your ID card (certificate), the teller verifies your identity, then the two of you agree on a secret code, and subsequent conversations can only be understood by the two of you. Even if someone eavesdrops nearby, they can only hear encrypted garbled text.

1. But note: HTTPS only guarantees that the "transmission process" is encrypted, not that the target website is a good actor. Phishing websites can also use HTTPS—that little lock icon only indicates that you're connected to "some website," not that the website is the one you want to visit. So you still need to verify the URL yourself.
2. 4. DNS Security: Is Your "Network Phonebook" Safe?
3. DNS (Domain Name System) is like the internet's phonebook: you type "baidu.com," and DNS helps you look up which IP address it corresponds to (such as 110.242.68.66), and then the browser can connect. The problem is that traditional DNS queries are
4. plaintext

It's just like going to a bank: you hand over your ID (the certificate), the teller verifies who you are, and then the two of you agree on a secret code. From that point on, only you two can understand the conversation — even if someone eavesdrops nearby, all they hear is encrypted gibberish.

not encrypted

#### ! This means your ISP, Wi-Fi provider, or any intermediate node can see which websites you've visited.

What's even more disgusting is "DNS hijacking": attackers tamper with the DNS process to point "baidu.com" to a fake phishing website. You clearly typed the correct URL, but you're taken to an identical but actually fake login page, and once you enter your account password, you're done for.<strong>Fortunately, there are now encrypted DNS solutions:</strong> DNS over HTTPS (DoH)<strong>: Hides DNS queries in HTTPS traffic, mixed in with normal web browsing traffic, making it impossible to distinguish which ones are DNS queries.</strong> DNS over TLS (DoT)

: Uses the TLS encryption protocol to specifically protect DNS queries, with an independent port. Network administrators can know you're using DoT but can't see the content.

I personally recommend using Cloudflare's 1.1.1.1 or Google's 8.8.8.8 as DNS servers; both support encrypted DNS. In Android's "Private DNS" setting, just enter "one.one.one.one" or "dns.google," super simple. iPhone is a bit more troublesome, requiring you to install a profile or set it up through an App, but it's worth doing.

- <strong>5. Does "Incognito Browsing" Really Make You Invisible?</strong> First, the conclusion:
- <strong>Incognito mode is your window curtain, not an invisibility cloak.</strong> What it does: It doesn't leave traces locally—after closing the incognito window, the browser doesn't save your browsing history, cookies, form fill-in records, or search history. It's appropriate to use incognito mode when looking something up on someone else's computer or buying a gift without family members finding out from browsing records.

What it can't do:

#### The website you visit

: When closed, it's the size of a regular phone; when opened, it's nearly square like a small tablet. Representatives: Huawei Mate X series, Samsung Galaxy Z Fold series, Xiaomi MIX Fold series, vivo X Fold series. Main selling point: "one phone = phone + tablet".<strong>; your IP address, device information, and browsing behavior are clear on the website's end.</strong>

Your network operator

can still see which websites you visited

- , just not the specific content (if HTTPS is used).<strong>Company/school network administrators</strong> can also monitor
- your internet behavior.<strong>Files you download and bookmarks you add will</strong> be retained
- and won't disappear when you close the window.<strong>So remember: Incognito mode is a "local eraser," not a "network invisibility cloak." If you really need to hide your internet traces, you need a combination punch like VPN + Tor browser, but for daily use, knowing this much is enough.</strong>6. Browser Privacy: Don't Let the Browser Sell You Out
- You may not realize that the browser itself is a huge information collector. Cookies, browsing history, cache, autofill, location permissions... each one could leak your privacy. A few suggestions:<strong>Clean browsing data regularly</strong>: Every once in a while, go to settings and clean out cookies, cache, and history. Not to prevent "being tracked"—that's no longer very effective by clearing cookies—but to prevent your phone from getting slower and slower. Browser cache can take up several GB of space.

Give up the "Do Not Track" fantasy

#### : The "Send 'Do Not Track' request" option in browsers is essentially "asking" websites not to track you. But whether websites listen is another matter entirely; most websites simply ignore it. Don't count on it.

Make good use of privacy-protecting browsers

- <strong>: Firefox Focus, DuckDuckGo browser, Brave—these browsers block trackers and ads by default, much cleaner than the default settings of Chrome and Safari.</strong> Search engines matter too
- <strong>: Use DuckDuckGo instead of Baidu/Google search; it doesn't record your search history or build user profiles. Honestly, the search results are indeed not as precise as Google, but it's enough for daily research.</strong> Check App permissions
- <strong>: Go to phone settings and see what permissions your browser has been granted. Does it really need to access your location, microphone, contacts? Probably not.</strong>7. Practical Security Checklist: Protect Yourself Starting Now
- <strong>Having said all this, here's a simple and straightforward security checklist. Spend half an hour to get it done, and your phone's security will have a qualitative leap:</strong> Turn off Wi-Fi auto-connect
- <strong>: iPhone in Settings-Wireless LAN, Android in Wi-Fi settings.</strong> Switch to an encrypted DNS

#### : Android directly set Private DNS to "dns.google"; iPhone use an App or profile to set up 1.1.1.1's DoH.

Enable Two-Factor Authentication (2FA)

1. <strong>: WeChat, Alipay, Apple ID, Google account—enable 2FA wherever possible. SMS verification codes are already the lowest level of 2FA; using TOTP (such as Google Authenticator, Microsoft Authenticator) is even better.</strong> Review all App permissions
2. <strong>: Go through each App's permissions, especially these five: location, contacts, SMS, microphone, camera. You'll find some flashlight Apps surprisingly want your contacts—uninstall them immediately.</strong> Clean browser data regularly
3. <strong>: Set a calendar reminder, once a month, to clean cache and cookies.</strong> Don't use data cables from public charging stations
4. <strong>: USB ports can both charge and transmit data; malicious charging stations (called "Juice Jacking") can steal data while you charge. Bring your own charger head and cable when going out.</strong> Do It Now: Give Your Phone a "Security Checkup"
5. <strong>DNS upgrade</strong>: Android: Settings &gt; Connections &amp; Sharing &gt; Private DNS &gt; enter "one.one.one.one" or "dns.google". iPhone: Use Safari to search "1.1.1.1 DNS profile" to install the profile, or download Cloudflare's 1.1.1.1 App.
6. <strong>Wi-Fi audit</strong>: Open the Wi-Fi list and "forget" all unfamiliar, infrequently used, and strangely named hotspots.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Permission cleanup

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>: Go to Settings &gt; Privacy/Permission management, review permissions for each App. Mark Apps with unreasonable permission requirements (such as a calculator wanting contacts), and consider uninstalling or using alternatives.</strong> Check account security
2. <strong>: Open the security page of your Apple ID or Google account, see if there are any unknown device logins, confirm 2FA is enabled, and check whether recovery contacts are trustworthy.</strong> Chapter 22: How AI Works in Mobile Phones
3. <strong>Welcome to the coolest "magic show" on mobile phones, starring: Artificial Intelligence. The "snap-and-get" beautiful photos you use every day, the voice assistant that responds as soon as you open your mouth, the input method that understands you better the more you use it—all have this invisible brain standing behind them.</strong>1. AI Camera: Your "Post-Production Darkroom" Moved into the Phone
4. <strong>Today's AI computational photography is more like stuffing a professional retoucher + photographer team directly into the shutter button. Before you press the shutter, AI has already started working: scanning the scene, identifying "this is blue sky," "this is a face," "this is a night scene."</strong>2. Voice Assistant: How Does Your "Voice Secretary" Understand You?
:::
