---
id: di-yi-zhang
num: 01
part: ji-chu-pian
nav: Chapter 1: Hello, My Personal Computer
toc: default
kind: chapter
---

### Chapter 1: Hello, My Personal Computer

{class="chapter-intro mb-4"}
Your phone is actually the most personal supercomputer in your pocket. It is countless times more powerful than the computers that once sent humans to the Moon, yet it rests quietly in your palm. Today, let's get to know this "silent giant."

#### 1. The "Innards" of Phone Hardware: A Deep Dive

Small as it is, the phone has all the vital organs. Let's get to know these precision components one by one, like in an anatomy class.

##### 1. SoC (System on Chip): The Phone's "Brain + Heart"

SoC stands for System on Chip, which translates to "cramming the entire system onto a single chip." It's not just the CPU (Central Processing Unit)—it integrates the CPU, GPU (Graphics Processing Unit), NPU (Neural Processing Unit), ISP (Image Signal Processor), baseband (responsible for communication), and more all together.

It's like building a city's government building, power plant, communication center, and police station all in one tower—extremely efficient.

##### CPU: The Core of General-Purpose Computing

The CPU is the most central component of the SoC, responsible for handling the vast majority of computing tasks. Phone CPUs use the ARM architecture, different from the x86 architecture of computers. ARM features a Reduced Instruction Set (RISC), with lower power consumption, making it more suitable for mobile devices.

<strong>CPU Big-LITTLE Core Design</strong>: Modern phone CPUs generally adopt a "big.LITTLE" core architecture (ARM's big.LITTLE technology), dividing cores into different performance tiers:

- <strong>Super core / Big core</strong>: Strongest performance, handles heavy-duty tasks. Such as game loading, app launching, complex computations. Highest frequency (3GHz+), but also highest power consumption.
- <strong>Medium core</strong>: Balances performance and power, handles everyday medium-load tasks. Scrolling Weibo, watching videos, and multitasking mainly rely on it.
- <strong>Small core / Efficiency core</strong>: Lowest power consumption, handles lightweight background tasks. Standby, listening to music, receiving messages—almost no power draw.

The three tiers of cores work together: the system scheduler automatically assigns tasks based on load—lightweight tasks go to small cores to save power, heavy work goes to big cores to crank through it, then switches back to small cores when done. This is why a phone can both run games smoothly and stay on standby all day.

<strong>Brand Architecture Characteristics</strong>:

- <strong>Qualcomm Snapdragon 8 Elite</strong>: Uses the self-developed Oryon CPU architecture (derived from the Nuvia acquisition), 2 super cores (4.32GHz) + 6 performance cores (3.53GHz), all based on TSMC's second-generation 3nm process. Completely departs from ARM's public architecture, with leapfrog improvements in both single-core and multi-core performance. GPU is Adreno 830 with a slice architecture, graphics performance up 40%; Hexagon NPU has about 45 TOPS of computing power, AI inference performance up 45%. (Note: Samsung Galaxy custom version has higher frequencies, with super cores up to 4.47GHz.)
- <strong>MediaTek Dimensity 9400</strong>: 1 super core (Cortex-X925, 3.62GHz) + 3 performance cores (Cortex-X4, 3.3GHz) + 4 efficiency cores (Cortex-A720, 2.4GHz), continuing the all-big-core architecture, TSMC's second-generation 3nm process. GPU is Immortalis-G925 (12-core), peak performance up 41%, ray tracing performance up 40%. AI processor is the 8th-generation NPU 890, supporting on-device LLM operation, on-device LoRA training, and on-device video generation.
- <strong>Apple A18 Pro</strong>: 2 performance cores (~4.04GHz) + 4 efficiency cores (~2.4GHz), TSMC's second-generation 3nm process. 6-core GPU supports hardware ray tracing; 16-core NPU (~35 TOPS) provides powerful computing for on-device AI and Apple Intelligence. Apple's self-developed architecture still leads in single-core performance and energy efficiency, and the unified memory architecture provides high-bandwidth advantages for AI inference.
- <strong>Huawei Kirin 9020</strong>: Equipped on the Mate 70 series, uses the self-developed Taishan CPU architecture, with continuously enhanced NPU and ISP capabilities, supports 5.5G and satellite communication, representing the latest breakthrough in domestic chips.

##### GPU: The Graphics Rendering Engine

The GPU (Graphics Processing Unit) is specifically responsible for graphics and parallel computing tasks. It has far more cores than the CPU (often hundreds or thousands), but each core's functionality is relatively simple, suitable for simultaneously processing large amounts of similar computations.

<strong>Graphics Rendering Pipeline</strong>:

1. <strong>Vertex processing</strong>: Calculates the position coordinates of each vertex in a 3D model.
2. <strong>Rasterization</strong>: Converts 3D graphics into pixels on a 2D screen.
3. <strong>Pixel shading</strong>: Calculates color, texture, and lighting effects for each pixel.
4. <strong>Output compositing</strong>: Composites all layers into the final image and sends it to the screen for display.

<strong>GPU Impact on Daily Use</strong>: Not just for games! Interface sliding, animation effects, video playback, photo filters, and AR apps all rely on the GPU. A phone with a weak GPU may drop frames when sliding the interface, and games will stutter directly.

<strong>GPUs by Brand</strong>: Qualcomm uses its self-developed Adreno GPU; MediaTek uses ARM Mali GPU; Apple uses its self-developed GPU, with performance and energy efficiency both being industry benchmarks.

##### NPU: The AI Acceleration Engine

The NPU (Neural Processing Unit) is a processor specifically designed for neural network operations. Compared to the CPU and GPU, the NPU is more efficient and consumes less power when handling AI tasks.

<strong>Neural Network Computing Methods</strong>: The core operations of an NPU are matrix multiplication and convolution—precisely the most fundamental and frequent computations in neural networks. Through hardware-level optimization, the NPU can process large amounts of matrix operations in parallel, dozens of times faster than a CPU, with much lower power consumption.

<strong>AI Processing Pipeline</strong>:

1. <strong>Data input</strong>: Camera images, microphone audio, sensor data, etc.
2. <strong>Preprocessing</strong>: Adjusts data format and size to fit neural network input requirements.
3. <strong>Inference computation</strong>: The NPU loads the trained model, performs forward computation on the input data, and outputs the result.
4. <strong>Post-processing</strong>: Converts AI output into usable results, such as face coordinates, text content, scene labels.

<strong>Practical Application Scenarios</strong>:

- <strong>Computational Photography</strong>: Night scene synthesis, portrait bokeh, HDR processing, AI beauty.
- <strong>Voice assistants</strong>: Speech recognition, natural language understanding, speech synthesis.
- <strong>Real-time translation</strong>: AI subtitles, conversation translation.
- <strong>Smart recognition</strong>: Text recognition (OCR), object recognition, scene recognition.
- <strong>On-device LLMs</strong>: The latest flagship chips already support running small AI LLMs (7B parameter class) on the phone, enabling offline AI conversations, document summarization, smart writing, and more. The Snapdragon 8 Elite's Hexagon NPU has about 45 TOPS of computing power, the Dimensity 9400's NPU 890 also supports on-device LLMs (LLM inference speed up 80%), and the Apple A18 Pro's 16-core NPU provides about 35 TOPS of computing power.
- <strong>AI image processing</strong>: AI erasure (one-tap removal of passersby from photos), AI image expansion (extending image boundaries), AI style transfer, text-to-image generation, and more.

##### ISP: Image Signal Processor

The ISP processes the raw data from the camera, turning light signals into beautiful photos.

<strong>How to judge performance?</strong> Look at the model! Apple A18 Pro, Qualcomm Snapdragon 8 Elite, MediaTek Dimensity 9400, and Huawei Kirin 9020 are all flagship-level. Mid-range options include Snapdragon 8s Gen3/7+ Gen3, Dimensity 8400. Don't just look at core count—architecture and process (nanometer number) are more important. The 3nm process is currently the most advanced, with energy efficiency far superior to 5nm and 4nm.

##### 2. RAM: The Temporary Workbench

RAM is like your desk—the bigger it is, the more files you can spread out at once. 12GB is the current mainstream, 16GB suits heavy users, and 24GB+ is for gamers and geeks.

RAM type also matters: LPDDR5 is faster and more power-efficient than LPDDR4X. Although Apple's RAM isn't large, system optimization is good, so it appears "sufficient."

<strong>What happens when RAM is insufficient?</strong> Apps get killed by the system in the background, requiring reload when switching. This is why sometimes you switch to WeChat and come back to find your game is gone.

##### 3. Storage (ROM/Flash): The Long-Term Warehouse

Storage is like your bookcase—the place that holds all your photos, videos, and apps. The mainstream now is UFS 3.1 or UFS 4.0, several times faster than the older eMMC.

<strong>Why does storage speed matter?</strong> It determines app opening speed, game loading speed, and photo saving speed. After long use, slow storage makes the phone increasingly laggy.

##### 4. Screen: Your Eyes

The screen is the main window for interaction between you and your phone; its quality directly affects the experience.

- <strong>Material</strong>: OLED has vivid colors, high contrast, and is more power-efficient (pixels don't emit light when displaying black), but may have flicker at low brightness that strains the eyes; LCD is more eye-friendly and lower cost, but contrast and color aren't as good as OLED.
- <strong>Resolution</strong>: 1080P is mainstream, 2K is sharper but more power-hungry. Apple's "Retina display" concept means: at a certain distance, the human eye cannot distinguish individual pixels.
- <strong>Refresh rate</strong>: 60Hz is standard, 90Hz/120Hz is smoother, silky-smooth when scrolling. High refresh rates consume more power, so many phones support adaptive refresh rate (LTPO), dynamically adjusting based on content.
- <strong>Touch sampling rate</strong>: Affects touch response speed; gamers should pay attention—the higher, the more responsive.
- <strong>Dimming method</strong>: DC dimming is more eye-friendly than PWM dimming, less likely to tire the eyes at low brightness. Many phones now support high-frequency PWM dimming, also for eye protection.

##### Screen HDR Technology

HDR (High Dynamic Range) lets the screen simultaneously display brighter highlights and darker shadows, greatly improving image layering.

- <strong>Implementation principle</strong>: Ordinary screens have a limited brightness range (SDR), with insufficient gap between the brightest and darkest. HDR screens have higher peak brightness (usually above 1000 nits), greater contrast, and wider color gamut, able to display more detail.
- <strong>Mainstream standards</strong>: HDR10 (most basic, free and open source), HDR10+ (promoted by Samsung, dynamic metadata), Dolby Vision (best image quality but requires licensing). Which standard a phone supports depends on screen hardware and system licensing.
- <strong>Practical effect</strong>: When watching HDR video, sunlight is more glaring, shadows deeper, colors richer. The prerequisite is that the video itself is HDR-produced and the screen supports HDR display.

##### Photography HDR Technology

HDR in photography and screen HDR are two different things. Photography HDR uses algorithms to solve the problem of "overexposed highlights, dead-black shadows."

- <strong>Algorithm principle</strong>: When you press the shutter, the phone actually takes multiple photos at different exposures (underexposed to preserve highlight detail, overexposed to preserve shadow detail, normal exposure to preserve midtones), then synthesizes them into a single high dynamic range photo.
- <strong>Processing pipeline</strong>: Multi-frame capture → alignment compensation (anti-shake) → exposure fusion / tone mapping → color correction → output final photo.
- <strong>Effect optimization</strong>: Modern phones can already achieve "real-time HDR"—what you see in the viewfinder is the HDR-processed result, WYSIWYG. Apple's Smart HDR and Android's auto HDR are both very mature.

##### 5. Battery and Charging: The Source of Energy

The battery is the phone's most "short-lived" component, visibly aging after two or three years. Mainstream capacity now is 5500-7500mAh.

- <strong>Charging power</strong>: The Android camp has already raced to 100W or even 200W, fully charging in a dozen minutes; Apple is still hovering at 20-30W. Does fast charging damage the battery? Using original accessories is generally fine—the phone has temperature protection.
- <strong>Wireless charging</strong>: Convenient but inefficient and generates heat. Suitable for casual charging at the office, not suitable when you're rushing out.
- <strong>Reverse charging</strong>: The phone becomes a power bank, charging earphones and watches—useful for emergencies.

##### 6. Camera: The Magic of Light and Shadow

Modern phones often have three or four cameras, each with its own role:

- <strong>Main camera</strong>: The most commonly used, with the largest sensor and best image quality.
- <strong>Ultra-wide angle</strong>: For landscapes and architecture, with a wider field of view.
- <strong>Telephoto</strong>: For distant subjects, with both optical zoom and digital zoom.
- <strong>Macro</strong>: For shooting very small things at close range.

<strong>Pixel count isn't everything!</strong> Sensor size (bigger sensor beats smaller), aperture size (f/1.8 is larger than f/2.4), and stabilization (OIS optical stabilization is important) all affect image quality. Computational Photography (AI algorithms) is becoming increasingly important, able to combine multiple photos into one good photo.

##### Periscope Telephoto Lens

Traditional telephoto lenses require a long optical path, which would make the phone very thick. The periscope telephoto uses a 90-degree prism to refract light, allowing the optical path to unfold horizontally inside the phone, thereby achieving 5x or even 10x optical zoom while keeping the phone slim.

- <strong>Structural principle</strong>: Light enters through the lens → prism refracts 90 degrees → passes through the lens group along the phone's width → reaches the sensor. It's like laying a vertical telescope on its side.
- <strong>Optical characteristics</strong>: High optical zoom multiplier (5x-10x), image quality far exceeding digital zoom. But the sensor is usually smaller than the main camera, with average low-light performance.
- <strong>Imaging advantages</strong>: Shooting the moon, distant buildings, and stage close-ups—beyond the reach of ordinary phones.

##### OIS Optical Stabilization vs EIS Electronic Stabilization

Stabilization is a key technology affecting photo and video quality; the two methods have completely different principles:

- <strong>OIS (Optical Image Stabilization)</strong>: Counteracts handshake by physically moving the lens or sensor. There's a micro-gyroscope inside the lens to detect the direction and magnitude of shake, then drives a motor to move the lens group in the opposite direction. The advantage is no image quality loss; the disadvantage is high cost and space usage.
- <strong>EIS (Electronic Image Stabilization)</strong>: Counteracts shake through software algorithms that crop and offset the image. The phone records a slightly larger frame, then crops a stable area based on gyroscope data. The advantage is no extra hardware needed; the disadvantage is that it crops the image (smaller field of view) and may blur in low light.
- <strong>Practical choice</strong>: For photos, prioritize OIS; for video, combining both works best. Many flagship phones now support "Sensor-Shift" sensor-shift stabilization, which works better than traditional lens stabilization.

##### Optical Zoom vs Digital Zoom

- <strong>Optical zoom</strong>: Changes focal length by physically moving the lens group, with no image quality loss. Optical zoom on phones usually has only fixed multiples (such as 2x, 3x, 5x, 10x), and cannot zoom continuously like a camera.
- <strong>Digital zoom</strong>: Enlarges the center area of the image, essentially cropping + interpolation upscaling. The more you zoom, the worse the image quality. 100x digital zoom looks cool, but the actual image quality is already very blurry.
- <strong>Hybrid zoom</strong>: Combines optical and digital, using multi-frame synthesis algorithms to make up for image quality loss between optical zoom multiples. Better than pure digital, but still not as good as optical.

##### Audio: Speakers and Display Chip

<strong>Single speaker vs Dual speakers</strong>:

- <strong>Single speaker</strong>: Only one sound unit at the bottom, sound biased to one side, no sense of stereo. Common in mid-to-low-end phones.
- <strong>Dual speakers (Stereo)</strong>: One speaker each at the top and bottom, forming a stereo sound field. When watching videos or listening to music, left and right channels are distinct, with much stronger immersion. Using the earpiece as the top speaker is a common solution.
- <strong>Sound quality difference</strong>: Dual speakers aren't just "louder"—the key is spatial sense and layering. Watching blockbusters with a single speaker always feels like something's missing.

<strong>Gaming phone dedicated display chip</strong>:

Some gaming phones and performance phones are equipped with an independent display processing chip, whose functions are:

- <strong>Frame insertion</strong>: Interpolates 30fps game footage to 60fps or 120fps through algorithms, making the picture smoother. This process is done on the dedicated display chip, not occupying the SoC's GPU resources.
- <strong>Super-resolution</strong>: Uses AI algorithms to upscale low-resolution footage to high resolution, making the picture clearer.
- <strong>Power reduction</strong>: Because frame insertion and super-resolution are handled by the dedicated display chip, the SoC's load is reduced, lowering heat and power consumption, making games more stable.

##### GPS Positioning: Single-Frequency and Dual-Frequency

Phone positioning mainly relies on satellite navigation systems such as GPS.

- <strong>Single-frequency GPS</strong>: Only receives L1 band signals, with positioning accuracy of about 3-5 meters. Sufficient in open areas, but in dense urban canyons with tall buildings, signal reflection causes significant positioning deviation.
- <strong>Dual-frequency GPS</strong>: Simultaneously receives both L1 and L5 band signals. The L5 band has a longer wavelength and stronger anti-interference capability; dual-frequency joint computation can eliminate most ionospheric errors, achieving positioning accuracy of 1-3 meters. The advantage is obvious for city navigation and ride-hailing positioning.
- <strong>Multi-constellation support</strong>: Modern phones support not only GPS but also BeiDou (China), GLONASS (Russia), Galileo (Europe), and other satellite systems. The more satellites connected simultaneously, the faster and more accurate the positioning.

##### 7. Sensors: The Phone's Little Tentacles

There are over a dozen sensors hidden inside the phone, working silently:

- <strong>Accelerometer + Gyroscope</strong>: Senses phone orientation, for game steering and auto-rotate.
- <strong>Ambient light sensor</strong>: Automatically adjusts screen brightness.
- <strong>Proximity sensor</strong>: Turns off the screen when the phone is close to your ear during a call.
- <strong>Fingerprint sensor</strong>: Mainstream now is under-display optical or ultrasonic fingerprint.
- <strong>Face recognition</strong>: Apple's Face ID uses 3D structured light, with high security; many Android phones use 2D photo recognition, with average security.
- <strong>That "System Update" button you tap in [Settings]—that's it.</strong>: Near Field Communication, for transit cards, access cards, bank cards.
- <strong>Barometer</strong>: Measures altitude, can even detect when you climb stairs.
- <strong>Hall sensor</strong>: Detects the opening and closing of magnetic cases.

#### 2. Operating Systems: Android vs iOS vs HarmonyOS

Hardware is the body; the operating system is the soul. The three major systems each have their own characteristics:

- <strong>Android</strong>: Like an open-source community, phone manufacturers can deeply customize it, offering many choices. You can change themes, install third-party app stores, and tinker with various tricks. But because of its openness, fragmentation is severe, with significant experience differences between brands.
- <strong>iOS</strong>: Like a carefully tended garden, Apple controls both hardware and software, with a unified and smooth experience. App quality is high, privacy protection is good, but freedom is low—many things must follow Apple's rules.
- <strong>HarmonyOS</strong>: Huawei's new species, focusing on distributed capabilities, allowing different devices to collaborate seamlessly. We'll cover it specifically later.

All three have extremely rich ecosystems—just choose the lifestyle you prefer. There's no absolute good or bad, only what suits you.

#### 3. Phone Ports Explained

Phone ports are bridges connecting to the outside world, and different ports vary greatly:

##### Micro USB

- <strong>Physical characteristics</strong>: Flat trapezoidal connector, with distinct front and back (you can't insert it reversed). It has been largely phased out on phones, but some low-end devices and old equipment still use it.
- <strong>Transmission limitations</strong>: Only supports USB 2.0 standard, with a maximum transfer rate of 480Mbps; charging power usually doesn't exceed 10W.
- <strong>Characteristics</strong>: Front and back are not interchangeable, short insertion lifespan, slow transfer speed, low charging power.

##### Lightning (Apple Lightning connector, discontinued)

- <strong>Physical characteristics</strong>: Apple's self-developed 8-pin connector, reversible. Used on iPhone 14 and earlier models, now fully discontinued.
- <strong>Transmission limitations</strong>: The Lightning connector physically only supports USB 2.0 standard, with a maximum transfer rate of 480Mbps. Even using a USB-C to Lightning cable, transfer speed is limited by the Lightning connector itself.
- <strong>Reason for discontinuation</strong>: The EU passed regulations requiring all phones to use USB-C connectors starting in 2024; Apple switched to Type-C from the iPhone 15 series. The Lightning connector has officially exited the stage.
- <strong>Note</strong>: Apple's MFi-certified cables contain a certification chip; non-certified cables may not charge or transfer data properly. If you're still using an older iPhone, it's recommended to keep Lightning cables on hand.

##### USB Type-C

- <strong>Physical characteristics</strong>: 24-pin oval connector, reversible. It has become the standard connector for phones and most electronic devices. The EU has legislated that all phones, tablets, earphones, and other portable devices must use USB-C connectors starting in 2024, and other regions worldwide are following suit.
- <strong>Transmission protocols</strong>: Type-C is just the connector form; actual transmission capability depends on the internal protocol. Supports USB 2.0 (480Mbps), USB 3.0/3.1/3.2 (5-20Gbps), and even USB4 (40Gbps).
- <strong>Important distinction</strong>: Not all Type-C ports support USB 3.0! Many phones use a Type-C connector but only connect USB 2.0 pins internally, making transfer speeds just as slow as older ports. The iPhone 16/17 standard models only support USB 2.0 speeds, while the Pro models support USB 3.0 (requires a USB-C to USB-C cable).
- <strong>Charging capability</strong>: Supports USB PD and other fast charging protocols, up to 240W charging.
- <strong>Video output</strong>: Supports DisplayPort Alt Mode, can output video to a monitor via an adapter cable.

##### 3.5mm Audio Connector

- <strong>Physical characteristics</strong>: Round 3-segment or 4-segment jack; 3-segment transmits left and right channel audio, 4-segment adds a microphone channel.
- <strong>Protocol</strong>: Analog signal transmission, plug-and-play, no drivers or conversion needed. Stable sound quality, zero latency.
- <strong>Current status</strong>: Most flagship phones have removed the 3.5mm connector, requiring a Type-C adapter or Bluetooth earphones. Some mid-range phones and gaming phones still retain it.

#### 4. Phone Product Lines and Naming Conventions

Faced with the dazzling product lines of various brands, understanding naming conventions can help you quickly locate the right model for you.

##### Mainstream Brand Product Lines:

- <strong>Apple</strong>: iPhone (standard) / iPhone Plus (large screen) / iPhone Pro (professional) / iPhone Pro Max (large screen professional) / iPhone SE (budget) / iPhone 16e (budget AI version, equipped with A18 chip and Apple's self-developed C1 baseband). The 2026 iPhone 17 lineup is fully equipped with the A19 Pro chip, with further enhanced AI capabilities.
- <strong>Huawei</strong>: Mate series (Business flagship) / P/Pura series (Imaging flagship) / Mate X series (Foldable flagship) / nova series (Youth mid-range) / Enjoy series (Entry-level)
- <strong>Xiaomi</strong>: Xiaomi Digital series (Flagship) / Xiaomi MIX (Exploration flagship/Foldable) / Redmi K series (Performance flagship) / Redmi Note series (Mid-range) / Redmi Digital series (Entry-level)
- <strong>OPPO</strong>: Find X series (Flagship) / Reno series (Mid-range) / A series (Entry-level) / OnePlus Digital series (Performance flagship)
- <strong>vivo</strong>: X series (Imaging flagship) / iQOO Digital series (Performance flagship) / S series (Selfie mid-range) / Y series (Entry-level)
- <strong>Samsung</strong>: Galaxy S series (Flagship) / Galaxy Z Fold/Flip (Foldable flagship) / Galaxy A series (Mid-range)

##### Common Suffix Meanings:

- <strong>Pro</strong>: Abbreviation for Professional, the professional version. Usually upgrades camera, screen, processor, and other core configurations on the basis of the standard version.
- <strong>Max</strong>: The maximum version. Largest screen, largest battery, but configuration may not be higher than Pro.
- <strong>Ultra</strong>: The ultimate version. Usually represents the highest configuration of the series, with the most powerful hardware and the highest price. Such as Samsung S24 Ultra, Xiaomi 14 Ultra.
- <strong>SE</strong>: Special Edition, actually mostly a budget version. Reduced configuration, lower price. Such as iPhone SE.
- <strong>Plus</strong>: The enlarged version. Larger screen than the standard version, larger battery, but basically the same configuration.
- <strong>Lite/Youth Edition</strong>: The lightweight version. Streamlined configuration, lower price.
- <strong>Note</strong>: Originally referred to large-screen phones, now used differently by various brands. Redmi Note is a mid-range series.
- <strong>Neo</strong>: The new sharp version. Usually refers to performance-oriented mid-range models.

#### 5. Baseband and Antenna: The Unsung Heroes of Phone Communication

Your phone can make calls and access the internet thanks to the partnership of the baseband chip and antenna.

##### Baseband Chip:

The baseband is the processor in the phone responsible for wireless communication. It modulates digital signals into radio waves for transmission, and demodulates received radio waves back into digital signals. Baseband performance directly affects call quality, internet speed, and signal stability. Qualcomm is the largest mobile baseband supplier; MediaTek and Samsung also have self-developed basebands. Starting from iPhone 16e, Apple has equipped its self-developed C1 baseband chip, marking Apple's official entry into the self-developed baseband era; the C1 baseband uses a 4nm process with excellent power consumption. iPhone 16/16 Plus/16 Pro/16 Pro Max still use Qualcomm basebands (Snapdragon X75 5G), with subsequent models expected to gradually transition to self-developed basebands. Earlier iPhone XS/11 series using Intel basebands had poor signal performance, which was a pain point for many users.

##### Antenna Design:

Phone antennas are hidden inside the body, usually arranged around the frame. Antenna design directly affects signal reception performance:

- <strong>MIMO technology</strong>: Multiple-input multiple-output, using multiple antennas to simultaneously send and receive data, improving speed and stability. 4×4 MIMO is faster than 2×2 MIMO.
- <strong>Number of antennas</strong>: Flagship phones usually have a dozen antennas (cellular, Wi-Fi, Bluetooth, NFC, GPS each need independent antennas).
- <strong>Impact of metal body</strong>: Metal shields signals, so metal-body phones need antenna bands designed in (plastic strips on the frame). Glass and plastic bodies have less impact on signals.

##### Network Technology Evolution:

- <strong>: Currently the widest coverage, sufficient speed (theoretically up to 100Mbps+), relatively low power consumption.</strong>: Theoretical peak rate 1Gbps downlink / 500Mbps uplink (Cat.18), actual experience usually 50-150Mbps. Widest coverage, sufficient for use.
- <strong>5G NR</strong>: Theoretical peak rate 10Gbps+ downlink. Sub-6GHz band has better coverage; mmWave millimeter wave is extremely fast but has very limited coverage.
- <strong>5G-A (5G Advanced)</strong>: An enhanced version of 5G, also known as 5.5G. Downlink speeds can reach 10Gbps, uplink 1Gbps, with significantly improved connection density and positioning accuracy. Since 2024, China Mobile, China Telecom, and China Unicom have been deploying 5G-A networks in key cities. Flagship phones like the Huawei Mate 70/80 series and Xiaomi 15/16 series already support 5G-A. 5G-A also brings "integrated communication and sensing" capabilities, where base stations can simultaneously communicate and sense the environment, providing infrastructure for low-altitude economy (drone delivery) and vehicle-to-everything (V2X).

##### Network Band Classification:

The network bands supported by a phone determine which countries and carriers' networks it can be used on:

- <strong>FDD-LTE Band (B series)</strong>: Such as B1, B3, B5, etc., 4G bands. Different countries use different bands; China mainly uses B1/B3/B5/B8/B34/B38/B39/B40/B41.
- <strong>TDD-LTE Band</strong>: Another 4G standard, heavily used in China with B38/B39/B40/B41.
- <strong>5G NR Band (N series)</strong>: Such as n1, n3, n28, n41, n78, n79, etc. n78 (3.5GHz) is China's main 5G band; n41 (2.5GHz) is used more by China Mobile.
- <strong>Purchase advice</strong>: If you need to use the phone abroad, confirm before purchase whether it supports the target country's bands. China mainland phones usually have the most complete support for Chinese bands, but may lack some overseas bands.

#### 6. How Many Roles Does Your Phone Actually Play?

It has long been more than just a phone:

1. <strong>Communication tool</strong>: Phone, SMS, WeChat, email...
2. <strong>Smart camera</strong>: Photos, videos, document scanning...
3. <strong>Wallet</strong>: Payments, transit cards, bank cards, membership cards...
4. <strong>Information portal</strong>: News, weather, stocks, knowledge...
5. <strong>Gaming console</strong>: From match-3 to AAA titles...
6. <strong>Mobile office</strong>: Documents, spreadsheets, meetings, collaboration...
7. <strong>Health assistant</strong>: Step counting, heart rate, sleep, exercise...
8. <strong>Smart home remote</strong>: Control lights, AC, TV, robot vacuums...
9. <strong>Digital ID</strong>: Electronic ID cards, electronic driver's license, health codes...
10. <strong>Entertainment center</strong>: Music, videos, e-books, podcasts...

Think about it—how much life is packed into one tiny device! So, learning to use it well is learning to live better.

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Hands-on: Understand Hardware Configuration

{class="mt-1"}
In [Settings], see if you can find the processor model, RAM, and ROM (storage) sizes. Get a sense of your phone's capabilities. Android users can download "AnTuTu" or "DevCheck" to view detailed hardware information.
:::
