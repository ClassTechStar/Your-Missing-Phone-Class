---
id: di-shi-wu-zhang
num: 15
part: jin-jie-pian
nav: Chapter 15: Battery Science and Battery Life Optimization
toc: default
kind: chapter
---

### Chapter 15: Battery Science and Battery Life Optimization

{class="chapter-intro mb-4"}
Afraid of heat

#### 1. What's the Deal with Batteries? Cycles and Health

Aging

- <strong>: Over time, the maximum capacity will decrease—this is normal.</strong> Core Metrics: Cycle Count and Battery Health
- <strong>One cycle is not one charge. For example, if you use 60% today and recharge to full, then use 40% tomorrow and recharge to full, the total 100% consumed counts as one cycle.</strong> Battery health is the current maximum capacity as a percentage of brand-new. Below 80%, you'll noticeably feel the battery life shorten.
- <strong>How to check?</strong> iPhone: Settings &gt; Battery &gt; Battery Health &amp; Charging; Android: usually search "battery health" in Settings.

##### 2. Charging Mysticism? Fast Charging, Wireless Charging, and the Golden Rule

- Does fast charging damage the battery?
- Using original or certified fast-charging accessories causes minimal harm. The phone and charger have temperature control and will automatically reduce power if overheated.
- <strong>Wireless charging</strong> : Convenient but less efficient, with more noticeable heat. Suitable for overnight charging.

#### 2. Charging Mysticism? Fast Charging, Wireless Charging, and the Golden Rule

- <strong>: Try to keep the battery level between 20%-80%. Don't keep it starving (0%) or stuffed (100%).</strong> 3. Complete Guide to Fast Charging Protocols: Why Won't Your Charger Charge Fast?
- <strong>Wireless charging</strong>1. Basic Principles of Fast Charging
- <strong>Charging power = voltage × current (P = U × I). To increase power, you either raise the voltage, raise the current, or both. Different protocols choose different technical approaches.</strong> Fast charging workflow:

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>iPhone "80% Charge Limit" Feature — Turning the Golden Rule into a System Setting

{class="mt-1"}
The iPhone 15/16 series (iOS 17+) has turned the "20%-80% rule" into a system feature. When enabled, the phone automatically stops charging at 80%, significantly slowing battery aging. Settings path:

{class="mt-1"}
<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Settings &gt; Battery &gt; Battery Health &amp; Charging &gt; Charging Optimization &gt; 80% Limit</code>

{class="mt-1"}
The three options mean: ①<strong>No Limit</strong>— charges to 100%; ②<strong>Optimized Battery Charging</strong>— learns your routine, only delays to 100% during the last portion of overnight charging; ③<strong>80% Limit</strong>— stops at 80% directly, best for battery longevity. For people who are always at home/office with charging available, the 80% Limit is strongly recommended; for frequent travelers who need a full charge on the go, Optimized Battery Charging is a good choice.
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-plug mr-2"></i>GaN Chargers — A Traveler's Best Companion

{class="mt-1"}
You may have noticed that fast chargers are getting smaller and smaller — the hero behind this is <strong>GaN (Gallium Nitride)</strong> this new semiconductor material. Compared to traditional silicon-based chargers, GaN chargers have several clear advantages:

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Compact Size</strong>: At the same power output, GaN chargers can be 1/2 or even 1/3 the size of traditional silicon ones. A 65W GaN charger is smaller than Apple's old 5W charger.
- <strong>High Efficiency, Low Heat</strong>: Gallium nitride's switching loss is far lower than silicon, with energy conversion efficiency reaching 95%+, so it doesn't get hot during charging.
- <strong>Travel-Friendly</strong>: A single 65W or 100W multi-port GaN charger can simultaneously charge a phone, tablet, and laptop — much lighter than carrying three "bricks."
- <strong>Buying Advice</strong>: Look for GaN chargers that support the PD protocol (65W+ can charge laptops). Well-known brands like Baseus, Anker, Nubia, and Xiaomi are all good choices. Make sure to check that the cable is compatible (high-power charging requires a Type-C cable with an E-Marker chip).
:::

{id="di-shi-wu-zhang-kuichong"}
#### Handshake phase

: The phone and charger communicate through the data cable, exchanging their supported protocols and power information.

##### Negotiation phase

: Both parties determine a commonly supported maximum power level.

Charging phase

1. <strong>: The charger outputs voltage and current according to the negotiated values, and the phone manages the power.</strong> Adjustment phase
2. <strong>: As the battery level increases, the phone gradually reduces the charging power to protect the battery.</strong>2. Mainstream Fast Charging Protocols in Detail
3. <strong>USB PD (Power Delivery)</strong>—King of Universal Protocols
4. <strong>Features</strong>: Official standard developed by USB-IF organization, with the widest coverage. PD 3.0 supports up to 100W (20V/5A), PD 3.1 extends to 240W (48V/5A).

##### Voltage levels

<strong>: 5V, 9V, 15V, 20V; PD 3.1 also supports 28V, 36V, 48V.</strong> Compatibility

- <strong>Protocol</strong> Advantages
- <strong>: Strong universality—one charger can charge multiple devices; supports PPS (Programmable Power Supply) for fine-tuning voltage and current.</strong> Disadvantages
- <strong>QC 5.0</strong> Qualcomm QC (Quick Charge)
- <strong>—Veteran of the Android Camp</strong> QC 3.0
- <strong>: Supports adjustable voltage from 3.6V-20V in 0.2V steps, up to 18W.</strong> QC 4.0/4+

<strong>: Compatible with USB PD protocol, supports up to 27W, adds dual-path charging technology.</strong> QC 5.0

- <strong>: Supports 100W+, 0-50% in just 5 minutes, significantly improved heat.</strong> Compatibility
- <strong>: Most phones with Qualcomm Snapdragon processors support it, but brands usually prioritize their own proprietary protocols.</strong> OPPO VOOC / OnePlus WARP / Realme Dart
- <strong>240W</strong> Technical approach
- <strong>QC 5.0</strong> VOOC 1.0

<strong>: 20W (5V/4A), released in 2014, pioneered the fast charging era.</strong> SuperVOOC

- <strong>Widest</strong> SuperVOOC 2.0
- <strong>: 65W, fully charges a 4000mAh battery in 30 minutes.</strong>150W/240W Super Flash Charge
- <strong>: Currently the fastest mass-produced fast charging technology.</strong> Features
- <strong>: Requires dedicated charger and cable (with extra contacts), not compatible with other protocols.</strong> Huawei SuperCharge
- <strong>—Evolution of High-Voltage Fast Charging</strong> FCP (Fast Charge Protocol)
- <strong>Protocol</strong> SCP (Super Charge Protocol)

<strong>: Supports higher power, from 22.5W to 66W to 100W.</strong> Technical features

- <strong>: Uses charge pump technology to convert high voltage into low voltage, high current input to the battery, with efficiency up to 98%.</strong> Compatibility
- <strong>: Exclusive to Huawei/Honor phones; some chargers support PD protocol.</strong> Xiaomi Surge Fast Charging
- <strong>: Only supports USB PD protocol.</strong> Surge P1 chip
- <strong>QC 5.0</strong> Surge G1 chip

<strong>: Battery management chip, works with P1 to achieve more efficient fast charging.</strong> Technical features

- <strong>: Uses dual-cell series + charge pump solution, supports multi-protocol compatibility.</strong> Apple Fast Charging
- <strong>—Conservative but Stable</strong> Protocol
- <strong>: Only supports USB PD protocol.</strong> Power

<strong>Wireless charging also has its own protocol standards:</strong> Features

- <strong>240W</strong> Accessory requirements
- <strong>: Requires USB-C to Lightning cable (or USB-C to USB-C cable) and PD charger.</strong>3. Fast Charging Protocol Comparison Table
- <strong>Protocol</strong> Max Power
- <strong>Technical Approach</strong> Compatibility

##### USB PD 3.1

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-4">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">240W</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">High voltage/Multi-level</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Widest</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">QC 5.0</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W+</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Charge pump</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Qualcomm models</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VOOC/Dart</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">240W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Low voltage, high current</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">OPPO family exclusive</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SuperCharge</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">100W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Charge pump</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Huawei/Honor</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Fast Charging</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">~27W</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PD protocol</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">iPhone/iPad</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">4. Wireless Charging Protocols</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wireless charging also has its own protocol standards:</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Qi standard</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">: Developed by WPC (Wireless Power Consortium), the most universal standard. Basic Qi supports 5W-15W.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Qi2 standard</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

##### : Released in 2023, introduces magnetic alignment (similar to Apple MagSafe), supports 15W+.

Proprietary protocols

- <strong>: Each brand has its own high-speed wireless charging, such as Xiaomi 50W wireless charging, Huawei 50W wireless charging, etc., requiring dedicated chargers.</strong>5. Fast Charging Purchasing Guide
- <strong>Check protocol matching</strong>: When purchasing a charger, confirm it supports your phone's fast charging protocol. Third-party chargers usually list supported protocols.
- <strong>Check the cable</strong>: High-power fast charging requires a dedicated cable. Ordinary cables may only support below 60W.

##### Check certification

- <strong>: Apple users should choose MFi-certified cables; Android users should choose original brand or well-known third-party.</strong> Check heat
- <strong>: It's normal for the phone to heat up during fast charging, but if it's burning hot, that's not normal—pause charging or change the charger.</strong> Fast Charging Safety Tips
- <strong>Avoid playing heavy games while charging, which will increase heat.</strong> Do not use low-quality chargers and cables, which may cause safety hazards.
- <strong>Remove thick phone cases while charging to help with heat dissipation.</strong> If the charger or phone heats abnormally or has an unusual smell, stop using it immediately.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>4. These Are the Real Battery-Saving Tips

{class="list-disc pl-6 mt-1 space-y-1"}
- Screen (the power hog)
- : Lower brightness, shorten auto-lock time. OLED screen phones can save a lot of power with dark mode.
- Poor signal
- : In elevators and basements, the phone will desperately search for signal, draining power quickly.
:::

#### IV. New Battery Technology: Silicon-Carbon Anode Batteries

If you've been paying attention to 2024-2026 flagship phone launches, "silicon-carbon anode" has practically become synonymous with premium batteries. This is an important upgrade to lithium battery anode materials, and the principle isn't complicated:

- <strong>Traditional Graphite Anode</strong>: Phone batteries have always used graphite as the anode — the technology is mature and stable, but energy density has approached the theoretical limit (approximately 372mAh/g).
- <strong>Adding Silicon Material</strong>: Silicon's theoretical specific capacity is about 10 times that of graphite (approximately 4200mAh/g). By adding a small amount of silicon to graphite to create a "silicon-carbon composite anode," the overall energy density of the battery can be significantly improved.
- <strong>Energy Density Improvement</strong>: At the same volume, silicon-carbon anode batteries can increase capacity by approximately <strong>15%-20%</strong>. This is the key reason 2024-2026 flagship phones can fit 5500-6000mAh batteries in 7-9mm bodies.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Which Models Use It?

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Honor</strong>: The Magic series pioneered the commercial use of silicon-carbon anodes. The Magic6 Pro, Magic7 series, and Magic V3 foldable all use it.
- <strong>Xiaomi</strong>: The Xiaomi 14 Ultra and Xiaomi 15 series feature a new generation of silicon-carbon anode batteries.
- <strong>vivo</strong>: The X100 Ultra and X200 Pro series use a high-density silicon-carbon anode solution.
- <strong>Huawei/OPPO, etc.</strong>: 2025-2026 flagships are widely following suit, and silicon-carbon anodes are transitioning from "black tech" to standard equipment for premium phones.
:::

<strong>Practical Impact on Users</strong>: The biggest benefit of silicon-carbon anodes is "larger battery capacity at the same size" — phones can be thinner without sacrificing battery life, or the body stays the same thickness but the battery goes from 4500mAh to 5500mAh. In other words, you no longer need to pay the price of "thick and heavy" for battery life. Note that silicon-carbon anode batteries still need optimization with fast-charging chips for low-temperature and full-charge management, which is one reason manufacturers recommend keeping charging at 80% long-term.

#### V. The Real Battery-Saving Tips

- <strong>: If the signal is poor, manually switch back to 4G, and battery life will be much better.</strong> Location services
- <strong>: For non-navigation apps, set location permission to "Only while using".</strong> Limit background activity
- <strong>: iPhone in Settings &gt; General &gt; Background App Refresh; Android in app battery settings.</strong> Let's Check: Give Your Battery a Health Exam
- <strong>Check health: Find and note your battery's maximum capacity.</strong> Analyze power consumption details: Look at the charts and app list in battery settings to find the power-hungry culprits.
- <strong>Formulate a strategy: Restrict apps with abnormal background power consumption.</strong> Chapter 16: Account Systems and Cloud Services

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>I have a friend whose phone was stolen last year. His first thought wasn't "how much was the phone worth", but "can I get my photos back?" Unfortunately, he hadn't enabled cloud backup. A phone is just a physical object, but the data in your account—once truly lost, can never be recovered. In this chapter, we'll talk about how to put real insurance on your digital life.

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 1. How Much Does Your Phone Account Actually Manage?
2. Many people think an account is just for downloading apps. In reality, a phone account is tied to much more than you imagine:
3. Contacts
:::
