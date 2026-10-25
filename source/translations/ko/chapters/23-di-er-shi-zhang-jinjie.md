---
id: di-er-shi-zhang-jinjie
num: 20
part: jin-jie-pian
nav: 제20장: 개발자 모드와 고급 권한
toc: default
kind: supplement
---

### 제20장: 개발자 모드와 고급 권한

{class="chapter-intro mb-4"}
이 장은 스마트폰의 "숨겨진 기능"을 깊이 탐구하려는 사용자를 위한 것입니다. 개발자 모드, Root 권한, BL 잠금...이 극인스러운 개념들은 사실 일반 사용자에게서 그리 멀지 않습니다.

#### 하나, 개발자 모드: 숨겨진 설정 잠금 해제

개발자 모드는 스마트폰 시스템에 내장된 숨겨진 메뉴로, 일반 사용자는 안 쓰지만 개발자에게 필요한 기능이 많이 있습니다.

##### 활성화 방법:

- <strong>Android</strong>: 설정 > 스마트폰 정보 > "버전 번호" 7회 연속 탭, "이미 개발자 모드에 있습니다" 표시될 때까지.
- <strong>HarmonyOS</strong>: 설정 > 스마트폰 정보 > "HarmonyOS 버전" 7회 연속 탭.
- <strong>iOS</strong>: 일반 사용자는 완전한 개발자 모드 활성화 불가, 유료 Apple Developer 계정 필요.

##### 자주 쓰는 기능 한눈에:

- <strong>USB 디버깅</strong>: 컴퓨터 연결 고급 조작(플래싱, 데이터 복구, ADB 명령)을 위한 필수 스위치, 본 장 "ADB 실용 명령" 절 참조.
- <strong>터치 조작 표시</strong>: 화면에 터치점 표시(작은 원점이 손가락 따라감), 조작 튜토리얼 녹화나 데모에 적합.

##### 성능과 유창도 관련:

- <strong>애니메이션 속도 조정(창 애니메이션 스케일 / 전환 애니메이션 스케일 / 애니메이션 프로그램 시간 스케일)</strong>: 이 세 옵션은 앱 열기, 페이지 전환 시 애니메이션 시간을 제어. 기본 1x, 0.5x로 조정하면 스마트폰이 "보기에" 더 빠름(실제 프로그램 실행 속도는 변하지 않고, 애니메이션만 빨라짐), 끄기로 설정하면 애니메이션 없이 바로 전환. 대부분 극인은 0.5x로 설정, 전환감 유지하면서 빠르게 보이게; 완전히 끄면 조작이 딱딱해 보이고, 프로그램 실제 버벅거림을 가릴 수 있어, 오히려 "매우 유창"으로 착각하게 만듦.
- <strong>GPU 렌더링 강제(Force GPU Rendering)</strong>: 모든 2D 드로잉을 CPU가 아닌 GPU로 처리하도록 강제. 구형 모델이나 일부 앱 최적화 불량 시 스크롤 유창성 향상, 하지만 GPU 부하와 전력 소모 증가. 현대 스마트폰은 기본적으로 GPU 렌더링 대량 사용, 이 스위치는 중고급 모델에 미미한 영향, 역사적 유물 옵션, 일반 사용자는 기본값 유지.
- <strong>GPU 렌더링 모드 분석 표시(Profile GPU Rendering)</strong>: 화면에 막대그래프로 매 프레임 렌더링 시간 실시간 표시, 녹색 가로선은 16.6ms(60fps 프레임 시간 임계값) 의미. 막대가 녹색선 넘으면 프레임 드롭. 개발자가 앱 버벅거림 진단하는 강력 도구, 일반 사용자도 어느 앱 최적화가 나쁜지 비교 가능——예: 특정 앱 스크롤 시 막대가 자주 빨간선 넘으면, 기본적으로 그 앱 탓.

##### 백그라운드와 배터리 관련:

- <strong>백그라운드 프로세스 제한</strong>: "표준 제한", "최대 1개 프로세스", "최대 2개 프로세스" 등으로 설정할 수 있습니다. 백그라운드 프로세스를 제한하면 전력을 절약할 것처럼 보이지만, 사실 Android 자체의 백그라운드 관리가 이미 잘 되어 있어, 강제로 제한하면 오히려 앱이 자주 다시 로드됩니다(콜드 스타트가 더 전력을 소모하고 사용자 경험도 나빠집니다). 이 옵션은 디버깅용으로 적합하며, 일반 사용자가 장기간 켜놓는 것은 권장하지 않고, "표준 제한"으로 유지하는 것이 좋습니다.
- <strong>활동 유지 안 함</strong>: 화면을 떠날 때마다 즉시 화면을 파괴합니다. 매우 권장하지 않으며, 앱이 자주 화이트 스크린과 재로드 현상을 일으키고, 앱의 복구 로직 테스트용으로만 사용됩니다.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>주의사항

{class="mt-1"}
개발자 모드의 설정은 시스템 안정성에 영향을 미칠 수 있으므로, 잘 모르는 옵션은 함부로 변경하지 마세요. USB 디버깅을 켠 후에는 컴퓨터에 연결할 때 주의하고, 신뢰할 수 없는 컴퓨터에는 연결하지 마세요.
:::

#### 둘, OEM 잠금 해제: 개발자 옵션의 "플래싱 스위치"

개발자 옵션에는 그리 눈에 띄지 않지만 중요한 스위치가 하나 있는데, 그것이 "OEM 잠금 해제"(일부 브랜드에서는 "OEM 잠금 해제 허용" 또는 "기기 잠금 해제"라고 함)입니다. 이 스위치 자체는 BL 잠금을 해제하지 않지만, "사전 허가" 역할을 합니다: 이것을 켜야만 제조사가 fastboot 명령이나 브랜드 도구를 통해 BL 잠금을 해제하는 것을 허용합니다.

- <strong>스위치의 역할</strong>: 제조사에 "나는 보증을 포기하고 스스로 책임지며 BL 잠금 해제를 허용해 달라고" 선언하는 것과 같습니다. 이 스위치가 꺼져 있으면, BL 잠금 해제 명령은 모두 직접 거부됩니다.
- <strong>BL 잠금과의 관계</strong>: OEM 잠금 해제는 "자격 신청"이고, BL 잠금 해제가 "실제 작동"입니다. 전자는 스마트폰 설정에서 한 번 누르기만 하면 되지만, 후자는 제조사 공식 웹사이트에서 잠금 해제 코드를 신청하고, 컴퓨터에서 fastboot 명령(예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing unlock</code>)을 실행해야 하며, 둘 다 반드시 필요합니다.
- <strong>공장 초기화로 재설정되는가</strong>: 그렇습니다. "OEM 잠금 해제" 스위치는 공장 초기화 후 꺼진 상태로 돌아가지만, BL 잠금은 한 번 해제되면 물리적 수준의 상태이므로, 공장 초기화로 다시 잠기지 않습니다 — <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot flashing lock</code>을 수동으로 실행해야만 다시 잠글 수 있습니다.
- <strong>언제 켜야 하는가</strong>: 플래싱이나 Root 작업을 확실히 하려는 경우가 아니면 꺼진 상태로 유지하세요. 이것은 "USB 디버깅"과 별개의 스위치이며, 플래싱할 때 보통 두 개를 모두 켜야 합니다.

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>알림: 제조사가 왜 이 스위치를 설정하는가

{class="mt-1"}
초기 안드로이드에는 이 스위치가 없어서, 악성 소프트웨어가 권한만 얻으면 몰래 시스템을 플래싱할 수 있었습니다. Google은 이후 모든 안드로이드 제조사에 개발자 옵션에 "OEM 잠금 해제" 스위치를 추가하도록 요구했고, 이를 "사용자 인지 동의" 확인 절차로 사용했습니다. 이것이 바로 BL 잠금을 해제했더라도 OEM 잠금 해제 스위치가 꺼져 있으면, 다시 플래싱할 때 실패하는 이유입니다.
:::

#### 셋, BL 잠금(Bootloader 잠금): 플래싱의 첫 번째 관문

Bootloader는 스마트폰이 시작될 때 운영체제를 로드하는 프로그램입니다. BL 잠금은 제조사가 보안을 위해 추가한 잠금으로, 사용자가 비공식 시스템을 플래싱하는 것을 방지합니다.

##### BL 잠금의 역할:

- <strong>보안 보호</strong>: 악성 소프트웨어가 시스템을 플래싱하는 것을 방지합니다.
- <strong>도난 방지</strong>: 스마트폰이 플래싱되더라도 원래 계정 비밀번호 없이는 사용할 수 없습니다.
- <strong>보증 제한</strong>: BL 잠금 해제는 보통 공식 보증을 잃는다는 것을 의미합니다.

##### 각 브랜드별 BL 잠금 정책:

- <strong>샤오미</strong>: 잠금 해제 가능, 계정 연결 및 대기 기간 필요(7-30일).
- <strong>화웨이</strong>: 2018년 이후 잠금 해제 코드 제공 중단, 공식적으로 잠금 해제가 거의 불가능합니다.
- <strong>원플러스</strong>: 잠금 해제 가능, 비교적 느슨합니다.
- <strong>OPPO/vivo</strong>: 일부 모델은 잠금 해제 가능, 신청 필요.
- <strong>삼성</strong>: 잠금 해제 가능하지만 Knox가 영구 손상되어 Samsung Pay 등 기능을 잃게 됩니다.
- <strong>애플</strong>: iOS 기기에는 전통적인 의미의 BL 잠금 개념이 없지만, 유사한 보안 메커니즘이 있습니다.

#### 넷, ADB 실용 명령: 컴퓨터로 스마트폰 제어

ADB는 Android Debug Bridge(안드로이드 디버그 브리지)의 약자로, Google에서 공식 제공하는 명령줄 도구로, 컴퓨터가 USB 또는 Wi-Fi를 통해 안드로이드 스마트폰과 통신할 수 있게 합니다. Root가 필요하지 않으며, 스마트폰에서 "USB 디버깅"을 켜기만 하면 사용할 수 있습니다. 이를 "컴퓨터로 스마트폰에 명령을 내리는 리모컨"이라고 이해하면 됩니다 — 플래싱, 앱 설치, 파일 전송, 로그 확인에 모두 필요합니다.

##### USB를 통해 연결하는 방법:

1. 스마트폰 측: 개발자 옵션 진입 → "USB 디버깅" 켜기.
2. 컴퓨터 측: Google 공식 웹사이트에서 Platform Tools 다운로드(<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb</code>와 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">fastboot</code> 두 개의 실행 파일 포함), 원하는 디렉터리에 압축 해제.
3. 데이터 케이블로 스마트폰과 컴퓨터를 연결하면, 스마트폰에 "USB 디버깅을 허용하시겠습니까?" 팝업이 나타나며, "항상 허용"을 선택하고 확인.
4. 컴퓨터 명령줄(Windows의 PowerShell 또는 cmd)에서 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>를 실행하고, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">List of devices attached / xxxxxxxx device</code>와 같은 출력이 나오면 연결된 것입니다.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>드라이버와 인증 팝업을 무시하지 마세요

{class="mt-1"}
Windows 사용자가 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb devices</code>에서 "unauthorized"가 표시되거나 기기가 아예 나열되지 않으면, 대부분 드라이버가 제대로 설치되지 않았거나 스마트폰에서 "허용"을 클릭하지 않은 것입니다. 삼성/샤오미 등 브랜드는 각자의 "USB 드라이버" 또는 "휴대폰 도우미"를 설치하여 드라이버를 보완할 수 있으며, Mac과 Linux는 일반적으로 드라이버가 필요 없습니다. 스마트폰 팝업을 실수로 닫은 경우, 데이터 케이블을 분리했다 다시 연결하면 팝업이 다시 나타납니다.
:::

##### 자주 사용하는 ADB 명령:

- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb install app.apk</code>: 컴퓨터의 APK를 스마트폰에 설치(<code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-r</code>은 데이터 유지하며 덮어쓰기 설치; <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>는 SD 카드에 설치).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb uninstall com.xxx.xxx</code>: 패키지 이름으로 앱을 제거합니다.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb push 컴퓨터경로 /sdcard/대상경로</code>: 컴퓨터 파일을 스마트폰으로 전송.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb pull /sdcard/파일 컴퓨터경로</code>: 스마트폰 파일을 컴퓨터로 가져오기(본인 위챗에 보내서 다운로드하는 것보다 훨씬 빠름).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell</code>: 스마트폰의 Linux Shell로 진입하여 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">ls</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm</code>, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">am</code> 등의 명령을 직접 실행할 수 있습니다.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot bootloader</code>: 스마트폰을 재시작하여 Fastboot 모드로 진입(플래싱의 시작점).
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb reboot recovery</code>: 재시작하여 Recovery 모드로 진입.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages</code>: 스마트폰에 설치된 모든 앱의 패키지 이름 나열(패키지 이름 찾기에 필수). <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-s</code>를 추가하면 시스템 앱만, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">-3</code>을 추가하면 서드파티 앱만 표시.
- <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 패키지명</code>: 현재 사용자에 대해 사전 설치된 앱을 제거하며, Root 불필요, 자세한 내용은 아래 실전 참조.

##### Root 없이 사전 설치된 앱 제거 실전:

이것은 ADB의 가장 실용적인 기능 중 하나입니다: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code> 명령을 사용하여 "현재 사용자"에 대해 사전 설치된 앱을 제거할 수 있으며, Root가 필요 없고 시스템 파티션에도 영향을 주지 않습니다. 제거된 앱은 시스템에서 "사라지지만", 실제로는 여전히 시스템 파티션에 있으며, 공장 초기화 후 다시 나타납니다.

1. 먼저 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages -s</code>로 모든 시스템 앱을 나열하고, 제거하려는 패키지 이름을 찾습니다. 예를 들어 샤오미 브라우저는 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.browser</code>, 화웨이 앱마켓은 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.vmall.client</code>입니다.
2. 패키지 이름이 어떤 앱에 해당하는지 확실하지 않다면? 컴퓨터에서 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm list packages | findstr 키워드</code>로 검색하거나, 서드파티 앱 "Package Viewer"를 스마트폰에 설치하여 각 앱의 패키지 이름을 직접 확인할 수 있습니다.
3. 제거 실행: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 패키지명</code>, 예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell pm uninstall --user 0 com.android.browser</code>. <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">Success</code>가 반환되면 성공입니다.
4. 복구하려면? 두 가지 방법: ① 공장 초기화(가장 철저하지만 번거로움); ② 재설치: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">adb shell cmd package install-existing 패키지명</code>.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>시스템 핵심 패키지를 함부로 삭제하지 마세요

{class="mt-1"}
"pm uninstall --user 0"은 Root가 필요 없는 안전한 방법이지만, 핵심 시스템 앱을 함부로 삭제하면(예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.systemui</code> 상태 표시줄, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.phone</code> 전화, <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">com.android.settings</code> 설정) 시스템 충돌, 검은 화면, 부팅 불가 등 심각한 문제를 일으킵니다. 삭제하기 전에 먼저 "이 패키지 이름을 삭제할 수 있는지" Google에서 검색하고, 적게 삭제하더라도 잘못 삭제하지 않도록 주의하세요. 한 번에 한두 개씩만 삭제하고, 문제가 없는지 확인한 후 계속 진행하는 것을 권장합니다.
:::

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>알림: --user 0의 의미

{class="mt-1"}
안드로이드 4.2 이후 다중 사용자가 지원되며, 각 사용자는 고유한 ID를 가집니다(기기 소유자는 0, 추가 사용자는 10부터 시작). <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">--user 0</code>은 "현재 기기 소유자에 대해서만 제거"를 의미하며, 시스템 파티션의 APK 파일은 여전히 존재하지만, 기기 소유자에게 표시되지 않을 뿐입니다. 이것이 Root가 필요하지 않은 이유입니다 — 시스템 파일을 건드리지 않고 "사용자 구성"만 변경했습니다. 이것이 Root 후 제거와의 가장 큰 차이점입니다: Root 제거는 시스템에서 실제로 삭제되어 모든 사용자에게 더 이상 표시되지 않지만, ADB 제거는 "현재 사용자에게 숨김"일 뿐입니다.
:::

#### 다섯, Root 권한: 안드로이드의 "슈퍼 관리자"

Root 권한은 Linux의 슈퍼 사용자에 해당하며(/ 디렉터리에 대한 완전한 제어권 소유, 모든 파일 읽기/쓰기 가능), 안드로이드 시스템의 최고 권한입니다. 이는 Windows의 Administrator와 본질적으로 다릅니다: Windows는 보안을 고려하여 관리자에 대해 많은 제한을 두었으며(진정한 최고 권한은 사실 TrustedInstaller임), Administrator라 할지라도 Linux root처럼 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">sudo rm -rf /*</code>을 직접 실행할 수 없습니다. Root 권한을 얻으면 시스템 파일 수정, 사전 설치된 앱 제거, Root가 필요한 고급 앱 사용이 가능합니다.

##### Root의 장점:

- 제거할 수 없는 사전 설치된 앱을 제거합니다.
- 고급 기능 앱(예: 타이타늄 백업, 그린 가드)을 사용합니다.
- 시스템 인터페이스와 기능을 수정합니다.
- 서드파티 Recovery와 커스텀 ROM을 설치합니다.

##### Root의 위험:

- <strong>보증 상실</strong>: 대부분의 제조사는 Root된 스마트폰에 대해 보증을 제공하지 않습니다.
- <strong>보안 위험</strong>: 악성 앱이 Root 권한을 얻어 심각한 결과를 초래할 수 있습니다.
- <strong>시스템 불안정</strong>: 잘못된 작업으로 시스템이 충돌할 수 있습니다.
- <strong>은행 앱 사용 불가</strong>: 많은 은행 및 결제 앱은 Root가 감지되면 실행을 거부합니다.
- <strong>OTA 업데이트 실패</strong>: 공식 시스템 업데이트를 정상적으로 받을 수 없을 수 있습니다.

::: div .danger-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-skull-crossbones mr-2"></i>심각한 경고

{class="mt-1"}
Root 작업에는 일정 위험이 있으며, 스마트폰이 벽돌(부팅 불가)이 될 수 있습니다. 초보자라면 먼저 관련 지식을 충분히 이해하고, 완전한 백업을 확보하세요. 작업 전 튜토리얼을 자세히 읽고, 기기 모델과 시스템 버전을 확인하세요.
:::

#### 여섯, SafetyNet과 Play Integrity 인증: Root 후 은행 앱이 사용 불가인 이유

많은 Root 사용자가 이러한 좌절스러운 순간을 겪어봤을 것입니다: Root 이후 신나서 모듈을 잔뜩 설치했는데, 은행 앱을 열면 — "기기가 안전하지 않아 사용할 수 없습니다", Google Pay도 사용할 수 없으며, Netflix도 고화질 재생을 거부합니다. 이 모든 것의 배경에는 Google의 두 가지 기기 무결성 인증 메커니즘이 있습니다: 구버전 SafetyNet과 새로운 Play Integrity API.

##### SafetyNet / Play Integrity란?

- <strong>SafetyNet Attestation(구버전, 2017년부터)</strong>: Google이 초기 출시한 기기 무결성 검사 API로, 앱이 이를 통해 Google 서버에 "이 기기가 CTS 호환성 테스트를 통과했는지, 수정되지 않은 공식 상태인지"를 조회합니다. 반환 결과는 Basic Attestation(기본 검증)과 Strong Attestation(강력한 검증, 하드웨어 키에 의존)으로 나뉩니다. Google은 SafetyNet이 2024년 이후 점차 중단될 것이라고 발표했습니다.
- <strong>Play Integrity API(신버전, 2022년부터)</strong>: Google이 출시한 대체 방안으로, SafetyNet보다 더 엄격하고 포괄적입니다. 기기 무결성 외에도 "앱 무결성"(앱이 변조되었는지)과 "계정/권한 무결성"(사용자 계정이 Google의 신뢰를 받는지)이 포함됩니다. 새로운 앱은 Play Integrity로 마이그레이션해야 합니다.
- <strong>누가 사용하는가</strong>: 은행, 금융, 결제 앱(예: Google Pay, 각 은행의 인터넷 뱅킹, Alipay/위챗 결제의 일부 시나리오), 스트리밍(Netflix 고화질 저작권 보호), 일부 게임 안티 치트(예: 텐센트/넷이즈의 일부 게임), 기업 업무용 앱(MDM 기기 규정 준수 검사).

##### Play Integrity의 3단계 인증 결과:

- <strong>MEETS_DEVICE_INTEGRITY(기기 무결성 통과)</strong>: 기기가 정품 Android 시스템을 실행하고, Bootloader가 잠겨 있으며, Root가 없고, CTS 호환성 테스트를 통과했습니다. 은행 및 결제 앱을 정상적으로 사용할 수 있습니다.
- <strong>MEETS_BASIC_INTEGRITY(기본 무결성 통과)</strong>: 기기가 기본적으로 신뢰할 수 있지만, 약간의 이상이 있을 수 있습니다. 일부 앱은 사용 수준을 낮춥니다(예: Netflix는 여전히 재생 가능하지만 화질 제한), 일부 엄격한 은행 앱은 직접 거부합니다.
- <strong>MEETS_STRONG_INTEGRITY(강력한 무결성 통과)</strong>: 최고 수준으로, 하드웨어 키 보증 필요(예: Google Pixel 시리즈의 Titan M 칩), 대부분의 타사 브랜드 기기는 Root가 없더라도 이 수준에 도달하지 못합니다.
- <strong>어떠한 레이블도 없음(NO_INTEGRITY)</strong>: 기기가 Root되었거나, BL이 잠금 해제되었거나, 서드파티 ROM이 플래싱되었거나, 에뮬레이터로 식별된 경우로, 거의 모든 결제/은행 앱이 실행을 거부합니다.

##### Root 후 이러한 앱이 작동하지 않는 이유:

앱은 Play Integrity API를 통해 Google 서버에 인증 요청을 보내며, Google은 기기의 여러 지표를 확인합니다 — Bootloader 잠금 상태, 시스템 파티션 수정 여부, su 바이너리 파일 존재 여부, SELinux가 완화 모드에 있는지 여부 등. 어느 하나라도 비정상적이어서 반환된 인증 수준이 낮아지거나 비어 있으면, 은행 앱은 "기기가 안전하지 않음"으로 간주하고 당연히 서비스 거부합니다. <h5 class="font-semibold mt-3 mb-1">현대적 숨김 방안: Magisk Hide / Shamiko / Zygisk:</h5> <p class="mb-2">Root의 편리함을 즐기면서 은행 앱도 사용하기 위해, 커뮤니티는 "Root 상태 숨김" 일련의 방안을 개발했습니다. 핵심 아이디어는 모두 같습니다: 감지 프로그램이 수정된 시스템이 아닌 "정상적으로 보이는" 기기를 보게 하는 것입니다. <ul class="list-disc pl-6 mb-3 space-y-1"> <li><strong>Magisk</strong>: 현재 가장 주류인 Systemless Root 방안 — 시스템 파티션을 수정하지 않고 마운트 방식으로 Root를 구현합니다. 이렇게 설계한 이점은 OTA 업데이트 실패 확률이 낮고, 제거가 비교적 깨끗한 점이며, 이후 모든 숨김 방안의 기초입니다. 하지만 Magisk를 사용하려면 여전히 BL 잠금을 해제해야 합니다.</li> <li><strong>Magisk Hide(업데이트 중단)</strong>: Magisk 초기에 내장된 숨김 모듈로, 지정된 앱에 대해 Root를 숨길 수 있습니다. 하지만 2021년부터 Magisk 공식에서 제거되었으며, 그 이유는 Google이 지속적으로 감지 수단을 업그레이드하면서 양측이 "고양이와 쥐 게임"에 빠졌기 때문입니다.</li> <li><strong>Zygisk</strong>: Magisk 24.0+에서 도입된 새로운 메커니즘으로, Riru와 유사하며 Zygote 프로세스에 주입하여 모듈을 로드하는 방식으로, 시스템을 직접 수정하는 것보다 더 은밀합니다. Zygisk를 켜는 것은 현대적 숨김 방안을 사용하는 전제 조건입니다.</li> <li><strong>Shamiko</strong>: 현재 가장 주류인 숨김 모듈로, Zygisk와 함께 작동하며, 지정된 앱("역방향 화이트리스트" 모드)에 대해 Root 숨김, Magisk 자체 숨김, Bootloader 잠금 상태 위조가 가능합니다. Shamiko는 LSPosed 저장소 또는 GitHub를 통해 배포됩니다.</li> <li><strong>Play Integrity Fix(osm0sis)</strong>: Google Play Integrity 감지를 특화 대상으로 하는 Magisk 모듈로, 기기 지문(fingerprint)을 수정하여 Google이 기기를 Root되지 않은 공식 기기로 인식하게 합니다.</li> </ul> <div class="warning-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-exclamation-triangle mr-2"></i>고양이와 쥐 게임은 절대 끝나지 않습니다</p> <p class="mt-1">Google은 주기적으로 감지 규칙을 업데이트하고, 앱 제조사도 Play Integrity 검증을 업그레이드합니다. 오늘 작동하는 숨김이 내일은 인식될 수 있습니다. 은행/결제 앱에 전적으로 의존하는 경우(예: 일상적인 계좌 이체, QR 결제), 가장 안정적인 선택은 여전히: Root하지 않기, BL 잠금 해제하지 않기. 숨김이 더 적합한 구성은 "주력기는 Root하지 않음 + 보조기로 Root 놀이"입니다. </p></div> <h4 class="text-lg font-semibold mt-4 mb-2">일곱, 일반 사용자를 위한 권장사항</h4> <ul class="list-disc pl-6 mb-3 space-y-1"> <li><strong>개발자 모드</strong>: 켤 수 있으며, 애니메이션 가속, GPU 렌더링 분석 등의 기능을 경험해 볼 수 있지만, 이해할 수 없는 다른 옵션은 함부로 변경하지 마세요.</li> <li><strong>OEM 잠금 해제와 BL 잠금</strong>: 플래싱이나 Root를 할 계획이 없다면, 두 스위치 모두 기본값(꺼짐) 상태로 유지하는 것이 가장 안전합니다.</li> <li><strong>ADB</strong>: Root가 필요 없는 강력한 도구로, 일반인도 사용할 수 있습니다 — 예를 들어 <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">pm uninstall --user 0</code>으로 사전 설치된 앱을 제거할 수 있습니다. 하지만 삭제하기 전에 반드시 패키지 이름을 조사하세요.</li> <li><strong>Root</strong>: 일반 사용자에게는 Root를 권장하지 않으며, 위험이 이점보다 큽니다. 특정 기능이 정말 필요한 경우, 먼저 Root가 필요 없는 대안이 있는지 확인하세요(예: ADB로 사전 설치 앱 제거, Shizuku로 일부 Root 기능 대체).</li> </ul> <div class="practice-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-hands mr-2"></i>직접 해보기: 개발자 모드를 켜고 애니메이션 속도 조정</p> <ol class="list-decimal pl-6 mt-1 space-y-1"> <li>설정 > 휴대전화 정보로 진입.</li> <li>"빌드 번호"를 7회 연속 탭하여 개발자 모드가 활성화되었다는 알림이 나타날 때까지.</li> <li>설정으로 돌아가 "개발자 옵션" 찾기(보통 설정 하단 또는 "시스템" 안에 있음).</li> <li>"창 애니메이션 배율", "전환 애니메이션 배율", "애니메이터 기간 배율"을 찾아 모두 0.5x로 설정하거나 끄기.</li> <li>스마트폰이 빨라졌는지 느껴보세요.</li> </ol> </div> </p>
