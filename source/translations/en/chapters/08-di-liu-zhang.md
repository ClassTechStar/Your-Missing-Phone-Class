---
id: di-liu-zhang
num: 06
part: ji-chu-pian
nav: Chapter 6: Guarding Your Digital Life
toc: default
kind: chapter
---

### Chapter 6: Guarding Your Digital Life

{class="chapter-intro mb-4"}
Phone security = privacy security + financial security. In this era where data is an asset, protecting your phone means protecting yourself.

#### I. Lock Screen: The First Physical Line of Defense

The lock screen is your phone's first line of defense, and also the most easily overlooked.

##### Security level ranking:

1. <strong>Password/PIN</strong>: Highest security, the ultimate safeguard (relied upon when fingerprint/face fails).
2. <strong>Fingerprint recognition</strong>: The perfect balance of security and convenience.
3. <strong>Face recognition</strong>: Most convenient, but security depends on technology (3D structured light is secure; 2D photos can be fooled).
4. <strong>Pattern unlock</strong>: Convenient but leaves traces that can be guessed.

##### Setting a strong lock screen:

- Be sure to set a complex password (don't use birthdays, 123456).
- Enable biometrics.
- Set lock screen time to "Immediately" or the shortest option.

#### II. "Find My Phone": The Ultimate Anti-Theft Tool

<strong>Must enable!</strong> It can:

- <strong>Locate</strong>: Find where you left your phone on a map.
- <strong>Play sound</strong>: Make your phone ring—good for finding it at home.
- <strong>Lost Mode</strong>: Remotely lock the phone and display a contact number.
- <strong>Remote erase</strong>: The last resort—wipes all data (but after erasing, it can no longer be located).

Go to [Settings]—Apple users look for "Find My iPhone," Android users look for "Find My Device" or similar brand services, and make sure it's enabled (green).

#### III. System Updates: Patch Holes, Plug Vulnerabilities

The primary purpose of system updates is to fix security vulnerabilities, just like patching holes in a house. So when you see a system update prompt, upgrade as soon as possible.

Of course, major version updates (like iOS 17 to iOS 18) may have compatibility issues—you can wait a few days before upgrading.

#### IV. Recognizing and Preventing Telecom Fraud

In today's era of rapid AI development, the traditional "seeing is believing" cognitive model has completely failed. Fraudsters are using AI technologies like Deepfake to achieve a comprehensive upgrade from "scatter-shot" fraud to "precision hunting" crime.

##### 1. The Most Common Fraud Patterns in the AI Era

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-user-secret mr-2"></i>① AI Face-Swap and Voice Cloning Fraud

{class="mt-1"}
Criminals illegally collect high-definition photos published by targets on social media or just a few seconds of voice samples, and use AI deepfake technology to clone "friend/family videos" or "voices" realistic enough to deceive. Common scripts include:<strong>sudden car accidents, emergency loans, kidnapping</strong>, etc. This type of fraud exploits emotional bonds like family and friendship, making it <strong>extremely deceptive</strong>.
:::

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-gavel mr-2"></i>② Impersonating Authority / Customer Service Fraud

{class="mt-1"}
AI technology can precisely simulate the voices and tones of official customer service and law enforcement personnel, and even synthesize highly realistic fake transfer screenshots, electronic documents, arrest warrants, and other files. By <strong>creating panic or authority pressure</strong>.
:::

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-chart-line mr-2"></i>③ AI Investment and Wealth Management Fraud

{class="mt-1"}
Through AI algorithms, fraudsters forge "guaranteed profit" fake return screenshots, virtual quantitative stock-picking software interfaces, or "master-level" investment analysis reports. Using high returns as bait, they sell expensive investment services or induce victims to transfer funds into trading accounts they control,<strong>ultimately absconding with the money</strong>.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. How to Break Through—"Magic Mirror" Defense Thinking

AI can clone voices and faces, but it's not invincible—there are several vulnerabilities to exploit:

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>Action verification method</strong>.<strong>easily shows flaws like screen stuttering, facial distortion, or edge bleeding</strong> when handling complex dynamic occlusion, rapid motion scenes, and lighting changes.
- <strong>Secret signal verification method</strong>: Establish and use preset private verification questions, such as "What did you order when we last had dinner together?" or "What was the first gift I gave you?"—details only both parties know. If the other party hesitates noticeably or answers irrelevantly, you should <strong>immediately terminate the call and activate safety protocols</strong>.
- <strong>Secondary verification method</strong>: Strictly follow the "<strong>Four Don'ts and One Verify</strong>.<strong>call back using the known original number or confirm in person</strong>. When making transfers, it's recommended to choose the "24-hour arrival" mode to allow ample time for potential fraud identification and fund recovery.

##### 3. Traditional Common Patterns (Still Need Vigilance):

- <strong>Lottery/brushing rebates</strong>: Lure with small gains first, then scam big money.
- <strong>Romance scams</strong>: "Pig-butchering" scams—build a relationship then steal money.
- <strong>Impersonating acquaintances</strong>: Borrow money after account theft (even harder to distinguish in the AI era).

##### 4. Built-in Phone Protections:

- Harassment call blocking.
- Verification code theft prevention.
- SMS link security detection.

##### 5. Anti-fraud mantra:

<strong>Don't readily believe, don't disclose, don't click, don't transfer, verify first when in doubt!</strong> When encountering an "emergency," stay calm for 5 minutes—almost all scams reveal their flaws in that moment.

#### V. Resist "Doxing" and Social Engineering Attacks: Cut the Privacy Leak Chain

The core principle of "doxing" (social engineering attacks) is to <strong>systematically collect, analyze, and piece together personal digital fragments to build a complete personal profile</strong>. The key to defense is drawing clear lines for personal privacy and establishing a multi-layered protection system.

##### 1. Photo Desensitization

Basic EXIF removal methods are covered in Chapter 2 "Image and File System Management." Before sharing photos on social media, further steps are needed:<strong>completely delete the photo's metadata (EXIF information)</strong>, including shooting time, device model, GPS location coordinates, and other sensitive data.<strong>house numbers, license plates, ticket barcodes, ID numbers</strong> and other key information—strictly redact or blur them to avoid unintentionally revealing your whereabouts.

- iOS: [Settings] &gt; [Privacy &amp; Security] &gt; [Camera] can turn off "Precise Location"; selecting "Current photo only" when sharing strips metadata.
- Android: Some album apps (like Google Photos) prompt whether to keep location info when sharing.
- General tools: ExifTool, Metapho, etc., can view/edit EXIF.

##### 2. App Permission Convergence

Basic permission management methods are detailed in Chapter 4 "Permission Management." For "anti-doxing" purposes, you should also periodically review and disable unnecessary permissions for e-commerce and utility apps:<strong>microphone, contacts, location</strong>, to prevent apps from "eavesdropping" on daily conversations in the background or illegally collecting personal relationship networks. Uninstall apps that are idle for a long time but still hold high permissions, reducing privacy leak risk points at the source.

- When you see a "Contacts permission" request, ask yourself: Does this app really need to know all my contacts?
- Haven’t used an app in three months? Uninstall it without hesitation. Permissions should get tighter over time, not looser.

##### 3. Smart Device Security Hardening

IoT devices like smart cameras, smart door locks, and smart speakers must have their <strong>default login passwords changed immediately</strong> upon first use. Set high-strength independent passwords containing uppercase and lowercase letters, numbers, and special symbols. Keep rarely used remote access features off, regularly check for device firmware updates, and promptly patch security vulnerabilities to <strong>prevent hackers from intruding and snooping on your home's private space</strong>.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Real Case Warning

{class="mt-1"}
In 2022, police in a certain area reported that hackers cracked the default passwords of a brand of home cameras (many users never changed them), stealing bedroom footage from thousands of households and selling it online.<strong>Not changing the default password = leaving your front door wide open</strong>.
:::

#### VI. Privacy Protection: Your Data Is Your Property

1\. The "Minimization Principle" for App Permissions:

##### Location

- <strong>Location</strong>: Use "Allow all the time" for ride-hailing/map apps; "Only while using the app" for everything else.
- <strong>: Only grant when necessary (like adding friends on WeChat); otherwise deny.</strong> Album / All Photos
- <strong>: Since iOS 14+, you can authorize "Selected Photos"; Android 13+ also supports granular authorization.</strong> Microphone / Camera
- <strong>Microphone / Camera</strong>: Keep them off by default and enable when needed. If you suspect covert recording, swipe open the Control Center and check for the "green dot / orange dot".
- <strong>Background tracking</strong>: Since iOS 14.5+, apps must ask before using IDFA; Android can turn off "Ad ID."

##### 2. Privacy Management in Practice:

- <strong>Privacy Report (iOS)</strong>: [Settings] &gt; [Privacy &amp; Security] &gt; [App Privacy Report], see which apps are secretly accessing your location, camera, microphone.
- <strong>Permission Usage History (Android)</strong>: [Settings] &gt; [Privacy] &gt; [Permission Usage History], see who accessed sensitive permissions and when.
- <strong>Limit ad tracking</strong>: Turn off "Ad ID" or "Limit Ad Tracking" in system settings to reduce "targeted ad harassment."

#### VII. "First Aid" Checklist After Loss / Theft

Don't panic if your phone is lost—follow these steps in order:

1. <strong>Immediately freeze the SIM card</strong>: Contact the carrier to report the loss, preventing it from being used to receive verification codes.
2. <strong>Remote lock</strong>: Enable "Lost Mode" through cloud services (iCloud / brand cloud).
3. <strong>Change important passwords</strong>: Immediately change passwords for all important accounts that were logged in on the phone (payments, banks, email).
4. <strong>Report to police</strong>: File a report at the police station and record the IMEI number. This also helps prove identity if the phone is recovered.
5. <strong>Notify family and friends</strong>: Prevent scammers from borrowing money in your name.
6. <strong>(Last resort) Remote erase</strong>: Only do this when recovery is hopeless—after erasing, the location feature stops working.

#### VIII. SIM Card and eSIM Security

- <strong>Set a SIM card PIN</strong>: Once enabled, you need to enter the PIN every time you restart the phone or swap cards, preventing "pull the card, swap the phone" bypass of the lock screen.
- <strong>eSIM advantages</strong>: No physical card to be pulled out, higher security; also supports multi-number switching, very convenient for travel.
- <strong>Secondary card swap risk</strong>: Beware of the "carrier secondary card swap" scam—scammers use your identity to reissue a SIM card, thereby taking over your phone number. Setting "card replacement requires the account holder to appear in person at a store with ID" is the most effective defense.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Things You Must Never Do

{class="list-disc pl-6 mt-1 space-y-1 text-sm"}
- Use weak passwords like birthdays / 123456 / qwerty;
- Send verification codes to anyone (even "customer service");
- Click unfamiliar links in text messages, especially those from overseas numbers starting with 00;
- Log into online banking or make payments on public Wi-Fi;
- Enable "screen sharing" or "remote control" for strangers.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Try Enabling and Simulating "Remote Lock"

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Make sure your "Find My Phone" feature is enabled.
2. On a computer browser or another phone, log into the corresponding cloud service account (iCloud.com or brand cloud service website).
3. Find the "Find Device" feature, try initiating a "Play Sound" or simulating a "Lock" command on your own phone to familiarize yourself with the entire process.
:::
