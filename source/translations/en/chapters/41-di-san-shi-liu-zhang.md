---
id: di-san-shi-liu-zhang
num: 36
part: er-tong-pian
nav: Chapter 36: Your Phone and the Smart Home — Making Your Home Smarter
toc: default
kind: chapter
---

### Chapter 36: Phones and Smart Home — Make Your House Think

{class="chapter-intro mb-4"}
Your phone can do one more increasingly important job: be the remote for your whole home. From a light bulb or plug to a door lock, smart home gear is moving from "geek toy" to everyday setup. This chapter sorts out protocols, ecosystems, hubs, and starter kits, then closes with a safety checklist so "smart" doesn't backfire.

#### 1. Smart home protocols: Pick the right one

Before buying a smart device, check which protocols it supports — that decides whether your phone and ecosystem can control it. Four mainstream options and their personalities:

- Matter: Released in 2022 by the CSA (Connectivity Standards Alliance), backed by Apple, Google, Amazon, Samsung, and others. One goal: make every brand speak the same language. Rapidly becoming the unified standard from 2023–2026. Matter devices can join Apple HomeKit, Google Home, Amazon Alexa, and Mi Home at once — no more single-ecosystem lock-in.
- Thread: Matter's underlying network "plumbing." Low power, self-healing mesh (if a node drops, signals reroute), fast and smooth. Devices with a Thread border router (HomePod mini, Apple TV 4K, Xiaomi central hub) feel noticeably more stable.
- Wi-Fi: Big bandwidth, connects directly to the router, but power-hungry and can clog channels with many devices. Good for cameras and robot vacuums that move lots of data.
- Bluetooth (BLE): Easy setup, power-efficient, but short range and no mesh. Good for locks and temp/humidity sensors with tiny payloads.
- Zigbee: Classic low-power mesh protocol; needs a dedicated hub. Devices are cheap and stable, but cross-brand interop is weak. Gradually replaced by Matter + Thread.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Rule of thumb

{class="mt-1"}
Buying smart gear in 2026? Prefer the "Matter over Thread" label — the most future-proof choice today. Older Wi-Fi or Bluetooth devices don't need to be tossed; keep using them and move to Matter on new purchases.
:::

#### 2. The big three ecosystems

Protocols are the "language"; ecosystems are the "club." Even with Matter, you'll still pick one main ecosystem for automations and voice. Quick comparison:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                    <thead>
                        <tr class="bg-light dark:bg-gray-700">
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Ecosystem</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Strengths</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Weaknesses</th>
                            <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Best for</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple HomeKit</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strongest privacy (mostly local), smooth iPhone/Siri/Shortcuts integration</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fewer, pricier devices; needs HomePod or Apple TV as hub</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple households that value privacy and polish</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Mi Home (Xiaomi)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Widest device range, best value, solid Xiao AI</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">More closed ecosystem, more cloud data, more ads</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Budget buyers who want one-stop whole-home setup</td>
                        </tr>
                        <tr>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei HiLink (HarmonyOS)</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Seamless with HarmonyOS phone/tablet/watch; device range growing fast</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Fewer overseas devices; ecosystem still catching up</td>
                            <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei phone users who want Super Device multi-device flow</td>
                        </tr>
                    </tbody>
                </table>
```

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
How to choose

{class="mt-1"}
Follow your phone: iPhone → HomeKit first. Huawei → HiLink first. Other Android → Mi Home is easiest. With Matter, devices from different ecosystems can still be controlled by the same phone — no need to pick sides all at once.
:::

#### 3. Your phone as the home hub

In most starter setups, the phone is your "home hub" — control lights, AC, curtains, and security from an app, and build automations so the house "moves on its own":

- Device control: Open HomeKit/Mi Home/Smart Life to toggle lights, change color temperature, set AC temperature, open/close curtains, and view cameras — locally or remotely.
- Automation scenes: Combine "condition → action." Three favorites:
- Away mode: Last person leaves (location leaves or door locks) → lights off + AC off + plugs off + cameras on + arm security.
- Sleep mode: Every night 23:00 → main lights off + curtains close + AC to 26°C + night light on.

- NFC tap: Stick an NFC tag by the door; tap the phone to trigger a scene (tap once for entry lights, twice for sleep). On iPhone use Shortcuts automation; on Android use Wallet or the brand app to write the tag.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
Try it: Build a "Coming home" scene

{class="mt-1"}
In your smart home app's "Automation," create one: trigger "arrive at place" (home), actions "entry light on," "AC to 26°C," "curtains close." Save it, go out for a walk, and see if the lights turn on when you return — that first success feels better than ordering new gear.
:::

#### 4. Starter kit picks

You don't need everything at once. These four cover about 80% of daily needs:

- Smart speaker: Xiao AI (Mi Home, great value) / HomePod mini (Apple, also a Thread border router) / Alexa (broad overseas ecosystem). Note: The speaker picks your voice ecosystem — decide the ecosystem before buying.
- Smart bulbs: Yeelight (Mi Home/Matter, adjustable color temperature and brightness, cheap) / Philips Hue (great color and stability, but needs a Hue hub and costs more). Note: Check socket type (E27/B22) and whether you need color changing.
- Smart plugs: Xiaomi Smart Plug (cheap, energy stats) / TP-Link Kasa (good Matter support overseas). Note: For high-power appliances (water heater, space heater), always check the rated wattage and don't overload.
- Smart locks: Loock/Xiaomi (value and Mi Home integration) / Kaadas (traditional lock maker, solid mechanics). Note: Check Matter/your ecosystem support, battery life, and where the emergency keyhole is.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Suggested buying order

{class="mt-1"}
Smart speaker first (locks your ecosystem) → then bulbs and plugs (low barrier, instant feedback) → finally locks and cameras (security-related, choose carefully). Add one category at a time so you don't end up with gear you can't use.
:::

#### 5. Safety basics

More smart devices mean a bigger attack surface. These four lines are non-negotiable — check them one by one:

1. Change default passwords: Factory passwords for cameras, routers, and locks are public online. First thing after unboxing: set a long, unique password.
2. Update firmware promptly: Vendor updates often fix security holes. Turn on auto-update in the app, or check manually at least monthly.
3. Network isolation: Put IoT devices on a separate Wi-Fi (or guest network) away from your phone and computer. If one device is compromised, it's harder to pivot to your important data.
4. Privacy: Enable camera "privacy zones" (skip bedrooms and bathrooms), turn off 24/7 cloud recording, and don't leave home camera feeds open to third-party apps long-term.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
Don't step in these traps

{class="list-disc pl-6 mt-1 space-y-1"}
- Don't use remote unlock for strangers — prefer temporary passwords that expire.
- Don't point cameras at beds or out the window — that's your own privacy leaking.
- Don't buy no-name "white label" gear for a bargain — it often never gets firmware updates, basically a back door into your home.
:::

::: div .chapter-summary
{class="font-semibold mb-1"}
Chapter recap

{class="list-disc pl-5 text-sm space-y-0.5"}
- Matter + Thread is the 2023–2026 direction — look for that label on new gear
- Each ecosystem has a strength: Apple for privacy/experience, Mi Home for value, Huawei for multi-device flow
- Your phone can be the hub — set up Coming home / Away / Sleep and the house runs itself
- Starter four: smart speaker, bulbs, plugs, locks — add them in that order
- Change default passwords, update firmware, isolate the network, privacy-mask cameras — four safety lines you can't skip
:::
