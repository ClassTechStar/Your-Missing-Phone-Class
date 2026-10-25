---
id: di-er-shi-si-zhang
num: 24
part: chao-yue-pian
nav: Chapter 24: Root Access and the Bootloader Lock Explained
toc: default
kind: chapter
---

### Chapter 24: Root Access and the Bootloader Lock Explained

{class="chapter-intro mb-4"}
This chapter is an in-depth expansion of Chapter 20, suitable for users who want to truly understand the underlying mechanisms of phones or even try flashing. Please note that these operations carry certain risks, so proceed with caution.

#### 1. Deep Understanding of Bootloader

Bootloader is the first program to run when the phone starts; its task is to initialize hardware and load the operating system kernel. You can think of Bootloader as the phone's "gatekeeper."

##### How BL Lock Works:

- <strong>Verify signature</strong>: BL lock verifies the digital signature of the boot image; only manufacturer-signed systems can boot.
- <strong>Prevent downgrade</strong>: Prevents users from flashing older system versions to exploit known vulnerabilities.
- <strong>Protect data</strong>: Even if a new system is flashed, user data cannot be accessed without the original account password.

##### 2. Detailed Process for Unlocking BL Lock (Using Xiaomi as an Example)

Apply for unlock permission

##### : Apply for unlocking on the Xiaomi Unlock Tool website.

Bind account

1. : Bind your Xiaomi account in phone settings.
2. 🔐 Hardware-Level Storage and Verification
3. The BL lock status (Locked/Unlocked) and the manufacturer's public key are typically stored in protected hardware areas (such as Qualcomm's devinfo partition, eFuse, or RPMB partition) to prevent software tampering. On each boot, the Bootloader reads the status from this secure area and decides whether to perform strict signature verification.

##### 🔏 Digital Signature Verification

When manufacturers release system updates or images, they sign them with their private keys. At device boot, the Bootloader verifies the system images (such as boot.img, recovery.img) using the built-in public key. The process works as follows:

##### Recalculate the hash value of the system image.

Decrypt the image's built-in signature with the public key to obtain a hash value.

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm">
                            <thead>
                                <tr class="bg-gray-100 dark:bg-gray-800">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Compare the two hash values — if they match, verification passes. This ensures the system image hasn't been tampered with by third parties.</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">🔗 Secure Boot Chain</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">The BL lock is the first link in the entire secure boot chain. Only after it passes verification does it load and execute the next stage bootloader (such as the kernel), ensuring the trustworthiness of the system boot environment layer by layer.</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">📊 Locked vs. Unlocked: The Dual Impact of BL Lock</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">To more intuitively understand the pros and cons of the BL lock, here's a comparison table showing its impact across 5 core dimensions:<br><span class="text-emerald-600 dark:text-emerald-400">Core Role</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">Locked State (Default)</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">Unlocked State</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System Security<br><span class="text-emerald-600 dark:text-emerald-400">Prevents flashing unsigned unofficial systems, protects system integrity and low-level security</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">✅ High security: only loads officially signed images, effectively resists malicious firmware tampering</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">⚠️ Reduced security: allows flashing third-party ROMs, system integrity verification fails, malware with Root access can deeply tamper with the system</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">System Stability<br><span class="text-emerald-600 dark:text-emerald-400">Ensures the phone runs the manufacturer-tested and optimized official system, guaranteeing stability and smoothness</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">✅ Stable: uses official firmware, complete features, reliable OTA updates</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">⚠️ Increased risk: third-party ROMs may have compatibility issues, potentially causing system crashes, bricking, hardware function anomalies (such as camera, fast charging), OTA update failures</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Warranty Rights<br><span class="text-emerald-600 dark:text-emerald-400">Manufacturers provide warranty service by locking BL to ensure a stable official system</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">✅ Warranty valid: enjoy official free warranty service (non-artificial damage)</span></td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">⚠️ Warranty void: most manufacturers consider BL unlocking as voluntarily waiving warranty. Even if relocked, historical unlock records may be detected and warranty refused</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Data Security<br><span class="text-emerald-600 dark:text-emerald-400">The unlock process usually forces data wipe to prevent old data from being maliciously exploited in the new system environment</span></td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2"><span class="text-amber-600 dark:text-amber-400">✅ Data security: in daily use, BL lock limits the ability of malware to modify the system partition</span></td>
                                </tr>
                            </tbody>
                        </table>
```
:::

#### 2. Detailed Process for Unlocking BL Lock (Using Xiaomi as an Example)

1. <strong>Feature Limitations</strong> Ensures security-dependent features (such as payment, banking apps) work normally
2. <strong>✅ Complete features: all official features work normally</strong>⚠️ Feature limited: some security-sensitive apps (such as Google Pay, banking apps) may refuse to run upon detecting BL unlock status; DRM services may be downgraded, affecting HD video playback
3. <strong>Waiting period</strong>: Depending on account level, you need to wait 7-30 days.
4. <strong>Unlock operation</strong>: Use the Xiaomi Unlock Tool to connect to your computer to unlock.

#### 3. Multiple Root Solutions

- <strong>Magisk</strong>: Modern Root solution, Systemless design, can hide Root status.
- <strong>Kernelsu</strong>: Kernel-based Root solution, more low-level, better concealment.
- <strong>SuperSU</strong>: Old-school Root solution, currently no longer updated.

#### 4. Flashing Introduction

Flashing refers to installing a new operating system on the phone. Common flashing types:

- <strong>Flash official ROM</strong>: Install the official system, used for rescuing bricked phones or downgrading.
- <strong>Flash third-party Recovery</strong>: Such as TWRP, used for backup and recovery, flashing third-party ROMs.
- <strong>Flash third-party ROM</strong>: Such as LineageOS, Pixel Experience, etc., to experience different systems.

#### V. Samsung Knox: The Irreversible Cost of Unlocking the BL

Flashing carries risks; proceed with caution. May lead to:<strong>Phone bricking (cannot boot)</strong> Loss of warranty

- <strong>Data loss</strong> V. Samsung Knox: The Irreversible Cost of BL Unlocking
- <strong>Unlike other Android manufacturers, Samsung's BL unlock mechanism has a unique "fuse" design:</strong> For Samsung phones, unlocking triggers Knox fuse tripping, permanently losing some security features (such as Samsung Pay); clears all protected data; affects warranty
- <strong>. Specifically:</strong> The Fuse Is One-Time
- <strong>: There's an eFuse inside the phone that permanently burns out once it detects BL has been unlocked — it cannot be restored.</strong> Affected Features

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>: Samsung Pay (transit cards/bank cards), Knox Secure Folder, enterprise MDM management, and some health insurance apps will all stop working.

{class="mt-1"}
Forced Data Wipe <strong>: After the fuse is triggered, the phone forces a factory reset — all local data is erased (cloud data is not affected).</strong> Warranty Impact
:::

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>Important Warning

{class="mt-1"}
Flashing carries risks—proceed with caution. It may cause:

{class="list-disc pl-6 mt-1 space-y-1"}
- Bricked phone (won’t boot)
- Loss of warranty
- Data loss
- Payment function abnormalities

{class="mt-1"}
Before flashing, be sure to make a complete backup, carefully read the tutorial, and confirm that the model and version match.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>Recommended Resources

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>XDA Developers</strong>: The world's largest Android developer community, with rich flashing tutorials and ROM resources.
- <strong>Coolapk</strong>: A well-known domestic digital community, with many Chinese tutorials and discussions.
- <strong>Various model forums</strong>: Such as Xiaomi Community, OnePlus Community, etc., with official and community tutorials.
:::

#### VI. FAQ (Q&amp; A)

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q1: Can BL Unlock Be Reversed?

{class="mb-2 pl-6"}
<strong>A:</strong> Yes, it can be relocked. Usually requires flashing the official complete firmware package and using a specific flashing script (such as Xiaomi's <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">flash_all_lock.bat</code>) to relock. However, note that after relocking, some security fuses triggered by unlocking (such as Samsung's Knox) may be irreversible.
:::

::: div .qa-item .mt-3
{class="font-semibold mb-1"}
<i class="fas fa-question-circle text-primary mr-1"></i>Q2: How to Root After Unlocking?

{class="mb-2 pl-6"}
<strong>A:</strong> Unlocking the BL is just the first step. Rooting usually requires:

{class="list-decimal pl-12 mb-2 space-y-1"}
1. Flashing a custom Recovery (such as TWRP).
2. Flashing Magisk or other Root managers through Recovery to patch the boot image and gain Root access.
:::
