---
id: di-san-zhang
num: 03
part: ji-chu-pian
nav: Chapter 3: Plugging Your Phone into Its “Lifeline”
toc: default
kind: chapter
---

### Chapter 3: Plugging Your Phone into Its “Lifeline”

{class="chapter-intro mb-4"}
Without a network, a smartphone loses half its "smart." Networks are the lifeline of modern phones—understanding them, using them well, and protecting them is required study for every phone user.

#### 0. Don't Get Lost Online—Telling Wi-Fi and Mobile Data Apart via "Roads" and "Cars"

Many people have both the Wi-Fi and signal icons lit up at the top of their phone screen, but are completely confused about the essential difference between them. The most classic misconception is:<strong>connected to Wi-Fi but pages won't load</strong>—because the router lost its internet connection, and the phone didn't automatically switch back to mobile data. To fully understand this issue, we need to build a "road and car" mental model.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-road mr-2"></i>Core Metaphor: Roads and Cars

{class="mt-1"}
Imagine the internet as a city.<strong>"Roads"</strong> are the channels between your phone and the internet, and <strong>"cars"</strong> are the data traveling on the roads. Wi-Fi and mobile data are two different roads, but the data (cars) itself is the same.
:::

{class="font-semibold mt-4 mb-1"}
##### 1. Essential Difference: Local Channel vs. Remote Highway

Wi-Fi is essentially a <strong>local area network technology</strong>—it's like the road wirelessly laid downstairs in your building, responsible for transmitting data from the router to your phone. But if your broadband bill is unpaid or the fiber cable is broken, the road is still there, but the "highway" beyond is cut off, so naturally you can't go anywhere. Mobile data, on the other hand, is transmitted through carrier 4G/5G base stations—equivalent to driving directly onto the carrier's high-speed dedicated line. As long as there's signal, you can connect directly to the internet.

{class="font-semibold mt-4 mb-1"}
##### 2. Cost and Scenarios: Fixed Monthly Fee vs. Pay-per-Use

Wi-Fi is usually a one-time investment (monthly broadband fee)—as long as the power is on, the whole family can use it unlimited, making it ideal for high-traffic scenarios like downloading movies and gaming. Mobile data is billed by usage—exceeding your plan may result in throttling or extra charges, making it more suitable for lightweight tasks in mobile scenarios like subways and business trips.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands-helping mr-2"></i>Try It: Check Your Data Plan

{class="mt-1"}
Open your phone's [Settings] &gt; [Mobile Network] &gt; [Data Management] to see how much data you have left this month and which apps use the most. Knowing your numbers means you won't panic when you go out.
:::

{class="font-semibold mt-4 mb-1"}
##### 3. Security Considerations: Public Wi-Fi Is a Hidden "Phishing Ground"

In terms of security, mobile data is usually safer than public Wi-Fi. Mobile data is encrypted by the carrier, while public Wi-Fi can indeed be set up by hackers as "fake hotspots" to intercept unencrypted traffic. But let's be clear: in today's world of ubiquitous HTTPS, what attackers can intercept is <strong>which websites you visit</strong>(domains) and <strong>unencrypted HTTP content</strong>; while HTTPS-encrypted data like WeChat messages and banking app login passwords <strong>cannot be directly read</strong>—unless a more complex SSL stripping attack is performed and the user ignores certificate warnings. Even so, when making payments on the go, using mobile data directly is still the safest choice.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Security Reminder

{class="mt-1"}
At airports, malls, cafés, and other public places, do not connect to free Wi-Fi with suspicious names (such as "Free_WiFi_2024"). Even if you do connect, never sign in to banking apps or enter passwords on it.
:::

{class="font-semibold mt-4 mb-1"}
##### 4. Checking on Your Phone: Decoding the Status Bar's "Hidden Language"

How do you know what your phone is using to connect right now? Taking a Huawei phone as an example, when a <strong>two-way arrow icon</strong> appears next to the carrier signal or WLAN signal in the status bar, it means you're using that method to access the internet; if both light up at the same time, it means network acceleration is in effect and the phone is using both channels simultaneously.

iPhone users have it more intuitive: if the Wi-Fi icon is lit, you're on Wi-Fi; if not, look at the signal bars in the upper right corner to know you're on mobile data. Some Android phones also display "5G" or "4G" in the status bar, directly telling you the current mobile network type.

{class="text-lg font-semibold mt-6 mb-2"}
#### I. Mobile Networks (4G/5G) and Data

Mobile networks are the foundation of staying connected anywhere. From 2G to 5G, speeds have increased a thousandfold, but the principles are much the same.

##### Network standards:

- <strong>4G LTE</strong>: Currently the widest coverage, sufficient speed (theoretically up to 100Mbps+), relatively low power consumption.
- <strong>5G</strong>: Fast (theoretically up to 10Gbps), but coverage is still expanding and power consumption is high. Best for downloading large files and watching HD video.
- <strong>5G SA vs NSA</strong>: SA is standalone networking; NSA relies on 4G base stations. SA offers a better experience, but requires both carrier and phone support.

##### Data management:

- <strong>What data is</strong>: The amount of data generated when your phone goes online. Video and images use the most data; text and voice use relatively little.
- <strong>Data-saving tips</strong>: Turn on "Data Saver" in settings, and update apps or watch HD video over Wi-Fi.
- <strong>Signal bars ≠ speed</strong>: Strong signal only means a good connection—speed also depends on how busy the base station is and how far you are from it.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-circle mr-2"></i>Important Warning: Turn off [Data Roaming] Before Going Abroad!

{class="mt-1"}
Using mobile data abroad can result in astronomical bills! Before going abroad, be sure to turn off data roaming in settings, or purchase a local data card/international roaming plan in advance.
:::

#### II. Wi-Fi: Connection, Sharing, and Security

Wi-Fi is the main connection for homes and offices—fast and doesn't use mobile data. But Wi-Fi is constantly evolving, and the differences between standards are significant.

##### Connecting to Wi-Fi:

Go to [Settings] &gt; [WLAN], select a network, and enter the password. Many phones now support QR code connection, which is even more convenient.

##### Sharing passwords:

Both Android and iOS let connected phones quickly share passwords with friends. Android generates a QR code; iOS can share automatically by bringing devices close together.

##### Wi-Fi standard evolution:

Wi-Fi standards are set by IEEE, and each generation brings significant improvements:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Standard</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Protocol</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Band</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Max Speed</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Features</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11n</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">600Mbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Legacy standard, decent coverage</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 5</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ac</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">3.5Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Currently the most widespread, sufficient speed</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Strong multi-device performance, low latency</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 6E</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11ax</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">9.6Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adds 6GHz band, less congestion</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Wi-Fi 7</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">802.11be</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">2.4/5/6GHz</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">46Gbps</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Ultra-fast transmission, multi-link aggregation</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

- <strong>Wi-Fi 6 key technologies</strong>: OFDMA (Orthogonal Frequency-Division Multiple Access) allows multiple devices to transmit simultaneously; MU-MIMO (Multi-User Multiple Input Multiple Output) improves multi-device concurrency efficiency; TWT (Target Wake Time) makes devices more power-efficient.
- <strong>Wi-Fi 6E</strong>: Built on Wi-Fi 6, it adds the 6GHz band, providing more channels and reducing interference. Requires support from both the phone and the router.
- <strong>Wi-Fi 7</strong>802.11be
- <strong>2.4GHz vs 5GHz</strong>: 2.4GHz has better wall penetration but slower speed and more interference; 5GHz is faster but weaker at penetrating walls. The 6GHz band of Wi-Fi 6E/7 is the fastest but weakest at wall penetration, suitable for use within the same room.

##### Public Wi-Fi risks:

Public Wi-Fi may have hackers eavesdropping on data or setting up phishing hotspots. Guidelines:

- Avoid logging into bank accounts or entering passwords.
- Best to use a VPN for encrypted connections.
- Don't auto-connect to unfamiliar Wi-Fi.
- Use HTTPS websites (look for the lock icon in the address bar).

#### III. Bluetooth: The All-Rounder of Short-Range Wireless Communication

Bluetooth is probably one of the most frequently used wireless technologies on your phone—wireless earbuds, smart watches, car systems, keyboards and mice all rely on it to connect.

##### Technical principles:

Bluetooth operates in the 2.4GHz ISM band and uses Frequency-Hopping Spread Spectrum (FHSS) to spread data across 79 channels and switch between them rapidly, effectively avoiding interference. Bluetooth range comes in three classes: Class 1 about 100 meters, Class 2 about 10 meters (commonly used by phones), and Class 3 about 1 meter.

##### Version evolution:

- <strong>Bluetooth 4.0</strong>: Introduced Bluetooth Low Energy (BLE), allowing small-battery devices like wristbands and heart rate monitors to connect wirelessly, extending battery life from days to months.
- <strong>Bluetooth 4.2</strong>: Improved transmission speed and privacy protection, supports IPv6 direct connection.
- <strong>Bluetooth 5.0</strong>: Doubled transmission speed (2Mbps), 4x the range (theoretically 300 meters), 8x the broadcast capacity. Supports dual audio (connecting two pairs of earbuds simultaneously).
- <strong>Bluetooth 5.1</strong>: Introduced direction finding (AoA/AoD), with centimeter-level positioning accuracy.
- <strong>Bluetooth 5.2</strong>: New LE Audio standard, supports LC3 codec (better sound quality, lower power consumption), multi-stream audio, and broadcast audio.
- <strong>Bluetooth 5.3/5.4</strong>: Further optimized power consumption and connection stability, enhanced periodic broadcasting.

<strong>LE Audio adoption</strong>: In 2025-2026, LE Audio has entered a rapid adoption phase. New true wireless earbuds from major brands (such as Huawei FreeBuds Pro 5, Xiaomi Buds 6 Pro, Samsung Galaxy Buds3 Pro, etc.) already support LE Audio and LC3 codec, offering lower latency and better sound quality. When buying new earbuds, it's recommended to prioritize products that support LE Audio.

##### Application scenarios:

- <strong>Audio transmission</strong>: Wireless earbuds, car audio. Bluetooth 5.2's LE Audio brings a qualitative leap in both sound quality and latency.
- <strong>Data transmission</strong>: Close-range file and photo transfer. While slower than Wi-Fi Direct, it's simpler.
- <strong>Device pairing</strong>: Smart watches, fitness bands, keyboards and mice, and game controllers.
- <strong>Location services</strong>: Bluetooth beacons for indoor navigation, item tracking (like Apple AirTag).
- <strong>Smart home</strong>: Bluetooth Mesh networks control light bulbs, smart locks, and more.

#### IV. Infrared Remote Control: Phone Becomes a Universal Remote

Infrared remote control is one of the oldest wireless control technologies, but it's still practical on phones. Some Android phones (such as certain Xiaomi and Huawei models) have built-in infrared emitters that can remote-control TVs, air conditioners, set-top boxes, and other appliances.

##### Working principle:

An infrared remote works by emitting infrared light pulses at a specific frequency (usually 38kHz) through an infrared LED, and the infrared receiver in the appliance decodes these pulses to carry out the corresponding actions. Different brands use different encoding protocols—common ones include NEC, RC5, RC6, and SONY. The infrared app on your phone ships with a code library for each brand, so picking the brand and model matches the right code.

##### Limitations:

- <strong>Directionality</strong>: Infrared travels in straight lines and must be aimed at the device—cannot pass through walls.
- <strong>Short range</strong>: Effective distance is generally 5-8 meters.
- <strong>No Apple support</strong>: iPhone has no infrared emitter and cannot use this feature.

#### V. NFC: The Magic of a Tap

NFC (Near Field Communication) is a very short-range (within 10 cm) high-frequency wireless communication technology, operating at 13.56MHz with a maximum transmission rate of 424Kbps.

##### Communication principles and modes:

NFC evolved from RFID technology and supports three working modes:

- <strong>Read/Write mode</strong>: The phone reads information from NFC tags, such as triggering actions by reading NFC stickers.
- <strong>Peer-to-Peer mode</strong>: Two NFC devices transmit data to each other, such as Android Beam (discontinued).
- <strong>Card Emulation mode</strong>: The phone emulates a smart card—this is the most commonly used mode. Transit cards, access cards, and bank cards all use this mode.

##### Security mechanisms:

- <strong>Ultra-short distance</strong>: The communication distance within 10 cm is itself a physical security guarantee—remote eavesdropping is virtually impossible.
- <strong>Secure chip</strong>: The phone has a built-in independent Secure Element (SE) or uses HCE (Host Card Emulation). Payment keys are stored in the secure area and cannot be extracted even if the phone is rooted.
- <strong>Fingerprint/Face verification</strong>: Payments require biometric confirmation—even if the phone is lost, it cannot be used for fraudulent transactions.
- <strong>Tokenization</strong>: Apple Pay, Huawei Pay, etc., do not transmit real card numbers but use one-time tokens—even if intercepted, they cannot be reused.

##### Typical applications:

- <strong>Transit cards/Access cards</strong>: Write physical card information into the phone—just tap your phone.
- <strong>Mobile payments</strong>: Apple Pay, Huawei Pay, etc.—bind your bank card to your phone and pay with a tap.
- <strong>Device pairing</strong>: Tap to quickly pair Bluetooth earbuds and speakers.
- <strong>Identity verification</strong>: NFC ID card reading, electronic driver's license verification.

#### VI. Personal Hotspot: Turn Your Phone into a Wi-Fi Router

When you have plenty of data, you can turn on the hotspot for tablets and computers.

- <strong>How to enable</strong>: Settings &gt; Personal Hotspot/Tethering, turn it on.
- <strong>Things to note</strong>: It drains battery and data—remember to set a strong password and limit the number of connected devices.
- <strong>USB tethering</strong>: Connect to a computer with a cable—more stable and faster than wireless hotspot.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hands-On: Set Up and Manage a Hotspot

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Open [Settings], find "Personal Hotspot" or "Tethering," turn it on, and set the name and password.
2. Use another device (like a computer) to search for and connect to this Wi-Fi.
3. On your phone, see if you can manage connected devices or kick off unrecognized ones.
:::
