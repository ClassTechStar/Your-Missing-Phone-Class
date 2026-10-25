---
id: di-er-shi-san-zhang-github
part: chao-yue-pian
nav:  부록: GitHub 입문 가이드
toc: sub
kind: chapter
---

### 제23장 부록: GitHub 입문 가이드 — 코드 호스팅에서 협업 플랫폼까지

{class="chapter-intro mb-4"}
이전 장에서 "프로그래밍 사고방식"을 배웠고, 프로그래밍 사고방식을 실제로 착지하고, 다른 사람과 함께 프로젝트를 하려면, 하나의 이름을 회피할 수 없습니다 — GitHub. 컴퓨터과 학생이 대회에 참가하거나, 자신의 코드 작품을 저장하거나, 단순히 전 세계 개발자들이 무엇을 삽질하는지 보고 싶든, GitHub는 반드시 알아야 할 플랫폼입니다. 이 절에서는 가장 기본적인 개념부터 설명하여, 명확한 인식을 세우는 데 도움을 드립니다.

#### 하나, GitHub란 도대체 무엇인가?

간단히 말해, GitHub는 Git 기반의 <strong>코드 호스팅 및 협업 플랫폼</strong>입니다. 2008년에 런칭되었으며, 2018년에 Microsoft가 인수하여, 현재까지도 세계 최대의 오픈 소스 코드 호스팅 플랫폼으로, 수억 개의 저장소를 호스팅하며, 거의 모든 주류 프로그래밍 언어를 망라합니다.

비유로 이해하자면: <strong>Git은 컴퓨터의 일기장이고, GitHub는 공개 블로그 플랫폼</strong>입니다 — 자신의 작품을 발표하고, 다른 사람의 프로젝트를 팔로우하며, 토론과 협업에 참여할 수 있습니다. 그것은 "프로그래머의 백엔드 창고"일 뿐만 아니라, 마치 전 세계 개발자들이 공동 건설하는 "기술 도시"와 같습니다 — 프로젝트가 여기서 탄생하고, 이터레이션되며, 토론되고, 재사용됩니다.

일반인에게 GitHub은 결코 멀지 않습니다. 많은 비프로그래머들이 노트, 전자책, 개인 블로그를 호스팅하거나, 설정 파일을 백업하는 데 사용합니다. "자신의 것을 정리하고 공유하고 싶다"는 수요가 조금이라도 있다면, GitHub는 알 만한 가치가 있습니다.

#### 둘, Git와 GitHub의 차이(핵심 개념!)

많은 사람들이 처음 접촉할 때 이 두 단어를 혼동하는데, 여기서 명확히 정리해 드립니다:

```html
<table class="w-full border-collapse border border-gray-300 text-sm mb-3">
                        <thead>
                            <tr class="bg-light dark:bg-gray-700">
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">대비 항목</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">Git</th>
                                <th class="border border-gray-300 dark:border-gray-600 px-3 py-2 text-left">GitHub</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">본질</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">버전 관리 도구(소프트웨어)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">코드 호스팅 플랫폼(웹사이트)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">실행 위치</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">로컬 컴퓨터</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">클라우드(브라우저로 접근)</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">핵심 책임</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">파일의 매번 변경 기록(어떻게, 누가, 언제 변경했는지)</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Git 저장소를 클라우드에 올려, 저장, 표시, 협업 용이</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">네트워크 필요 여부</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">필요 없음, 오프라인 사용 가능</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">네트워크 연결 필요</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">소속</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">오픈 소스 소프트웨어, Linus Torvalds(Linux의 아버지)가 만듦</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">Microsoft 산하 제품</td>
                            </tr>
                            <tr>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">동종 경쟁 제품</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">SVN, Mercurial</td>
                                <td class="border border-gray-300 dark:border-gray-600 px-3 py-2">GitLab, Gitee(코드클라우드), Bitbucket</td>
                            </tr>
                        </tbody>
                    </table>
```

간단히 말해: <strong>Git은 "변경을 어떻게 기록할지", GitHub는 "변경이 어디에 있고 어떻게 협업할지"를 관리</strong>. Git은 도구로, 로컬에서 실행; GitHub은 플랫폼으로, Git 저장소를 클라우드에 올려, 협업과 표시를 용이하게 합니다. Git만 사용하고 GitHub을 사용하지 않을 수 있지만(예: 자신만 코드를 쓰고 버전 관리), GitHub을 사용하려면 반드시 Git을 사용해야 합니다(GitHub은 Git 기반이기 때문).

#### 셋, GitHub의 핵심 개념과 기능

##### 📁 기본 개념

착수하기 전에, 먼저 몇 가지 고빈도 용어를 알아야 합니다, 그렇지 않으면 GitHub 인터페이스를 보고 완전히 멍해질 것입니다:

- <strong>저장소(Repository, 약칭 Repo)</strong>: 한 프로젝트에 한 저장소가 대응하며, 이 프로젝트의 모든 코드 파일, 역사 버전, 문서가 들어 있습니다. "프로젝트 폴더"로 이해할 수 있습니다.
- <strong>커밋(Commit)</strong>: 코드에 대한 한 번의 수정 기록. 매 커밋마다 설명 정보가 첨부되어, "이번에 무엇을, 왜 변경했는지"를 기록. 이것이 Git/GitHub가 "시간 역행"할 수 있는 기초.
- <strong>브랜치(Branch)</strong>: 주류에서 갈라져 나온 독립 개발 라인. 예를 들어 새 기능을 추가하고 싶다면, 브랜치를 열어 단독 개발할 수 있으며, 개발 완료 후 주류로 병합하며, 다른 사람에게 영향을 주지 않습니다.
- <strong>클론(Clone)</strong>: 클라우드 저장소를 로컬 컴퓨터에 완전히 복사, 이후 로컬에서 코드를 수정할 수 있습니다.
- <strong>푸시(Push)/풀(Pull)</strong>: 푸시는 로컬 코드를 GitHub에 업로드, 풀은 GitHub에서 최신 코드를 로컬로 다운로드. 이것은 팀 협업 시 코드를 동기화하는 두 가지 핵심 동작.
- <strong>병합 요청(Pull Request, 약칭 PR)</strong>: 한 브랜치에서 코드 수정을 완료하고 주 브랜치로 병합하고 싶을 때, PR을 발기하여 팀원이 코드를 검토한 후 병합하도록 합니다. 이것이 GitHub 협업의 핵심 메커니즘.
- <strong>이슈(Issue)</strong>: 버그, 기능 수요, 토론 주제를 기록하는 데 사용. 각 이슈는 토론 게시물과 같으며, 담당자를 지정하고, 레이블을 붙일 수 있습니다.
- <strong>Fork</strong>: 다른 사람의 저장소를 자신의 계정 아래로 복사하며, 원본 저장소에 영향을 주지 않고 자신의 복사본에서 자유롭게 수정할 수 있습니다. 수정 후 원작자에게 PR을 보내 병합을 요청할 수 있습니다.

##### 🛠️ 핵심 기능

GitHub는 코드 저장만 제공하는 것이 아니라, 다음도 포함합니다:

- <strong>버전 관리</strong>: 매번 코드 변경의 역사 기록, 코드를 잘못 수정해도 언제든 이전 정상 버전으로 돌아갈 수 있음.
- <strong>팀 협업</strong>: 동일 프로젝트에 대한 다중 사용자의 병렬 개발 지원, 여러 사람이 동시에 개발해도 덮어쓰기, 충돌 없음.
- <strong>문제 추적</strong>: 이슈로 버그와 기능 요청 기록, 팀의 후속 조치 용이.
- <strong>프로젝트 관리</strong>: 할 일, 프로젝트 칸반(Projects) 등 관리 도구 통합, 경량형 Trello 내장.
- <strong>자동화</strong>: <strong>GitHub Actions</strong>를 통해 코드 제출 후 자동 컴파일, 테스트, 패키징, 배포 구현, 현대 "CI/CD(지속적 통합/지속적 배포)"의 핵심 도구.
- <strong>문서 관리</strong>: README로 프로젝트 소개, Wiki에 자세한 아키텍처와 개발 규범 보관, Pages는 정적 웹사이트를 직접 호스팅할 수도 있음.
- <strong>코드 호스팅 및 표시</strong>: 각 저장소는 모두 멋진 웹 페이지 표시가 있으며, 구문 강조를 지원, 기술 작품의 "정면"입니다.
- <strong>오픈 소스 커뮤니티</strong>: 좋아하는 프로젝트 Star(즐겨찾기), Watch(프로젝트 동적 팔로우), Follow(개발자 팔로우), 전 세계 오픈 소스 협업 참여 가능.

#### 넷, 가입 및 시작: 5분 만에 첫 번째 저장소 만들기

##### 📝 등록계정

1. <a href="https://github.com" class="text-primary hover:underline" target="_blank" rel="noopener">github.com</a> 방문, "Sign up" 클릭.
2. 이메일 작성, 비밀번호와 사용자 이름 설정(사용자 이름은 개인 홈페이지 주소에 나타나며, 영어 사용 권장, 예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">github.com/yourname</code>).
3. 이메일 인증 및 사람-기계 인증 완료.
4. 무료 플랜(Free) 선택하면 됨, 개인 사용자에게는 완전히 충분.

##### 📁 첫 번째 저장소 만들기

1. 로그인 후 오른쪽 상단 "+" 클릭, "New repository" 선택.
2. 저장소 이름(Repository name) 작성, 예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">my-first-project</code>.
3. 간단한 설명(Description) 작성, 다른 사람들이 이 저장소가 무엇인지 알 수 있도록.
4. 공개(Public) 또는 비공개(Private) 선택. 공개 저장소는 모든 사람에게 보이며, 비공개는 자신과 협력자에게만 보입니다. 무료 계정도 무한 비공개 저장소를 지원합니다.
5. "Add a README file" 체크 — README는 프로젝트의 "설명서"이며, 모든 저장소에 있을 것을 권장.
6. "Create repository" 클릭, 당신의 첫 번째 GitHub 저장소가 탄생했습니다!

::: div .info-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-info-circle mr-2"></i>알림: README란 무엇인가

{class="mt-1"}
README.md는 Markdown 형식의 파일로, 다른 사람이 저장소를 열 때 첫 눈에 보는 내용입니다. 좋은 README는 보통 포함: 프로젝트 소개, 설치 방법, 사용 예시, 라이선스, 연락처 정보. README를 잘 쓰는 것은 프로그래머의 기본 소양이며, 프로젝트가 다른 사람에게 사용될 수 있는 첫 번째 관문입니다.
:::

#### 다섯, 기본 작업 흐름: 로컬에서 클라우드로

GitHub의 작업 흐름을 이해하는 핵심은 이 순환을 기억하는 것입니다: <strong>로컬 수정 → 스테이징 → 커밋 → 푸시 → 클라우드 업데이트</strong>. 아래에서 백설로 각 단계를 설명합니다:

1. <strong>파일 수정</strong>: 로컬 컴퓨터에서 편집기로 코드를 쓰거나 문서를 수정.
2. <strong>git add</strong>: 수정된 파일을 "스테이징 영역"에 추가, 즉 Git에게 "이 변경 사항을 기록할 준비가 됨"을 알림.
3. <strong>git commit</strong>: 스테이징 영역의 변경 사항을 공식적으로 "커밋"으로 기록, 설명 문구 첨부, 예: "로그인 버그 수정". 이 단계는 로컬에서만 완료.
4. <strong>git push</strong>: 로컬 커밋을 GitHub 클라우드에 업로드, 이렇게 다른 사람들이 볼 수 있게 됨.
5. <strong>git pull</strong>: 작업 시작 전, 먼저 클라우드에서 최신 코드를 풀, 로컬과 팀의 다른 구성원이 동기화되도록 보장.

초보자에게는 이 구절을 기억하세요: <strong>"먼저 pull 후 수정, 수정 후 add, 커밋에 설명 첨부, 마지막에 push"</strong>. 이 습관을 기르면, 팀 협업이 어지럽지 않습니다.

#### 여섯, 팀 협업 흐름: Pull Request는 어떻게 작동하는가

GitHub의 가장 강력한 점은 그 협업 메커니즘입니다. 일반적인 팀 협업 흐름은 다음과 같습니다:

1. <strong>브랜치 열기</strong>: 주 브랜치(보통 main 또는 master)에서 새 브랜치를 엽니다, 예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">feature/login</code>, 이 브랜치에서 새 기능 개발.
2. <strong>개발 및 커밋</strong>: 새 브랜치에서 코드 작성, 여러 번 커밋하여 진행 상황 기록.
3. <strong>GitHub에 푸시</strong>: 브랜치를 클라우드 저장소에 푸시.
4. <strong>Pull Request 발기</strong>: GitHub 웹페이지에서 PR을 발기, 브랜치를 주 브랜치로 병합 요청. 이 PR이 무엇을 변경했는지, 왜 변경했는지 명확히 작성.
5. <strong>코드 검토(Code Review)</strong>: 팀원이 코드를 보고, 의견 또는 수정 제안 제출. 피드백에 따라 계속 커밋할 수 있으며, PR이 자동 업데이트됨.
6. <strong>병합</strong>: 검토 통과 후, "Merge" 클릭하여 코드를 주 브랜치로 병합. 당신의 공헌이 공식적으로 프로젝트에 들어갔습니다!

이 흐름은 <strong>모든 코드가 주 브랜치에 진입하기 전에 검토를 거치도록</strong> 보장하여, 오류 발생률을 크게 낮춥니다. 오픈 소스 프로젝트 또한 이 메커니즘을 사용하여 전 세계 낯선 사람들의 공헌을 받습니다 — 당신은 어떤 유명 오픈 소스 프로젝트에 PR을 제출하여, 채택되면 당신이 바로 이 프로젝트의 기여자가 될 수 있습니다. <h4 class="text-lg font-semibold mt-4 mb-2">일곱, GitHub의 일반적인 응용 시나리오</h4> <h5 class="font-semibold mt-3 mb-1">🎓 학생 대회 및 과제 프로젝트 참여</h5> <p class="mb-2">컴퓨터과 학생이 ACM, 해커톤, 졸업 설계에 참가할 때, 거의 모두 GitHub에서 떨어질 수 없습니다. 그것은 팀 협업 플랫폼이자 작품 표시 창구 역할을 합니다 — 심사위원이 직접 저장소를 보고, 코드 품질과 협업 과정을 이해할 수 있습니다. 많은 회사 채용 시 기술 능력의 증명으로서 GitHub 홈페이지를 첨부할 것을 요구합니다. <h5 class="font-semibold mt-3 mb-1">📚 개인 지식 창고 및 노트 호스팅</h5> <p class="mb-2">비프로그래머도 GitHub을 사용할 수 있습니다. 많은 사람들이 학습 노트, 기술 블로그(GitHub Pages와 결합하여 무료 웹사이트 구축), 전자책을 호스팅하는 데 사용. Markdown 형식 작성 + Git 버전 관리 + 클라우드 백업, 3 in 1. <h5 class="font-semibold mt-3 mb-1">🌐 오픈 소스 프로젝트 참여</h5> <p class="mb-2">GitHub은 전 세계 오픈 소스 운동의 핵심 거점입니다. 좋아하는 프로젝트를 Fork하여, 수정 후 PR을 커뮤니티에 환원할 수 있습니다; 또는 단순히 Star로 좋은 프로젝트를 북마크하고, 업데이트 추적. 오픈 소스 참여는 기술을 높이고 평판을 쌓는 절호의 기회.</p> <h5 class="font-semibold mt-3 mb-1">🤖 자동화 배포 및 CI/CD</h5> <p class="mb-2">GitHub Actions의 도움으로, "코드 push, 자동 테스트 + 서버에 자동 배포"의 완전 자동 흐름 구현 가능. 많은 개인 블로그, 문서 사이트가 이렇게 구축되며, 글 작성 후 push하면 사이트가 자동 업데이트.</p> <h5 class="font-semibold mt-3 mb-1">💾 코드 백업 및 다중 기기 동기화</h5> <p class="mb-2">코드 저장소를 클라우드 디스크로 사용, 기기 변경, 다중 기기 사무 시, git pull만 하면 최신 코드를 얻을 수 있어, 더 이상 USB 드라이브로 복사할 필요 없음.</p> <h4 class="text-lg font-semibold mt-4 mb-2">여덟, 초보자를 위한 몇 가지 조언</h4> <ul class="list-disc pl-6 mb-3 space-y-1"> <li><strong>커밋 설명을 명확히 작성</strong>: "update" 같은 쓸모없는 설명을 쓰지 마세요. 좋은 커밋 메시지는 "사용자 로그인 후 잘못된 페이지로 이동하는 문제 수정"을 쓰며, 반 년 후에 다시 봐도 그때 무엇을 했는지 알 수 있습니다.</li> <li><strong>자주 커밋, 작은 걸음 빠른 걸음</strong>: 작은 기능을 완료할 때마다 커밋하며, 하루 종일 쓴 다음에 한 번 커밋하지 마세요. 이렇게 하면 문제가 발생했을 때 더 쉽게 위치 파악.</li> <li><strong>브랜치로 개발, 주 브랜치를 직접 수정하지 말 것</strong>: 개인 프로젝트라도 브랜치를 여는 습관을 기르세요, 미래에 팀 협업 시 황란하지 않습니다.</li> <li><strong>.gitignore 잘 활용</strong>: 이 파일은 Git에게 어떤 파일을 버전 관리에 포함하지 말지 알려줍니다(예: 비밀번호 설정, 컴파일 산출물, 의존성 폴더), 쓰레기 파일이 업로드되는 것을 방지.</li> <li><strong>훌륭한 오픈 소스 프로젝트 많이 보기</strong>: GitHub Trending을 둘러보고, 높은 별점 프로젝트의 코드 구조, README 작성법, 협업 흐름을 보는 것이 가장 빠른 무료 향상 방법.</li> <li><strong>GitHub 학생 팩 신청</strong>: 학생 인증 후 대량의 유료 도구와 서비스 크레딧을 무료로 받을 수 있으며(Copilot, 도메인, 클라우드 서비스 등), 가치가 수천 달러에 달합니다.</li> </ul> <div class="warning-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-exclamation-triangle mr-2"></i>보안리마인더</p> <ul class="list-disc pl-6 mt-1 space-y-1"> <li>비밀번호, API 키, 데이터베이스 연결 문자열 등 민감한 정보를 GitHub에 절대 제출하지 마세요, 특히 공개 저장소 — 유출되면 크롤러가 즉시 가져가며, 결과가 심각합니다.</li> <li>실수로 민감한 정보를 제출했다면, 파일 삭제만으로는 부족하며(역사 기록에 아직 있음), <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">git filter-branch</code> 또는 전문 도구로 역사를 정리하고, 즉시 유출된 키를 교체해야 합니다.</li> <li>비공개 저장소도 절대 안전하지 않으며, 민감한 정보는 가장 좋은 것은 환경 변수로 관리, 코드 저장소에 넣지 마세요.</li> </ul> </div> <div class="info-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-info-circle mr-2"></i>국내에서 GitHub 접근 시 주의사항</p> <p class="mt-1">GitHub은 국내에서 접근이 때때로 불안정하여, 열리지 않거나 클론이 느린 상황이 발생할 수 있습니다. 시도해 볼 수 있습니다: ① 국내 미러 사이트(예: GitClone, ghproxy)로 클론 가속; ② Hosts 설정 또는 프록시 사용; ③ 주로 국내 협업을 대상으로 한다면, 국산 대체품 <strong>Gitee(코드클라우드)</strong>를 고려해 볼 수 있으며, 기능이 유사하고 접근 속도가 빠릅니다. 많은 팀이 GitHub과 Gitee에 동시에 호스팅하여, 국제화와 국내 속도를 모두 겸합니다.</p> </div> <div class="success-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-lightbulb mr-2"></i>고급 플레이법: GitHub Pages로 무료 개인 블로그 구축</p> <p class="mt-1">GitHub Pages는 정적 웹사이트를 무료 호스팅할 수 있게 해주며, Jekyll, Hexo, Hugo 등 정적 사이트 생성기와 결합하여, 쉽게 개인 블로그를 구축할 수 있습니다. Markdown 글 작성 후 저장소에 push하면, 블로그가 자동 업데이트되며, HTTPS와 사용자 정의 도메인 내장. 무수한 기술 블로거의 블로그가 이렇게 구축되었으며, 비용 0, 광고 없음, 버전 제어 가능.</p> </div> <h4 class="text-lg font-semibold mt-4 mb-2">아홉, 요약: 왜 모든 사람이 GitHub을 알아야 하는가</h4> <p class="mb-2">GitHub은 이미 "프로그래머의 도구"에 그치지 않고, <strong>디지털 시대의 작업 방식</strong>과 같습니다: 버전 관리로 모든 것을 추적 가능하게 하고, 협업 메커니즘으로 팀이 효율적으로 운영하게 하며, 오픈 소스 정신으로 지식이 자유롭게 흐르게 합니다. 코드를 쓰지 않더라도, "커밋, 브랜치, 병합"의 개념을 이해하면, "반복 수정 + 다중 협업"이 필요한 모든 콘텐츠를 더 잘 관리하는 데 도움이 됩니다 — 논문에서 문서, 노트에서 방안까지.</p> <p class="mb-2">컴퓨터과 학생에게 GitHub은 필수 기술입니다: 그것은 당신의 작품집, 협업 플랫폼, 학습 자료 창고이며, 미래 구직 시 가장 설득력 있는 "이력서"입니다. 일찍 계정을 등록하고, 자신의 과제, 소규모 프로젝트를 올려두며, 천천히 쌓아가세요, 몇 년 후 당신은 면접관의 눈을 밝게 할 기술 이력을 갖게 될 것입니다.</p> <div class="practice-box rounded-lg p-4 mt-4"> <p class="font-semibold"><i class="fas fa-hands mr-2"></i>직접 해보기: GitHub 첫 경험 완료</p> <ol class="list-decimal pl-6 mt-1 space-y-1"> <li>GitHub 계정을 등록하고, 개인 자료(아바타, 소개, 관심 있는 기술 분야)를 완성.</li> <li><code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">hello-github</code>라는 이름의 공개 저장소를 만들고, "Add a README file" 체크.</li> <li>저장소로 들어가, README.md의 편집 버튼(연필 아이콘) 클릭, Markdown으로 자기 소개 작성, 변경 사항 제출.</li> <li>GitHub 검색창에서 관심 있는 키워드 검색(예: <code class="bg-gray-100 dark:bg-gray-800 px-1 rounded">python-tutorial</code>), 좋아하는 프로젝트 두 개에 Star.</li> <li>(고급) 컴퓨터에 Git 설치, 저장소를 로컬로 Clone, README 수정 후 클라우드로 push, 완전한 "로컬→클라우드" 작업 흐름 한 번 완료.</li> </ol> </div> </p></p>
