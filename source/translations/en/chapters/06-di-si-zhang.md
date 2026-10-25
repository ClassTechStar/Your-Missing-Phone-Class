---
id: di-si-zhang
num: 04
part: ji-chu-pian
nav: Chapter 4: Installing and Managing Apps
toc: default
kind: chapter
---

### Chapter 4: Installing and Managing Apps

{class="chapter-intro mb-4"}
Apps make your phone capable of anything, but they need to be managed. Just like you'd assign a new employee a desk and permissions, installing apps requires a standardized process.

#### I. Official App Stores: The Safest "App Supermarket"

- <strong>Android</strong>: Google Play (outside China) or each brand's built-in store (such as Huawei AppGallery or Xiaomi GetApps).
- <strong>iOS</strong>: Only the App Store.
- <strong>HarmonyOS</strong>: Huawei AppGallery.

Core security value: reviewed, guaranteed updates, payment security. Action guideline:<strong>prioritize downloading only from official stores!</strong>

#### II. Pure/Protection Mode: Turn On Your Phone's "Antivirus Wall"

Mainstream domestic brands (Huawei, Xiaomi, OPPO, vivo, Honor) all have a built-in <strong>Pure Mode</strong> or <strong>Protection Mode</strong>—a system-level security switch.<strong>Strongly recommended for all users to enable</strong>.

##### 1. What exactly is it?

The core function of Pure Mode (also called "Protection Mode") is to <strong>block third-party app installations</strong>: when enabled, the system will <strong>only allow app installations from the official app store</strong>. Installation packages downloaded from browsers, QR codes, chat apps, and other channels will be directly intercepted, eliminating malware at the source.

##### 2. Who it's for

- <strong>Elderly users</strong>: Can't tell "official" from "fake" ads—Pure Mode is the most reliable safeguard.
- <strong>Users insensitive to app permissions</strong>: Don't need to install niche apps, beta versions, or foreign-region games.
- <strong>All users who want to improve device security</strong>: Even for power users, having it on is better than off—if you have a temporary need, just turn it off briefly.

##### 3. How to enable (taking Huawei/Xiaomi as examples)

- <strong>Huawei/HarmonyOS</strong>: [Settings] &gt; [System &amp; Updates] &gt; <strong>[Pure Mode]</strong>, select "Enable."
- <strong>Xiaomi</strong>: [Settings] &gt; [Privacy Protection] &gt; <strong>[Protect Privacy]</strong> , or [Settings] &gt; [App Settings] &gt; [App Installation], turn off "Install unknown apps."
- <strong>OPPO/vivo</strong>: [Settings] &gt; [Security] &gt; <strong>[Install Apps from External Sources]</strong>, turn off each authorization one by one.

{class="font-semibold mt-4 mb-1"}
##### 4. App Store Security Detection Mechanisms

App stores aren't just for show—there's a complete security pipeline behind them:

- <strong>Virus scanning</strong>: Each app is jointly scanned by multiple antivirus engines before listing, to identify known trojan and virus signatures.
- <strong>Permission review</strong>: The store reviews whether the permissions an app requests are "reasonable"—a flashlight app asking for contacts? Directly rejected or delisted.
- <strong>Developer certification</strong>: Listing requires enterprise qualification, personal ID, or credit card verification. If problems arise, someone can be held accountable—not a "black app."
- <strong>Continuous monitoring</strong>: Listed apps are also continuously rescanned, and newly discovered malicious behavior results in forced delisting.

#### III. Third-Party Sources and "Electronic Parasites": Extremely High Risk!

Downloading apps from webpages or unknown links may bundle viruses, steal privacy, or commit payment fraud. Here we specifically mention a new concept:<strong>"electronic parasites."</strong>.

::: div .danger-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-bug mr-2"></i>What are "electronic parasites"?

{class="mt-1"}
This refers to <strong>.</strong>—you think you "saved money," but actually "got infected." Common forms:

{class="list-disc pl-6 mt-2 space-y-1 text-sm"}
- "Cracked," "free," "ad-free" versions of paid software;
- "Like-farming," "red packet grabbing," "game cheats" and other gray-area tools;
- So-called "internal versions" of apps recommended by "small ads" in group chats.

{class="mt-2"}
These programs appear usable, but behind the scenes they may be <strong>stealing contacts, reading SMS, eavesdropping on the microphone, mining in the background</strong>. Pure Mode is the <strong>first line of defense</strong> against them—simply not letting you install them.
:::

##### Second line of defense recommendations:

- <strong>Regular full virus scans</strong>: Use the phone's built-in security center (like Huawei Phone Manager, Xiaomi Security Center) to scan once a month.
- <strong>Cautiously grant sensitive permissions</strong>: Contacts, SMS, location, camera, microphone—these five "high-risk permissions" must be strictly reviewed.
- <strong>Watch for battery and data anomalies</strong>: Phone suddenly heating up, battery draining fast, data running at night—most likely a "parasite" hiding in the background.

If you absolutely must install a third-party app:

1. Ensure the source is absolutely trustworthy.
2. Carefully review permission requests before installing.
3. Scan with a security app afterward.

Ultimate advice: In system settings, turn off the "Install unknown apps" permission.

#### IV. Install, Update, Uninstall

- <strong>Install</strong>: Tap "Get" or "Install" in the store. After installation, the first launch will ask for permissions.
- <strong>Update</strong>:<strong>Must update!</strong> Mainly to fix security vulnerabilities. Recommend enabling auto-update.
- <strong>Uninstall</strong>: Long-press the icon and drag to the uninstall area. For a more thorough clean, go to [Settings] &gt; [App Management] to find and uninstall.

#### V. Permission Management: You Are the App's "Boss"

Apps requesting permissions (like contacts, location) is sometimes reasonable (maps need location), sometimes not (flashlight needs contacts).

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Permission options</strong>: "Always allow," "Only while using the app," "Deny," "Ask every time."</li>
                        <li><strong>Management principles</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Minimization: Don't grant unless necessary.</li>
                                <li>Post-audit: Regularly check permission settings to see who's "overstepping."</li>
                                <li>Context-based: Like ride-hailing apps, only grant location permission while in use.</li>
                            </ol>
                        </li>
                    </ul>
```

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>Key Permissions to Watch

{class="list-disc pl-6 mt-1 space-y-1"}
- Contacts/SMS: May be used to send spam messages.
- Real-time location: Your movements may be tracked.
- Camera/Microphone: May be used for secret photography/recording.
- File access: May read your private files.
:::

{id="di-si-zhang-apk"}
#### VI. Components of an App Installation Package

Have you ever wondered what's inside that installation package you download from the app store? Understanding the components of an installation package helps you better understand how apps work, and when problems arise, you'll know where to look.

##### 1. Android APK File Structure

An APK (Android Package Kit) is essentially a ZIP archive. After extraction, you can see the following core directories and files:

- <strong>AndroidManifest.xml</strong>: The app's "ID card" and "instruction manual." Records core information like app package name, version number, required permissions, supported system versions, entry Activity, etc. The system reads this file first when installing the app.
- <strong>classes.dex</strong>: The app's core code. Java/Kotlin source code is compiled into Dalvik bytecode and stored in this file. An app may have multiple dex files (like classes2.dex, classes3.dex).
- <strong>resources.arsc</strong>: The compiled resource index table. Records the IDs and corresponding relationships of all resources.
- <strong>res/ directory</strong>: Resource folder. Contains images, layout files, strings, color definitions, etc. Images for different resolutions are placed in different drawable folders (like drawable-hdpi, drawable-xhdpi).
- <strong>assets/ directory</strong>: Raw resource folder. Stores resources that don't need compilation, such as web files, fonts, audio, etc. Apps can read them via AssetManager at runtime.
- <strong>lib/ directory</strong>: Native library folder. Stores compiled .so files (C/C++ compilation output), categorized by CPU architecture (like arm64-v8a, armeabi-v7a). Games and apps requiring high-performance computation usually have this directory.
- <strong>META-INF/ directory</strong>: Signature information folder. Contains MANIFEST.MF, CERT.SF, CERT.RSA files, used to verify the APK's integrity and signature.

##### 2. iOS IPA File Structure

IPA (iOS App Store Package) is also a compressed archive, with a slightly different structure:

- <strong>Payload/ directory</strong>: Where the core content lives. Inside is a .app folder containing all the app's content.
- <strong>Info.plist</strong>: The app's configuration file, similar to Android's AndroidManifest.xml. Records app ID, version, permission requirements, supported devices, etc.
- <strong>Executable file</strong>: The main program with the same name as the .app folder, a compiled Mach-O format binary.
- <strong>Frameworks/ directory</strong>: Dynamic libraries and frameworks the app depends on.
- <strong>Resource files</strong>: Images, audio, video, and other resources, usually stored inside the .app folder.
- <strong>_CodeSignature/ directory</strong>: Code signature information, used to verify the app's integrity and origin.

##### 3. Signature Verification Mechanism

Why are apps downloaded from official stores safer? Signature verification is key.

```html
<ul class="list-disc pl-6 mb-3 space-y-1">
                        <li><strong>Android signing</strong>: Developers sign APKs with private keys, and the system verifies with public keys during installation. If an APK is tampered with (e.g., implanted with a virus), the signature becomes invalid and the system refuses to install. Google Play also requires App Signing, where Google holds the signing key, further protecting app security.</li>
                        <li><strong>iOS signing</strong>: Apple's review is stricter. Every IPA must be signed with a certificate issued by Apple, otherwise it cannot be installed. This is why iOS can only install apps from the App Store or enterprise certificates. Apps signed with enterprise certificates have limited validity and Apple can revoke them at any time.</li>
                        <li><strong>Role of signatures</strong>:
                            <ol class="list-alpha pl-6 mt-1 space-y-1">
                                <li>Verify origin: Confirm the app indeed comes from the claimed developer.</li>
                                <li>Verify integrity: Ensure the app wasn't tampered with during transmission.</li>
                                <li>Prevent impersonation: A malicious app cannot disguise itself as another app.</li>
                            </ol>
                        </li>
                    </ul>
```

##### 4. Installation Package Size and Optimization

You may notice that the app size shown in the app store differs from the space it occupies after installation. This is because:

- <strong>Download size</strong>: The compressed APK/IPA size.
- <strong>Installation size</strong>: The extracted size, usually much larger than the download size.
- <strong>Runtime footprint</strong>: Apps also generate cache and data files at runtime, occupying more space.

Modern app optimization methods:

- <strong>App Bundle (Android)</strong>: Google Play's dynamic delivery technology. Users only download resources suited to their device when downloading (e.g., only images for the corresponding screen resolution), greatly reducing download size.
- <strong>App Thinning (iOS)</strong>: Similar technology—Apple automatically trims unneeded resources based on the device.
- <strong>On-demand download</strong>: Large apps like games can download the core package first, then download resource packs later.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Trivia: Why are some app installation packages so large?

{class="mt-1"}
Game apps are usually the largest because they contain lots of high-definition textures, 3D models, and audio files. Social apps are also quite large because they need to support various functional modules. Tool apps are usually the smallest. If you find a tool app that's unusually large, be alert to whether it bundles unnecessary features.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hands-On: Audit 3 Apps' Permissions

{class="mt-1"}
Pick 3 commonly used apps (e.g., social, shopping, tool), go to the app permission management page in [Settings], review each item, and turn off or change unnecessary sensitive permissions to "Only while using the app."
:::
