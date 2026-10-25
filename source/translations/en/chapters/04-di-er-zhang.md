---
id: di-er-zhang
num: 02
part: ji-chu-pian
nav: Chapter 2: Tidying Up Your Digital Room
toc: default
kind: chapter
---

### Chapter 2: Organize Your Digital Room—File Management

{class="chapter-intro mb-4"}
Phones get messy over time, and good habits start with managing files. Just like your room needs regular tidying, your digital space needs upkeep too. An organized phone isn't just easier to find things on—it runs more smoothly too.

#### I. Three-Tier Storage System: Your Digital Warehouse

{class="list-decimal pl-6 mb-3 space-y-2"}
1. <strong>Device storage</strong>: The core zone—fast, and where the system and apps live. This is your phone's most precious space, so spend it wisely.
2. <strong>SD card (if supported)</strong>: An extra closet—slower, but good for large files like movies and photos. Note: many flagship phones no longer support SD cards.
3. <strong>Cloud storage</strong>: A safe + sync drive. Prevents loss and syncs across multiple devices. iCloud, Baidu Netdisk, and OneDrive are common choices.

#### II. Understanding the "File Manager"

Android usually has a [Files] or [File Manager] app, while iOS has the built-in [Files] app. These are the "Explorer" you use to view all files on your phone.

##### Common folder meanings:

- <strong>DCIM</strong>: Photos and videos taken by the camera.
- <strong>Pictures</strong>: Other images, such as screenshots and saved pictures.
- <strong>Download</strong>: Files downloaded by the browser.
- <strong>Music</strong>: Music files.
- <strong>Movies</strong>: Video files.
- <strong>Documents</strong>: Document files.
- <strong>Android</strong>: Android system folder containing data for each app—generally do not delete manually.

#### III. File System Structure: A Deeper Look

Android is based on Linux, so its file system has a hierarchical structure. While ordinary users don't need to dive deep, knowing some basics helps.

##### Storage partitions:

- <strong>/system</strong>: System partition, storing operating system files. Ordinary users have no access—root permission is required.
- <strong>/data</strong>: Data partition, storing user data and app data. This is the space you use day to day.
- <strong>/sdcard or /storage/emulated/0</strong>: User-accessible storage, where your photos and downloads live.

##### App data storage:

- <strong>Internal storage</strong>: The app's private space, inaccessible to other apps. Deleted when the app is uninstalled.
- <strong>External storage</strong>: Files the app stores in the user-accessible area, such as photos and downloads. Not necessarily deleted when the app is uninstalled.

#### IV. Data Backup and Recovery: Insure Your Data

Data is priceless—backup is a habit you must build.

##### Backup strategies:

1. <strong>Cloud backup</strong>: Automatic and convenient, but requires network and cloud space. iCloud, Huawei Cloud, Xiaomi Cloud, etc., all support this.
2. <strong>Local backup</strong>: Connect to a computer with a cable and back up using official tools. Fast and spacious, but requires manual operation.
3. <strong>Dual backup</strong>: Cloud + local—the safest option.

##### What to back up?

- <strong>Photos and videos</strong>: Take up the most space and are the most precious.
- <strong>Contacts</strong>: Most convenient when stored in a cloud account.
- <strong>WeChat chat history</strong>: Use WeChat's built-in backup feature.
- <strong>Important documents</strong>: Keep them on cloud drives or a computer.

#### V. File Security: Protect Your Privacy

- <strong>Encrypt sensitive files</strong>: Many phones have a "Secure Folder" or "Private Space" feature where you can place sensitive files that require a password or fingerprint to access.
- <strong>Deleting ≠ destroying</strong>: Ordinary deletion only marks the space as available to overwrite—the data is still there. To truly delete, use dedicated secure erasure tools or overwrite multiple times.
- <strong>Cloud security</strong>: Choose reputable cloud providers, enable two-factor authentication, and regularly review logged-in devices.

#### VI. Out of Space? Time for a Deep Clean

- <strong>Clear cache</strong>: Apps' temporary memory—clearing it frees up space. You can do this in Settings &gt; Storage.
- <strong>Find large files</strong>: Use the file manager to sort by size and catch the "culprits" hogging space.
- <strong>Delete leftovers</strong>: After uninstalling apps, junk files are sometimes left behind—clean them up manually.
- <strong>Clean up albums</strong>: Delete duplicate photos, blurry photos, and unneeded screenshots.
- <strong>Clean up WeChat</strong>: WeChat is a space hog—regularly cleaning chat history and cache is essential.

#### VII. Complete Guide to Common File Formats

All those file extensions on your phone can be dizzying—understanding them helps you manage files better:

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Format</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Type</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Characteristics</th>
                                    <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Recommended way to open</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">JPG/JPEG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lossy compression, small size, best compatibility. Default format for phone photos.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Album/any image viewer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PNG</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lossless compression, supports transparent backgrounds. Common for screenshots and icons. Larger than JPG.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Album/any image viewer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP3</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Audio</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lossy compression, small size, excellent compatibility. The most universal audio format.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Any music player</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">FLAC</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Audio</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Lossless compression, CD-quality sound, 3-5x larger than MP3. Audiophiles' top choice.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Music player/professional player app</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WAV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Audio</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Uncompressed raw audio, best sound quality but huge size. Common for professional recordings.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Music player</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">M4A</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Audio</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">AAC encoding, better sound quality than MP3 at the same bitrate. Common in the Apple ecosystem.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Apple Music/music player</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MP4</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The most universal video container format, with excellent compatibility. Default format for phone-recorded videos.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Album/any video player</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">MKV</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Video</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Open-source container format, supports multiple audio tracks and subtitles. Common for movie resources.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">VLC/nPlayer</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">DOC/DOCX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Document</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Word document. DOCX is a compressed format with smaller size. DOC is the legacy format.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PPT/PPTX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Presentation</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PowerPoint presentation. PPTX is a compressed format.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">XLS/XLSX</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Spreadsheet</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Excel spreadsheet. XLSX is a compressed format.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">WPS/Office</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">PDF</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Document</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Cross-platform format, fixed layout, not editable. Common for contracts, papers, and e-books.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Adobe Reader/WPS</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ZIP</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compressed</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">The most universal compression format, with good cross-platform compatibility.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Built-in/extraction app</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">RAR</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Compressed</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Higher compression ratio than ZIP, but requires dedicated software to extract.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Extraction app</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">ISO</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Image</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Disc image file, a complete copy of disc content. Common for system installation packages.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Extraction app/virtual drive</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">HTML</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Webpage</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Webpage file, opened with a browser. Common format for saved webpages.</td>
                                    <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Browser</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Try It Now: Organize the "Downloads" Folder

{class="mt-1"}
Open the file manager &gt; go to the "Downloads" folder. See what's inside? Delete the useless stuff, and categorize the useful stuff (for example, create new "Work Materials" and "Memes" folders to put them in). Also check your storage space to see which file types take up the most.
:::

{class="text-lg font-semibold mt-6 mb-2"}
#### VIII. Image and File System Management: Keep Your Assets in Order

In the previous section we learned to "recognize folders," but recognition alone isn't enough. This section is about <strong>how to proactively establish a set of long-term sustainable management practices</strong> so your files are always findable, not lost, and not snooped on.

{class="font-semibold mt-4 mb-1"}
##### 1. File Classification and Naming Conventions

The root of chaos is the lack of rules. Establishing rules is actually simple—the key is <strong>persistence</strong>.

```html
<ul class="list-disc pl-6 mb-3 space-y-2">
                        <li><strong>"Time + Event" naming method</strong>: Include a timestamp and event description in folder names for easy recall and retrieval later. For example, <code>202606_Travel_Receipts</code> and <code>2025_Year_End_Summary</code> and <code>2024_Kids_Birthday</code>. This way you can see the timeline and know the content at a glance.</li>
                        <li><strong>Three-tier classification system</strong>:
                            <ul class="list-disc pl-6 mt-1 space-y-0.5">
                                <li><strong>Tier 1</strong>: By file type (Document / Image / Video / Audio)</li>
                                <li><strong>Tier 2</strong>: By use case (Work / Life / Study)</li>
                                <li><strong>Tier 3</strong>: By specific event or project (e.g., "2026Q2_ProjectA")</li>
                            </ul>
                        </li>
                        <li><strong>Monthly cleanup plan</strong>: Pick a fixed date each month (payday or the 1st is recommended) to do a focused cleanup of the "Downloads" folder:<strong>archive the useful, delete the useless, back up the precious</strong>. Twelve small cleanups a year are far easier than one massive annual overhaul.</li>
                    </ul>
```

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-calendar-check mr-2"></i>This Month's Task List

{class="mt-1"}
Pick a free weekend and follow these steps in order:

{class="list-decimal pl-6 mt-1 space-y-0.5 text-sm"}
1. Create a work folder for this month in the file manager in the form <code>2026Q2_ProjectA</code> ;
2. Go through all the files from this week in the "Downloads" folder—keep the useful ones, archive them, and delete the useless ones;
3. Create annual folders like <code>2025_Family</code> and <code>2026_Family</code> for this year's family photos.
:::

{class="font-semibold mt-4 mb-1"}
##### 2. Redundant File Handling Strategies

Phones "gain weight" over time—mostly because of redundant files.

{class="list-disc pl-6 mb-3 space-y-2"}
- <strong>72-hour auto-cleanup</strong>: Temporary files received by social apps like WeChat and QQ (stickers, chat images, short videos) are usually useless after one view. In [WeChat] &gt; [Settings] &gt; [General] &gt; [Storage], turn on "Auto Cleanup" and set the cache expiration to 72 hours. Your phone will feel instantly lighter, and you won't lose important records.
- <strong>Targeted storage cleanup</strong>: Android [Settings] &gt; [Storage] &gt; [Cleanup], iOS [Settings] &gt; [General] &gt; [iPhone Storage]—the system will list items by category: cache / temporary files / uninstallable apps / large files. Focus on: ① cache files; ② expired installation packages (old versions left after app upgrades); ③ duplicate files (photos with the same name and size).
- <strong>Auto-classification rules</strong>: Most brand album apps support smart classification: people, scenery, documents, screenshots. Once enabled, a newly taken group photo will be automatically filed under "People &gt; Zhang San," and a scanned contract under "Documents."<strong>Combined with monthly organizing, this greatly reduces the chance of "not being able to find things."</strong>.

{class="font-semibold mt-4 mb-1"}
##### Images are the most "sensitive" data type on your phone—a casual photo can reveal your location, device, and time. We recommend

establishing a "dual protection" workflow <strong>:</strong>:

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-image mr-2"></i>Mask visible information

{class="list-decimal pl-6 mt-1 space-y-1 text-sm"}
1. <strong>: Use the built-in or third-party tools (such as Meitu XiuXiu, Snapseed) to</strong> redact the middle digits of ID numbers, license plates, house numbers, names, amounts <strong>, and other key fields;</strong> Strip metadata
2. <strong>: Before sending, tap "Share" or "Export" in the album—the system will ask whether to keep location info—choose</strong>"Don't Keep."<strong>This way the shooting device model, GPS coordinates, and shooting time won't be sent along with the image;</strong> Temporary watermark
3. <strong>(optional): Add a text watermark like "For XX processing only" on sensitive screenshots to prevent misuse.</strong> Common methods for metadata (EXIF) cleanup:
:::

{class="mt-3 mb-2"}
Common methods for metadata (EXIF) removal (basic operations; for advanced protection see Chapter 6 "Photo Anonymization"):

- <strong>: iOS [Settings] &gt; [Privacy &amp; Security] &gt; [Camera], you can turn off "Precise Location"; when sharing, selecting "Current photo only" will</strong> automatically strip most EXIF <strong>.</strong>.
- <strong>Android</strong> Professional tools
- <strong>: ExifTool (desktop), Metapho (iOS), Photo Metadata Remover (Android) can thoroughly remove all metadata.</strong> For sensitive images that need

long-term storage <strong>(ID cards, bank cards, household register scans, passports), we recommend storing them in an</strong> encrypted album <strong>:</strong>:

- Huawei/Xiaomi: [Album] &gt; long-press photo &gt; "Move to Safe";
- Third-party encrypted apps:
- 360 Safe Album <strong>,</strong> and <strong>,</strong> and <strong>, etc., with separate password protection and better concealment.</strong>
