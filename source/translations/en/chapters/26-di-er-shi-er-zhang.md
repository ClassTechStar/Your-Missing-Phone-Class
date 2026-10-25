---
id: di-er-shi-er-zhang
num: 22
part: chao-yue-pian
nav: Chapter 22: How AI Works Inside Your Phone
toc: default
kind: chapter
---

### Chapter 22: How AI Works in Phones

{class="chapter-intro mb-4"}
: Converts sound waves into text.

#### Understanding (natural language understanding)

: Understands intent, extracts key entities.

#### Execution and response

1. <strong>: Calls the corresponding App or service, then "speaks" to you through speech synthesis.</strong>3. On-Device AI vs. Cloud AI
2. <strong>On-device AI keeps computation in the phone, with fast speed, high privacy, and offline capability. Cloud AI requires internet connection but can handle more complex tasks.</strong>4. AI LLMs and Mobile Phones: Your Portable Smart Assistant
3. <strong>In 2024-2025, the explosion of AI LLMs (such as DeepSeek, ChatGPT, Wenxin Yiyan, Tongyi Qianwen, etc.) profoundly changed the way mobile phones are used. Phones are no longer just tools that execute instructions, but intelligent partners that can understand, reason, and create.</strong> What is an AI LLM?

#### AI LLMs (Large Language Models) are AI systems trained on massive amounts of text data that can understand and generate natural language. You can imagine it as a "super scholar" who has read almost all the text on the internet, capable of answering questions, writing articles, translating, programming, and analyzing data.

AI LLM Applications on Mobile Phones:

#### Conversational assistants

In 2025-2026, the explosion of AI large models (such as DeepSeek R1, ChatGPT-5, ERNIE Bot 5.0, Tongyi Qianwen 3, etc.) profoundly changed how phones are used. Phones are no longer just tools that execute commands — they have become intelligent partners that can understand, reason, and create. On-device AI chips (NPU computing power exceeding 80 TOPS) made large model inference run locally on phones for the first time, enabling AI without an internet connection.

##### Writing and creation

: Let AI help you write emails, summarize meeting minutes, polish articles, and generate creative copy.

##### Image generation and editing

- <strong>: AI can one-click remove passersby from photos, expand image boundaries, convert styles, and even generate images based on text descriptions.</strong> Real-time translation
- <strong>: Real-time call translation, face-to-face dialogue translation, photo translation—no more language barriers when traveling abroad.</strong> Learning tutoring
- <strong>: AI can explain concepts, create practice questions, and grade homework; it's a portable tutor.</strong> On-Device LLMs: Phones Run AI Themselves
- <strong>Real-time translation</strong> No network needed
- <strong>: AI functions work even offline—on airplanes, in subways, anywhere.</strong> More secure privacy

##### : Your conversations and data are not uploaded to the cloud; everything is processed locally on the phone.

Faster response

- <strong>: No network latency; AI replies are almost instantaneous.</strong> Current limitations
- <strong>: On-device models still can't match cloud-based LLMs in capability; complex tasks still require internet. But as chip AI computing power improves, on-device models will become increasingly powerful.</strong> System-Level AI Integration:
- <strong>Apple Apple Intelligence</strong>: The AI system introduced in iOS 18, integrating writing tools, image magic wand, enhanced Siri, notification summaries, and more. On-device processing first; only complex tasks go to the cloud.
- <strong>Huawei Pangu LLM</strong>: Integrated into the HarmonyOS system, the Xiaoyi assistant gains LLM capabilities, supporting document summaries, smart screen reading, AI photo editing, and more.

##### Xiaomi Pengpai AI

- <strong>: System-level AI capabilities, supporting AI image search, AI summaries, AI real-time captions, on-device LLM conversations, and more.</strong> Samsung Galaxy AI
- <strong>: Real-time call translation, note AI summaries, image generation and editing, search circle selection, and other functions.</strong>5. Several Typical Application Scenarios and Practical Operations
- <strong>To give you a more intuitive feel for the "superpowers" of mobile AI, below we use five specific scenarios to show how AI "comes to the rescue" in daily life:</strong> Scenario 1: Real-Time Translation—Your Personal Translator for Traveling Abroad
- <strong>Actual performance</strong>: Can't speak French when ordering in Paris? iPhone's "Translate" App supports a face-to-face dual-person dialogue mode, where both parties see subtitles in their own language, and can even do simultaneous interpretation. On the Android side, Samsung Galaxy AI's real-time call translation lets you speak Chinese directly on the phone, and the other party hears English, and vice versa.

#### Underlying principle

: A three-step pipeline of speech recognition (ASR) → machine translation (NMT) → speech synthesis (TTS), with end-to-end latency now controllable within 1 second.

##### Scenario 2: AI Erase—Saving Tourist Photos "Ruined" by Passersby

<strong>Actual performance</strong>: Took a beautiful selfie at a scenic spot, but the background is crowded with other tourists? Use "Magic Erase" to circle the passersby, and the phone will automatically identify and "erase" them, then intelligently fill in the background. The results are often stunning.

<strong>Underlying principle</strong>: The image segmentation (Inpainting) model first identifies and deletes the selected area, then "imagines" reasonable fill content based on surrounding pixels and semantic understanding. The AI model behind this is trained on millions of images.

##### Scenario 3: AI Photo Editing—One-Click to Become a "Photography Master"

<strong>Actual performance</strong>: Took a gray, hazy landscape photo on a cloudy day? AI "Magic Sky" can one-click replace the sky with clear sky, sunset, or even starry sky. AI image expansion can turn a vertical composition into a horizontal one, with the phone "imagining" scenes beyond the frame.

<strong>Underlying principle</strong>: Based on Generative AI's Diffusion Model, it understands the semantic content of the image and then generates new pixels. This is the "cutting edge" of current AI image processing.

##### Scenario 4: Document Processing—An Efficiency Multiplier for Office Workers

<strong>Actual performance</strong>: After a meeting, throw the meeting recording to AI, and it can automatically organize structured meeting minutes, extract action items, and generate summaries. A 10-page English PDF report can be distilled by AI in 10 seconds to give you the core conclusions.

<strong>Underlying principle</strong>: Long Context LLMs can "read through" documents of tens of thousands of words, performing multi-round reasoning and information extraction. Apple Intelligence, Huawei Xiaoyi, WPS AI, Tencent Yuanbao, etc., all have this capability.

##### Scenario 5: AI Image Search and Object Recognition—Your "Visual Search Engine"

<strong>Actual performance</strong>: See an unfamiliar flower on the street, open the camera, and AI immediately tells you "This is a hibiscus." Looking through your album for photos taken at the beach last year, search for "ocean," and AI automatically finds all photos containing the sea, without manual scrolling.

<strong>Underlying principle</strong>: Computer Vision (CV) models vectorize (Embedding) image content, then match it with text queries for similarity. This "multimodal search" is a major leap in phone album management.

##### 6. Prompt Optimization: The "Communication Formula" That Makes AI Follow Your Commands

<strong>Actual performance</strong> most practical, easiest-to-use "Role-Background-Task-Constraint" communication approach

<strong>Underlying principle</strong> Why do we need a framework?

#### Many people use AI like using Baidu—typing in a few keywords. But AI is not a search engine; it's a language model that "reads, understands, and then answers."

Give it more context, clearly state what you want, and constrain it from going off track <strong>, and it can give you precise results. A framework translates "what a good answer looks like" in your head into instructions AI can understand.</strong>1. Role: Tell AI Who It Is

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-puzzle-piece mr-2"></i>Give AI a specific "identity," and it will draw on the professional knowledge and expression style of the corresponding field.

{class="mt-1"}
The more specific the role setting, the more professional the output <strong>.</strong> Practical examples:
:::

{class="font-semibold mt-4 mb-1"}
##### "You are a

Xiaomi phone repair engineer with 10 years of experience <strong>." (Technical question)</strong>.

##### The tone should be warm and natural, like chatting with a friend

{class="list-disc pl-6 mb-3 space-y-2"}
- knowledge scope <strong>"You are a</strong> book editor with good aesthetics, well-read, and your own style
- knowledge scope <strong>"You are a</strong> cooking blogger who makes breakfast for office workers every day
- knowledge scope <strong>"You are a</strong> patient, gentle Traditional Chinese Medicine practitioner who never laughs at beginners
- knowledge scope <strong>Why is it effective?</strong> The role sets AI's
- knowledge scope <strong>,</strong> expression style

::: div .highlight-quote
{class="mb-1"}
<strong>, then send to AI:</strong> professional depth <strong>. An AI without a role is a "jack of all trades but master of none"; with a role, it can "enter" that identity and think like that professional.</strong> and <strong>Clearly state "who you are, your current situation, your constraints" in advance, and AI can give answers that are</strong> verb <strong>, rather than generic talk.</strong> Practical examples:
:::

{class="font-semibold mt-4 mb-1"}
##### "My phone is a

Xiaomi 14, bought half a year ago, recently overheating severely when playing games <strong>." (Device situation)</strong>"I am

##### The tone should be warm and natural, like chatting with a friend

{class="list-disc pl-6 mb-3 space-y-2"}
- ." (User profile)<strong>"I am</strong> preparing for the June 2026 CET-6 English exam, with average foundation
- ." (Study background)<strong>"I run</strong> a small coffee shop in a third-tier city, with monthly revenue of 30,000 yuan and two employees
- ." (Business background)<strong>"I</strong> just had a baby and am doing postpartum confinement at home, severely sleep-deprived
- ." (Life stage)<strong>Why is it effective?</strong> Background information lets AI know
- "who to serve"<strong>just had a baby and I'm on postpartum confinement at home, severely short of sleep</strong>"under what conditions"

::: div .highlight-quote
{class="mb-1"}
<strong>, then send to AI:</strong>3. Task: Clearly Tell AI What to Do <strong>This step should start with a</strong> verb <strong>(write, list, compare, translate, explain, summarize...), and describe the task</strong> specifically and executably
:::

{class="font-semibold mt-4 mb-1"}
##### . Vague tasks only get vague answers.

Practical examples:<strong>"Please</strong> list 5 permissions I should immediately turn off <strong>and explain why." (Clear action)</strong>"Please

##### The tone should be warm and natural, like chatting with a friend

{class="list-disc pl-6 mb-3 space-y-2"}
- The clearer the verb and the more specific the requirements, the better AI knows "what to deliver"<strong>"Please</strong> compare these four phones in the 3,000 yuan price range
- The clearer the verb and the more specific the requirements, the better AI knows "what to deliver"<strong>"Please</strong> explain 'what is 5G' in words a primary school student can understand
- The clearer the verb and the more specific the requirements, the better AI knows "what to deliver"<strong>"Please</strong> write three short video scripts for my breakfast shop
- The clearer the verb and the more specific the requirements, the better AI knows "what to deliver"<strong>Why is it effective?</strong> The task part is the "command center" for AI's actions.
- The clearer the verb and the more specific the requirements, the better AI knows "what to deliver"<strong>. Vague words like "do something," "make a," "take a look" are taboos for AI—it will guess your meaning, and the results often go off track.</strong>4. Constraints: Tell AI What Not to Do

::: div .highlight-quote
{class="mb-1"}
<strong>, then send to AI:</strong> making AI converge on the output that suits you best <strong>. Common dimensions include: word count, format, tone, things to avoid, things to include.</strong> Practical examples:
:::

{class="font-semibold mt-4 mb-1"}
##### "

No more than 200 words, list in bullet points <strong>." (Length + format)</strong>"

##### The tone should be warm and natural, like chatting with a friend

{class="list-disc pl-6 mb-3 space-y-2"}
- , only explain principles." (Boundaries)<strong>"</strong> Don't use technical terms
- , only explain principles." (Boundaries)<strong>"</strong> Each paragraph no more than 3 lines
- , only explain principles." (Boundaries)<strong>"</strong> Must include: usage scenarios, pros and cons, my budget match
- , only explain principles." (Boundaries)<strong>"</strong> Don't give specific investment advice
- , only explain principles." (Boundaries)<strong>Why is it effective?</strong> Without constraints, AI tends to "freestyle"—either too academic, too long, or off-topic. Clear constraints = clear "delivery standards," aligning expectations on both sides, making results controllable.
- , only explain principles." (Boundaries)<strong>Writing good prompts is not a one-time thing.</strong> After writing, first self-check these five points

::: div .highlight-quote
{class="mb-1"}
<strong>, then send to AI:</strong> Specific rather than abstract
:::

{class="font-semibold mt-4 mb-1"}
##### : Not "write an article," but "write an 800-word, 3-section phone buying guide for new moms."

Include background rather than isolated <strong>: Tell AI "who I am, why I'm asking this," so it can give you a "customized" answer.</strong> Have a clear output format

1. <strong>: Is it a table, list, paragraph, or JSON? State it in advance.</strong> Constraints in place
2. <strong>: Word count, style, things to avoid—any one of these three brings noticeable improvement.</strong> Verifiable by AI
3. <strong>: After asking, have AI repeat your requirements; if it can't articulate them clearly, you haven't been clear.</strong>6. Common Problems and Solutions
4. <strong>Symptom</strong> Solution
5. <strong>Answer too generic, not practical</strong> Add background (who you are/what scenario)

{class="font-semibold mt-4 mb-1"}
##### Answer too academic/too official

::: div .overflow-x-auto
```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                            <thead>
                                <tr class="bg-light dark:bg-gray-700">
                                    <th class="border border-gray-300 px-3 py-2 text-left">Add tone constraints + reject "bureaucratic language" list</th>
                                    <th class="border border-gray-300 px-3 py-2 text-left">Answer off-topic/not answering the question</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">Restate the task with verbs and require "only answer this"</td>
                                    <td class="border border-gray-300 px-3 py-2">Answer too long to finish reading</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">Hard limit on word count (within 200 words)</td>
                                    <td class="border border-gray-300 px-3 py-2">AI speaks nonsense with a straight face</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">Add "if uncertain, mark 'I'm not sure'" + self-check important facts</td>
                                    <td class="border border-gray-300 px-3 py-2">Not satisfied with the first version </td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">Don't rewrite; append "a bit more..." to the original prompt</td>
                                    <td class="border border-gray-300 px-3 py-2">7. Three Complete Scenario Cases</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">Scenario 1: Life Assistant (Breakfast Pairing Suggestions)</td>
                                    <td class="border border-gray-300 px-3 py-2">Prompt</td>
                                </tr>
                                <tr>
                                    <td class="border border-gray-300 px-3 py-2">:</td>
                                    <td class="border border-gray-300 px-3 py-2">You are a breakfast blogger who excels at nutritional pairing (</td>
                                </tr>
                            </tbody>
                        </table>
```
:::

{class="font-semibold mt-4 mb-1"}
##### Role

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-coffee mr-2"></i>). I am an office worker mom with only 15 minutes every morning to make breakfast, with a 6-year-old child and a 60-year-old mother-in-law at home (

{class="mt-1"}
<strong>discussing the Q2 marketing promotion plan</strong>:

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
list 7 days of non-repeating breakfast pairings <strong>(</strong> Task <strong>). Each breakfast requires: ① Preparation time no more than 15 minutes ② Nutritionally balanced (protein + carbs + fruits/vegetables) ③ Suitable for all ages ④ Ingredients available at ordinary supermarkets (</strong> Constraints <strong>).</strong> Why it's effective <strong>: Role sets professionalism, background gives the commonalities of three types of people, task clearly defines deliverables, and 4 constraints ensure executability.</strong> Scenario 2: Study Assistance (CET-6 Exam Preparation)<strong>Prompt</strong> Fill in the repository name, such as

{class="mt-1"}
<strong>: When unsatisfied with AI's answer, you can say "This is too professional, please explain again in words a primary school student can understand."</strong> experienced CET-6 English teacher
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-graduation-cap mr-2"></i>(Role). I am an ordinary undergraduate student,

{class="mt-1"}
<strong>discussing the Q2 marketing promotion plan</strong>:

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
Please organize the following meeting notes into structured minutes <strong>(Task). Requirements: ① Clear time allocation for listening, speaking, reading, and writing each week ② Give the key breakthrough direction for each month ③ Recommend 3 suitable review materials (explain reasons in Chinese) ④ Output in table format (Constraints).</strong> Why it's effective <strong>: Role sets professional background, background gives score and time anchors, task clearly defines "phased plan," constraints require "tabular" and "executable."</strong> Scenario 3: Work Efficiency (Meeting Minutes Organization)<strong>Prompt</strong>:

{class="mt-1"}
<strong>: When unsatisfied with AI's answer, you can say "This is too professional, please explain again in words a primary school student can understand."</strong> senior administrative assistant
:::

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-briefcase mr-2"></i>(Role). I just finished a 1-hour department meeting,

{class="mt-1"}
<strong>discussing the Q2 marketing promotion plan</strong>:

{class="mt-1 text-sm" style="font-family: monospace; background: #f5f5f5; padding: 8px; border-radius: 4px;"}
Please organize the following meeting notes into structured minutes <strong>(Task). Requirements: ① Divide into three parts: "Resolutions / Action Items / Risks and Dissents" ② Mark the responsible person and deadline for action items (if not mentioned, write "to be confirmed") ③ Total word count within 600 words ④ Output in markdown format (Constraints).</strong> Why it's effective <strong>: Role sets administrative perspective, background gives meeting topic, task clearly defines structured output, 4 constraints make the result directly reusable.</strong> Advanced Techniques: Make AI Your "Personal Assistant"<strong>Try these advanced uses to experience AI's true power:</strong> Multi-round dialogue optimization

{class="mt-1"}
<strong>: When unsatisfied with AI's answer, you can say "This is too professional, please explain again in words a primary school student can understand."</strong> Chain of Thought (CoT)
:::

::: div .success-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-rocket mr-2"></i>: Have AI "think step by step"; answer quality is usually higher: "Please analyze this math problem step by step."

{class="mt-1"}
Multi-AI collaboration

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>: Use A to write the first draft, B to polish, C to translate—combining them works even better.</strong> System prompts
- <strong>: Preset your identity, preferences, taboos, etc. in AI settings to make answers better fit your needs.</strong>7. AI's Limitations and Challenges: Maintain Clear Judgment
- <strong>Although AI is powerful, it's by no means "omnipotent." Clearly understanding its limitations is key to using it better:</strong>"Hallucination" problem
- <strong>Challenge 2: AI Photo Editing</strong> Knowledge cutoff
:::

#### : Most AI's training data has a cutoff date (such as early 2024); it doesn't know what happened after that.

Limited reasoning ability

- <strong>: Complex multi-step reasoning, mathematical proofs, and logical traps—AI still easily makes mistakes.</strong> Privacy risks
- <strong>: In cloud AI services, your conversations may be used for model training. For sensitive information, prioritize on-device AI.</strong> Bias and values
- <strong>: AI may carry biases from training data; you need to maintain independent thinking.</strong> AI Usage Tips
- <strong>AI-generated content may be inaccurate ("hallucination" problem); important information must be verified.</strong> Don't enter personal privacy information into AI (ID numbers, passwords, bank information, etc.).
- <strong>Make good use of prompts: The more specific and clear the description, the higher the quality of AI's answer.</strong> AI is a tool, not an authority; maintain independent thinking and judgment.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>For key decisions (medical, legal, financial), consult professionals rather than relying on AI.

{class="list-disc pl-6 mt-1 space-y-1"}
- Advanced Techniques: Make AI Your "Personal Assistant"
- Try these advanced uses to experience AI's true power:
- Multi-round dialogue optimization
- : When unsatisfied with AI's answer, you can say "This is too professional, please explain again in words a primary school student can understand."
- Chain of Thought (CoT)
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>Challenge 3: Prompt Optimization

{class="list-decimal pl-6 mt-1 space-y-1"}
1. <strong>: First use a simple prompt "write a travel guide" to ask AI, then use the CRISPE framework to write a detailed prompt. Compare the quality difference of the two answers.</strong> Chapter 23: Programming Thinking and Automation Enlightenment
2. <strong>In the previous two chapters, we built a secure "boundary wall" for our phones and witnessed its increasingly smart "AI brain" within the wall. Now, let's unlock one of the phone's ultimate potentials: letting it "think" like a programmer and automatically complete the continuous tasks you set. You might say: "I don't know how to write code, what does this have to do with me?" Don't worry, this chapter doesn't require you to write a single line of code—modern phones have lowered the threshold for "programming" to the point where you can do it with simple dragging and dropping.</strong>1. What Exactly Is Automation?
3. <strong>In plain language, automation is:</strong> letting your phone automatically do a series of things for you when a certain condition is met.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>Case 2: Complete Phone Replacement Data Migration

{class="list-disc pl-6 mt-1 space-y-1"}
- <strong>Scenario</strong>: iPhone 13 → Xiaomi 15 cross-brand phone replacement.
- <strong>Steps</strong>: ① Old phone iCloud/WeChat built-in backup → ② Sign out of Apple ID + turn off "Find" → ③ New phone uses "Xiaomi Migration" app to scan QR code → ④ Select migration items → ⑤ WeChat uses built-in "Chat History Migration" separately → ⑥ Verify key data (contacts/photos/WeChat) → ⑦ Old phone encrypted wipe.
- <strong>Expected Result</strong>: Zero data loss, old phone can be safely resold.
:::
