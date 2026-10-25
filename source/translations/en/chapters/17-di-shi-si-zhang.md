---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: Chapter 14: Password Managers
toc: default
kind: chapter
---

### Chapter 14: Password Managers

{class="chapter-intro mb-4"}
In the digital age, your passwords are the keys to your front door. But with too many keys, all too complex—what then? A password manager is your "universal key butler".

#### I. Why Do You Need a Password Manager?

Modern people have dozens or even hundreds of online accounts on average. If every account uses the same password, one hacked website puts all accounts at risk. If every account uses a different complex password, they are impossible to remember.

A password manager solves this dilemma: you only need to remember one master password, and it remembers all the others for you.

#### 2. How Password Managers Work

1. <strong>Encrypted Storage</strong>: All passwords are stored with high-strength encryption, and only you can decrypt them.
2. <strong>Master Password</strong>: You set a master password to unlock the password vault. The master password itself is not stored on the server.
3. <strong>Auto-Fill</strong>: On website or app login pages, the password manager automatically fills in your account and password.
4. <strong>Password Generation</strong>: Can generate random, complex passwords to improve security.

#### III. Introduction to Encryption Principles

Understanding the encryption principles behind password managers helps you judge whether a service provider is trustworthy. Below are several core concepts explained in plain language.

##### 1. AES-256 Encryption

AES (Advanced Encryption Standard) is a symmetric encryption algorithm certified by the U.S. National Institute of Standards and Technology (NIST), widely used by banks, military, and government. "256" refers to the 256-bit key length — it would theoretically take longer than the age of the universe to brute-force. Mainstream password managers (1Password, Bitwarden, KeePass, etc.) all use AES-256 to encrypt your password vault.

##### 2. Zero-Knowledge Architecture

"Zero-knowledge" doesn't mean the service provider stores nothing — it means that <strong>encryption and decryption are both done locally on your device, and the server only stores encrypted ciphertext</strong>. The specific process:

1. You enter your master password in the client.
2. The client derives an encryption key from the master password (this happens on your phone/computer).
3. Only the encrypted ciphertext is uploaded to the server.
4. On next login, the server sends back the ciphertext, and the client decrypts it again using your master password.

Key Point:<strong>The master password itself never leaves your device</strong>, and the server doesn't have it either. So even if the service provider is hacked, the attacker only gets a pile of unbreakable ciphertext — unless they can guess your master password.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Why does "zero-knowledge" mean the service provider can't see your passwords either?

{class="mt-1"}
Because the decryption key is derived from your master password, which exists only in your mind and is used only on your local device. The service provider's server has neither the master password nor the decryption key — only ciphertext. That's why legitimate providers like Bitwarden and 1Password explicitly state "we cannot see your passwords either" — it's not that they don't want to, it's that they technically can't.
:::

##### 3. Key Derivation Functions: PBKDF2 and Argon2

The master password can't be used directly as an encryption key — it needs to be processed by a "key derivation function." The purpose of this function is to <strong>deliberately slow down computation</strong>, making the cost of brute-force attacks prohibitively high.

- <strong>PBKDF2</strong>: A well-established standard, widely used by iCloud Keychain, Bitwarden, LastPass, and others. Slows down cracking through repeated iteration (typically 100,000+ times) of hashing.
- <strong>Argon2</strong>: The winner of the 2015 Password Hashing Competition, more modern than PBKDF2. In addition to "computational cost," it introduces "memory cost" — making it difficult for specialized hardware like GPUs/ASICs to accelerate cracking. Already supported by Bitwarden, KeePassXC, and others.

Higher iteration counts are more secure but also slower to unlock. Legitimate providers publicly disclose their derivation algorithm and iteration counts for security community auditing.

##### 4. Case Study: The LastPass 2022 Data Breach

In August 2022, the veteran password manager LastPass announced that its development environment was breached; in November of the same year, it further disclosed that hackers had taken backups of users' password vaults (encrypted ciphertext). Key lessons from the incident:

- <strong>Zero-Knowledge Architecture Held the Line</strong>: Since the password vault was encrypted, hackers got the ciphertext but couldn't decrypt it — provided the user's master password was strong enough.
- <strong>Users with Weak Master Passwords Are Most at Risk</strong>: Hackers can brute-force weak master passwords offline, so users with weak or reused master passwords face real risk.
- <strong>Metadata Was Also Leaked</strong>: Although password contents were encrypted, metadata like site URLs and notes may not have been, revealing which services the user used.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Lessons Learned from LastPass

{class="mt-1"}
First, your master password must be long and unique (16+ characters recommended, with upper/lower case, digits, and symbols); second, prioritize providers that support Argon2id with high iteration counts; third, always enable independent two-factor authentication for high-value accounts (bank, email) — don't rely solely on a password manager.
:::

#### IV. Mainstream Password Manager Recommendations

##### System Built-in:

- <strong>iCloud Keychain</strong>: The first choice for Apple ecosystem users. Seamlessly integrated with Safari and apps, free, secure. The downside is that cross-platform use is inconvenient.
- <strong>Google Password Manager</strong>: Convenient for Android users. Integrates with Chrome and the Android system, free.
- <strong>Huawei Password Vault</strong>: Built into HarmonyOS, suitable for Huawei users.

##### Third-Party Professional Tools:

- <strong>Bitwarden</strong>: Open source and free, powerful, supports all platforms. Highly recommended for privacy-conscious users.
- <strong>1Password</strong>: Beautiful interface, rich features, suitable for families and teams. Paid.
- <strong>LastPass</strong>: A long-established password manager, with limited features in the free version.
- <strong>KeePass</strong>: Completely local storage, open source and free. Suitable for geek users.

#### V. Real Password Strength Assessment

Password managers generally display a "password strength" indicator bar (red/yellow/green), but this assessment often only considers length and character variety, which isn't comprehensive. To truly judge whether a password is secure, you need to consider "entropy" and "whether it has been leaked."

##### 1. Entropy: The Scientific Measure of Password Strength

"Entropy" measures the uncertainty of a password, measured in bits. The higher the entropy, the more attempts are needed for brute-force cracking.

- <strong>"123456"</strong>: Extremely low entropy, cracked instantly.
- <strong>"P@ssw0rd"</strong>: Appears complex, but appears in all dictionary attack lists, so entropy is still low.
- <strong>"correct horse battery staple"</strong>: Four random words, approximately 44 bits of entropy, far harder to crack than "P@ssw0rd."
- <strong>16 random characters (including upper/lower case + digits + symbols)</strong>: Approximately 100 bits of entropy, uncrackable by brute force with current computing power.

Conclusion:<strong>"Length + randomness" is more important than "complex symbols"</strong>. This is why the random long passwords generated by password managers are truly secure.

##### 2. HaveIBeenPwned: Check If Your Password Has Been Leaked

Maintained by security researcher Troy Hunt, <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a> it collects accounts and passwords leaked in major data breaches. You can:

1. Enter your email to check if your account was exposed in a breach.
2. Use the Pwned Passwords feature to check if a password is in the known leaked database (password managers and browsers have this built in).

If a password appears in the leaked database,<strong>no matter how complex it looks, you must change it immediately</strong>— because dictionary attacks prioritize these known passwords.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity Query Principle

{class="mt-1"}
Worried that entering your password on HaveIBeenPwned will cause another leak? No need to worry. Modern queries use the "k-anonymity" protocol: the browser only sends the first 5 characters of the password hash to the server, the server returns all hashes starting with those 5 characters, and the comparison is done locally. In other words, the server never sees your complete password hash. 1Password and Bitwarden's "leaked password detection" both work this way.
:::

##### 3. Built-in Monitoring Features in Password Managers

- <strong>1Password Watchtower</strong>: Real-time monitoring of weak passwords, reused passwords, leaked passwords, expired passwords, and sites not using 2FA, displayed with red/orange/yellow severity levels.
- <strong>Bitwarden Vault Health</strong>: Free version shows weak and reused passwords; paid version can detect leaked passwords (based on HaveIBeenPwned).
- <strong>iCloud Keychain "Security Recommendations"</strong>: iOS Settings → Passwords → Security Recommendations, alerts you which passwords appear in known leaks and which are reused.
- <strong>Google Password Manager "Password Checkup"</strong>: Built into Chrome, can one-tap check for leaked, weak, and reused passwords.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Check Now: Are Your Passwords Safe?

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Go to haveibeenpwned.com, enter your commonly used email, and see which breach events it appeared in.
2. iPhone users: Settings → Passwords → Security Recommendations, address each red warning one by one.
3. Chrome users: Settings → Passwords → Check Passwords, follow prompts to change.
4. 1Password/Bitwarden users: Open Watchtower/Health Reports, prioritize "leaked" and "reused" items.
:::

#### VI. Passkey: The Future of Passwordless Login

In 2024-2026, password technology is undergoing a revolution —<strong>Passkey</strong> is poised to completely replace traditional passwords. Jointly promoted by Apple, Google, and Microsoft, endorsed by the FIDO Alliance and the World Wide Web Consortium (W3C), this is the biggest change in login methods in decades.

##### 1. What Is Passkey?

Passkey is based on the FIDO2 / WebAuthn standard, using <strong>on-device key pairs</strong> to replace passwords. The principle can be simplified as:

- Your phone generates a key pair:<strong>Public key</strong>(registered with the website) + <strong>Private key</strong>(permanently stored in your device's secure chip).
- When logging in, the website sends a "challenge," your phone signs it with the private key, and the website verifies it with the public key.
- Before signing, you need to confirm your identity via biometrics (Face ID / fingerprint) or device PIN.
- Throughout this process,<strong>no password is transmitted over the network</strong>.

##### 2. Passkey vs. Traditional Passwords

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Dimension</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Traditional Password</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Phishing Resistance</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Poor, phishing sites can steal passwords</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Naturally phishing-resistant, private key only signs for real domains</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Server Breach Impact</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Password hashes may be cracked</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Server only stores public key, no impact from breach</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Convenience</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Requires memorization/entry/management</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/fingerprint login in one second</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Replay Attack</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">May be intercepted and replayed by man-in-the-middle</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Each signature is one-time, cannot be replayed</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. Platform Support Status

- <strong>Apple iCloud Keychain Passkey</strong>: Native support on iOS 16+ / macOS Ventura+, Passkeys sync across all devices signed in with the same Apple ID, no need to recreate on new devices.
- <strong>Google Password Manager Passkey</strong>: Native support on Android + Chrome, Passkeys stored in Google Account, sync across Android devices; since 2023, Google personal accounts support Passkey login.
- <strong>Microsoft</strong>: Windows 11 / Edge already supports Passkey; Microsoft Account, Outlook, Office and other services are gradually opening up Passkey login, manageable in Microsoft Authenticator.
- <strong>1Password / Bitwarden</strong>: Already supports Passkey creation, storage, and cross-platform sync, freeing you from being locked into a single ecosystem.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Cross-Device Sync Is the Key Breakthrough

{class="mt-1"}
The biggest pain point of early Passkey was being "bound to a single device" — you had to recreate it when switching phones. Starting in 2023, Apple, Google, and Microsoft implemented cloud sync for Passkeys: iCloud Keychain syncs across Apple devices, Google Password Manager syncs across Android devices. Third parties like 1Password have enabled cross-ecosystem sync. This means Passkey is now practical enough to replace passwords.
:::

##### 4. How to Create and Use Passkey on Your Phone

<strong>iOS (iPhone) Path:</strong>

1. On the account security page of a Passkey-supporting website (such as Google, Microsoft, Amazon, eBay, PayPal), select "Add passkey."
2. The system shows a Face ID / Touch ID verification window. Once verified, the Passkey is automatically generated and saved to iCloud Keychain.
3. Next time you log in to this website, enter your username and select "Sign in with iPhone" — just a Face ID scan and you're in.
4. Management: Settings → Passwords → find the corresponding website to see the Passkey entry.

<strong>Android Path:</strong>

1. On the account security page of a Passkey-supporting website, select "Add passkey."
2. Google Password Manager popup → select your Google account → screen lock verification (fingerprint/pattern/PIN).
3. Passkey is automatically saved to Google Password Manager and synced across Android devices with the same account.
4. Next time you log in, select "Use Passkey" — just unlock your screen and you're in.
5. Management: Android Settings → Passwords, passkeys &amp; autofill → Password Manager → google.com.

##### 5. Cross-Device Passkey Login

If you're on a Windows PC logging into a website that only has a Passkey on your iPhone, you can authorize via QR code scan:

1. On the website login page, select "Use Passkey."
2. Select "Use another device."
3. The PC displays a QR code — scan it with your iPhone.
4. iPhone shows a Face ID verification, and upon confirmation, the website login is completed on the PC.

This process uses dual encrypted communication via Bluetooth + internet — the Passkey private key never leaves your iPhone.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Try It Now: Experience Passwordless Login

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Sign in to your Google Account → Security → Passkeys → Add a passkey, experience Face ID/fingerprint login.
2. Sign in to your Microsoft account → Security → Advanced Security Options → Add a passkey.
3. Try it on services that already support Passkey, such as Taobao, JD.com, eBay, and PayPal.
4. Keep traditional passwords as backup, gradually migrate high-value accounts to Passkey.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Transition Period Recommendations

{class="mt-1"}
Passkey hasn't completely replaced passwords — many websites are still in a "Passkey + password" coexistence phase. Recommendation: prioritize enabling Passkey for high-value accounts, but <strong>don't immediately delete traditional passwords</strong>, keep them as backup; continue using your password manager, since not all websites support Passkey. Treat Passkey as a "powerful supplement to password managers" rather than an "immediate replacement."
:::

#### VII. Hardware Security Keys

If your security requirements exceed those of ordinary users — for example, if you hold significant cryptocurrency, are an executive/journalist/activist, or protect enterprise core accounts — hardware security keys are a more reliable choice than SMS verification codes.

##### 1. What Is a Hardware Security Key?

A hardware key is a physical device (shaped like a USB drive) with an internal security chip that stores your private key, requiring physical contact or NFC to complete authentication. Representative products:

- <strong>YubiKey</strong>(Yubico): The most mainstream, supports FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGP, with USB-C / USB-A / NFC and other interfaces. Series 5 costs $50-70.
- <strong>Google Titan</strong>: Made by Google, USB-C + NFC / Bluetooth, about $30-40.
- <strong>OnlyKey</strong>: Open-source alternative, supports multiple protocols.
- <strong>Domestic Alternatives</strong>: Such as Feitian ePasskey, more affordable.

##### 2. Why Are Hardware Keys Safer Than SMS Verification Codes?

- <strong>Phishing Resistance</strong>: Like Passkey, hardware keys only respond to the real domain, so phishing sites can't trick them into providing verification codes.
- <strong>SIM-Swap Resistance</strong>: SMS verification codes can be intercepted via SIM-swap attacks, while hardware keys don't need a phone number.
- <strong>Man-in-the-Middle Resistance</strong>: The FIDO2 protocol includes a challenge value in each signature, preventing replay.
- <strong>Physical Isolation</strong>: The private key remains inside the hardware chip forever — even if malware compromises your computer, it can't read it.

##### 3. Applicable Scenarios

- Cryptocurrency exchange accounts, wallet recovery.
- Enterprise SSO, remote work VPN, SSH server login.
- Email, GitHub, social media and other "master accounts" — once compromised, all other accounts can be reset.
- Journalists, lawyers, executives, and other high-sensitivity individuals.

##### 4. How to Configure a Hardware Key as Two-Factor Authentication

Using a Google Account + YubiKey as an example:

1. Purchase a YubiKey (recommended to buy two at once — one for daily use and one as backup, stored in different locations).
2. Sign in to myaccount.google.com → Security → 2-Step Verification.
3. Select "Add security key" → insert the YubiKey into the USB-C port or tap it against your phone's NFC sensor.
4. Follow the prompt to touch the YubiKey's metal contact to complete registration.
5. It's recommended to register a second backup key.
6. In the "2-Step Verification" settings, set the hardware key as the preferred verification method, with SMS as backup.

Websites with mainstream support: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance, and more.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Dual-Key Strategy

{class="mt-1"}
The biggest risk of hardware keys is "loss." Recommendations: ① Register two different keys simultaneously; ② Carry one with you (on a keychain) and store one in a home safe or bank deposit box; ③ Some websites allow printing "backup recovery codes" for offline storage. This way, even if the primary key is lost, you won't be permanently locked out of your accounts.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Be Careful with Purchase Channels

{class="mt-1"}
Always purchase from official stores or authorized dealers — don't buy used or keys from unknown sources, as pre-configured hardware could theoretically have been implanted with a backdoor. YubiKey firmware cannot be updated after manufacturing, but Yubico continuously publishes security advisories — follow their official website.
:::

#### VIII. Family/Team Password Sharing

In family scenarios, Netflix, home Wi-Fi, router admin, and smart lock passwords need to be shared among the whole family; in team scenarios, servers, databases, and social media accounts require multi-person collaboration.<strong>Sending passwords via WeChat or writing them in shared documents are high-risk practices</strong>— once chat history or document permissions are leaked, the passwords are leaked too.

##### 1. 1Password's "Shared Vaults"

1Password is the benchmark product for family and team sharing. Its core mechanism is <strong>multiple vaults</strong>:

- <strong>Personal Vault</strong>: Only you can see it, for private accounts like banks and email.
- <strong>Shared Vault</strong>: Family or team members can all see it, for shared items like Netflix, home Wi-Fi, and shared credit cards.
- <strong>Permission Tiers</strong>: The team version can set certain members to "view only" or "view but not edit."

Family or team members don't need to share a master password — each logs in with their own account and can see the shared vault content they're authorized for. Password changes sync in real-time to all members.

##### 2. Bitwarden's "Organizations" Feature

Bitwarden's free version supports individual password sharing (via the "Send" feature for time-limited sharing of a single password); the paid version can create "Organizations" to share entries with family or team colleagues with fine-grained permissions. Bitwarden also offers a self-hosted option, suitable for enterprises with high data sovereignty requirements.

##### 3. Family Scenarios: Secure Ways to Share Netflix, Wi-Fi, and Other Passwords

- <strong>Netflix / Streaming Sites</strong>: Store login passwords in 1Password Families' "Shared Vault" — family members log in individually without sharing in a group chat.
- <strong>Home Wi-Fi Password</strong>: iOS devices can share Wi-Fi passwords directly via AirDrop to visiting guests without reading it aloud; Android 12+ also has a "Nearby Share Wi-Fi" feature.
- <strong>Smart Locks, Smart Appliances</strong>: Use the manufacturer app's "Family Members" feature to create individual accounts for each person, rather than sharing one admin account.
- <strong>Home Router Admin</strong>: Store the admin password in a 1Password Shared Vault, and set up a separate SSID for guest Wi-Fi.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password Families Value for Money

{class="mt-1"}
1Password Families costs about $4.99/month, supporting up to 5 family members, each with an independent personal vault + 4 shared vaults. That's less than $1/person/month — currently the best family sharing experience. Bitwarden's family plan at $10/year supports 6 people, offering better value but with a slightly less polished interface.
:::

##### 4. Team Scenarios: Server/Database Password Sharing

- <strong>1Password Teams / Business</strong>: Can create multiple vaults by department and project team, with fine-grained permission control and auditable access logs.
- <strong>Bitwarden Teams / Enterprise</strong>: Open-source solution, self-hostable, enterprise version supports SSO integration and directory sync.
- <strong>Separation of Duties Principle</strong>: Admin passwords should not be held by only one person — designate 2-3 "emergency contacts" to ensure business continuity when key personnel leave or take vacation.
- <strong>Offboarding Process</strong>: Immediately revoke departing employees' password manager access, and rotate all high-sensitivity passwords they had access to if necessary.

##### 5. Emergency Access: In Case Something Happens to You

Imagine a scenario: you alone manage all the family's important accounts, but you're unexpectedly hospitalized or pass away, and your family can't log into the bank, email, or insurance accounts.<strong>The "Emergency Access" feature</strong> is designed exactly for this — authorize a trusted family member/friend to access your password vault when you can't respond.

<strong>Bitwarden Emergency Access Setup:</strong>

1. Log in to Bitwarden Web Vault → Settings → Emergency Access.
2. Add the trusted contact's email and invite them to accept.
3. Set a "wait period" (7-14 days recommended): the time window from when they make a request to when you confirm.
4. If you don't respond during the wait period (decline or take no action), the other person automatically gains access after it expires.
5. You can manually reject requests or revoke emergency access permissions at any time.

<strong>1Password Emergency Access:</strong>

1. 1Password doesn't call it "Emergency Access" directly, but it can be achieved through the "Family/Team Organization" feature — after adding family members to the family plan, place some entries in a "Shared Vault."
2. For individual plan users, it's recommended to tell one highly trusted family member your master password, or write it in a sealed envelope stored in a safe.
3. 1Password also provides a "Recovery Code" — be sure to print and save it when enabling two-factor authentication.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Set Up Now: Leave a "Spare Key" for Your Family

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Choose a trusted family member as your "emergency contact."
2. Set up emergency access in your password manager (Bitwarden) or add them to a family shared vault (1Password).
3. Write the master password + recovery code on paper, seal in an envelope, store in a home safe or inform a trusted family member.
4. Review every six months to confirm the emergency contact is still appropriate.
:::

#### IX. Password Manager Best Practices

- <strong>Set a Strong Master Password</strong>: The master password is the last line of defense — make sure to set a long, complex password and memorize it firmly.
- <strong>Enable Two-Factor Authentication</strong>: Turn on 2FA for your password manager account to add a layer of protection.
- <strong>Regularly Check for Weak Passwords</strong>: Most password managers have a "security audit" feature that helps you find weak and duplicate passwords.
- <strong>Don't Forget the Master Password</strong>: The master password cannot be recovered — forgetting it means losing all passwords. It's recommended to write it down on paper and keep it in a safe place.
- <strong>Emergency Access</strong>: Set up an emergency contact, so if you can't access your account, a trusted person can obtain your passwords.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Important Reminder

{class="mt-1"}
Password managers are convenient but come with risks: if your master password leaks, all your passwords are exposed. So your master password must never reuse any other password, nor be written somewhere easily found. Also, choose a provider with a good security track record.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Try It Now: Get Started with a Password Manager

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Pick a password manager (Bitwarden or your system’s built-in one is recommended).
2. Register an account and set a strong master password.
3. Import existing passwords (if any) or start adding new passwords.
4. Install the browser extension or mobile app, and experience the auto-fill feature.
5. Check the security audit report to find passwords that need improvement.
:::
