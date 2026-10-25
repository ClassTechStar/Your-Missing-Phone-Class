---
id: di-er-shi-san-zhang
num: 23
part: chao-yue-pian
nav: Chapter 23: An Introduction to Programming Thinking and Automation
toc: default
kind: chapter
---

### Chapter 23: Programming Thinking and Automation Enlightenment

{class="chapter-intro mb-4"}
For example: every morning when you wake up, you manually turn off Do Not Disturb mode, open WeChat to check messages, open the weather App to see what to wear today, and open NetEase Cloud Music to play a song. If you package these steps into an automated flow, set it to "automatically execute at 7 AM every day," then when you wake up, you just need to pick up your phone, and everything is already prepared. Doesn't it feel great just thinking about it?

#### Automation is essentially the "if... then..." logic chain, the if-else in programming. Once you understand this way of thinking, even if you never write code in your life, your problem-solving organization will be much stronger. Core elements:

Trigger condition <strong>: When to start? It can be "every morning at 7 AM," "when I connect to home Wi-Fi," "when I arrive at a certain location," "when phone battery is below 20%."</strong> Action to execute

: What specifically to do? It can be sending a WeChat message, opening an App, adjusting volume, switching wallpaper, playing music, sending notifications... almost everything you can do manually on your phone, automation can do.

Intermediate logic

1. <strong>(optional but powerful): If situation A, do X; otherwise do Y. For example, "if it's a workday, play news podcast; on weekends, play music"—this is called conditional branching.</strong>2. iOS "Shortcuts"—The Automation Magic Tool for Apple Users
2. <strong>Apple's "Shortcuts" App is a built-in application that doesn't need to be downloaded. Its core concept is to put various operations together like building blocks. First, let's cover a few key concepts:</strong>"Shortcut"
3. <strong>: A complete automation flow that can be manually tapped to run, or triggered by Siri voice. For example, you say "Hey Siri, going home mode," and it automatically executes a series of operations you've set up.</strong>"Automation"

#### : Instructions that run automatically based on trigger conditions, without needing you to manually trigger them. For example, "when the phone connects to car Bluetooth, automatically open the Maps App." Automations are set up under the "Automation" tab, separate from "Shortcuts."

"Action"

- <strong>: The smallest execution unit. Opening an App is an action, sending a message is an action, getting weather is an action, adjusting brightness is an action. You can chain hundreds or thousands of actions together.</strong> Let me show you a few genuinely useful examples; you'll understand after following along:
- <strong>Example 1: One-Click "Good Morning Routine"</strong> Every morning, tap once (or say "Good morning" to Siri), and the phone will automatically: get today's weather → read out the weather and temperature → show today's calendar schedule → open your frequently used music App to start playing. Steps: Create new shortcut → add action "Get Current Weather" → add "Speak Text" → add "Get Calendar Events" → add "Show Reminder" → add "Open App" and select NetEase Cloud Music. It's that simple, all drag-and-drop.
- <strong>Example 2: Automatic "Power Saving Mode"</strong> In the "Automation" tab, create new automation → select "Battery Level" → set "below 30%" → add actions "Set Low Power Mode to On," "Reduce Screen Brightness to 30%," "Turn off Bluetooth." From now on, when phone battery drops below 30%, it automatically enters power saving mode without you worrying about it.

Example 3: Scan Code Automatic Bookkeeping

##### Every time you scan a code to pay with WeChat/Alipay, the phone reads the payment notification and automatically records the amount and merchant to a memo or Numbers spreadsheet. This requires using the "Receive SMS/Notification" trigger in Shortcuts' "Automation" (iOS 17+ supports reading Wallet transactions), combined with the "Append to Numbers" action. For people who want to keep accounts but are too lazy to do it manually, this is a lifesaver.

There's also a clever use many people don't know about: you can add shortcuts to your home screen, turning them into an App icon. For example, make a "Call a Ride Home" shortcut, put the icon on the desktop, and with one tap, it directly opens Didi and sets the destination to home—much faster than opening the App yourself and slowly typing.

##### 3. Android Automation—Tasker and Its Friends

On the Android side, things are a bit more complicated, but the ceiling is also higher. Let's start with the simple ones:

##### Entry Level: Auto Clicker

Many Android phones come with "Auto Clicker" built-in, or you can download it from the app store. Its principle is super simple: you manually operate once, it records the coordinates and time intervals of your taps, then can play them back at high speed. For example, if a certain App gives daily check-in rewards, you record the tapping process once, and then it automatically runs every day. The downside is: it only recognizes coordinates; if the interface layout changes (such as a pop-up ad), it taps the wrong place.

Intermediate Level: Tasker—The King of Android Automation

#### Tasker is universally recognized as the most powerful automation tool on the Android platform, consistently topping the charts. Honestly, its learning curve is a bit steep and the interface isn't pretty, but once you get the hang of it, you'll feel your phone suddenly becomes omnipotent. Tasker's core is also the "trigger → task" pattern:

Profile

##### : Defines "when to trigger." Trigger conditions can be time, location, Wi-Fi connection status, Bluetooth connection, receiving specific notifications, battery status, screen orientation... Tasker supports an absurd number of trigger conditions, dozens of them.

Task

##### : Defines "what to do after triggering." A task can contain multiple actions, executed in order. Action types include: adjusting system settings (volume, brightness, Wi-Fi, Bluetooth, airplane mode), sending SMS, HTTP requests, executing Shell commands, controlling media playback, popping up dialogs, and so on.

Here are some classic practical Tasker scenarios:

- <strong>Auto-turn on Wi-Fi when arriving home</strong>: Set the trigger condition to "connect to specific cell tower" (because you'll connect to a fixed tower near your home) → task "Turn on Wi-Fi." No GPS needed and no power consumption; the phone automatically turns on Wi-Fi as soon as it enters the community area.
- <strong>Meeting mode</strong>: Trigger condition "calendar event title contains 'meeting'" → task "Set silent mode, turn off media volume, auto-reply to WeChat (requires plugin support)." Never worry about your phone suddenly ringing during a meeting again.

Late-night eye protection

- <strong>: Trigger condition "time 22:00-06:00" → task "Turn on eye protection mode, reduce brightness to 20%, set screen to black and white (grayscale mode)." Black and white screen has a miraculous effect on the desire to scroll short videos—once the picture goes gray, you don't want to scroll anymore.</strong> Auto-play podcast when headphones inserted
- <strong>: Trigger condition "wired headphones inserted/Bluetooth headphones connected" → task "Open Xiaoyuzhou App and start playing the latest episode." Put on headphones and start listening, without unlocking the phone to find the App.</strong> If you find Tasker too hard to learn, try its simplified sibling:
- <strong>MacroDroid</strong>. The interface is much friendlier, with rich templates, suitable for users who don't want to tinker. Also, many domestic Android systems (Xiaomi's MIUI, Huawei's HarmonyOS, OPPO's ColorOS) now come with "Scenes" or "Smart Assistant" features; while not as powerful as Tasker, they're completely sufficient for daily automation.
- <strong>4. Daily Applications of Automation Thinking</strong> The biggest gain from learning automation is actually not saving that little bit of time, but

changing the way you think about problems <strong>. Once you're used to the "if X happens, automatically do Y" thinking pattern, you'll find that a large number of repetitive tasks in life can be eliminated. For example:</strong> After taking photos each time, automatically back up to cloud storage and then compress local photos to small sizes to save space.

#### Every morning, automatically read today's schedule from the calendar and generate a text message sent to family via WeChat.

After receiving a delivery sign-off SMS, automatically add a "pick up package" to-do in the memo.<strong>When the phone is fully charged, automatically send a voice reminder to unplug the charger (to avoid overcharging damage to the battery).</strong> Every day at quitting time, if still near the company (through cell tower positioning), automatically remind "time to get off work."

- These sound advanced, but actually, as long as you master the two basic concepts of "trigger + action," combined with Shortcuts or Tasker, you can make them all. The key is
- you first need to realize "this thing can be automated"
- —many people don't lack the ability, they just never think in that direction.
- 5. Pitfall Guide: Common Problems with Automation
- Automation isn't all smooth sailing; I've stepped into a few pitfalls for you first:

Location triggers may not work reliably <strong>: iOS's "arrive/leave location" trigger uses geofencing technology, and accuracy depends on GPS signal and system optimization. Sometimes it triggers only 10 minutes after you've arrived home. It's recommended to use Wi-Fi connection or cell tower triggers instead of location triggers—more reliable and more power-efficient.</strong> Shortcuts "Automation" requires authorization

#### : In iOS, most triggers under the "Automation" tab require manual confirmation to run (iOS's security mechanism). However, Wi-Fi connection, Bluetooth connection, and alarm stopped triggers can run fully automatically without confirmation.

Tasker requires accessibility permission

- <strong>: Many advanced features (such as simulating taps) require accessibility service permission, which makes the phone display a persistent notification in settings. This is Android's security design and can't be removed.</strong> Don't make automation too complicated
- <strong>: When starting automation, begin with small flows of "2-3 actions." Don't jump straight into a 20-step super flow—you'll go crazy debugging it.</strong> Tip: The Right Posture for Getting Started with Automation
- <strong>First spend 5 minutes thinking: What are the top 3 things you repeat most on your phone every day? For example, your morning routine, your habits after connecting Bluetooth headphones, your settings before going out... Start with these high-frequency small things and make a simple automation for each. Even if each automation only saves you 5 seconds, it adds up over time. And the sense of accomplishment after making them is truly addictive.</strong> Practice: Three Beginner Automation Challenges
- <strong>Choose the one most suitable for you to complete, and you'll be on your way after finishing:</strong> Challenge 1: Good Morning Automation

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>: iOS: In the Shortcuts App, create a new shortcut → add "Get Current Weather" → "Speak Text" → "Open App and select NetEase Cloud Music." After completion, you can say "Good morning" to Siri to trigger it. Android: In Tasker, create a new task → add "Get Weather" → "Speak" → "Open App" → set trigger time to 7:00 every day.

{class="mt-1"}
Challenge 2: Low Battery Auto Power Saving
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>: iOS: Automation tab → New → "Battery Level" → below 25% → add "Set Low Power Mode On" + "Set Brightness 25%." Android: Tasker new Profile → State → Power → Battery 0-25% → Task "Power Saving Mode On" + "Lower Brightness."

{class="mt-1 mb-2"}
Challenge 3: Connect Car Bluetooth Auto Navigation

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>: iOS: Automation → New → "Bluetooth" → select your car Bluetooth → add "Open App and select Amap" + "Media Volume to 80%." Android: Tasker → Profile → State → Bluetooth Connected → select car Bluetooth → Task "Open Amap" + "Raise Media Volume."</strong>
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Case 3: Automated "Good Morning Routine"

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Scenario</strong>: Automatically announce weather + turn off silent mode + open news at 7:00 every day.
- <strong>Steps</strong>: iOS: Shortcuts → Automation → Time Trigger → Add "Get Weather" + "Set Volume" + "Open App"; Android: MacroDroid → Trigger (Time 7:00) → Actions (Media Volume / Open URL / TTS Read Weather).
- <strong>Expected Result</strong>: Can be implemented without installation, lowering the barrier to entry.
:::
