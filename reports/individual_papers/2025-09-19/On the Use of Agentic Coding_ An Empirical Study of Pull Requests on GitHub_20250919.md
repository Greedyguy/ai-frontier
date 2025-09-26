---
keywords:
  - Large Language Models
  - Agentic Coding
  - GitHub
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14745
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:31:39.919604",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Agentic Coding",
    "GitHub"
  ],
  "rejected_keywords": [
    "Pull Requests"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Agentic Coding": 0.7,
    "GitHub": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub

**Korean Title:** 에이전트적 코딩의 사용에 관한 연구: GitHub의 풀 리퀘스트에 대한 실증적 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large language models]], [[keywords/GitHub|GitHub]]
**⚡ Unique Technical**: [[keywords/Agentic Coding|agentic coding]]

## 🔗 유사한 논문
- [[AI Agents with Human-Like Collaborative Tools Adaptive Strategies for Enhanced Problem-Solving]] (84.2% similar)
- [[On the Use of Agentic Coding Manifests An Empirical Study of Claude Code]] (83.9% similar)
- [[An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (83.5% similar)
- [[Designing AI-Agents with Personalities A Psychometric Approach]] (83.4% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14745v1 Announce Type: new 
Abstract: Large language models (LLMs) are increasingly being integrated into software development processes. The ability to generate code and submit pull requests with minimal human intervention, through the use of autonomous AI agents, is poised to become a standard practice. However, little is known about the practical usefulness of these pull requests and the extent to which their contributions are accepted in real-world projects. In this paper, we empirically study 567 GitHub pull requests (PRs) generated using Claude Code, an agentic coding tool, across 157 diverse open-source projects. Our analysis reveals that developers tend to rely on agents for tasks such as refactoring, documentation, and testing. The results indicate that 83.8% of these agent-assisted PRs are eventually accepted and merged by project maintainers, with 54.9% of the merged PRs are integrated without further modification. The remaining 45.1% require additional changes benefit from human revisions, especially for bug fixes, documentation, and adherence to project-specific standards. These findings suggest that while agent-assisted PRs are largely acceptable, they still benefit from human oversight and refinement.

## 🔍 Abstract (한글 번역)

arXiv:2509.14745v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)은 점점 더 소프트웨어 개발 프로세스에 통합되고 있습니다. 자율 AI 에이전트를 통해 최소한의 인간 개입으로 코드를 생성하고 풀 리퀘스트를 제출하는 능력은 표준 관행이 될 것으로 예상됩니다. 그러나 이러한 풀 리퀘스트의 실질적인 유용성과 실제 프로젝트에서 그 기여가 수용되는 정도에 대해서는 거의 알려져 있지 않습니다. 본 논문에서는 157개의 다양한 오픈 소스 프로젝트에서 에이전트 코딩 도구인 Claude Code를 사용하여 생성된 567개의 GitHub 풀 리퀘스트(PR)를 실증적으로 연구합니다. 우리의 분석에 따르면 개발자들은 리팩토링, 문서화, 테스트와 같은 작업에 에이전트를 의존하는 경향이 있습니다. 결과는 이러한 에이전트 지원 PR 중 83.8%가 프로젝트 유지 관리자에 의해 최종적으로 수락 및 병합되며, 병합된 PR의 54.9%는 추가 수정 없이 통합된다는 것을 나타냅니다. 나머지 45.1%는 버그 수정, 문서화 및 프로젝트별 표준 준수를 위해 인간의 수정이 특히 유익한 추가 변경이 필요합니다. 이러한 결과는 에이전트 지원 PR이 대체로 수용 가능하지만 여전히 인간의 감독과 정제가 필요하다는 것을 시사합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 소프트웨어 개발 과정에 통합되는 현상을 연구합니다. 특히, 자율 AI 에이전트를 통해 코드 생성 및 풀 리퀘스트(PR) 제출이 어떻게 실무에 적용되는지를 조사했습니다. 연구는 Claude Code라는 도구를 사용하여 157개의 다양한 오픈소스 프로젝트에서 생성된 567개의 PR을 분석했습니다. 결과적으로, 개발자들은 리팩토링, 문서화, 테스트와 같은 작업에 에이전트를 활용하며, 83.8%의 PR이 프로젝트 유지자에 의해 수락 및 병합되었습니다. 그 중 54.9%는 추가 수정 없이 통합되었고, 나머지 45.1%는 버그 수정, 문서화, 프로젝트 기준 준수를 위해 인간의 추가 수정이 필요했습니다. 이는 에이전트가 생성한 PR이 대체로 수용 가능하지만, 인간의 검토와 개선이 여전히 중요함을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 소프트웨어 개발 과정에 점점 더 통합되고 있다.

- 2. 자율 AI 에이전트를 사용하여 코드 생성 및 풀 리퀘스트 제출이 최소한의 인간 개입으로 가능해지고 있다.

- 3. 연구 결과, 에이전트가 지원한 풀 리퀘스트의 83.8%가 프로젝트 유지자에 의해 수락 및 병합되었다.

- 4. 병합된 PR 중 54.9%는 추가 수정 없이 통합되었으나, 45.1%는 버그 수정, 문서화, 프로젝트 기준 준수 등을 위해 인간의 추가 수정이 필요했다.

- 5. 에이전트 지원 PR은 대체로 수용 가능하지만, 인간의 감독과 개선이 여전히 필요하다.

---

*Generated on 2025-09-19 16:42:18*