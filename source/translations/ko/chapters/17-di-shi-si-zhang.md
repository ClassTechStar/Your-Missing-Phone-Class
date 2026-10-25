---
id: di-shi-si-zhang
num: 14
part: ruan-jian-pian
nav: 제14장: 비밀번호 관리자 특집
toc: default
kind: chapter
---

### 제14장:비밀번호 관리자특집

{class="chapter-intro mb-4"}
디지털 시대에 비밀번호는 당신의 집 열쇠와 같습니다. 하지만 열쇠가 너무 많고 너무 복잡하면 어떡할까요? 비밀번호 관리자가 바로 당신의 "만능 열쇠 집사"입니다.

#### 1. 왜 비밀번호 관리자가 필요한가?

현대인은 평균 수십 개에서 수백 개의 네트워크 계정을 갖고 있습니다. 각 계정마다 같은 비밀번호를 쓰면, 한 웹사이트가 해킹당했을 때 모든 계정이 위험해집니다. 각 계정마다 다른 복잡한 비밀번호를 쓰면, 도저히 외울 수 없습니다.

비밀번호 관리자가 이 딜레마를 해결합니다: 주 비밀번호 하나만 기억하면, 나머지 모든 비밀번호를 대신 기억해 줍니다.

#### 2. 비밀번호 관리자의 작동 원리

1. <strong>암호화 저장</strong>: 모든 비밀번호는 고강도 암호화로 저장되며, 오직 당신만 복호화할 수 있습니다.
2. <strong>주 비밀번호</strong>: 비밀번호 보관함을 잠금 해제할 주 비밀번호 하나를 설정합니다. 주 비밀번호 자체는 서버에 저장되지 않습니다.
3. <strong>자동 채우기</strong>: 웹사이트나 App 로그인 화면에서 비밀번호 관리자가 계정 비밀번호를 자동으로 채워 줍니다.
4. <strong>비밀번호 생성</strong>: 무작위의 복잡한 비밀번호를 생성하여 보안성을 높일 수 있습니다.

#### 3. 암호화 원리 간략 소개

비밀번호 관리자의 암호화 원리를 이해하면, 서비스 제공자가 신뢰할 만한지 판단하는 데 도움이 됩니다. 아래에 알기 쉬운 언어로 핵심 개념 몇 가지를 설명합니다.

##### 1. AES-256 암호화

AES(고급 암호화 표준)는 미국 국립표준기술원(NIST)이 인정한 대칭 암호화 알고리즘으로, 은행, 군사, 정부에서 광범위하게 사용됩니다. "256"은 키 길이가 256비트임을 의미합니다 — 이론적으로 우주 나이보다 더 긴 시간이 필요해 무차별 대입 공격으로는 깰 수 없습니다. 주류 비밀번호 관리자(1Password, Bitwarden, KeePass 등)는 모두 AES-256으로 비밀번호 보관함을 암호화합니다.

##### 2. 제로 지식 아키텍처(Zero-Knowledge Architecture)

"제로 지식"은 서비스 제공자가 아무것도 저장하지 않는다는 뜻이 아니라, <strong>암호화와 복호화가 모두 당신의 기기 로컬에서 완료되며, 서버는 암호화된 암호문만 저장</strong>한다는 의미입니다. 구체적 흐름:

1. 클라이언트에서 주 비밀번호를 입력합니다.
2. 클라이언트가 주 비밀번호에서 파생된 암호화 키를 생성합니다(이 단계는 스마트폰/컴퓨터에서 완료됨).
3. 암호화된 암호문만 서버에 업로드됩니다.
4. 다음 로그인 시 서버가 암호문을 내려보내면, 클라이언트가 다시 주 비밀번호로 복호화합니다.

핵심 포인트:<strong>마스터 비밀번호 자체는 절대 기기를 떠나지 않습니다</strong>, 서버에도 없습니다. 그래서 설령 서비스 제공자가 해킹당하더라도, 해커가 손에 넣는 것은 해독할 수 없는 암호문일 뿐입니다——당신의 마스터 비밀번호를 추측하지 못하는 한.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>"제로 지식"이 서비스 제공자도 비밀번호를 볼 수 없다는 의미인 이유는?

{class="mt-1"}
해독 키가 마스터 비밀번호에서 파생되는데, 마스터 비밀번호는 오직 당신 머릿속에만 존재하고 로컬 기기에서만 사용되기 때문입니다. 서비스 제공자의 서버에는 마스터 비밀번호도, 해독 키도 없고 암호문만 있습니다. 그래서 Bitwarden, 1Password 같은 정식 서비스 제공자들은 "우리도 고객의 비밀번호를 볼 수 없다"고 명시합니다——보고 싶지 않아서가 아니라, 기술적으로 불가능하기 때문입니다.
:::

##### 3. 키 파생 함수: PBKDF2 와 Argon2

마스터 비밀번호는 암호화 키로 직접 사용할 수 없습니다——"키 파생 함수" 처리를 거쳐야 합니다. 이 함수의 역할은<strong>고의로 계산을 느리게 만드는 것</strong>입니다, 해커의 무차별 대입 공격 비용을 실행 불가능할 만큼 높이기 위해.

- <strong>PBKDF2</strong>: 노련한 표준으로, iCloud 키체인, Bitwarden, LastPass 등에 광범위하게 사용됩니다. 반복 반복(보통 10만 회 이상) 해싱으로 크래킹을 늦춥니다.
- <strong>Argon2</strong>: 2015년 비밀번호 해싱 대회 우승자로, PBKDF2보다 현대적입니다. "연산력 소모" 외에 "메모리 소모"도 도입하여——GPU/ASIC 같은 전용 하드웨어로도 가속 크래킹이 어렵습니다. Bitwarden, KeePassXC 등이 이미 지원합니다.

반복 횟수가 높을수록 더 안전하지만, 잠금 해제 속도도 느려집니다. 정식 서비스 제공자는 사용하는 파생 알고리즘과 반복 횟수를 공개하여 보안 커뮤니티의 감사를 받습니다.

##### 4. 사례 경고: LastPass 2022년 데이터 유출

2022년 8월, 노련한 비밀번호 관리자 LastPass가 개발 환경 침입을 공시했습니다; 같은 해 11월에는 해커가 사용자 비밀번호 보관함 백업(암호화된 암호문)을 가져갔다고 추가 공시했습니다. 사건의 핵심 교훈:

- <strong>제로 지식 아키텍처가 최소한의 선은 지켰습니다</strong>: 비밀번호 보관함 자체가 암호화되어 있어 해커가 암호문을 가져도 풀 수 없었습니다——사용자의 마스터 비밀번호가 충분히 강한 전제하에.
- <strong>약한 마스터 비밀번호 사용자가 가장 위험합니다</strong>: 해커가 오프라인으로 약한 마스터 비밀번호를 무차별 대입할 수 있어, 약한 마스터 비밀번호나 재사용한 사용자가 실질적 위험에 직면합니다.
- <strong>메타데이터도 유출됩니다</strong>: 비밀번호 내용은 암호화되지만, 사이트 URL, 메모 등 메타데이터는 암호화되지 않았을 수 있어 사용자가 어떤 서비스를 쓰는지 노출됩니다.

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>LastPass 사건에서 배운 점

{class="mt-1"}
첫째, 마스터 비밀번호는 길고 고유해야 합니다(16자 이상, 대소문자/숫자/기호 포함 권장); 둘째, Argon2id 지원, 반복 횟수가 높은 서비스 제공자를 우선 선택하세요; 셋째, 고가치 계정(은행, 이메일)에는 반드시 독립된 2단계 인증을 켜고, 비밀번호 관리자에만 의존하지 마세요.
:::

#### 4. 비밀번호 관리자 사용 모범 사례

##### 시스템 내장:

- <strong>iCloud 키체인</strong>: Apple 생태계 사용자의 첫 선택. Safari, App과 원활하게 통합, 무료, 안전. 단점은 크로스 플랫폼 사용이 불편합니다.
- <strong>Google 비밀번호 관리자</strong>: Android 사용자에게 편리. Chrome, Android 시스템과 통합, 무료.
- <strong>화웨이 비밀번호 보험상자</strong>: HarmonyOS 내장, 화웨이 사용자에게 적합.

##### 서드파티 전문 도구:

- <strong>Bitwarden</strong>: 오픈소스 무료, 기능 강력, 모든 플랫폼 지원. 프라이버시를 중시하는 사용자에게 강력 추천.
- <strong>1Password</strong>: 인터페이스 미려, 기능 풍부, 가정과 팀에 적합. 유료.
- <strong>LastPass</strong>: 노련한 비밀번호 관리자, 무료 버전 기능 제한.
- <strong>KeePass</strong>: 완전 로컬 저장, 오픈소스 무료. 극인 사용자에게 적합.

#### 다섯, 비밀번호 강도 진짜 평가

비밀번호 관리자는 보통 "비밀번호 강도" 표시 바(빨강/노랑/초록)를 보여주지만, 이 평가는 종종 길이와 문자 종류만 보고, 포괄적이지 않습니다. 비밀번호가 진짜 안전한지 판단하려면, "엔트로피"와 "이미 유출되었는지"를 고려해야 합니다.

##### 1. 엔트로피(Entropy): 비밀번호 강도의 과학적 척도

"엔트로피"는 비밀번호의 불확실성을 측정하며, 단위는 비트입니다. 엔트로피가 높을수록 무차별 대입에 필요한 시도 횟수가 많아집니다.

- <strong>"123456"</strong>: 엔트로피 극히 낮음, 순간 크래킹.
- <strong>"P@ssw0rd"</strong>: 복잡해 보이지만, 모든 사전 공격 리스트에 들어 있어 엔트로피는 여전히 낮습니다.
- <strong>"correct horse battery staple"</strong>: 네 개의 무작위 단어, 엔트로피 약 44 비트, 크래킹 난이도는 "P@ssw0rd"보다 훨씬 높습니다.
- <strong>16자 무작위 문자(대소문자+숫자+기호 포함)</strong>: 엔트로피 약 100 비트, 현재 연산력으로 무차별 대입 불가.

결론:<strong>"길이 + 무작위성"이 "복잡한 기호"보다 더 중요합니다</strong>. 이것이 비밀번호 관리자가 생성한 무작위 긴 비밀번호가 진짜 안전한 이유입니다.

##### 2. HaveIBeenPwned: 당신의 비밀번호가 유출되었는지 확인

보안 연구자 Troy Hunt가 운영하는 <a href="https://haveibeenpwned.com" class="text-primary hover:underline" target="_blank" rel="noopener">haveibeenpwned.com</a>은 역대 대형 데이터 유출에서 흘러나온 계정과 비밀번호를 수록하고 있습니다. 다음을 할 수 있습니다:

1. 이메일을 입력하여 당신의 계정이 어떤 유출에서 노출되었는지 확인.
2. Pwned Passwords 기능으로 특정 비밀번호가 알려진 유출 DB에 있는지 조회(비밀번호 관리자와 브라우저에 이미 내장됨).

비밀번호가 유출 DB에 있다면,<strong>아무리 복잡해 보여도 즉시 교체해야 합니다</strong>——사전 공격이 이런 알려진 비밀번호를 우선 시도하기 때문입니다.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-shield-alt mr-2"></i>k-Anonymity 조회 원리

{class="mt-1"}
HaveIBeenPwned에 비밀번호를 입력하면 또 유출될까 봐 걱정되세요? 걱정 마세요. 현대 조회는 "k-익명" 프로토콜을 사용합니다: 브라우저는 비밀번호 해시의 앞 5자리만 서버에 보내고, 서버는 이 5자리로 시작하는 모든 해시 리스트를 반환하며, 로컬에서 비교합니다. 즉, 서버는 당신의 완전한 비밀번호 해시를 절대 볼 수 없습니다. 1Password, Bitwarden의 "유출 비밀번호 검사"가 모두 이렇게 작동합니다.
:::

##### 3. 비밀번호 관리자 내장 모니터링 기능

- <strong>1Password Watchtower</strong>: 약한 비밀번호, 중복 비밀번호, 유출된 비밀번호, 오래된 비밀번호, 2FA 미사용 웹사이트를 실시간 모니터링, 빨강/주황/노랑 등급으로 표시.
- <strong>Bitwarden Vault Health</strong>: 무료 버전에서도 약한 비밀번호, 중복 비밀번호 조회 가능; 유료 버전은 유출 비밀번호 검사(HaveIBeenPwned 기반) 가능.
- <strong>iCloud 키체인 "보안 권고"</strong>: iOS 설정 → 비밀번호 → 보안 권고, 어떤 비밀번호가 알려진 유출에 등장했는지, 어떤 것이 중복 사용되었는지 알려줌.
- <strong>Google 비밀번호 관리자 "비밀번호 검사 도구"</strong>: Chrome 내장, 유출/약한/중복 비밀번호를 한 번에 검사.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>지금 바로 확인: 당신의 비밀번호가 안전한지

{class="list-decimal pl-6 mt-1 space-y-1"}
1. haveibeenpwned.com을 열고, 자주 쓰는 이메일을 입력해 어떤 유출 사건에 등장했는지 확인.
2. iPhone 사용자: 설정 → 비밀번호 → 보안 권고, 빨간 경고를 한 항목씩 처리.
3. Chrome 사용자: 설정 → 비밀번호 → 비밀번호 검사, 안내에 따라 수정.
4. 1Password/Bitwarden 사용자: Watchtower/Health Reports를 열고 "유출됨"과 "중복" 항목을 우선 처리.
:::

#### 여섯, Passkey: 비밀번호 없는 로그인의 미래

2024-2026년, 비밀번호 기술은 혁명을 겪고 있습니다——<strong>Passkey(통행 키)</strong>가 전통 비밀번호를 완전히 대체할 전망입니다. Apple, Google, Microsoft 3대 플랫폼이 연합하여 추진하고, FIDO 얼라이언스와 W3C가 보증하며, 이는 수십 년래 로그인 방식의 가장 큰 변화입니다.

##### 1. Passkey란?

Passkey는 FIDO2 / WebAuthn 표준 기반,<strong>기기 상의 키 쌍</strong>으로 비밀번호를 대체합니다. 원리를 단순화하면:

- 당신의 스마트폰이 키 쌍을 생성합니다:<strong>공개 키</strong>(웹사이트에 등록) + <strong>개인 키</strong>(기기의 보안 칩에 영구 보관).
- 로그인 시, 웹사이트가 "챌린지"를 보내고, 당신의 스마트폰이 개인 키로 서명, 웹사이트가 공개 키로 검증.
- 서명 전에 생체 인증(Face ID / 지문) 또는 기기 PIN으로 신원 확인 필요.
- 전체 과정에서,<strong>어떤 비밀번호도 네트워크로 전송되지 않습니다</strong>.

##### 2. Passkey vs 전통 비밀번호

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">차원</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">전통 비밀번호</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Passkey</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">피싱 내성</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">낮음, 피싱 사이트가 비밀번호 탈취 가능</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">천성적으로 피싱 내성, 개인 키는 진짜 도메인에만 서명</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">서버 유출 영향</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">비밀번호 해시가 크래킹될 수 있음</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">서버는 공개 키만 저장, 유출 영향 없음</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">편의성</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">기억/입력/관리 필요</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Face ID/지문 1초 로그인</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2 font-semibold">재전송 공격</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">중간자가 가로채 재전송 가능</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">매 서명 일회성, 재전송 불가</td>
                            </tr>
                        </tbody>
                    </table>
```

##### 3. 각 플랫폼 지원 현황

- <strong>Apple iCloud 키체인 Passkey</strong>: iOS 16+ / macOS Ventura+ 네이티브 지원, Passkey는 같은 Apple ID로 로그인한 모든 기기 간 동기화, 새 기기에서 웹사이트 로그인 시 재생성 불필요.
- <strong>Google 비밀번호 관리자 Passkey</strong>: Android + Chrome 네이티브 지원, Passkey는 Google 계정에 저장, Android 기기 간 동기화; 2023년부터 Google 개인 계정은 Passkey 로그인 지원.
- <strong>Microsoft</strong>: Windows 11 / Edge가 Passkey 지원; Microsoft 계정, Outlook, Office 등 서비스가 차례로 Passkey 로그인 개방, Microsoft Authenticator에서 관리 가능.
- <strong>1Password / Bitwarden</strong>: Passkey 생성, 저장, 크로스 플랫폼 동기화 지원, 단일 생태계에 얽매이지 않음.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>크로스 디바이스 동기화가 핵심 돌파구

{class="mt-1"}
초기 Passkey의 가장 큰 골칫거리는 "단일 기기 바인딩"——스마트폰을 바꾸면 다시 만들어야 한다는 점이었습니다. 2023년부터 Apple, Google, Microsoft가 Passkey의 클라우드 동기화를 구현했습니다: iCloud 키체인 동기화는 Apple 기기 간, Google 비밀번호 관리자 동기화는 Android 기기 간. 1Password 같은 서드파티는 크로스 생태계 동기화를 열었습니다. 이는 Passkey가 비밀번호를 대체할 실용성을 갖추었음을 의미합니다.
:::

##### 4. 스마트폰에서 Passkey를 생성하고 사용하는 방법

<strong>iOS(iPhone) 경로:</strong>

1. Passkey를 지원하는 웹사이트(예: Google, Microsoft, Amazon, eBay, PayPal)의 계정 보안 페이지에서 "통행 키 추가 / Add passkey"를 선택.
2. 시스템이 Face ID / Touch ID 인증 창을 띄우고, 통과하면 Passkey가 자동 생성되어 iCloud 키체인에 저장.
3. 다음에 해당 웹사이트에 로그인할 때, 사용자 이름 입력 후 "iPhone으로 로그인" 선택, Face ID 한 번 인증하면 끝.
4. 관리 입구: 설정 → 비밀번호 → 해당 웹사이트를 찾으면 Passkey 항목이 보입니다.

<strong>Android 경로:</strong>

1. Passkey를 지원하는 웹사이트의 계정 보안 페이지에서 "통행 키 추가"를 선택.
2. Google 비밀번호 관리자 팝업 → Google 계정 선택 → 화면 잠금 인증(지문/패턴/PIN).
3. Passkey가 자동으로 Google 비밀번호 관리자에 저장, 같은 계정의 Android 기기 간 동기화.
4. 다음 로그인 시, "Passkey 사용" 선택, 화면 잠금을 풀면 끝.
5. 관리 입구: Android 설정 → 비밀번호, 키 및 자동 완성 → 비밀번호 관리자 → google.com.

##### 5. Passkey 기기 간 로그인

Windows PC에서 iPhone에만 Passkey가 있는 웹사이트에 로그인하려면, QR 코드를 스캔해 인증할 수 있습니다:

1. 웹사이트 로그인 페이지에서 "Passkey 사용" 선택.
2. "다른 기기 사용" 선택.
3. PC에 QR 코드가 표시되면, iPhone으로 스캔.
4. iPhone이 Face ID 인증 팝업, 확인하면 PC에서 웹사이트 로그인 완료.

이 과정은 Bluetooth+인터넷 이중 암호화 통신으로, Passkey 개인 키는 iPhone을 떠나지 않습니다.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>지금 바로 시도: 비밀번호 없는 로그인 체험

{class="list-decimal pl-6 mt-1 space-y-1"}
1. Google 계정 로그인 → 보안 → 통행 키 → 통행 키 추가, Face ID/지문 로그인 체험.
2. Microsoft 계정 로그인 → 보안 → 고급 보안 옵션 → 통행 키 추가.
3. 타오바오, 징둥, eBay, PayPal 등 Passkey를 이미 지원하는 서비스에서 체험.
4. 전통 비밀번호를 예비로 남겨두고, 고가치 계정을 점진적으로 Passkey로 이전.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>과도기 권장

{class="mt-1"}
Passkey가 비밀번호를 완전히 대체한 것은 아닙니다——많은 웹사이트는 여전히 "Passkey + 비밀번호" 공존 단계입니다. 권장: 고가치 계정은 Passkey를 우선 켜되,<strong>전통 비밀번호를 즉시 삭제하지 마세요</strong>, 예비용으로 남겨두세요; 동시에 비밀번호 관리자를 계속 사용하세요, 모든 웹사이트가 Passkey를 지원하지는 않기 때문입니다. Passkey를 "비밀번호 관리자의 강력한 보충"으로 보지, "즉시 교체"로 보지 마세요.
:::

#### 일곱, 하드웨어 보안 키

보안 요구가 일반 사용자보다 높다면——예를 들어 대량의 암호화폐를 보유하거나, 임원/기자/활동가이거나, 기업 핵심 계정을 보호한다면——하드웨어 보안 키는 SMS 인증번호보다 더 신뢰할 수 있는 선택입니다.

##### 1. 하드웨어 보안 키란?

하드웨어 키는 물리적 기기(USB 메모리 모양)로, 내부 보안 칩이 개인 키를 저장하며, 물리적 접촉 또는 NFC로만 인증을 완료할 수 있습니다. 대표 제품:

- <strong>YubiKey</strong>(Yubico 사): 가장 주류, FIDO2/WebAuthn, U2F, OTP, PIV, OpenPGP 지원, USB-C / USB-A / NFC 등 다양한 인터페이스. 5 시리즈 50-70 달러.
- <strong>Google Titan</strong>: Google 자체 제작, USB-C + NFC / Bluetooth, 약 30-40 달러.
- <strong>OnlyKey</strong>: 오픈소스 대체품, 다양한 프로토콜 지원.
- <strong>국산 대체품</strong>: 페이톈 청신 ePasskey 등, 가격이 더 저렴함.

##### 2. 하드웨어 키가 SMS 인증번호보다 안전한 이유?

- <strong>피싱 내성</strong>: Passkey와 마찬가지로, 하드웨어 키는 진짜 도메인에만 응답, 피싱 사이트가 인증번호를 가로채지 못함.
- <strong>SIM 하이재킹 내성</strong>: SMS 인증번호는 SIM-swap 공격으로 가로채일 수 있지만, 하드웨어 키는 전화번호가 필요 없음.
- <strong>중간자 내성</strong>: FIDO2 프로토콜은 매 서명마다 챌린지 값을 포함, 재전송 불가.
- <strong>물리적 격리</strong>: 개인 키는 항상 하드웨어 칩 내부에, 악성코드가 PC를 감염시켜도 읽을 수 없음.

##### 3. 적용 시나리오

- 암호화폐 거래소 계정, 지갑 복구.
- 기업 SSO, 재택근무 VPN, SSH 서버 로그인.
- 이메일, GitHub, 소셜 미디어 등 "마스터 계정"——한번 뚫리면 다른 모든 계정을 재설정할 수 있음.
- 기자, 변호사, 임원 등 고민감도 인물.

##### 4. 하드웨어 키를 2단계 인증으로 설정하는 방법

Google 계정 + YubiKey를 예로:

1. YubiKey 구매(한 번에 두 개 구매 권장, 하나는 일상용, 하나는 예비용, 다른 장소에 보관).
2. myaccount.google.com 로그인 → 보안 → 2단계 인증.
3. "보안 키 추가" 선택 → YubiKey를 USB-C 포트에 꽂거나 스마트폰 NFC 감응 구역에 가까이 대기.
4. 안내에 따라 YubiKey 금속 접점을 터치해 등록 완료.
5. 두 번째 예비 키 등록 권장.
6. "2단계 인증" 설정에서 하드웨어 키를 선호 인증 방식으로, SMS 인증번호를 예비로 설정.

주류 지원 웹사이트: Google, GitHub, Microsoft, Apple ID, Facebook, Twitter, Dropbox, GitLab, AWS, Coinbase, Binance 등.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>듀얼 키 전략

{class="mt-1"}
하드웨어 키의 가장 큰 위험은 "분실"입니다. 권장: ① 두 개의 다른 키를 동시에 등록; ② 하나는 휴대(열쇠고리), 하나는 집 금고나 은행 보관함에 보관; ③ 일부 웹사이트는 "예비 복구 코드"를 인쇄해 오프라인 보관할 수 있음. 이렇게 하면 주 키를 잃어도 계정에서 영구 잠기지 않습니다.
:::

::: div .warning-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>구매 루트 주의

{class="mt-1"}
반드시 공식 매장이나 공인 대리점에서 구매, 중고나 출처 불명의 키는 사지 마세요——이론적으로 사전 설정된 하드웨어에 백도어가 심어져 있을 수 있습니다. YubiKey의 펌웨어는 출고 후 업데이트할 수 없지만, Yubico는 지속적으로 보안 공지를 게시하니 공식 홈페이지를 확인하면 됩니다.
:::

#### 여덟, 가족/팀 비밀번호 공유

가족 시나리오에서는 Netflix, 가족 Wi-Fi, 라우터 백엔드, 스마트 도어록 비밀번호를 온 가족이 공유해야; 팀 시나리오에서는 서버, 데이터베이스, 소셜 미디어 계정을 여러 명이 협업해야 합니다.<strong>위챗으로 비밀번호를 보내거나 공유 문서에 적는 것은 모두 고위험 행위</strong>——채팅 기록이나 문서 권한이 유출되면 비밀번호도 유출됩니다.

##### 1. 1Password의 "공유 보관함"(Vault)

1Password는 가족과 팀 공유의 벤치마크 제품입니다. 핵심 메커니즘은<strong>여러 보관함</strong>입니다:

- <strong>개인 보관함</strong>: 본인만 볼 수 있음, 은행, 이메일 등 개인 계정.
- <strong>공유 보관함</strong>: 가족이나 팀원 모두 볼 수 있음, Netflix, 가족 Wi-Fi, 공유 신용카드.
- <strong>권한 등급</strong>: 팀 버전은 일부 멤버를 "보기 전용" 또는 "보기는 가능하나 편집 불가"로 설정 가능.

가족이나 팀원은 마스터 비밀번호를 공유할 필요 없이, 각자 자신의 계정으로 로그인, 권한을 받은 공유 보관함 내용을 볼 수 있습니다. 비밀번호 수정 후 모든 멤버에게 실시간 동기화.

##### 2. Bitwarden의 "조직" 기능

Bitwarden의 무료 버전은 개인 비밀번호 공유를 지원("Send 보내기" 기능으로 시간 제한 단일 비밀번호 공유); 유료 버전은 "조직"을 생성, 여러 항목을 가족 구성원이나 팀 동료에게 공유, 권한 세분화 가능. Bitwarden은 자체 호스팅 옵션도 제공, 데이터 주권 요구가 높은 기업에 적합.

##### 3. 가족 시나리오: Netflix, Wi-Fi 등 비밀번호의 안전한 공유 방식

- <strong>Netflix / 비디오 웹사이트</strong>: 1Password 가족 버전의 "공유 보관함"에 로그인 비밀번호 저장, 가족 구성원이 각자 로그인, 그룹에서 보낼 필요 없음.
- <strong>가족 Wi-Fi 비밀번호</strong>: iOS 기기 간 AirDrop으로 방문객에게 Wi-Fi 비밀번호를 직접 공유, 말할 필요 없음; Android 12+도 "주변 공유 Wi-Fi" 기능이 있음.
- <strong>스마트 도어록, 스마트 가전</strong>: 제조사 앱의 "가족 구성원" 기능으로 각자 별도 계정을 생성, 하나의 관리자 계정을 공유하지 않는 것을 권장.
- <strong>가정용 라우터 백엔드</strong>: 관리자 비밀번호는 1Password 공유 보관함에 저장, 게스트 Wi-Fi는 별도 SSID로 개설.

::: div .info-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-lightbulb mr-2"></i>1Password 가족 버전의 가성비

{class="mt-1"}
1Password Families는 약 4.99달러/월, 최대 5명의 가족 구성원 지원, 각자 독립된 개인 보관함 + 4개 공유 보관함. 1인당 월 1달러 미만, 현재 가족 공유 경험 최고의 방안. Bitwarden 가족 버전은 10달러/년에 6명 지원, 가성비 더 높지만 인터페이스 경험은 약간 떨어짐.
:::

##### 4. 팀 시나리오: 서버/데이터베이스 비밀번호 공유

- <strong>1Password Teams / Business</strong>: 부서, 프로젝트 그룹별로 여러 보관함 생성, 세분화된 권한 제어, 모든 접근 행위 감사 가능.
- <strong>Bitwarden Teams / Enterprise</strong>: 오픈소스 방안, 자체 호스팅 가능, 기업 버전은 SSO 통합, 디렉터리 동기화 지원.
- <strong>직무 분리 원칙</strong>: 관리자 비밀번호는 한 사람만 알아서는 안 됨——2-3명의 "비상 연락처"를 설정, 핵심 인물 퇴사/휴가 시 업무 중단 방지.
- <strong>퇴사 프로세스</strong>: 직원 퇴사 시 즉시 비밀번호 관리자 접근 권한 회수, 필요시 그가 접촉한 모든 고민감도 비밀번호 교체.

##### 5. 비상 접근(Emergency Access): 만약 당신에게 무슨 일이 생기면

상황을 상상해 보세요: 당신이 가족의 모든 중요 계정을 혼자 관리하는데, 갑자기 입원하거나 불행히도 세상을 떠나면, 가족이 은행, 이메일, 보험 계정에 로그인할 수 없게 됩니다.<strong>"비상 접근" 기능</strong>이 바로 이를 위해 설계되었습니다——신뢰하는 가족/친구 한 명에게 권한을 부여하여, 당신이 응답할 수 없을 때 비밀번호 보관함에 접근할 수 있도록.

<strong>Bitwarden 비상 접근 설정:</strong>

1. Bitwarden Web Vault 로그인 → 설정 → 비상 접근.
2. 신뢰하는 연락처의 이메일을 추가, 상대방이 수락하도록 초대.
3. "대기 기간" 설정(7-14일 권장): 상대방이 요청을 보낸 후 당신이 확인하는 시간 창.
4. 대기 기간 내 응답하지 않으면(거부 또는 조치 없음), 기간 만료 후 상대방이 자동으로 접근 권한을 얻음.
5. 언제든 수동으로 요청을 거부하거나 비상 접근 권한을 철회할 수 있음.

<strong>1Password 비상 접근:</strong>

1. 1Password는 직접 "비상 접근"이라 부르지 않지만, "가족/팀 조직" 기능으로 구현 가능——가족을 가족 버전에 추가한 후, 일부 항목을 "공유 보관함"에 넣기.
2. 개인 버전 사용자는 마스터 비밀번호를 고도로 신뢰하는 가족에게 알리거나, 밀봉한 봉투에 적어 금고에 보관하는 것을 권장.
3. 1Password는 "복구 코드"도 제공, 2단계 인증 켤 때 반드시 인쇄해 보관.

::: div .practice-box .rounded-lg .p-4 .mt-3
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>지금 바로 설정: 가족에게 "예비 열쇠"를 남기기

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 신뢰하는 가족 한 명을 "비상 연락처"로 선택.
2. 비밀번호 관리자에서 비상 접근 설정(Bitwarden) 또는 가족 공유 보관함에 추가(1Password).
3. 마스터 비밀번호 + 복구 코드를 종이에 적어 봉투에 넣고, 집 금고에 보관하거나 신뢰할 가족에게 알리기.
4. 반년마다 한 번씩 검토, 비상 연락처가 여전히 적합한지 확인.
:::

#### 아홉, 비밀번호 관리자 사용 모범 사례

- <strong>강한 마스터 비밀번호 설정</strong>: 마스터 비밀번호는 마지막 방어선, 길고 복잡한 비밀번호를 설정하고 외우세요.
- <strong>2단계 인증 활성화</strong>: 비밀번호 관리자 계정에 2단계 인증을 켜서 보호 계층 추가.
- <strong>정기적으로 약한 비밀번호 점검</strong>: 대부분의 비밀번호 관리자에는 "보안 감사" 기능이 있어 약한 비밀번호와 중복 비밀번호를 찾아줌.
- <strong>마스터 비밀번호 잊지 않기</strong>: 마스터 비밀번호는 복구 불가, 잊으면 모든 비밀번호를 잃는 것을 의미. 종이에 적어 안전한 곳에 보관 권장.
- <strong>비상 접근</strong>: 비상 연락처 설정, 당신이 접근할 수 없을 때 신뢰하는 사람이 비밀번호를 얻을 수 있도록.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>중요 알림

{class="mt-1"}
비밀번호 관리자는 편리하지만 위험도 있습니다: 마스터 비밀번호가 유출되면 모든 비밀번호가 노출됩니다. 그러므로 마스터 비밀번호는 다른 비밀번호와 절대 같으면 안 되고, 쉽게 찾을 수 있는 곳에 적어서도 안 됩니다. 또한, 좋은 보안 기록이 있는 서비스 제공자를 선택하세요.
:::

::: div .practice-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-hands mr-2"></i>지금 바로 시도: 비밀번호 관리자 사용 시작

{class="list-decimal pl-6 mt-1 space-y-1"}
1. 비밀번호 관리자 선택(Bitwarden 또는 시스템 내장 권장).
2. 계정 등록, 강한 마스터 비밀번호 설정.
3. 기존 비밀번호 가져오기(있다면) 또는 새 비밀번호 추가 시작.
4. 브라우저 플러그인이나 스마트폰 앱 설치, 자동 완성 기능 체험.
5. 보안 감사 보고서 점검, 개선이 필요한 비밀번호 찾기.
:::
